PipPractice_EventScript::
	callnative Script_PipPracticePreview
	goto_if_eq VAR_RESULT, FALSE, PipPractice_NotReady
	msgbox gStringVar4, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, Cozy_EventScript_Stay
	callnative Script_PipPracticeStart
	goto_if_eq VAR_RESULT, FALSE, Cozy_EventScript_Stay
	dotrainerbattle
	releaseall
	end
PipPractice_NotReady:
	msgbox gStringVar4, MSGBOX_DEFAULT
	goto Cozy_EventScript_Stay
