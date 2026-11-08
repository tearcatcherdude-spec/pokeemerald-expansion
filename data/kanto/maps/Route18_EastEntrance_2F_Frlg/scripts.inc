KantoRoute18_EastEntrance_2F_MapScripts::
	.byte 0

Route18_EastEntrance_2F_EventScript_LeftBinoculars::
	msgbox Route18_EastEntrance_2F_Text_PalletTownInWest, MSGBOX_SIGN
	end

Route18_EastEntrance_2F_EventScript_RightBinoculars::
	msgbox Route18_EastEntrance_2F_Text_PeopleSwimming, MSGBOX_SIGN
	end

Route18_EastEntrance_2F_EventScript_Haden::
	lock
	faceplayer
	setvar KANTO_VAR_0x8008, INGAME_TRADE_LICKITUNG
	call EventScript_GetInGameTradeSpeciesInfo
	goto_if_set KANTO_FLAG_DID_MARC_TRADE, Route18_EastEntrance_2F_EventScript_AlreadyTraded
	msgbox Trade_Text_LookingForMonWannaTradeForMon, MSGBOX_YESNO
	goto_if_eq KANTO_VAR_RESULT, NO, Route18_EastEntrance_2F_EventScript_DeclineTrade
	call EventScript_ChooseMonForInGameTrade
	goto_if_ge KANTO_VAR_0x8004, PARTY_SIZE, Route18_EastEntrance_2F_EventScript_DeclineTrade
	call EventScript_GetInGameTradeSpecies
	goto_if_ne KANTO_VAR_RESULT, KANTO_VAR_0x8009, Route18_EastEntrance_2F_EventScript_NotRequestedMon
	call EventScript_DoInGameTrade
	msgbox Trade_Text_HeyThanks
	setflag KANTO_FLAG_DID_MARC_TRADE
	release
	call Pip_EventScript_NPCReaction
	end

Route18_EastEntrance_2F_EventScript_DeclineTrade::
	msgbox Trade_Text_AwwOhWell
	release
	call Pip_EventScript_NPCReaction
	end

Route18_EastEntrance_2F_EventScript_NotRequestedMon::
	bufferspeciesname STR_VAR_1, KANTO_VAR_0x8009
	msgbox Trade_Text_WhatThatsNoMon
	release
	call Pip_EventScript_NPCReaction
	end

Route18_EastEntrance_2F_EventScript_AlreadyTraded::
	msgbox Trade_Text_IsntMyOldMonGreat
	release
	call Pip_EventScript_NPCReaction
	end

Route18_EastEntrance_2F_Text_PalletTownInWest::
	.string "Let's see what the binoculars have\n"
	.string "to show…\p"
	.string "PALLET TOWN is in the west.$"

Route18_EastEntrance_2F_Text_PeopleSwimming::
	.string "Let's see what the binoculars have\n"
	.string "to show…\p"
	.string "There are people swimming.$"
