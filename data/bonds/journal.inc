Bonds_EventScript_Journal::
	callnative Script_BondsJournalIntro
	goto_if_eq VAR_RESULT, FALSE, Bonds_EventScript_ChooseFriend
	msgbox gStringVar4, MSGBOX_DEFAULT
Bonds_EventScript_ChooseFriend::
	callnative Script_CastHidePortrait
	multichoicegrid 0, 0, MULTI_CAST_ROSTER, 3, FALSE
	goto_if_eq VAR_RESULT, MULTI_B_PRESSED, Bonds_EventScript_Close
	goto_if_eq VAR_RESULT, 11, Bonds_EventScript_Close
	callnative Script_BondsSelect
	goto_if_eq VAR_RESULT, FALSE, Bonds_EventScript_ChooseFriend
Bonds_EventScript_Status::
	callnative Script_BondsStatus
	msgbox gStringVar4, MSGBOX_DEFAULT
Bonds_EventScript_Menu::
	callnative Script_BondsMenu
	waitstate
	goto_if_eq VAR_RESULT, 0, Bonds_EventScript_Event
	goto_if_eq VAR_RESULT, 1, Bonds_EventScript_Gift
	goto_if_eq VAR_RESULT, 2, Bonds_EventScript_Story
	goto_if_eq VAR_RESULT, 3, Bonds_EventScript_Relationship
	goto_if_eq VAR_RESULT, 4, Bonds_EventScript_More
	goto Bonds_EventScript_ChooseFriend
Bonds_EventScript_More::
	callnative Script_BondsMoreMenu
	waitstate
	goto_if_eq VAR_RESULT, 0, Bonds_EventScript_Rest
	goto_if_eq VAR_RESULT, 1, Bonds_EventScript_Details
	goto_if_eq VAR_RESULT, 2, Bonds_EventScript_Tutor
	goto_if_eq VAR_RESULT, 3, Bonds_EventScript_Keepsake
	goto_if_eq VAR_RESULT, 4, Bonds_EventScript_Train
	goto Bonds_EventScript_Menu
Bonds_EventScript_Event::
	callnative Script_BondsEventInfo
	goto_if_eq VAR_RESULT, FALSE, Bonds_EventScript_InfoOnly
	msgbox gStringVar4, MSGBOX_DEFAULT
	callnative Script_BondsEventMenu
	waitstate
	goto_if_eq VAR_RESULT, 0, Bonds_EventScript_Track
	goto_if_eq VAR_RESULT, 1, Bonds_EventScript_Meet
	goto_if_eq VAR_RESULT, 2, Bonds_EventScript_ViewMap
	goto_if_eq VAR_RESULT, 3, Bonds_EventScript_RewardInfo
	goto Bonds_EventScript_Menu
Bonds_EventScript_Track::
	callnative Script_BondsTrack
	goto Bonds_EventScript_InfoOnly
Bonds_EventScript_RewardInfo::
	callnative Script_BondsRewardInfo
	goto Bonds_EventScript_InfoOnly
Bonds_EventScript_Meet::
	msgbox Bonds_Text_Begin, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, Bonds_EventScript_Menu
	callnative Script_BondsMeet
	goto_if_eq VAR_RESULT, FALSE, Bonds_EventScript_InfoOnly
	goto Bonds_EventScript_SceneBegin
Bonds_EventScript_ViewMap::
	callnative Script_BondsViewMap
	waitstate
	goto Bonds_EventScript_Menu
Bonds_EventScript_Story::
	callnative Script_BondsStory
	goto Bonds_EventScript_InfoOnly
Bonds_EventScript_Details::
	callnative Script_BondsDetails
	goto Bonds_EventScript_InfoOnly
Bonds_EventScript_Keepsake::
	callnative Script_BondsKeepsake
	goto Bonds_EventScript_InfoOnly
Bonds_EventScript_Rest::
	msgbox Bonds_Text_Rest, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, Bonds_EventScript_Menu
	callnative Script_BondsRest
	goto Bonds_EventScript_InfoOnly
Bonds_EventScript_Relationship::
	callnative Script_BondsInterestMenu
	waitstate
	goto_if_ge VAR_RESULT, 4, Bonds_EventScript_Menu
	copyvar VAR_0x800A, VAR_RESULT
	msgbox Bonds_Text_Relationship, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, Bonds_EventScript_Menu
	copyvar VAR_RESULT, VAR_0x800A
	callnative Script_BondsInterest
	goto Bonds_EventScript_InfoOnly
Bonds_EventScript_Gift::
	callnative Script_BondsGiftMenu
	waitstate
	goto_if_ge VAR_RESULT, 3, Bonds_EventScript_Menu
	callnative Script_BondsGiftPreview
	goto_if_eq VAR_RESULT, FALSE, Bonds_EventScript_InfoOnly
	msgbox gStringVar4, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, Bonds_EventScript_Menu
	callnative Script_BondsGiftCommit
	goto Bonds_EventScript_InfoOnly
Bonds_EventScript_Tutor::
	callnative Script_BondsTutorMenu
	waitstate
	goto_if_ge VAR_RESULT, 2, Bonds_EventScript_Menu
	callnative Script_BondsTutor
	goto_if_eq VAR_RESULT, FALSE, Bonds_EventScript_InfoOnly
	msgbox Bonds_Text_Tutor, MSGBOX_DEFAULT
	call MoveTutor_EventScript_OpenBox
	goto Bonds_EventScript_Menu
Bonds_EventScript_InfoOnly::
	msgbox gStringVar4, MSGBOX_DEFAULT
	callnative Script_CastHidePortrait
	goto Bonds_EventScript_Menu
Bonds_EventScript_Marker::
	lockall
	facefollowernpc
	msgbox Bonds_Text_Begin, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, Bonds_EventScript_Close
	callnative Script_BondsMeet
	goto_if_eq VAR_RESULT, FALSE, Bonds_EventScript_MarkerError
Bonds_EventScript_SceneBegin::
	callnative Script_BondsSceneIntro
	msgbox gStringVar4, MSGBOX_DEFAULT
	callnative Script_BondsSceneRoute
	goto_if_ne VAR_RESULT, FALSE, Bonds_EventScript_EventTrial
Bonds_EventScript_Scene::
	callnative Script_BondsScenePage
	goto_if_eq VAR_RESULT, 1, Bonds_EventScript_SceneText
	goto_if_eq VAR_RESULT, 2, Bonds_EventScript_SceneChoice
	goto_if_eq VAR_RESULT, 3, Bonds_EventScript_Complete
	goto Bonds_EventScript_Close
Bonds_EventScript_SceneText::
	msgbox gStringVar4, MSGBOX_DEFAULT
	goto Bonds_EventScript_Scene
Bonds_EventScript_SceneChoice::
	callnative Script_BondsSceneChoiceMenu
	waitstate
	callnative Script_BondsSceneChoice
	goto_if_eq VAR_RESULT, FALSE, Bonds_EventScript_MarkerError
	goto Bonds_EventScript_Scene
Bonds_EventScript_Complete::
	callnative Script_BondsSceneComplete
	msgbox gStringVar4, MSGBOX_DEFAULT
	goto Bonds_EventScript_Close
Bonds_EventScript_MarkerError::
	msgbox gStringVar4, MSGBOX_DEFAULT
Bonds_EventScript_Close::
	callnative Script_BondsClose
	releaseall
	end
Bonds_EventScript_Train::
	callnative Script_BondsTrainPreview
	goto_if_eq VAR_RESULT, FALSE, Bonds_EventScript_InfoOnly
	msgbox gStringVar4, MSGBOX_DEFAULT
	callnative Script_BondsTrainMenu
	waitstate
	goto_if_ne VAR_RESULT, 0, Bonds_EventScript_Menu
	callnative Script_BondsTrainStart
	goto_if_eq VAR_RESULT, FALSE, Bonds_EventScript_InfoOnly
	dotrainerbattle
	callnative Script_BondsTrainEnd
	goto Bonds_EventScript_InfoOnly
Bonds_EventScript_EventTrial::
	callnative Script_BondsTrainPreview
	goto_if_eq VAR_RESULT, FALSE, Bonds_EventScript_MarkerError
	msgbox gStringVar4, MSGBOX_DEFAULT
	callnative Script_BondsTrainMenu
	waitstate
	goto_if_eq VAR_RESULT, 1, Bonds_EventScript_Scene
	goto_if_ne VAR_RESULT, 0, Bonds_EventScript_Close
	callnative Script_BondsTrainStart
	goto_if_eq VAR_RESULT, FALSE, Bonds_EventScript_MarkerError
	dotrainerbattle
	callnative Script_BondsTrainEnd
	goto_if_eq VAR_RESULT, 2, Bonds_EventScript_Scene
	goto Bonds_EventScript_MarkerError
Bonds_Text_Begin::
	.string "Begin this personal event?\nYou can choose Later without\llosing affection or the invitation.$"
Bonds_Text_Rest::
	.string "Rest and start another outing?\nRequires 2048 on-foot steps together\land a nearby POKEMON CENTER.\lRest itself gives no EXP.$"
Bonds_Text_Relationship::
	.string "Talk about this choice together?\nOnly one committed romance at a time.\lFriendship and all earned rewards\lremain after a respectful breakup.$"
Bonds_Text_Tutor::
	.string "Choose a compatible POKEMON.\nThis move reward is reusable and\lcosts no item, money or affection.$"
