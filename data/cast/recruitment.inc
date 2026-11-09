Cast_EventScript_Meet_Silas::
	lock
	faceplayer
	setvar VAR_0x8004, 0
	callnative Script_CastRecruitStatus
	goto_if_eq VAR_RESULT, 2, Cast_EventScript_AfterBattle
	goto_if_eq VAR_RESULT, 1, Cast_EventScript_Meet_Silas_Challenge
	msgbox gStringVar4, MSGBOX_DEFAULT
	goto Cast_EventScript_End
Cast_EventScript_Meet_Silas_Challenge::
	msgbox gStringVar4, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, Cast_EventScript_End
	callnative Script_CastCommitRequirement
	goto_if_eq VAR_RESULT, FALSE, Cast_EventScript_End
	trainerbattle_no_intro CAST_TRAINER_SILAS, Cast_Text_Silas_Defeat
	goto Cast_EventScript_AfterBattle
Cast_Text_Silas_Defeat::
	.string "The hypothesis has been\nthoroughly tackled.$"

Cast_EventScript_Meet_Kade::
	lock
	faceplayer
	setvar VAR_0x8004, 1
	callnative Script_CastRecruitStatus
	goto_if_eq VAR_RESULT, 2, Cast_EventScript_AfterBattle
	goto_if_eq VAR_RESULT, 1, Cast_EventScript_Meet_Kade_Challenge
	msgbox gStringVar4, MSGBOX_DEFAULT
	goto Cast_EventScript_End
Cast_EventScript_Meet_Kade_Challenge::
	msgbox gStringVar4, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, Cast_EventScript_End
	callnative Script_CastCommitRequirement
	goto_if_eq VAR_RESULT, FALSE, Cast_EventScript_End
	trainerbattle_no_intro CAST_TRAINER_KADE, Cast_Text_Kade_Defeat
	goto Cast_EventScript_AfterBattle
Cast_Text_Kade_Defeat::
	.string "Signed for. By every member of\nyour team.$"

Cast_EventScript_Meet_Ashe::
	lock
	faceplayer
	setvar VAR_0x8004, 2
	callnative Script_CastRecruitStatus
	goto_if_eq VAR_RESULT, 2, Cast_EventScript_AfterBattle
	goto_if_eq VAR_RESULT, 1, Cast_EventScript_Meet_Ashe_Challenge
	msgbox gStringVar4, MSGBOX_DEFAULT
	goto Cast_EventScript_End
Cast_EventScript_Meet_Ashe_Challenge::
	msgbox gStringVar4, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, Cast_EventScript_End
	callnative Script_CastCommitRequirement
	goto_if_eq VAR_RESULT, FALSE, Cast_EventScript_End
	trainerbattle_no_intro CAST_TRAINER_ASHE, Cast_Text_Ashe_Defeat
	goto Cast_EventScript_AfterBattle
Cast_Text_Ashe_Defeat::
	.string "We may need to rehearse the\nwinning part.$"

Cast_EventScript_Meet_Nico::
	lock
	faceplayer
	setvar VAR_0x8004, 3
	callnative Script_CastRecruitStatus
	goto_if_eq VAR_RESULT, 2, Cast_EventScript_AfterBattle
	goto_if_eq VAR_RESULT, 1, Cast_EventScript_Meet_Nico_Challenge
	msgbox gStringVar4, MSGBOX_DEFAULT
	goto Cast_EventScript_End
Cast_EventScript_Meet_Nico_Challenge::
	msgbox gStringVar4, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, Cast_EventScript_End
	callnative Script_CastCommitRequirement
	goto_if_eq VAR_RESULT, FALSE, Cast_EventScript_End
	trainerbattle_no_intro CAST_TRAINER_NICO, Cast_Text_Nico_Defeat
	goto Cast_EventScript_AfterBattle
Cast_Text_Nico_Defeat::
	.string "Well. That is my humble pie\nsorted.$"

Cast_EventScript_Meet_Riven::
	lock
	faceplayer
	setvar VAR_0x8004, 4
	callnative Script_CastRecruitStatus
	goto_if_eq VAR_RESULT, 2, Cast_EventScript_AfterBattle
	goto_if_eq VAR_RESULT, 1, Cast_EventScript_Meet_Riven_Challenge
	msgbox gStringVar4, MSGBOX_DEFAULT
	goto Cast_EventScript_End
Cast_EventScript_Meet_Riven_Challenge::
	msgbox gStringVar4, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, Cast_EventScript_End
	callnative Script_CastCommitRequirement
	goto_if_eq VAR_RESULT, FALSE, Cast_EventScript_End
	trainerbattle_no_intro CAST_TRAINER_RIVEN, Cast_Text_Riven_Defeat
	goto Cast_EventScript_AfterBattle
Cast_Text_Riven_Defeat::
	.string "A disappearing victory!\nUnfortunately, it was mine.$"

Cast_EventScript_Meet_Emi::
	lock
	faceplayer
	setvar VAR_0x8004, 5
	callnative Script_CastRecruitStatus
	goto_if_eq VAR_RESULT, 2, Cast_EventScript_AfterBattle
	goto_if_eq VAR_RESULT, 1, Cast_EventScript_Meet_Emi_Challenge
	msgbox gStringVar4, MSGBOX_DEFAULT
	goto Cast_EventScript_End
Cast_EventScript_Meet_Emi_Challenge::
	msgbox gStringVar4, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, Cast_EventScript_End
	callnative Script_CastCommitRequirement
	goto_if_eq VAR_RESULT, FALSE, Cast_EventScript_End
	trainerbattle_no_intro CAST_TRAINER_EMI, Cast_Text_Emi_Defeat
	goto Cast_EventScript_AfterBattle
Cast_Text_Emi_Defeat::
	.string "A tragic ending. For my winning\nstreak of zero.$"

Cast_EventScript_Meet_Vera::
	lock
	faceplayer
	setvar VAR_0x8004, 6
	callnative Script_CastRecruitStatus
	goto_if_eq VAR_RESULT, 2, Cast_EventScript_AfterBattle
	goto_if_eq VAR_RESULT, 1, Cast_EventScript_Meet_Vera_Challenge
	msgbox gStringVar4, MSGBOX_DEFAULT
	goto Cast_EventScript_End
Cast_EventScript_Meet_Vera_Challenge::
	msgbox gStringVar4, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, Cast_EventScript_End
	callnative Script_CastCommitRequirement
	goto_if_eq VAR_RESULT, FALSE, Cast_EventScript_End
	trainerbattle_no_intro CAST_TRAINER_VERA, Cast_Text_Vera_Defeat
	goto Cast_EventScript_AfterBattle
Cast_Text_Vera_Defeat::
	.string "Excellent stress test. The\nstress was me.$"

Cast_EventScript_Meet_Lume::
	lock
	faceplayer
	setvar VAR_0x8004, 7
	callnative Script_CastRecruitStatus
	goto_if_eq VAR_RESULT, 2, Cast_EventScript_AfterBattle
	goto_if_eq VAR_RESULT, 1, Cast_EventScript_Meet_Lume_Challenge
	msgbox gStringVar4, MSGBOX_DEFAULT
	goto Cast_EventScript_End
Cast_EventScript_Meet_Lume_Challenge::
	msgbox gStringVar4, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, Cast_EventScript_End
	callnative Script_CastCommitRequirement
	goto_if_eq VAR_RESULT, FALSE, Cast_EventScript_End
	trainerbattle_no_intro CAST_TRAINER_LUME, Cast_Text_Lume_Defeat
	goto Cast_EventScript_AfterBattle
Cast_Text_Lume_Defeat::
	.string "The witnesses agree: you won.$"

Cast_EventScript_Meet_Mochi::
	lock
	faceplayer
	setvar VAR_0x8004, 8
	callnative Script_CastRecruitStatus
	goto_if_eq VAR_RESULT, 2, Cast_EventScript_AfterBattle
	goto_if_eq VAR_RESULT, 1, Cast_EventScript_Meet_Mochi_Challenge
	msgbox gStringVar4, MSGBOX_DEFAULT
	goto Cast_EventScript_End
Cast_EventScript_Meet_Mochi_Challenge::
	msgbox gStringVar4, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, Cast_EventScript_End
	callnative Script_CastCommitRequirement
	goto_if_eq VAR_RESULT, FALSE, Cast_EventScript_End
	trainerbattle_no_intro CAST_TRAINER_MOCHI, Cast_Text_Mochi_Defeat
	goto Cast_EventScript_AfterBattle
Cast_Text_Mochi_Defeat::
	.string "A clean victory. Mine has a\nloose seam.$"

Cast_EventScript_Meet_Zuri::
	lock
	faceplayer
	setvar VAR_0x8004, 9
	callnative Script_CastRecruitStatus
	goto_if_eq VAR_RESULT, 2, Cast_EventScript_AfterBattle
	goto_if_eq VAR_RESULT, 1, Cast_EventScript_Meet_Zuri_Challenge
	msgbox gStringVar4, MSGBOX_DEFAULT
	goto Cast_EventScript_End
Cast_EventScript_Meet_Zuri_Challenge::
	msgbox gStringVar4, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, Cast_EventScript_End
	callnative Script_CastCommitRequirement
	goto_if_eq VAR_RESULT, FALSE, Cast_EventScript_End
	trainerbattle_no_intro CAST_TRAINER_ZURI, Cast_Text_Zuri_Defeat
	goto Cast_EventScript_AfterBattle
Cast_Text_Zuri_Defeat::
	.string "Bold composition. Devastating\nuse of my mistakes.$"

Cast_EventScript_AfterBattle::
	callnative Script_CastAfterBattle
	goto_if_eq VAR_RESULT, FALSE, Cast_EventScript_End
	msgbox gStringVar4, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, Cast_EventScript_End
	callnative Script_CastJoin
	goto_if_eq VAR_RESULT, FALSE, Cast_EventScript_Unavailable
	goto Cast_EventScript_End
Cast_EventScript_Unavailable::
	msgbox Cast_Text_Unavailable, MSGBOX_DEFAULT
Cast_EventScript_End::
	callnative Script_CastHidePortrait
	release
	end
Cast_EventScript_Companion::
	lockall
	facefollowernpc
	multichoice 0, 0, MULTI_PIP_COMPANION, FALSE
	goto_if_eq VAR_RESULT, 4, Bonds_EventScript_Journal
	goto_if_eq VAR_RESULT, 2, Cast_EventScript_Roster
	goto_if_eq VAR_RESULT, 1, Cast_EventScript_Dismiss
	goto_if_ne VAR_RESULT, 0, Cast_EventScript_Stay
	callnative Script_PipChooseDialogue
	goto_if_eq VAR_RESULT, FALSE, Cast_EventScript_Stay
	msgbox gStringVar4, MSGBOX_DEFAULT
	goto Cast_EventScript_Stay
Cast_EventScript_Dismiss::
	msgbox Cast_Text_Dismiss, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, Cast_EventScript_Stay
	callnative Script_CastFarewell
	msgbox gStringVar4, MSGBOX_DEFAULT
	callnative Script_CastDismiss
	goto Cast_EventScript_Stay
Cast_EventScript_Roster::
	multichoicegrid 0, 0, MULTI_CAST_ROSTER, 3, FALSE
	goto_if_eq VAR_RESULT, MULTI_B_PRESSED, Cast_EventScript_Stay
	goto_if_eq VAR_RESULT, 11, Cast_EventScript_Stay
	callnative Script_CastSwitchRoster
	goto_if_ne VAR_RESULT, FALSE, Cast_EventScript_Stay
	msgbox Cast_Text_Locked, MSGBOX_DEFAULT
Cast_EventScript_Stay::
	callnative Script_CastHidePortrait
	releaseall
	end
Cast_Text_Unavailable::
	.string "Your current escort needs you.\nThere is no room to change company\lright now.$"
Cast_Text_Locked::
	.string "Befriend that trainer first.\nYour current companion will stay.$"
Cast_Text_Dismiss::
	.string "Part ways for now?\nThey will return to where you met.$"
