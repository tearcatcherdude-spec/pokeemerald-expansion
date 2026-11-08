KantoNavelRock_Base_MapScripts::
	map_script MAP_SCRIPT_ON_TRANSITION, NavelRock_Base_Frlg_OnTransition
	map_script MAP_SCRIPT_ON_RESUME, NavelRock_Base_Frlg_OnResume
	.byte 0

NavelRock_Base_Frlg_OnTransition::
	call_if_set KANTO_FLAG_FOUGHT_LUGIA, NavelRock_Base_Frlg_EventScript_HideLugia
	call_if_unset KANTO_FLAG_FOUGHT_LUGIA, NavelRock_Base_Frlg_EventScript_TryShowLugia
	end

NavelRock_Base_Frlg_EventScript_HideLugia::
	setflag KANTO_FLAG_HIDE_LUGIA
	return

NavelRock_Base_Frlg_EventScript_TryShowLugia::
	goto_if_set KANTO_FLAG_LUGIA_FLEW_AWAY, Common_EventScript_NopReturn
	clearflag KANTO_FLAG_HIDE_LUGIA
	return

NavelRock_Base_Frlg_OnResume::
	call_if_set KANTO_FLAG_SYS_CTRL_OBJ_DELETE, NavelRock_Base_Frlg_EventScript_TryRemoveLugia
	end

NavelRock_Base_Frlg_EventScript_TryRemoveLugia::
	specialvar KANTO_VAR_RESULT, GetBattleOutcome
	goto_if_ne KANTO_VAR_RESULT, B_OUTCOME_CAUGHT, Common_EventScript_NopReturn
	removeobject LOCALID_NAVEL_ROCK_LUGIA
	return

NavelRock_Base_Frlg_EventScript_Lugia::
	lock
	faceplayer
	waitse
	delay 20
	playse SE_THUNDERSTORM_STOP
	setvar KANTO_VAR_0x8004, 0  @ Vertical pan
	setvar KANTO_VAR_0x8005, 3  @ Horizontal pan
	setvar KANTO_VAR_0x8006, 4  @ Num shakes
	setvar KANTO_VAR_0x8007, 2  @ Shake delay
	special ShakeScreen
	delay 30
	playse SE_THUNDERSTORM_STOP
	setvar KANTO_VAR_0x8004, 0  @ Vertical pan
	setvar KANTO_VAR_0x8005, 3  @ Horizontal pan
	setvar KANTO_VAR_0x8006, 4  @ Num shakes
	setvar KANTO_VAR_0x8007, 2  @ Shake delay
	special ShakeScreen
	delay 30
	delay 50
	waitse
	playmoncry SPECIES_LUGIA, CRY_MODE_ENCOUNTER
	waitmoncry
	delay 20
	seteventmon SPECIES_LUGIA, 70
	setflag KANTO_FLAG_SYS_CTRL_OBJ_DELETE
	special BattleSetup_StartLegendaryBattle
	clearflag KANTO_FLAG_SYS_CTRL_OBJ_DELETE
	specialvar KANTO_VAR_RESULT, GetBattleOutcome
	goto_if_eq KANTO_VAR_RESULT, B_OUTCOME_WON, NavelRock_Base_Frlg_EventScript_DefeatedLugia
	goto_if_eq KANTO_VAR_RESULT, B_OUTCOME_RAN, NavelRock_Base_Frlg_EventScript_RanFromLugia
	goto_if_eq KANTO_VAR_RESULT, B_OUTCOME_PLAYER_TELEPORTED, NavelRock_Base_Frlg_EventScript_RanFromLugia
	setflag KANTO_FLAG_FOUGHT_LUGIA
	release
	call Pip_EventScript_NPCReaction
	end

NavelRock_Base_Frlg_EventScript_DefeatedLugia::
	setflag KANTO_FLAG_LUGIA_FLEW_AWAY
	setvar KANTO_VAR_0x8004, SPECIES_LUGIA
	goto EventScript_MonFlewAway
	end

NavelRock_Base_Frlg_EventScript_RanFromLugia::
	setvar KANTO_VAR_0x8004, SPECIES_LUGIA
	goto EventScript_MonFlewAway
	end
