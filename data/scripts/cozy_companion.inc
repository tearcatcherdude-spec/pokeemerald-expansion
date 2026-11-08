@ Pip: travelling companion across Hoenn. No battle partner.
@ Uses a separate test save: enabling NPC followers changes SaveBlock3.
Cozy_EventScript_Recruit::
	lock
	faceplayer
	goto_if_unset FLAG_SYS_B_DASH, Cozy_EventScript_NotYet
	checkfollowernpc
	goto_if_eq VAR_RESULT, TRUE, Cozy_EventScript_AlreadyFollowing
	goto_if_set FLAG_MET_PIP, Pip_EventScript_RecruitAgain
	msgbox Cozy_Text_Recruit, MSGBOX_YESNO
	goto Pip_EventScript_RecruitDecision
Pip_EventScript_RecruitAgain:
	msgbox Pip_Text_RecruitAgain, MSGBOX_YESNO
Pip_EventScript_RecruitDecision:
	goto_if_eq VAR_RESULT, NO, Cozy_EventScript_Decline
	msgbox Cozy_Text_Joining, MSGBOX_DEFAULT
	setflag FLAG_MET_PIP
	setfollowernpc LOCALID_COZY_COMPANION, FNPC_ALL_LAND | FNPC_ALL_WATER, Cozy_EventScript_Companion, 0
	release
	end

Cozy_EventScript_NotYet::
	msgbox Cozy_Text_NotYet, MSGBOX_DEFAULT
	release
	end

Cozy_EventScript_AlreadyFollowing::
	msgbox Cozy_Text_AlreadyFollowing, MSGBOX_DEFAULT
	release
	end

Cozy_EventScript_Decline::
	msgbox Cozy_Text_Decline, MSGBOX_DEFAULT
	release
	end

Cozy_EventScript_Companion::
	lockall
	facefollowernpc
	multichoice 0, 0, MULTI_PIP_COMPANION, FALSE
	goto_if_eq VAR_RESULT, 1, Pip_EventScript_HeadHome
	goto_if_ne VAR_RESULT, 0, Cozy_EventScript_Stay
	callnative Script_PipChooseDialogue
	goto_if_eq VAR_RESULT, FALSE, Pip_EventScript_Quiet
	msgbox gStringVar4, MSGBOX_DEFAULT
	releaseall
	end
Pip_EventScript_Quiet:
	delay 16
	releaseall
	end
Pip_EventScript_HeadHome:
	msgbox Cozy_Text_HeadHome, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, Cozy_EventScript_Stay
	msgbox Cozy_Text_GoingHome, MSGBOX_DEFAULT
	destroyfollowernpc
	clearflag FLAG_HIDE_COZY_COMPANION
	releaseall
	end

Cozy_EventScript_Stay::
	releaseall
	end

Cozy_EventScript_Gardener::
	lock
	faceplayer
	goto_if_set FLAG_COZY_BERRY_TRADE, Cozy_EventScript_GardenDone
	msgbox Cozy_Text_GardenRequest, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, Cozy_EventScript_GardenDecline
	checkitem ITEM_ORAN_BERRY, 1
	goto_if_eq VAR_RESULT, FALSE, Cozy_EventScript_NoBerry
	checkitemspace ITEM_PECHA_BERRY, 1
	goto_if_eq VAR_RESULT, FALSE, Cozy_EventScript_BagFull
	giveitem ITEM_PECHA_BERRY, 1
	goto_if_eq VAR_RESULT, FALSE, Cozy_EventScript_BagFull
	removeitem ITEM_ORAN_BERRY, 1
	setflag FLAG_COZY_BERRY_TRADE
	msgbox Cozy_Text_GardenThanks, MSGBOX_DEFAULT
	release
	end

Cozy_EventScript_GardenDecline::
	msgbox Cozy_Text_GardenDecline, MSGBOX_DEFAULT
	release
	end

Cozy_EventScript_NoBerry::
	msgbox Cozy_Text_NoBerry, MSGBOX_DEFAULT
	release
	end

Cozy_EventScript_GardenDone::
	msgbox Cozy_Text_GardenDone, MSGBOX_DEFAULT
	release
	end

Cozy_EventScript_GardenHelper::
	msgbox Cozy_Text_GardenHelper, MSGBOX_NPC
	end

Cozy_EventScript_Welcome::
	lock
	faceplayer
	goto_if_set FLAG_COZY_WELCOME_GIFT, Cozy_EventScript_WelcomeAgain
	msgbox Cozy_Text_Welcome, MSGBOX_DEFAULT
	giveitem ITEM_POTION, 1
	goto_if_eq VAR_RESULT, FALSE, Cozy_EventScript_BagFull
	setflag FLAG_COZY_WELCOME_GIFT
	msgbox Cozy_Text_WelcomeGift, MSGBOX_DEFAULT
	release
	end

Cozy_EventScript_WelcomeAgain::
	msgbox Cozy_Text_WelcomeAgain, MSGBOX_DEFAULT
	release
	end

Cozy_EventScript_WelcomeHelper::
	msgbox Cozy_Text_WelcomeHelper, MSGBOX_NPC
	end

Cozy_EventScript_BagFull::
	msgbox Cozy_Text_BagFull, MSGBOX_DEFAULT
	release
	end

Cozy_Text_Recruit::
	.string "PIP: Hey! I am Pip.\p"
	.string "Heading out? I could come along.\n"
	.string "I know a shortcut to most places.\l"
	.string "It is usually the regular path.\l"
	.string "Want some company?$"

Cozy_Text_Joining::
	.string "PIP: Great! You navigate.\n"
	.string "I will handle moral support.\l"
	.string "And identifying suspicious chairs.$"

Cozy_Text_NotYet::
	.string "You look busy getting settled.\n"
	.string "Find me after you get your\l"
	.string "RUNNING SHOES. No rush.$"

Cozy_Text_AlreadyFollowing::
	.string "You already have company!\n"
	.string "I refuse to become a queue.$"

Cozy_Text_Decline::
	.string "I will be here. Practicing being\n"
	.string "an interesting local landmark.$"

Cozy_Text_ChatOne::
	.string "PIP: Good walking today.\n"
	.string "Very convincing footwork.$"

Cozy_Text_ChatTwo::
	.string "PIP: We should pack snacks.\n"
	.string "For emergencies. Like being awake.$"

Cozy_Text_HeadHome::
	.string "Ask PIP to head home?$"

Cozy_Text_GoingHome::
	.string "PIP: See you in LITTLEROOT!\n"
	.string "Take a little walk before you\l"
	.string "look for me. I am a slow goodbye.$"

Cozy_Text_AskComment::
	.string "Ask PIP about it?$"

Cozy_Text_GardenRequest::
	.string "We are welcoming this shrub.\n"
	.string "My neighbor made it a name tag.\l"
	.string "Could you spare an ORAN BERRY?\l"
	.string "I can trade a PECHA BERRY.$"

Cozy_Text_GardenDecline::
	.string "Of course. The shrub has been\n"
	.string "very patient with us so far.$"

Cozy_Text_NoBerry::
	.string "No ORAN BERRY? Another time.\n"
	.string "We will offer it encouraging words.$"

Cozy_Text_GardenThanks::
	.string "Thank you! A fine housewarming gift.\n"
	.string "For a house with mostly roots.$"

Cozy_Text_GardenDone::
	.string "It has not said a word.\n"
	.string "I think it likes the neighborhood.$"

Cozy_Text_GardenHelper::
	.string "I wrote HELLO, I AM A SHRUB.\n"
	.string "It is important to feel seen.$"

Cozy_Text_Welcome::
	.string "Welcome to LITTLEROOT!\n"
	.string "We practiced saying that together.\l"
	.string "He came in on the wrong beat.$"

Cozy_Text_WelcomeGift::
	.string "A POTION for your travels!\n"
	.string "He wanted to give you a shrub.\l"
	.string "We are working on boundaries.$"

Cozy_Text_WelcomeAgain::
	.string "Welcome back!\n"
	.string "That one was completely unrehearsed.$"

Cozy_Text_WelcomeHelper::
	.string "I was the welcome committee.\n"
	.string "Then she joined. Now we have minutes.\l"
	.string "Most of them are about shrubs.$"

Cozy_Text_BagFull::
	.string "Your BAG is full. Come back later.\n"
	.string "We will keep this safe for you.$"

Cozy_Text_TownSign::
	.string "PIP: A town so small,\n"
	.string "even the sign knows everyone.$"

Cozy_Text_BirchsLabSign::
	.string "PIP: A whole building\n"
	.string "for asking POKéMON questions.\l"
	.string "I usually just ask the POKéMON.$"

Cozy_Text_BrendansHouseSign::
	.string "PIP: A name on a house.\n"
	.string "Bold. Now everyone knows\l"
	.string "where to return borrowed things.$"

Cozy_Text_MaysHouseSign::
	.string "PIP: Looks cozy.\n"
	.string "That is my professional opinion\l"
	.string "as someone who likes chairs.$"

Cozy_Text_PictureBookShelf::
	.string "PIP: Pictures! Finally,\n"
	.string "a book that respects my schedule.$"

Cozy_Text_BookShelf::
	.string "PIP: A guide to adventure.\n"
	.string "Chapter one says to pack carefully.\l"
	.string "We have already failed chapter one.$"

Cozy_Text_Vase::
	.string "PIP: It is empty. Finally,\n"
	.string "a vase with room for ambition.$"

Cozy_Text_EmptyTrashCan::
	.string "PIP: Nothing in there.\n"
	.string "A spotless record. Unlike mine.$"

Cozy_Text_ShopShelf::
	.string "PIP: Everything we need.\n"
	.string "And several things I could argue\l"
	.string "we need if you gave me a minute.$"

Cozy_Text_Blueprint::
	.string "PIP: I understand this.\n"
	.string "It is a building before it hatches.$"

Pip_EventScript_NPCReaction::
	callnative Script_PipBeginNPCReaction
	goto_if_eq VAR_RESULT, FALSE, Pip_EventScript_EndNPCReaction
	lockall
	msgbox Pip_Text_AskAboutThem, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, Pip_EventScript_FinishNPCReaction
	callnative Script_PipChooseNPCDialogue
	msgbox gStringVar4, MSGBOX_DEFAULT
Pip_EventScript_FinishNPCReaction:
	releaseall
Pip_EventScript_EndNPCReaction:
	callnative Script_PipEndNPCReaction
	return

Pip_Text_AskAboutThem::
	.string "Ask PIP about them?$"

Pip_Text_RecruitAgain::
	.string "PIP: Ready to head out again?\n"
	.string "My shoes were getting bored.$"

Pip_EventScript_ObjectReaction::
	callnative Script_PipBeginObjectReaction
	goto_if_eq VAR_RESULT, FALSE, Pip_EventScript_EndObjectReaction
	lockall
	msgbox Cozy_Text_AskComment, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, Pip_EventScript_FinishObjectReaction
	callnative Script_PipChooseObjectDialogue
	msgbox gStringVar4, MSGBOX_DEFAULT
Pip_EventScript_FinishObjectReaction:
	releaseall
Pip_EventScript_EndObjectReaction:
	callnative Script_PipEndNPCReaction
	return
