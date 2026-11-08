KantoMtEmber_Summit_MapScripts::
	map_script MAP_SCRIPT_ON_TRANSITION, MtEmber_Summit_OnTransition
	map_script MAP_SCRIPT_ON_RESUME, MtEmber_Summit_OnResume
	.byte 0

MtEmber_Summit_OnResume::
	call_if_set KANTO_FLAG_SYS_CTRL_OBJ_DELETE, MtEmber_Summit_EventScript_TryRemoveMoltres
	end

MtEmber_Summit_EventScript_TryRemoveMoltres::
	specialvar KANTO_VAR_RESULT, GetBattleOutcome
	goto_if_ne KANTO_VAR_RESULT, B_OUTCOME_CAUGHT, Common_EventScript_NopReturn
	removeobject KANTO_VAR_LAST_TALKED
	return

MtEmber_Summit_OnTransition::
	call_if_unset KANTO_FLAG_FOUGHT_MOLTRES, MtEmber_Summit_EventScript_ShowMoltres
	end

MtEmber_Summit_EventScript_ShowMoltres::
	clearflag KANTO_FLAG_HIDE_MOLTRES
	return

MtEmber_Summit_EventScript_Moltres::
	lock
	faceplayer
	setwildbattle SPECIES_MOLTRES, 50
	waitse
	playmoncry SPECIES_MOLTRES, CRY_MODE_ENCOUNTER
	message Text_Gyaoo
	waitmessage
	waitmoncry
	delay 10
	playbgm MUS_RG_ENCOUNTER_GYM_LEADER, 0
	waitbuttonpress
	setflag KANTO_FLAG_SYS_CTRL_OBJ_DELETE
	special BattleSetup_StartLegendaryBattle
	clearflag KANTO_FLAG_SYS_CTRL_OBJ_DELETE
	specialvar KANTO_VAR_RESULT, GetBattleOutcome
	goto_if_eq KANTO_VAR_RESULT, B_OUTCOME_WON, MtEmber_Summit_EventScript_DefeatedMoltres
	goto_if_eq KANTO_VAR_RESULT, B_OUTCOME_RAN, MtEmber_Summit_EventScript_RanFromMoltres
	goto_if_eq KANTO_VAR_RESULT, B_OUTCOME_PLAYER_TELEPORTED, MtEmber_Summit_EventScript_RanFromMoltres
	setflag KANTO_FLAG_FOUGHT_MOLTRES
	release
	end

MtEmber_Summit_EventScript_DefeatedMoltres::
	setflag KANTO_FLAG_FOUGHT_MOLTRES
	goto EventScript_RemoveStaticMon
	end

MtEmber_Summit_EventScript_RanFromMoltres::
	setvar KANTO_VAR_0x8004, SPECIES_MOLTRES
	goto EventScript_MonFlewAway
	end
