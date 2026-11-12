PipPractice_EventScript::
	callnative Script_PipPracticePreview
	goto_if_eq VAR_RESULT, FALSE, PipPractice_NotReady
	msgbox gStringVar4, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, PipPractice_End
	callnative Script_PipPracticeStart
	goto_if_eq VAR_RESULT, FALSE, PipPractice_End
	dotrainerbattle
	releaseall
	end
PipPractice_NotReady:
	msgbox gStringVar4, MSGBOX_DEFAULT
	goto PipPractice_End

PipPractice_End:
	releaseall
	end
