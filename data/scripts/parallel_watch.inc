@ Parallel Watch trial: new events only, no original Kanto story flags.
ParallelWatch_EventScript_Use::
	lockall
	callnative Script_VoidWatchIsHere
	goto_if_eq VAR_RESULT, TRUE, VoidWatch_Return
	callnative Script_ParallelWatchCheck
	goto_if_eq VAR_RESULT, FALSE, ParallelWatch_Denied
	msgbox ParallelWatch_Text_Use, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, ParallelWatch_End
	closemessage
	multichoice 0, 0, MULTI_VOID_WATCH, FALSE
	goto_if_eq VAR_RESULT, 1, VoidWatch_Enter
	goto_if_ne VAR_RESULT, 0, ParallelWatch_End
	callnative Script_ParallelWatchSwitch
	goto_if_eq VAR_RESULT, FALSE, ParallelWatch_Denied
	waitstate
	end
VoidWatch_Enter:
	callnative Script_VoidWatchEnter
	goto_if_eq VAR_RESULT, FALSE, ParallelWatch_Denied
	waitstate
	end
VoidWatch_Return:
	callnative Script_ParallelWatchCheck
	goto_if_eq VAR_RESULT, FALSE, ParallelWatch_Denied
	msgbox ParallelWatch_Text_Use, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, ParallelWatch_End
	closemessage
	callnative Script_VoidWatchReturn
	goto_if_eq VAR_RESULT, FALSE, ParallelWatch_Denied
	waitstate
	end
ParallelWatch_Denied:
	message gStringVar4
	waitmessage
	waitbuttonpress
ParallelWatch_End:
	releaseall
	end
ParallelWatch_Text_Use:
	.string "Turn the watch's hands?$"
ParallelWatch_EventScript_Pickup::
	lock
	faceplayer
	giveitem ITEM_PARALLEL_WATCH
	goto_if_eq VAR_RESULT, FALSE, ParallelWatch_EndPickup
	setflag FLAG_HIDE_PARALLEL_WATCH
	removeobject LOCALID_PARALLEL_WATCH
	msgbox ParallelWatch_Text_Found, MSGBOX_DEFAULT
ParallelWatch_EndPickup:
	release
	end
ParallelWatch_Text_Found:
	.string "The hands turn in opposite directions.$"
ParallelWatch_Nurse::
	lock
	faceplayer
	msgbox ParallelWatch_Text_Heal, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, ParallelWatch_EndPickup
	special HealPlayerParty
	playfanfare MUS_HEAL
	waitfanfare
	msgbox ParallelWatch_Text_Healed, MSGBOX_DEFAULT
	release
	end
ParallelWatch_Text_Heal:
	.string "Welcome! Rest your POKéMON here?\nVisiting teams are always welcome.$"
ParallelWatch_Text_Healed:
	.string "All rested!\nWe hope to see you again.$"
ParallelWatch_Mart::
	lock
	faceplayer
	message gText_HowMayIServeYou
	waitmessage
	pokemart ParallelWatch_Stock
	msgbox gText_PleaseComeAgain, MSGBOX_DEFAULT
	release
	end
	.align 2
ParallelWatch_Stock:
	.2byte ITEM_POKE_BALL, ITEM_POTION, ITEM_ANTIDOTE, ITEM_PARALYZE_HEAL
	pokemartlistend
ParallelWatch_WatchPallet_0::
	msgbox ParallelWatch_WatchPallet_0_Text, MSGBOX_NPC
	end
ParallelWatch_WatchPallet_0_Text:
	.string "Welcome to PALLET TOWN!\nYou look rather far from home.\pThe road north leads to VIRIDIAN.\nThe coast is closed for repairs.$"
ParallelWatch_WatchPallet_1::
	msgbox ParallelWatch_WatchPallet_1_Text, MSGBOX_NPC
	end
ParallelWatch_WatchPallet_1_Text:
	.string "I set off for a morning walk.\nIt turned into a lunch break.$"
ParallelWatch_WatchRoute1_0::
	msgbox ParallelWatch_WatchRoute1_0_Text, MSGBOX_NPC
	end
ParallelWatch_WatchRoute1_0_Text:
	.string "POKéMON live in the tall grass.\nThe ledges are a one-way shortcut.\pI learned that by trying to jump\nUP one. The ledge won.$"
ParallelWatch_WatchViridian_0::
	msgbox ParallelWatch_WatchViridian_0_Text, MSGBOX_NPC
	end
ParallelWatch_WatchViridian_0_Text:
	.string "The roads north and west are closed.\nWe are repairing the bridges.\pThe GYM is closed too. Fortunately,\nresting at the CENTER is still free.$"
ParallelWatch_WatchViridian_1::
	msgbox ParallelWatch_WatchViridian_1_Text, MSGBOX_NPC
	end
ParallelWatch_WatchViridian_1_Text:
	.string "I keep a spare key in my bag.\nNow I just need a spare bag.$"
ParallelWatch_WatchHouse1F_0::
	msgbox ParallelWatch_WatchHouse1F_0_Text, MSGBOX_NPC
	end
ParallelWatch_WatchHouse1F_0_Text:
	.string "A visitor! Make yourself at home.\nThe room upstairs is empty.\pI keep meaning to find someone\nwho understands that TV remote.$"
ParallelWatch_WatchNeighbor_0::
	msgbox ParallelWatch_WatchNeighbor_0_Text, MSGBOX_NPC
	end
ParallelWatch_WatchNeighbor_0_Text:
	.string "My brother left to become a legend.\nI asked him to bring back bread.\pLegends are very bad at errands.$"
ParallelWatch_WatchLab_0::
	msgbox ParallelWatch_WatchLab_0_Text, MSGBOX_NPC
	end
ParallelWatch_WatchLab_0_Text:
	.string "My notes were perfectly organized.\nThen I invented a better system.\pNow I have two missing notebooks.$"
ParallelWatch_WatchCenter_1::
	msgbox ParallelWatch_WatchCenter_1_Text, MSGBOX_NPC
	end
ParallelWatch_WatchCenter_1_Text:
	.string "I came in for a quick rest.\nThat was three cups of tea ago.$"
ParallelWatch_WatchHouse_0::
	msgbox ParallelWatch_WatchHouse_0_Text, MSGBOX_NPC
	end
ParallelWatch_WatchHouse_0_Text:
	.string "I moved one town over.\nIt took six boxes and three days.\pThe sofa still hasn't forgiven me.$"
ParallelWatch_WatchSchool_0::
	msgbox ParallelWatch_WatchSchool_0_Text, MSGBOX_NPC
	end
ParallelWatch_WatchSchool_0_Text:
	.string "Today we are studying type matchups.\nTomorrow: remembering them in a panic.$"
ParallelWatch_GymClosed::
	msgbox ParallelWatch_GymClosed_Text, MSGBOX_NPC
	end
ParallelWatch_GymClosed_Text:
	.string "The GYM is closed.\nA notice says: Back after lunch.$"
ParallelWatch_UpstairsClosed::
	msgbox ParallelWatch_UpstairsClosed_Text, MSGBOX_NPC
	end
ParallelWatch_UpstairsClosed_Text:
	.string "The upstairs link rooms are closed.\nThe PC and nurse are available here.$"
