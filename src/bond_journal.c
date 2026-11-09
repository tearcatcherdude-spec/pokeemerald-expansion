#include "global.h"
#include "bonds.h"
#include "bond_journal.h"
#include "cast.h"
#include "pip.h"
#include "event_data.h"
#include "string_util.h"
#include "script.h"
#include "script_menu.h"
#include "field_player_avatar.h"
#include "event_object_movement.h"
#include "overworld.h"
#include "fieldmap.h"
#include "sprite.h"
#include "item.h"
#include "move.h"
#include "pokemon_storage_system.h"
#include "constants/kanto_symbols.h"
#include "constants/rgb.h"
#include "region_map.h"
#include "main.h"
#include "battle.h"
#include "battle_setup.h"
#include "data.h"
#include "pokemon.h"
#include "money.h"
#include "script_pokemon_util.h"
#include "metatile_behavior.h"
#include "constants/event_objects.h"

#if FNPC_ENABLE_NPC_FOLLOWERS && !IS_FRLG
struct BondEvent
{
    u16 map;
    u8 x, y, destination;
    const u8 *title, *directions, *objective;
};
struct BondCenter { u16 map; u8 x,y; };
struct BondScene
{
    const u8 *intro, *questions[3], *options[3][3], *responses[3][3], *ending;
    u8 rounds, expression;
};
struct BondGift { u16 item; u8 exp; };
#include "data/bond_events.h"
#include "data/bond_scenes.h"
#include "data/bond_marker.h"
#include "data/bond_trial_previews.h"
static const u8 *const sNames[] = {
    COMPOUND_STRING("SILAS"), COMPOUND_STRING("KADE"), COMPOUND_STRING("ASHE"),
    COMPOUND_STRING("NICO"), COMPOUND_STRING("RIVEN"), COMPOUND_STRING("EMI"),
    COMPOUND_STRING("VERA"), COMPOUND_STRING("LUME"), COMPOUND_STRING("MOCHI"), COMPOUND_STRING("ZURI"),
};
static const u8 sEventLevels[] = {4,8,12,16,20};
static EWRAM_DATA u8 sWho = 0;
static EWRAM_DATA u8 sGift = 0;
static EWRAM_DATA u8 sSceneEvent = 0; // event index + 1; transient, no save during scenes.
static EWRAM_DATA u8 sScenePage = 0;
static EWRAM_DATA u8 sSceneChoice = 0;
static EWRAM_DATA u8 sSceneRound = 0;
static EWRAM_DATA u8 sGiftNames[3][48] = {};
static EWRAM_DATA struct MenuAction sGiftMenu[3] = {};
static EWRAM_DATA u8 sMarkerSprite = 0;
static EWRAM_DATA u8 sMapPin = 0;
static EWRAM_DATA bool8 sMapView = FALSE;
static EWRAM_DATA struct RegionMap *sViewedMap = NULL;
static EWRAM_DATA bool8 sTraining = FALSE;
static EWRAM_DATA bool8 sTrainingEvent = FALSE;
static EWRAM_DATA bool8 sTrialWon = FALSE;
static EWRAM_DATA u32 sTrialMoney = 0;
static EWRAM_DATA u32 sTrialKey = 0;
static EWRAM_DATA struct Bag sTrialBag = {};
static EWRAM_DATA struct Pokemon sTrialParty[PARTY_SIZE] = {};
static EWRAM_DATA u8 sTrialPartyCount = 0;
static EWRAM_DATA u8 sPreviewBand = 0;
static EWRAM_DATA u8 sStageActors[3] = {};
static EWRAM_DATA u16 sStageMap = 0;
static void ClearStage(void);
static void StageActors(u32 index);
static const struct OamData sHeartOam={.shape=0,.size=1,.priority=1};
static const struct SpriteTemplate sHeartTemplate={
    .tileTag=0x7C51,.paletteTag=0x7C51,.oam=&sHeartOam,
    .anims=gDummySpriteAnimTable,.affineAnims=gDummySpriteAffineAnimTable,.callback=SpriteCallbackDummy,
};
static const struct SpriteTemplate sMapHeartTemplate={
    .tileTag=0x7C52,.paletteTag=0x7C52,.oam=&sHeartOam,
    .anims=gDummySpriteAnimTable,.affineAnims=gDummySpriteAffineAnimTable,.callback=SpriteCallbackDummy,
};
extern const u8 Bonds_EventScript_Marker[];

static u32 EventIndex(void)
{
    return sWho * 5 + min(Bonds_GetProgress()->people[sWho].hearts, 4);
}
static bool32 OnMap(u16 map)
{
    return gSaveBlock1Ptr->location.mapGroup == MAP_GROUP(map)
        && gSaveBlock1Ptr->location.mapNum == MAP_NUM(map);
}
static void Number(u32 n)
{
    u8 buffer[12];
    ConvertIntToDecimalStringN(buffer, n, STR_CONV_MODE_LEFT_ALIGN, 5);
    StringAppend(gStringVar4, buffer);
}
static void Text(const u8 *text) { StringCopy(gStringVar4, text); }
static void Menu(const struct MenuAction *items, u32 count)
{
    Cast_HidePortrait();
    DrawMultichoiceMenuInternal(0, 0, MULTI_CAST_ROSTER, FALSE, 0, items, count);
}
static bool32 FourBadges(void)
{
    u32 hoenn=0, kanto=0;
    for (u32 i=0; i<8; i++)
    {
        u32 flag=FLAG_BADGE01_GET+i;
        hoenn += !!(gSaveBlock1Ptr->flags[flag/8] & (1 << (flag%8)));
        kanto += !!FlagGet(KANTO_FLAG_BADGE01_GET+i);
    }
    return hoenn >= 4 || kanto >= 4;
}
static const u8 *Unmet(u32 index)
{
    const struct BondEvent *e=&sBondEvents[index];
    u32 who=index/5, stage=index%5;
    struct BondProgress *p=Bonds_GetProgress();
    if (!(gSaveBlock3Ptr->cast.recruited & (1 << who)))
        return COMPOUND_STRING("Befriend this trainer first.$");
    if (p->people[who].hearts != stage)
        return COMPOUND_STRING("Complete the earlier event first.$");
    if (Bonds_Level(who) < sEventLevels[stage])
        return COMPOUND_STRING("Raise your Bond Level first.$");
    if (!(p->visited[e->destination/8] & (1 << (e->destination%8))))
        return COMPOUND_STRING("Visit this destination first.\nNormal story access is required.$");
    if (stage>=3 && !FourBadges())
        return COMPOUND_STRING("Earn four badges in either region.$");
    if (stage==4 && gSaveBlock3Ptr->cast.loreStage[who]<6)
        return COMPOUND_STRING("Hear their six story passages.\nChoose Hear their story together.$");
    return NULL;
}
static bool32 AtMeeting(u32 index)
{
    const struct BondEvent *e=&sBondEvents[index];
    s16 x,y;
    if (!OnMap(e->map)) return FALSE;
    PlayerGetDestCoords(&x,&y);
    x-=7; y-=7;
    return abs(x-e->x)+abs(y-e->y)<=1;
}
static bool32 AtCenter(void)
{
    s16 x,y;
    PlayerGetDestCoords(&x,&y); x-=7;y-=7;
    for (u32 i=0;i<ARRAY_COUNT(sBondCenters);i++)
    {
        const struct BondCenter *c=&sBondCenters[i];
        if(OnMap(c->map) && abs(x-c->x)+abs(y-c->y)<=5)
            return TRUE;
    }
    return FALSE;
}

void Script_BondsSelect(struct ScriptContext *ctx)
{
    u32 choice=gSpecialVar_Result;
    gSpecialVar_Result=FALSE;
    Bonds_EnsureInitialized();
    if (choice<1 || choice>BOND_COUNT || !(gSaveBlock3Ptr->cast.recruited & (1 << (choice-1))))
        return;
    sWho=choice-1;
    gSpecialVar_Result=TRUE;
}
void Script_BondsStatus(struct ScriptContext *ctx)
{
    struct BondPerson *p=&Bonds_GetProgress()->people[sWho];
    u32 level=Bonds_Level(sWho);
    Cast_HidePortrait();
    Text(sNames[sWho]); StringAppend(gStringVar4,COMPOUND_STRING(" - Bond Lv. ")); Number(level);
    StringAppend(gStringVar4,COMPOUND_STRING("\n"));
    if(level==20) StringAppend(gStringVar4,COMPOUND_STRING("EXP: MAX"));
    else
    {
        Number(p->exp-Bonds_TotalForLevel(level));
        StringAppend(gStringVar4,COMPOUND_STRING(" / ")); Number(Bonds_TotalForLevel(level+1)-Bonds_TotalForLevel(level));
        StringAppend(gStringVar4,COMPOUND_STRING(" EXP to next level"));
    }
    StringAppend(gStringVar4,COMPOUND_STRING("\lHearts: "));
    for(u32 i=0;i<5;i++) StringAppend(gStringVar4,i<p->hearts?COMPOUND_STRING("{EMOJI_HEART}"):COMPOUND_STRING("-"));
    StringAppend(gStringVar4,COMPOUND_STRING("\l"));
    StringAppend(gStringVar4,p->interest==BOND_COMMITTED?COMPOUND_STRING("In a committed relationship."):p->interest==BOND_INTERESTED?COMPOUND_STRING("Exploring romantic interest."):p->interest==BOND_FRIENDSHIP?COMPOUND_STRING("Friends, with room to grow."):COMPOUND_STRING("No romantic choice made."));
}
void Script_BondsDetails(struct ScriptContext *ctx)
{
    struct BondPerson *p=&Bonds_GetProgress()->people[sWho];
    Text(COMPOUND_STRING("Total Bond EXP: "));Number(p->exp);
    StringAppend(gStringVar4,COMPOUND_STRING(" / 3040\nWalking EXP this outing: "));Number(p->walkingExp);
    StringAppend(gStringVar4,COMPOUND_STRING("/40\lOn-foot steps: "));Number(p->outingSteps);
    StringAppend(gStringVar4,COMPOUND_STRING("/2048\l"));
    StringAppend(gStringVar4,p->giftUsed?COMPOUND_STRING("Gift EXP used this outing."):COMPOUND_STRING("One gift can grant EXP this outing."));
    StringAppend(gStringVar4,COMPOUND_STRING("\lGift EXP in this heart band: "));Number(p->hearts<5?p->giftExp[p->hearts]:150);
    StringAppend(gStringVar4,COMPOUND_STRING("/150\l256 foot steps: +5; new comment: +10.\lNew story: +25; new landmark: +30.\lUnique request: +40. No repeat EXP.\lNew victories and unique objectives\lrenew outings. Switching does not.\lAfter 2048 steps, rest outside any\lPOKEMON CENTER to renew an outing."));
}
void Script_BondsMenu(struct ScriptContext *ctx)
{
    static const struct MenuAction items[]={
        {COMPOUND_STRING("Personal event")},{COMPOUND_STRING("Give a gift")},
        {COMPOUND_STRING("Hear their story")},{COMPOUND_STRING("Relationship")},
        {COMPOUND_STRING("More")},{COMPOUND_STRING("Back")},
    };
    Menu(items,ARRAY_COUNT(items));
}
void Script_BondsMoreMenu(struct ScriptContext *ctx)
{
    static const struct MenuAction items[]={
        {COMPOUND_STRING("Rest together")},{COMPOUND_STRING("EXP details")},
        {COMPOUND_STRING("Move rewards")},{COMPOUND_STRING("Keepsake")},
        {COMPOUND_STRING("Train together")},{COMPOUND_STRING("Back")},
    };
    Menu(items,ARRAY_COUNT(items));
}
void Script_BondsJournalIntro(struct ScriptContext *ctx)
{
    Bonds_EnsureInitialized();
    gSpecialVar_Result=FALSE;
    if(Bonds_GetProgress()->people[0].flags & 0x80) return;
    Bonds_GetProgress()->people[0].flags|=0x80;
    Text(COMPOUND_STRING("You set out on your first journey\nas an adult. Your ten recruitable\lcompanions are adults too.\lHearts count shared personal events.\lRomance is optional and explicit.\lFriendship earns the same rewards.\lOnly one committed romance at a time.\lNo neglect, jealousy or EXP decay.$"));
    gSpecialVar_Result=TRUE;
}
void Script_BondsKeepsake(struct ScriptContext *ctx)
{
    if(Bonds_GetProgress()->people[sWho].hearts<5)
    {Text(COMPOUND_STRING("Complete their fifth personal event\nto receive a journal keepsake.$"));return;}
    Text(sBondKeepsakes[sWho]);
    StringAppend(gStringVar4,(Bonds_GetProgress()->people[sWho].flags & 1)?COMPOUND_STRING("\nA reminder of choosing a shared\lfuture with room for two lives.$"):COMPOUND_STRING("\nA reminder of a lasting friendship\land the journey still ahead.$"));
}
void Script_BondsEventInfo(struct ScriptContext *ctx)
{
    u32 index=EventIndex();
    const struct BondEvent *e=&sBondEvents[index];
    const u8 *unmet=Unmet(index);
    gSpecialVar_Result=FALSE;
    if(Bonds_GetProgress()->people[sWho].hearts==5)
    {
        Text(COMPOUND_STRING("All five personal events complete.\nYour story together continues.\lKeepsake recorded in this journal.$"));
        return;
    }
    Text(e->title);StringAppend(gStringVar4,COMPOUND_STRING("\nRequired Bond Lv. "));Number(sEventLevels[index%5]);
    StringAppend(gStringVar4,COMPOUND_STRING("\l"));StringAppend(gStringVar4,e->directions);
    StringAppend(gStringVar4,COMPOUND_STRING("\l"));
    StringAppend(gStringVar4,unmet?unmet:COMPOUND_STRING("Ready. No payment or time window."));
    gSpecialVar_Result=TRUE;
}
void Script_BondsTrack(struct ScriptContext *ctx)
{
    Bonds_GetProgress()->trackedEvent=EventIndex()+1;
    Text(COMPOUND_STRING("Destination tracked. Bring this\ncompanion to the heart marker.\lNo doors or paths are blocked.$"));
}
void Script_BondsEventMenu(struct ScriptContext *ctx)
{
    static const struct MenuAction items[]={
        {COMPOUND_STRING("Track destination")},{COMPOUND_STRING("Meet here")},
        {COMPOUND_STRING("View region map")},{COMPOUND_STRING("Task and reward")},
        {COMPOUND_STRING("Later")},
    };
    Menu(items,ARRAY_COUNT(items));
}
void Script_BondsRewardInfo(struct ScriptContext *ctx)
{
    u32 stage=EventIndex()%5;
    Text(sBondEvents[EventIndex()].objective);
    StringAppend(gStringVar4,COMPOUND_STRING("\lReward: "));
    if(stage==2 || stage==3)
    {
        StringAppend(gStringVar4,GetMoveName(sBondRewardMoves[sWho][stage==3]));
        StringAppend(gStringVar4,COMPOUND_STRING(" tutoring.\lBond EXP +")); Number(stage==3?100:60);
    }
    else
    {
        Number(stage==0?1:stage==1?2:3);StringAppend(gStringVar4,COMPOUND_STRING(" RARE CANDY."));
        if(stage==4) {StringAppend(gStringVar4,COMPOUND_STRING("\l"));StringAppend(gStringVar4,sBondKeepsakes[sWho]);}
        else StringAppend(gStringVar4,COMPOUND_STRING("\lBond EXP +60."));
    }
    StringAppend(gStringVar4,COMPOUND_STRING("\lFriendship and romance earn the\lsame practical rewards. No payment."));
}
void Script_BondsMeet(struct ScriptContext *ctx)
{
    u32 index=EventIndex();
    const u8 *unmet=Unmet(index);
    gSpecialVar_Result=FALSE;
    if(unmet) { Text(unmet);return; }
    if(!Cast_IsFollowing() || Cast_Active()!=sWho+1 || Pip_IsSceneSuspended())
    { Text(COMPOUND_STRING("Travel with this companion first.$"));return; }
    if(!AtMeeting(index))
    { Text(COMPOUND_STRING("Meet at the named heart marker.\nYou must walk there normally.$"));return; }
    sSceneEvent=index+1;sScenePage=0;sSceneChoice=0;sSceneRound=0;sTrialWon=FALSE;
    StageActors(index);
    gSpecialVar_Result=TRUE;
}
void Script_BondsRest(struct ScriptContext *ctx)
{
    if(Bonds_Rest(sWho,AtCenter()))
        Text(COMPOUND_STRING("You rest together. A new outing\nbegins. No EXP awarded for resting.$"));
    else Text(COMPOUND_STRING("Travel 2048 on-foot steps together,\nthen rest outside a POKEMON CENTER.\lChanging company does not reset it.$"));
}
void Script_BondsStory(struct ScriptContext *ctx)
{
    gSpecialVar_Result=FALSE;
    if(!Cast_IsFollowing() || Cast_Active()!=sWho+1)
    { Text(COMPOUND_STRING("Travel together to hear their story.$"));return; }
    if(gSaveBlock3Ptr->cast.loreStage[sWho]>=6)
    { Text(COMPOUND_STRING("You have heard their story so far.\nThere is no need to repeat it.$"));return; }
    // Existing ordered lore still uses its own spoken-observation thresholds.
    if(Cast_TryBondStory()) gSpecialVar_Result=TRUE;
    else Text(COMPOUND_STRING("Give your friendship time and hear\nnew observations together. Their\lstory will continue in order.$"));
}
void Script_BondsInterestMenu(struct ScriptContext *ctx)
{
    static const struct MenuAction items[]={
        {COMPOUND_STRING("Romantic interest")},{COMPOUND_STRING("Close friendship")},
        {COMPOUND_STRING("Not sure yet")},{COMPOUND_STRING("Commit together")},
        {COMPOUND_STRING("Back")},
    };
    Menu(items,ARRAY_COUNT(items));
}
void Script_BondsInterest(struct ScriptContext *ctx)
{
    static const u8 choices[]={BOND_INTERESTED,BOND_FRIENDSHIP,BOND_UNDECIDED,BOND_COMMITTED};
    u32 choice=gSpecialVar_Result;
    if(choice>=4) { Text(COMPOUND_STRING("You leave the conversation for later.$"));return; }
    if(!Cast_IsFollowing() || Cast_Active()!=sWho+1)
    { Text(COMPOUND_STRING("Talk about this while together.$"));return; }
    if(choice==3 && (Bonds_GetProgress()->people[sWho].hearts<5 || !AtMeeting(sWho*5+4)))
    { Text(COMPOUND_STRING("Complete the final personal event,\nthen revisit its meeting place to\ldiscuss a new commitment.$"));return; }
    if(Bonds_GetProgress()->people[sWho].hearts<3
     || (choice!=1 && !AtMeeting(sWho*5+2)
      && !(Bonds_GetProgress()->people[sWho].hearts>=4 && AtMeeting(sWho*5+4))))
    { Text(COMPOUND_STRING("Revisit your third-event meeting\nplace after that event, or your\lfinal meeting place when ready.$"));return; }
    if(!Bonds_SetInterest(sWho,choices[choice]))
    { Text(COMPOUND_STRING("Interest opens at the third event.\nCommitment opens at the last event.\lOnly one committed relationship\lis possible. End it respectfully\lbefore making another commitment.$"));return; }
    Text(choice==3?COMPOUND_STRING("You both choose a committed\nrelationship. Your friendship,\lgoals and journey still matter.$"):choice==1?COMPOUND_STRING("You agree to continue as friends.\nAny commitment ends respectfully.\lYour hearts and rewards remain.$"):choice==0?COMPOUND_STRING("You talk honestly about interest.\nThere is no commitment yet.$"):COMPOUND_STRING("You agree to take your time.\nNo affection or rewards are lost.$"));
}
void Script_BondsGiftMenu(struct ScriptContext *ctx)
{
    for(u32 i=0;i<3;i++)
    {
        CopyItemName(sBondGifts[sWho][i].item,sGiftNames[i]);
        StringAppend(sGiftNames[i],i==0?COMPOUND_STRING(" (favorite)"):i==1?COMPOUND_STRING(" (liked)"):COMPOUND_STRING(" (neutral)"));
        sGiftMenu[i].text=sGiftNames[i];
    }
    Menu(sGiftMenu,3);
}
void Script_BondsGiftPreview(struct ScriptContext *ctx)
{
    u32 choice=gSpecialVar_Result;
    gSpecialVar_Result=FALSE;
    if(choice>=3) return;
    sGift=choice;
    if(!Cast_IsFollowing() || Cast_Active()!=sWho+1)
    { Text(COMPOUND_STRING("Give a gift while traveling together.$"));return; }
    if(!CheckBagHasItem(sBondGifts[sWho][choice].item,1))
    { Text(COMPOUND_STRING("You do not have that item.\nNothing was taken.$"));return; }
    Text(COMPOUND_STRING("Give one "));StringAppend(gStringVar4,GetItemName(sBondGifts[sWho][choice].item));
    StringAppend(gStringVar4,COMPOUND_STRING("?\nBond EXP: +"));Number(Bonds_GiftPreview(sWho,sBondGifts[sWho][choice].exp));
    StringAppend(gStringVar4,COMPOUND_STRING("\lOne item will be consumed.\lCancel keeps your item.\lAt the limit, this is a flavor gift."));
    gSpecialVar_Result=TRUE;
}
void Script_BondsGiftCommit(struct ScriptContext *ctx)
{
    const struct BondGift *gift=&sBondGifts[sWho][sGift];
    if(!Cast_IsFollowing() || Cast_Active()!=sWho+1 || !CheckBagHasItem(gift->item,1) || !RemoveBagItem(gift->item,1))
    { Text(COMPOUND_STRING("The gift could not be given.\nNothing was taken.$"));return; }
    Bonds_RecordGift(sWho,gift->exp);
    Text(sBondGiftReplies[sWho]);Cast_ShowPortrait(sWho,1);
}
void Script_BondsScenePage(struct ScriptContext *ctx)
{
    const struct BondScene *scene;
    gSpecialVar_Result=0;
    if(!sSceneEvent || sSceneEvent>50) return;
    scene=&sBondScenes[sSceneEvent-1];
    if(sScenePage==0) {Text(scene->intro);sScenePage=1;}
    else if(sScenePage==1) {Text(scene->questions[sSceneRound]);sScenePage=2;}
    else if(sScenePage==2) {gSpecialVar_Result=2;return;}
    else if(sScenePage==3) {Text(scene->responses[sSceneRound][sSceneChoice]);sScenePage=4;}
    else if(sScenePage==4)
    {
        if(sTrialWon) {Text(COMPOUND_STRING("You finish the practice battle\nand talk through what each of you\lnoticed. Winning was not a promise\lof romance, or a test of worth.$"));sScenePage=5;}
        else if(sSceneRound+1<scene->rounds)
        {sSceneRound++;Text(scene->questions[sSceneRound]);sScenePage=2;}
        else {Text(scene->ending);sScenePage=5;}
    }
    else {gSpecialVar_Result=3;return;}
    Cast_ShowPortrait(sWho,sScenePage==1?scene->expression:sScenePage==4?1:0);
    gSpecialVar_Result=1;
}
void Script_BondsSceneChoiceMenu(struct ScriptContext *ctx)
{
    struct MenuAction items[3];
    const struct BondScene *scene=&sBondScenes[sSceneEvent-1];
    u32 count=(sSceneEvent-1)%5==2 || (sSceneEvent-1)%5==4?3:2;
    for(u32 i=0;i<count;i++) items[i]=(struct MenuAction){scene->options[sSceneRound][i]};
    // Menu text points into ROM; PrintMenuTable consumes this temporary action
    // array synchronously before input is handled on following frames.
    Menu(items,count);
}
void Script_BondsSceneChoice(struct ScriptContext *ctx)
{
    u32 choice=gSpecialVar_Result,stage=(sSceneEvent-1)%5;
    gSpecialVar_Result=FALSE;
    if(choice>=((stage==2 || stage==4)?3:2))
    {Text(COMPOUND_STRING("Another time. The invitation stays\navailable. Nothing is lost.$"));sSceneEvent=0;return;}
    if(stage==2 && !Bonds_SetInterest(sWho,choice==0?BOND_INTERESTED:choice==1?BOND_FRIENDSHIP:BOND_UNDECIDED)) return;
    if(stage==4)
    {
        if(choice==2)
        {
            Text(sBondScenes[sSceneEvent-1].responses[0][2]);Cast_ShowPortrait(sWho,0);
            sSceneEvent=0;return;
        }
        if(!Bonds_SetInterest(sWho,choice==0?BOND_COMMITTED:BOND_FRIENDSHIP))
        {
            Text(COMPOUND_STRING("Only one committed relationship\nat a time. We can remain friends\lor talk after a respectful breakup.$"));
            return;
        }
    }
    sSceneChoice=choice;sScenePage=3;
    gSpecialVar_Result=TRUE;
}
void Script_BondsSceneComplete(struct ScriptContext *ctx)
{
    u32 index,stage,count,beforeExp;
    gSpecialVar_Result=FALSE;
    if(!sSceneEvent || sScenePage!=5) return;
    index=sSceneEvent-1;stage=index%5;
    if(Unmet(index)) {Text(Unmet(index));sSceneEvent=0;return;}
    count=stage==0?1:stage==1?2:stage==4?3:0;
    if(count && !CheckBagHasSpace(ITEM_RARE_CANDY,count))
    {Text(COMPOUND_STRING("Make room for the RARE CANDY reward.\nThis event stays available; no\lreward or heart was consumed.$"));sSceneEvent=0;return;}
    if(count && !AddBagItem(ITEM_RARE_CANDY,count))
    {Text(COMPOUND_STRING("The reward could not be stored.\nThe event stays available.$"));sSceneEvent=0;return;}
    beforeExp=Bonds_GetProgress()->people[sWho].exp;
    if(!Bonds_CompleteEvent(sWho,stage))
    {
        if(count) RemoveBagItem(ITEM_RARE_CANDY,count);
        Text(COMPOUND_STRING("This event is already complete.$"));sSceneEvent=0;return;
    }
    if(stage==4 && Bonds_GetProgress()->people[sWho].interest==BOND_COMMITTED)
        Bonds_GetProgress()->people[sWho].flags|=1;
    if(Bonds_GetProgress()->trackedEvent==sSceneEvent) Bonds_GetProgress()->trackedEvent=0;
    Text(COMPOUND_STRING("Personal event complete!\n"));
    if(count) {Number(count);StringAppend(gStringVar4,COMPOUND_STRING(" RARE CANDY received.\l"));}
    if(stage==2 || stage==3)
    {
        StringAppend(gStringVar4,GetMoveName(sBondRewardMoves[sWho][stage==3]));
        StringAppend(gStringVar4,COMPOUND_STRING(" tutoring unlocked.\lUse Move rewards in the journal.\lNormal move compatibility applies.\l"));
    }
    if(stage==4)
    {
        StringAppend(gStringVar4,sBondKeepsakes[sWho]);
        StringAppend(gStringVar4,COMPOUND_STRING("\lRecorded in the journal.\lBond Level: MAX."));
    }
    else if(Bonds_GetProgress()->people[sWho].exp>beforeExp)
    {StringAppend(gStringVar4,COMPOUND_STRING("Bond EXP +"));Number(Bonds_GetProgress()->people[sWho].exp-beforeExp);}
    else StringAppend(gStringVar4,COMPOUND_STRING("Bond EXP: MAX."));
    sSceneEvent=0;gSpecialVar_Result=TRUE;
}
void Script_BondsTutorMenu(struct ScriptContext *ctx)
{
    struct MenuAction items[3];
    items[0]=(struct MenuAction){GetMoveName(sBondRewardMoves[sWho][0])};
    items[1]=(struct MenuAction){GetMoveName(sBondRewardMoves[sWho][1])};
    items[2]=(struct MenuAction){COMPOUND_STRING("Back")};
    Menu(items,3);
}
void Script_BondsTutor(struct ScriptContext *ctx)
{
    u32 choice=gSpecialVar_Result;
    gSpecialVar_Result=FALSE;
    if(choice>=2) return;
    if(Bonds_GetProgress()->people[sWho].hearts<3+choice)
    {Text(COMPOUND_STRING("Complete personal event three for\nthe first move, or event four for\lthe second. Friendship earns both.$"));return;}
    gSpecialVar_0x8005=sBondRewardMoves[sWho][choice];
    gSpecialVar_Result=TRUE;
}
void Script_BondsClose(struct ScriptContext *ctx)
{
    ClearStage();
    sSceneEvent=0;sScenePage=0;sSceneRound=0;
    sTrialWon=FALSE;
    Cast_HidePortrait();
}

static bool32 MarkerReady(void)
{
    u32 tracked=Bonds_GetProgress()->trackedEvent;
    if(!tracked || tracked>50 || !Cast_IsFollowing() || Cast_Active()!=(tracked-1)/5+1
     || Pip_IsSceneSuspended() || ScriptContext_IsEnabled() || ArePlayerFieldControlsLocked() || sSceneEvent)
        return FALSE;
    return OnMap(sBondEvents[tracked-1].map) && Unmet(tracked-1)==NULL;
}
static void HideMarker(void)
{
    if(sMarkerSprite && sMarkerSprite<=MAX_SPRITES && gSprites[sMarkerSprite-1].inUse
     && gSprites[sMarkerSprite-1].template==&sHeartTemplate)
        DestroySprite(&gSprites[sMarkerSprite-1]);
    sMarkerSprite=0;
    FreeSpriteTilesByTag(0x7C51);FreeSpritePaletteByTag(0x7C51);
}
void Bonds_UpdateField(void)
{
    u32 active;
    Bonds_EnsureInitialized();
    if(!Bonds_GetProgress()) return;
    if(sStageMap && !OnMap(sStageMap))
    {ClearStage();sSceneEvent=0;sScenePage=0;}
    if(!ScriptContext_IsEnabled() && !ArePlayerFieldControlsLocked())
    {
        active=Cast_IsFollowing()?Cast_Active():0;
        for(u32 i=0;i<50;i++) if(OnMap(sBondEvents[i].map))
        {
            u32 d=sBondEvents[i].destination;
            Bonds_GetProgress()->visited[d/8]|=1 << (d%8);
            if(active && !Pip_IsSceneSuspended()) Bonds_Landmark(active-1,d);
            break;
        }
    }
    if(!MarkerReady()) {HideMarker();return;}
    if(sMarkerSprite && (sMarkerSprite>MAX_SPRITES || !gSprites[sMarkerSprite-1].inUse
     || gSprites[sMarkerSprite-1].template!=&sHeartTemplate)) sMarkerSprite=0;
    if(!sMarkerSprite)
    {
        struct SpriteSheet sheet={sBondHeartTiles,sizeof(sBondHeartTiles),0x7C51};
        struct SpritePalette palette={sBondHeartPalette,0x7C51};
        u32 sprite;
        if(LoadSpriteSheet(&sheet)==0xFFFF) return;
        if(LoadSpritePalette(&palette)==0xFF) {FreeSpriteTilesByTag(0x7C51);return;}
        sprite=CreateSprite(&sHeartTemplate,0,0,0);
        if(sprite>=MAX_SPRITES) {HideMarker();return;}
        sMarkerSprite=sprite+1;
    }
    {
        struct Sprite *s=&gSprites[sMarkerSprite-1];
        const struct BondEvent *e=&sBondEvents[Bonds_GetProgress()->trackedEvent-1];
        s16 x=e->x+7,y=e->y+7;
        SetSpritePosToOffsetMapCoords(&x,&y,8,8);
        s->x=x;s->y=y;s->coordOffsetEnabled=TRUE;
        s->invisible=(++s->data[0]%64)>=56;
    }
}
bool32 Bonds_TryMarker(s16 x,s16 y)
{
    u32 tracked;
    if(!Bonds_GetProgress() || !MarkerReady()) return FALSE;
    tracked=Bonds_GetProgress()->trackedEvent;
    if(x-7!=sBondEvents[tracked-1].x || y-7!=sBondEvents[tracked-1].y) return FALSE;
    sWho=(tracked-1)/5;
    ScriptContext_SetupScript(Bonds_EventScript_Marker);
    return TRUE;
}
u16 Bonds_TrackedMapSection(void)
{
    u32 tracked;
    Bonds_EnsureInitialized();
    if(!Bonds_GetProgress() || !(tracked=Bonds_GetProgress()->trackedEvent) || tracked>50) return 0xFFFF;
    return Overworld_GetMapHeaderByGroupAndId(MAP_GROUP(sBondEvents[tracked-1].map),MAP_NUM(sBondEvents[tracked-1].map))->regionMapSectionId;
}
bool32 Bonds_IsMapView(void) {return sMapView;}
u16 Bonds_DisplayedMapSection(u16 normal)
{
    u16 goal=Bonds_TrackedMapSection();
    return sMapView && goal!=0xFFFF?goal:normal;
}
bool32 Bonds_PositionMapView(struct RegionMap *map)
{
    u16 goal=Bonds_TrackedMapSection();
    if(!sMapView || goal==0xFFFF) return FALSE;
    map->mapSecId=goal;
    map->cursorPosX=gRegionMapEntries[goal].x+1;
    map->cursorPosY=gRegionMapEntries[goal].y+2;
    map->playerIconSpritePosX=map->cursorPosX;
    map->playerIconSpritePosY=map->cursorPosY;
    map->playerIsInCave=FALSE;
    return TRUE;
}
static void MapPinCallback(struct Sprite *s)
{
    u16 goal=Bonds_TrackedMapSection();
    s16 x,y;
    if(!sViewedMap || goal==0xFFFF) {s->invisible=TRUE;return;}
    x=gRegionMapEntries[goal].x+1;y=gRegionMapEntries[goal].y+2;
    if(sViewedMap->zoomed)
    {s->x=x*16-0x30-2*sViewedMap->scrollX;s->y=y*16-0x42-2*sViewedMap->scrollY;}
    else {s->x=x*8+4;s->y=y*8+4;}
    s->invisible=s->x<0 || s->x>DISPLAY_WIDTH || s->y<0 || s->y>DISPLAY_HEIGHT;
}
void Bonds_FreeMapPin(void)
{
    if(sMapPin && sMapPin<=MAX_SPRITES && gSprites[sMapPin-1].inUse
     && gSprites[sMapPin-1].template==&sMapHeartTemplate) DestroySprite(&gSprites[sMapPin-1]);
    sMapPin=0;sViewedMap=NULL;
    FreeSpriteTilesByTag(0x7C52);FreeSpritePaletteByTag(0x7C52);
}
void Bonds_CreateMapPin(struct RegionMap *map)
{
    u16 goal=Bonds_TrackedMapSection();
    struct SpriteSheet sheet={sBondHeartTiles,sizeof(sBondHeartTiles),0x7C52};
    struct SpritePalette palette={sBondHeartPalette,0x7C52};
    u32 sprite;
    Bonds_FreeMapPin();
    if(goal==0xFFFF || GetRegionMapType(goal)!=GetRegionMapType(Bonds_DisplayedMapSection(gMapHeader.regionMapSectionId))) return;
    if(LoadSpriteSheet(&sheet)==0xFFFF) return;
    if(LoadSpritePalette(&palette)==0xFF) {FreeSpriteTilesByTag(0x7C52);return;}
    sprite=CreateSprite(&sMapHeartTemplate,0,0,0);
    if(sprite>=MAX_SPRITES) {Bonds_FreeMapPin();return;}
    sMapPin=sprite+1;sViewedMap=map;
    gSprites[sprite].callback=MapPinCallback;MapPinCallback(&gSprites[sprite]);
}
static void ReturnFromBondMap(void)
{
    sMapView=FALSE;Bonds_FreeMapPin();
    SetMainCallback2(CB2_ReturnToFieldContinueScriptPlayMapMusic);
}
void Script_BondsViewMap(struct ScriptContext *ctx)
{
    Bonds_GetProgress()->trackedEvent=EventIndex()+1;
    Cast_HidePortrait();HideMarker();
    sMapView=TRUE;
    FieldInitRegionMap(ReturnFromBondMap);
}
static void ClearStage(void)
{
    for(u32 i=0;i<3;i++)
    {
        u32 id=sStageActors[i];
        if(id && id<=OBJECT_EVENTS_COUNT && gObjectEvents[id-1].active
         && gObjectEvents[id-1].localId==0xF0+i)
            RemoveObjectEvent(&gObjectEvents[id-1]);
        sStageActors[i]=0;
    }
    sStageMap=0;
}
static bool32 StageTile(s16 x,s16 y,u32 elevation)
{
    if(!AreCoordsInsidePlayerMap(x+7,y+7) || MapGridGetCollisionAt(x+7,y+7)
     || MapGridGetElevationAt(x+7,y+7)!=elevation
     || MetatileBehavior_IsSurfableWaterOrUnderwater(MapGridGetMetatileBehaviorAt(x+7,y+7))) return FALSE;
    for(u32 i=0;i<OBJECT_EVENTS_COUNT;i++)
        if(gObjectEvents[i].active && gObjectEvents[i].currentCoords.x==x+7 && gObjectEvents[i].currentCoords.y==y+7) return FALSE;
    for(u32 i=0;i<gMapHeader.events->warpCount;i++)
        if(abs(gMapHeader.events->warps[i].x-x)+abs(gMapHeader.events->warps[i].y-y)<=1) return FALSE;
    for(u32 i=0;i<gMapHeader.events->coordEventCount;i++)
        if(gMapHeader.events->coordEvents[i].x==x && gMapHeader.events->coordEvents[i].y==y) return FALSE;
    return TRUE;
}
static void StageActors(u32 index)
{
    u16 graphics[3];u32 count=0,who=index/5,stage=index%5;
    const struct BondEvent *e=&sBondEvents[index];
    ClearStage();
    if(who==0 && stage==0) graphics[count++]=OBJ_EVENT_GFX_SPECIES(WURMPLE);
    if(who==2 && stage==0) graphics[count++]=OBJ_EVENT_GFX_SPECIES(WHISMUR);
    if(who==3 && stage==0) graphics[count++]=OBJ_EVENT_GFX_MAN_1;
    if(who==6 && (stage==0 || stage==3)) graphics[count++]=OBJ_EVENT_GFX_SPECIES(ELECTRIKE);
    if((who==5 || who==2) && stage==3)
    {graphics[count++]=OBJ_EVENT_GFX_WOMAN_1;graphics[count++]=OBJ_EVENT_GFX_MAN_1;graphics[count++]=OBJ_EVENT_GFX_EXPERT_M;}
    if(who==4 && (stage==0 || stage==3))
    {graphics[count++]=OBJ_EVENT_GFX_MAN_1;graphics[count++]=OBJ_EVENT_GFX_WOMAN_1;}
    if(who==9 && stage==1)
    {graphics[count++]=OBJ_EVENT_GFX_WOMAN_1;graphics[count++]=OBJ_EVENT_GFX_MAN_1;graphics[count++]=OBJ_EVENT_GFX_EXPERT_M;}
    sStageMap=e->map;
    for(u32 i=0;i<count;i++)
    {
        bool32 spawned=FALSE;
        for(s32 radius=1;radius<=4 && !spawned;radius++)
            for(s32 dy=-radius;dy<=radius && !spawned;dy++)
                for(s32 dx=-radius;dx<=radius && !spawned;dx++)
                {
                    s16 x=e->x+dx,y=e->y+dy;
                    u32 id;
                    struct ObjectEventTemplate actor={0};
                    if(abs(dx)+abs(dy)!=radius || !StageTile(x,y,MapGridGetElevationAt(e->x+7,e->y+7))) continue;
                    actor.localId=0xF0+i;actor.graphicsId=graphics[i];actor.kind=OBJ_KIND_NORMAL;
                    actor.x=x;actor.y=y;actor.elevation=MapGridGetElevationAt(x+7,y+7);
                    actor.movementType=MOVEMENT_TYPE_FACE_DOWN;
                    id=SpawnSpecialObjectEvent(&actor);
                    if(id<OBJECT_EVENTS_COUNT) {sStageActors[i]=id+1;spawned=TRUE;}
                }
    }
}
static u32 TrialBand(void)
{
    u32 hoenn=0,kanto=0;
    bool32 hclear=!!(gSaveBlock1Ptr->flags[FLAG_SYS_GAME_CLEAR/8] & (1 << (FLAG_SYS_GAME_CLEAR%8)));
    bool32 kclear=FlagGet(KANTO_FLAG_SYS_GAME_CLEAR);
    if(hclear && kclear) return 3;
    if(hclear || kclear) return 2;
    for(u32 i=0;i<8;i++)
    {
        u32 flag=FLAG_BADGE01_GET+i;
        hoenn+=!!(gSaveBlock1Ptr->flags[flag/8] & (1 << (flag%8)));
        kanto+=!!FlagGet(KANTO_FLAG_BADGE01_GET+i);
    }
    return max(hoenn,kanto)>=7?1:0;
}
bool32 Bonds_IsTraining(void) {return sTraining;}
void Script_BondsSceneRoute(struct ScriptContext *ctx)
{
    gSpecialVar_Result=sSceneEvent && (sSceneEvent-1)%5==3;
}
void Script_BondsTrainPreview(struct ScriptContext *ctx)
{
    gSpecialVar_Result=FALSE;
    if(!FourBadges() || (!sSceneEvent && Bonds_GetProgress()->people[sWho].hearts<5)
     || !Cast_IsFollowing() || Cast_Active()!=sWho+1)
    {Text(COMPOUND_STRING("Practice unlocks at personal event\nfour, with four badges in one region.\lFinish event five for later rematches.\lTravel with this companion first.$"));return;}
    sPreviewBand=TrialBand();
    Text(sBondTrialPreviews[sWho][sPreviewBand]);
    gSpecialVar_Result=TRUE;
}
void Script_BondsTrainMenu(struct ScriptContext *ctx)
{
    static const struct MenuAction items[]={
        {COMPOUND_STRING("Practice battle")},{COMPOUND_STRING("Nonbattle challenge")},
        {COMPOUND_STRING("Later")},
    };
    static const struct MenuAction rematch[]={
        {COMPOUND_STRING("Practice battle")},{COMPOUND_STRING("Later")},
    };
    Menu(sSceneEvent?items:rematch,sSceneEvent?3:2);
}
void Script_BondsTrainStart(struct ScriptContext *ctx)
{
    bool32 healthy=FALSE;
    gSpecialVar_Result=FALSE;
    if(!FourBadges() || !Cast_IsFollowing() || Cast_Active()!=sWho+1
     || (!sSceneEvent && Bonds_GetProgress()->people[sWho].hearts<5))
    {Text(COMPOUND_STRING("This practice battle is not ready.$"));return;}
    if(TrialBand()!=sPreviewBand)
    {Text(COMPOUND_STRING("The practice level has changed.\nPlease review the updated team\lbefore accepting a battle.$"));return;}
    for(u32 i=0;i<gPartiesCount[B_TRAINER_PLAYER];i++)
        if(GetMonData(&gParties[B_TRAINER_PLAYER][i],MON_DATA_HP)
         && !GetMonData(&gParties[B_TRAINER_PLAYER][i],MON_DATA_IS_EGG)) healthy=TRUE;
    if(!healthy) {Text(COMPOUND_STRING("Bring a healthy POKEMON first.$"));return;}
    sTrialMoney=GetMoney(&gSaveBlock1Ptr->money);
    sTrialBag=gSaveBlock1Ptr->bag;sTrialKey=gSaveBlock2Ptr->encryptionKey;
    memcpy(sTrialParty,gParties[B_TRAINER_PLAYER],sizeof(sTrialParty));
    sTrialPartyCount=gPartiesCount[B_TRAINER_PLAYER];
    sTraining=TRUE;sTrainingEvent=sSceneEvent!=0;
    memset(&gTrainerBattleParameter,0,sizeof(gTrainerBattleParameter));
    TRAINER_BATTLE_PARAM.opponentA=KANTO_TRAINER_BASE+634+sWho*4+TrialBand();
    TRAINER_BATTLE_PARAM.earlyRival=TRUE;
    TRAINER_BATTLE_PARAM.skipFlagCheck=TRUE;
    TRAINER_BATTLE_PARAM.rivalBattleFlags=RIVAL_BATTLE_HEAL_AFTER;
    TRAINER_BATTLE_PARAM.defeatTextA=(u8 *)COMPOUND_STRING("A good practice. Let us talk about\nwhat we noticed.$");
    TRAINER_BATTLE_PARAM.victoryText=(u8 *)COMPOUND_STRING("We can try again, or take the\nnonbattle route. No harm done.$");
    gNoOfApproachingTrainers=1;
    gSpecialVar_Result=TRUE;
}
void Script_BondsTrainEnd(struct ScriptContext *ctx)
{
    u32 key=gSaveBlock2Ptr->encryptionKey;
    bool32 won=gBattleOutcome==B_OUTCOME_WON;
    if(!sTraining) {gSpecialVar_Result=FALSE;return;}
    gSaveBlock1Ptr->bag=sTrialBag;
    gSaveBlock2Ptr->encryptionKey=sTrialKey;
    ApplyNewEncryptionKeyToBagItems(key);
    gSaveBlock2Ptr->encryptionKey=key;
    SetMoney(&gSaveBlock1Ptr->money,sTrialMoney);
    if(!won)
    {
        memcpy(gParties[B_TRAINER_PLAYER],sTrialParty,sizeof(sTrialParty));
        gPartiesCount[B_TRAINER_PLAYER]=sTrialPartyCount;
    }
    else for(u32 i=0;i<gPartiesCount[B_TRAINER_PLAYER];i++)
        for(u32 j=0;j<sTrialPartyCount;j++)
            if(GetMonData(&gParties[B_TRAINER_PLAYER][i],MON_DATA_PERSONALITY)==GetMonData(&sTrialParty[j],MON_DATA_PERSONALITY)
             && GetMonData(&gParties[B_TRAINER_PLAYER][i],MON_DATA_OT_ID)==GetMonData(&sTrialParty[j],MON_DATA_OT_ID))
            {
                u32 held=GetMonData(&sTrialParty[j],MON_DATA_HELD_ITEM);
                SetMonData(&gParties[B_TRAINER_PLAYER][i],MON_DATA_HELD_ITEM,&held);
                break;
            }
    HealPlayerParty();sTraining=FALSE;
    Text(won?COMPOUND_STRING("Practice complete. Your team and\nsupplies recover. Later rematches\lgive no Bond EXP or repeated rewards.$"):COMPOUND_STRING("Your team and supplies recover.\nNo money, Bond EXP or hearts lost.\lRetry for free or take the\lnonbattle challenge another time.$"));
    if(won && sTrainingEvent) {sTrialWon=TRUE;sScenePage=4;gSpecialVar_Result=2;}
    else {sSceneEvent=0;gSpecialVar_Result=won;}
}
#else
void Bonds_UpdateField(void) {}
bool32 Bonds_TryMarker(s16 x,s16 y) { return FALSE; }
u16 Bonds_TrackedMapSection(void) { return 0xFFFF; }
u16 Bonds_DisplayedMapSection(u16 normal) {return normal;}
bool32 Bonds_IsMapView(void) {return FALSE;}
bool32 Bonds_PositionMapView(struct RegionMap *map) {return FALSE;}
void Bonds_CreateMapPin(struct RegionMap *map) {}
void Bonds_FreeMapPin(void) {}
bool32 Bonds_IsTraining(void) {return FALSE;}
#endif
