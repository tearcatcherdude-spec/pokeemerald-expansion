@ Runs only after the original player-initiated script has finished.
CompanionDialogue_EventScript_React::
	lockall
	callnative Script_CastBufferSpeaker
	msgbox CompanionDialogue_Text_Ask, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, CompanionDialogue_EventScript_Done
	callnative Script_CompanionDialogueChoose
	goto_if_eq VAR_RESULT, FALSE, CompanionDialogue_EventScript_Done
	msgbox gStringVar4, MSGBOX_DEFAULT
CompanionDialogue_EventScript_Done:
	releaseall
	callnative Script_CompanionDialogueRestore
	end

CompanionDialogue_EventScript_Settings::
	callnative Script_CompanionDialogueBufferMode
	msgbox gStringVar4, MSGBOX_DEFAULT
	multichoice 0, 0, MULTI_COMPANION_DIALOGUE, FALSE
	callnative Script_CompanionDialogueSetMode
	releaseall
	end

CompanionDialogue_Text_Ask:
	.string "Ask {STR_VAR_1} about that?$"
