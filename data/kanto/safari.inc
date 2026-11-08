KantoSafariZone_EventScript_OutOfBallsMidBattle::
	setvar KANTO_VAR_MAP_SCENE_FUCHSIA_CITY_SAFARI_ZONE_ENTRANCE, 3
	special ExitSafariMode
	setwarp MAP_KANTO_FUCHSIA_CITY_SAFARI_ZONE_ENTRANCE, 4, 1
	end

KantoSafariZone_EventScript_Exit::
	setvar KANTO_VAR_MAP_SCENE_FUCHSIA_CITY_SAFARI_ZONE_ENTRANCE, 1
	special ExitSafariMode
	warp MAP_KANTO_FUCHSIA_CITY_SAFARI_ZONE_ENTRANCE, 4, 1
	waitstate
	end

KantoSafariZone_EventScript_RetirePrompt::
	lockall
	msgbox KantoSafariZone_Text_WouldYouLikeToExit, MSGBOX_YESNO
	goto_if_eq KANTO_VAR_RESULT, YES, KantoSafariZone_EventScript_Retire
	releaseall
	end

KantoSafariZone_EventScript_Retire::
	goto KantoSafariZone_EventScript_Exit

KantoSafariZone_EventScript_TimesUp::
	lockall
	playse SE_DING_DONG
	message KantoSafariZone_Text_TimesUp
	waitmessage
	waitbuttonpress
	releaseall
	goto KantoSafariZone_EventScript_Exit

KantoSafariZone_EventScript_OutOfBalls::
	lockall
	playse SE_DING_DONG
	message KantoSafariZone_Text_OutOfBalls
	waitmessage
	waitbuttonpress
	releaseall
	goto KantoSafariZone_EventScript_Exit

KantoEventScript_PokeBlockFeeder::
	lockall
	special GetPokeblockFeederInFront
	goto_if_ne KANTO_VAR_RESULT, 0xFFFF, KantoSafariZone_EventScript_PokeblockPresent
	msgbox KantoSafariZone_Text_PlacePokeblockOnFeeder, MSGBOX_YESNO
	goto_if_eq KANTO_VAR_RESULT, YES, KantoSafariZone_EventScript_ChoosePokeblock
	releaseall
	end

KantoSafariZone_EventScript_ChoosePokeblock::
	fadescreen FADE_TO_BLACK
	special OpenPokeblockCaseOnFeeder
	goto_if_ne KANTO_VAR_RESULT, 0xFFFF, KantoSafariZone_EventScript_PokeblockPlaced
#ifdef BUGFIX
	releaseall  @ Only gets called from KantoEventScript_PokeBlockFeeder which uses lockall.
#endif
	end

KantoSafariZone_EventScript_PokeblockPlaced::
	message KantoSafariZone_Text_PokeblockWasPlaced
	waitmessage
	waitbuttonpress
	releaseall
	end

KantoSafariZone_EventScript_PokeblockPresent::
	message KantoSafariZone_Text_PokeblockStillHere
	waitmessage
	waitbuttonpress
	releaseall
	end

KantoSafariZone_Text_WouldYouLikeToExit:
	.string "Would you like to exit the SAFARI\n"
	.string "ZONE right now?$"

KantoSafariZone_Text_TimesUp:
	.string "Ding-dong! Time's up!\n"
	.string "Your SAFARI Game is over.$"

KantoSafariZone_Text_OutOfBalls:
	.string "You've run out of SAFARI BALLS.\n"
	.string "Your SAFARI Game is over.$"

KantoSafariZone_Text_PlacePokeblockOnFeeder:
	.string "Would you like to place a {POKEBLOCK}\n"
	.string "on the {POKEBLOCK} FEEDER?$"

KantoSafariZone_Text_PokeblockStillHere:
	.string "The {STR_VAR_1} you left\n"
	.string "before is still here.$"

KantoSafariZone_Text_PokeblockWasPlaced:
	.string "The {STR_VAR_1} was placed\n"
	.string "on the {POKEBLOCK} FEEDER.$"

KantoRoute121_SafariZoneEntrance_Text_WelcomeToSafariZone:
	.string "Welcome to the SAFARI ZONE!\p"
	.string "Here, you may witness many kinds of\n"
	.string "POKéMON rarely seen in HOENN.\p"
	.string "And, you'll see them in their wild,\n"
	.string "untamed state in natural habitats.\p"
	.string "What's more, we've thrown open the\n"
	.string "gates to POKéMON TRAINERS.\p"
	.string "You're encouraged to catch POKéMON\n"
	.string "for keeps!\p"
	.string "Come in and enjoy the SAFARI ZONE!$"

KantoRoute121_SafariZoneEntrance_Text_WelcomeFirstTime:
	.string "Welcome to the SAFARI ZONE!\n"
	.string "Is it your first time here?$"

KantoRoute121_SafariZoneEntrance_Text_ComeInAndEnjoy:
	.string "Come in and enjoy the SAFARI ZONE!$"

KantoRoute121_SafariZoneEntrance_Text_FirstTimeInfo:
	.string "When you enter the SAFARI ZONE, you\n"
	.string "start with 30 SAFARI BALLS for\l"
	.string "catching POKéMON.\p"
	.string "The SAFARI Game is over when you run\n"
	.string "out of SAFARI BALLS, or when you've\l"
	.string "walked 500 steps.\p"
	.string "Come in and enjoy the SAFARI ZONE!$"

KantoRoute121_SafariZoneEntrance_Text_WouldYouLikeToPlay:
	.string "Welcome to the SAFARI ZONE!\p"
	.string "All you can catch for just ¥500!\n"
	.string "Would you like to play a SAFARI Game?$"

KantoRoute121_SafariZoneEntrance_Text_PlayAnotherTime:
	.string "Okay.\n"
	.string "Please play another time!$"

KantoRoute121_SafariZoneEntrance_Text_NotEnoughMoney:
	.string "You don't have enough money.\n"
	.string "Sorry.$"

KantoRoute121_SafariZoneEntrance_Text_ThatWillBe500Please:
	.string "That will be ¥500, please.$"

KantoRoute121_SafariZoneEntrance_Text_HereAreYourSafariBalls:
	.string "Here are your SAFARI BALLS.$"

KantoRoute121_SafariZoneEntrance_Text_Received30SafariBalls:
	.string "{PLAYER} received 30 SAFARI BALLS.$"

KantoRoute121_SafariZoneEntrance_Text_PleaseEnjoyYourself:
	.string "We'll let you know when your game\n"
	.string "is over.\p"
	.string "So, until then, enjoy yourself, please!\n"
	.string "Off you go on your wild excursion!$"

KantoRoute121_SafariZoneEntrance_Text_PCIsFull:
	.string "Excuse me!\n"
	.string "Your PC BOX is full.$"

KantoRoute121_SafariZoneEntrance_Text_YouNeedPokeblockCase:
	.string "Excuse me!\n"
	.string "You seem to be without a {POKEBLOCK} CASE.\p"
	.string "Your SAFARI Game will be much more\n"
	.string "fruitful if you use {POKEBLOCK}S.\p"
	.string "Please come back with a {POKEBLOCK} CASE.\p"
	.string "You may obtain a {POKEBLOCK} CASE from\n"
	.string "the LILYCOVE CONTEST HALL.$"

KantoSafariZone_South_Text_StillHaveTimeExit:
	.string "You still have time left. Would you like\n"
	.string "to exit the SAFARI ZONE now?$"

KantoSafariZone_South_Text_EnjoyTheRestOfYourAdventure:
	.string "Please enjoy the rest of your wild\n"
	.string "adventure!$"

KantoSafariZone_South_Text_ExitEarlyThankYouForPlaying:
	.string "Okay.\p"
	.string "I'll take back your remaining SAFARI\n"
	.string "BALLS.\p"
	.string "Thank you for playing.\n"
	.string "We hope to see you again.$"

KantoSafariZone_South_Text_GoodLuck:
	.string "Good luck!\p"
	.string "If you need anything, don't hesitate\n"
	.string "to tell me, please!$"

KantoSafariZone_South_Text_Boy:
	.string "Did you know?\p"
	.string "If you put a {POKEBLOCK} in that square box,\n"
	.string "POKéMON gather around.$"

KantoSafariZone_South_Text_Man:
	.string "I want to keep going deeper, but I\n"
	.string "forgot to bring a BIKE.\p"
	.string "Something tells me that rare POKéMON\n"
	.string "live in the outlying areas.$"

KantoSafariZone_Southwest_Text_Woman:
	.string "Sometimes, when I toss a {POKEBLOCK} at \n"
	.string "POKéMON, it gets ignored.\p"
	.string "Do POKéMON have likes and dislikes\n"
	.string "about what they eat?$"

KantoSafariZone_Northwest_Text_Man:
	.string "Gasp… Gasp…\n"
	.string "I…made it out here…but…\p"
	.string "I'm exhausted… I don't have the\n"
	.string "energy to catch POKéMON…$"

KantoSafariZone_North_Text_Fisherman:
	.string "I'm on a mission to find WATER POKéMON\n"
	.string "you don't see in HOENN.\p"
	.string "Do you have any idea where the lake is?$"

KantoSafariZone_North_Text_Man:
	.string "I'm going to catch a lot of rare POKéMON\n"
	.string "here and trade them with my friends!$"

KantoSafariZone_South_Text_Youngster:
	.string "I put a {POKEBLOCK} on the {POKEBLOCK} FEEDER.\n"
	.string "But it seems to have disappeared.\p"
	.string "I guess POKéMON must have eaten it\n"
	.string "without me noticing.$"

KantoRoute121_SafariZoneEntrance_Text_TrainerTip:
	.string "SAFARI ZONE TRAINER TIP!\p"
	.string "Throw {POKEBLOCK}S at wild POKéMON to make\n"
	.string "them less likely to flee.$"

KantoSafariZone_Southwest_Text_RestHouseSign:
	.string "“Relieve your tired feet.”\n"
	.string "REST HOUSE$"

KantoSafariZone_RestHouse_Text_Youngster:
	.string "I don't have any {POKEBLOCK}S, but I caught\n"
	.string "a good number of POKéMON.\p"
	.string "You can improve your chances of making\n"
	.string "a catch by getting closer to them\l"
	.string "before throwing a SAFARI BALL.$"

KantoSafariZone_RestHouse_Text_PsychicM:
	.string "If you use {POKEBLOCK}S, wild POKéMON won't\n"
	.string "be so quick to run away.\p"
	.string "It's not much use to give {POKEBLOCK}S to\n"
	.string "POKéMON that don't flee easily.$"

KantoSafariZone_RestHouse_Text_FatMan:
	.string "If you put a {POKEBLOCK} on the FEEDER,\n"
	.string "POKéMON are attracted to it.\p"
	.string "I think POKéMON with the same sort of\n"
	.string "nature are drawn by a certain {POKEBLOCK}.$"

KantoSafariZone_South_Text_AreaOffLimits1:
	.string "This area is still under construction.\n"
	.string "It's off-limits, sorry!$"

KantoSafariZone_Southeast_Text_ExpansionIsFinished:
	.string "The SAFARI ZONE's expansion project\n"
	.string "is finished now.\p"
	.string "We hope you will enjoy the new area.$"

KantoSafariZone_South_Text_AreaOffLimits2:
	.string "This area is still under construction.\n"
	.string "It's off-limits, sorry!$"

KantoSafariZone_Southeast_Text_LittleGirl:
	.string "Wow! Whee! I haven't seen any of\n"
	.string "these POKéMON before!$"

KantoSafariZone_Southeast_Text_FatMan:
	.string "The POKéMON in this area are all\n"
	.string "new to me.\p"
	.string "And I'm allowed to catch these rare\n"
	.string "POKéMON! Too cool!$"

KantoSafariZone_Southeast_Text_RichBoy:
	.string "The POKéMON around here seem to be\n"
	.string "from somewhere other than HOENN.$"

KantoSafariZone_Northeast_Text_Boy:
	.string "I only have a couple SAFARI BALLS left.\p"
	.string "I'm having a hard time trying to\n"
	.string "decide what I should catch.$"

KantoSafariZone_Northeast_Text_Woman:
	.string "I heard that you can see PIKACHU here.\n"
	.string "Where might one be?$"

KantoSafariZone_Northeast_Text_Girl:
	.string "Oh, boo!\n"
	.string "I can't seem to catch anything!\p"
	.string "I'll end up wasting the admission\n"
	.string "price if I don't catch something!$"
