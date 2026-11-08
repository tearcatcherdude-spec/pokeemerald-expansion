KantoFiveIsland_Harbor_MapScripts::
	.byte 0

FiveIsland_Harbor_EventScript_Sailor::
	lock
	faceplayer
	message Text_WhereDoYouWantToSail
	waitmessage
	setvar KANTO_VAR_0x8004, SEAGALLOP_FIVE_ISLAND
	goto EventScript_ChooseDestFromIsland
	end
