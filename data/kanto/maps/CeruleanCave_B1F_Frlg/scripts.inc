KantoCeruleanCave_B1F_MapScripts::
	map_script MAP_SCRIPT_ON_RESUME, CeruleanCave_B1F_OnResume
	map_script MAP_SCRIPT_ON_TRANSITION, CeruleanCave_B1F_OnTransition
	.byte 0

CeruleanCave_B1F_OnResume::
	call_if_set KANTO_FLAG_SYS_CTRL_OBJ_DELETE, CeruleanCave_B1F_EventScript_TryRemoveMewtwo
	end

CeruleanCave_B1F_EventScript_TryRemoveMewtwo::
	specialvar KANTO_VAR_RESULT, GetBattleOutcome
	goto_if_ne KANTO_VAR_RESULT, B_OUTCOME_CAUGHT, Common_EventScript_NopReturn
	removeobject KANTO_VAR_LAST_TALKED
	return

CeruleanCave_B1F_OnTransition::
	call_if_unset KANTO_FLAG_FOUGHT_MEWTWO, CeruleanCave_B1F_EventScript_ShowMewtwo
	end

CeruleanCave_B1F_EventScript_ShowMewtwo::
	clearflag KANTO_FLAG_HIDE_MEWTWO
	return

CeruleanCave_B1F_EventScript_Mewtwo::
	lock
	faceplayer
	waitse
	playmoncry SPECIES_MEWTWO, CRY_MODE_ENCOUNTER
	message CeruleanCave_B1F_Text_Mew
	waitmessage
	waitmoncry
	delay 20
	playbgm MUS_RG_ENCOUNTER_GYM_LEADER, 0
	waitbuttonpress
	setwildbattle SPECIES_MEWTWO, 70
	setflag KANTO_FLAG_SYS_CTRL_OBJ_DELETE
	special BattleSetup_StartLegendaryBattle
	clearflag KANTO_FLAG_SYS_CTRL_OBJ_DELETE
	specialvar KANTO_VAR_RESULT, GetBattleOutcome
	goto_if_eq KANTO_VAR_RESULT, B_OUTCOME_WON, CeruleanCave_B1F_EventScript_DefeatedMewtwo
	goto_if_eq KANTO_VAR_RESULT, B_OUTCOME_RAN, CeruleanCave_B1F_EventScript_RanFromMewtwo
	goto_if_eq KANTO_VAR_RESULT, B_OUTCOME_PLAYER_TELEPORTED, CeruleanCave_B1F_EventScript_RanFromMewtwo
	setflag KANTO_FLAG_FOUGHT_MEWTWO
	release
	call Pip_EventScript_NPCReaction
	end

CeruleanCave_B1F_EventScript_DefeatedMewtwo::
	setflag KANTO_FLAG_FOUGHT_MEWTWO
	goto EventScript_RemoveStaticMon
	end

CeruleanCave_B1F_EventScript_RanFromMewtwo::
	setvar KANTO_VAR_0x8004, SPECIES_MEWTWO
	goto EventScript_MonFlewAway
	end

CeruleanCave_B1F_Text_Mew::
	.string "Mew!$"
