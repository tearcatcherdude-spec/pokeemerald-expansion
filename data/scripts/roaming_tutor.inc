RoamingTutor_EventScript_Meet::
	lock
	faceplayer
	msgbox RoamingTutor_Text_Intro, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, RoamingTutor_End
	special ChoosePartyMon
	goto_if_ge VAR_0x8004, PARTY_SIZE, RoamingTutor_End
	callnative Script_RoamingTutorPrepare
	goto_if_eq VAR_RESULT, 0, RoamingTutor_Unavailable
	msgbox RoamingTutor_Text_Choose, MSGBOX_DEFAULT
	callnative Script_RoamingTutorMenu
	goto_if_eq VAR_RESULT, 127, RoamingTutor_End
	waitstate
	goto_if_ge VAR_RESULT, 4, RoamingTutor_End
	callnative Script_RoamingTutorExplain
	msgbox gStringVar4, MSGBOX_DEFAULT
	msgbox RoamingTutor_Text_Slot, MSGBOX_DEFAULT
	callnative Script_RoamingTutorSlotMenu
	goto_if_eq VAR_RESULT, 127, RoamingTutor_End
	waitstate
	goto_if_ge VAR_RESULT, 4, RoamingTutor_End
	copyvar VAR_0x8005, VAR_RESULT
	msgbox RoamingTutor_Text_Confirm, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, RoamingTutor_End
	callnative Script_RoamingTutorCommit
	goto_if_eq VAR_RESULT, 0, RoamingTutor_Unavailable
	msgbox RoamingTutor_Text_Done, MSGBOX_DEFAULT
	goto RoamingTutor_End

RoamingTutor_Unavailable:
	msgbox RoamingTutor_Text_Unavailable, MSGBOX_DEFAULT
RoamingTutor_End:
	release
	end

RoamingTutor_Text_Intro:
	.string "Psst. Professor Loophole. Licensed\n"
	.string "by this extremely confident hat.\p"
	.string "I can even teach a MAGIKARP!\n"
	.string "Odd methods. Sensible moves.\p"
	.string "One free lesson per POKEMON, then\n"
	.string "it must gain at least 20 levels.\p"
	.string "Types, body, level. Four extra moves.\n"
	.string "Want me to inspect your team?$"
RoamingTutor_Text_Choose:
	.string "Four for {STR_VAR_2}. B cancels.\n"
	.string "Choose one, and I will explain it.$"
RoamingTutor_Text_Slot:
	.string "Choose an empty slot or the move\n"
	.string "you want to replace. B cancels.$"
RoamingTutor_Text_Confirm:
	.string "Teach {STR_VAR_1} in this slot?\n"
	.string "Its current move will be replaced.\p"
	.string "Afterwards, this POKEMON needs\n"
	.string "20 more levels before my next lesson.$"
RoamingTutor_Text_Done:
	.string "Lesson complete! Entirely sound.\n"
	.string "Please ignore the suspicious hat.\p"
	.string "That POKEMON needs 20 more levels\n"
	.string "before I can teach it again.$"
RoamingTutor_Text_Unavailable:
	.string "No lesson today. A previous pupil\n"
	.string "needs 20 levels since its last one.\p"
	.string "I also need four safe extra\n"
	.string "moves. Eggs cannot take lessons.\p"
	.string "I will not erase an HM, either.\n"
	.string "Some techniques need more practice.$"
