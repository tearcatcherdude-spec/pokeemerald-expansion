@ Cozy upperworld prototype. Existing human art; no battle partner.
@ Uses a separate test save: enabling NPC followers changes SaveBlock3.
Cozy_EventScript_Recruit::
	lock
	faceplayer
	goto_if_unset FLAG_SYS_B_DASH, Cozy_EventScript_NotYet
	checkfollowernpc
	goto_if_eq VAR_RESULT, TRUE, Cozy_EventScript_AlreadyFollowing
	msgbox Cozy_Text_Recruit, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, Cozy_EventScript_Decline
	msgbox Cozy_Text_Joining, MSGBOX_DEFAULT
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
	addvar VAR_COZY_COMPANION_CHAT, 1
	call_if_eq VAR_COZY_COMPANION_CHAT, 1, Cozy_EventScript_ChatOne
	call_if_ge VAR_COZY_COMPANION_CHAT, 2, Cozy_EventScript_ChatTwo
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

Cozy_EventScript_ChatOne::
	msgbox Cozy_Text_ChatOne, MSGBOX_DEFAULT
	return

Cozy_EventScript_ChatTwo::
	msgbox Cozy_Text_ChatTwo, MSGBOX_DEFAULT
	setvar VAR_COZY_COMPANION_CHAT, 0
	return

@ Do not comment for an unrelated follower. No automatic text after inspection.
Cozy_EventScript_AskComment::
	setvar VAR_RESULT, FALSE
	goto_if_unset FLAG_HIDE_COZY_COMPANION, Cozy_EventScript_NoComment
	checkfollowernpc
	goto_if_eq VAR_RESULT, FALSE, Cozy_EventScript_NoComment
	lockall
	msgbox Cozy_Text_AskComment, MSGBOX_YESNO
	releaseall
	return

Cozy_EventScript_NoComment::
	return

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

Cozy_EventScript_InspectTownSign::
	call Cozy_EventScript_AskComment
	call_if_eq VAR_RESULT, YES, Cozy_EventScript_CommentTownSign
	return

Cozy_EventScript_CommentTownSign::
	msgbox Cozy_Text_TownSign, MSGBOX_SIGN
	return

Cozy_EventScript_InspectBirchsLabSign::
	call Cozy_EventScript_AskComment
	call_if_eq VAR_RESULT, YES, Cozy_EventScript_CommentBirchsLabSign
	return

Cozy_EventScript_CommentBirchsLabSign::
	msgbox Cozy_Text_BirchsLabSign, MSGBOX_SIGN
	return

Cozy_EventScript_InspectBrendansHouseSign::
	call Cozy_EventScript_AskComment
	call_if_eq VAR_RESULT, YES, Cozy_EventScript_CommentBrendansHouseSign
	return

Cozy_EventScript_CommentBrendansHouseSign::
	msgbox Cozy_Text_BrendansHouseSign, MSGBOX_SIGN
	return

Cozy_EventScript_InspectMaysHouseSign::
	call Cozy_EventScript_AskComment
	call_if_eq VAR_RESULT, YES, Cozy_EventScript_CommentMaysHouseSign
	return

Cozy_EventScript_CommentMaysHouseSign::
	msgbox Cozy_Text_MaysHouseSign, MSGBOX_SIGN
	return

Cozy_EventScript_InspectPictureBookShelf::
	call Cozy_EventScript_AskComment
	call_if_eq VAR_RESULT, YES, Cozy_EventScript_CommentPictureBookShelf
	return

Cozy_EventScript_CommentPictureBookShelf::
	msgbox Cozy_Text_PictureBookShelf, MSGBOX_SIGN
	return

Cozy_EventScript_InspectBookShelf::
	call Cozy_EventScript_AskComment
	call_if_eq VAR_RESULT, YES, Cozy_EventScript_CommentBookShelf
	return

Cozy_EventScript_CommentBookShelf::
	msgbox Cozy_Text_BookShelf, MSGBOX_SIGN
	return

Cozy_EventScript_InspectVase::
	call Cozy_EventScript_AskComment
	call_if_eq VAR_RESULT, YES, Cozy_EventScript_CommentVase
	return

Cozy_EventScript_CommentVase::
	msgbox Cozy_Text_Vase, MSGBOX_SIGN
	return

Cozy_EventScript_InspectEmptyTrashCan::
	call Cozy_EventScript_AskComment
	call_if_eq VAR_RESULT, YES, Cozy_EventScript_CommentEmptyTrashCan
	return

Cozy_EventScript_CommentEmptyTrashCan::
	msgbox Cozy_Text_EmptyTrashCan, MSGBOX_SIGN
	return

Cozy_EventScript_InspectShopShelf::
	call Cozy_EventScript_AskComment
	call_if_eq VAR_RESULT, YES, Cozy_EventScript_CommentShopShelf
	return

Cozy_EventScript_CommentShopShelf::
	msgbox Cozy_Text_ShopShelf, MSGBOX_SIGN
	return

Cozy_EventScript_InspectBlueprint::
	call Cozy_EventScript_AskComment
	call_if_eq VAR_RESULT, YES, Cozy_EventScript_CommentBlueprint
	return

Cozy_EventScript_CommentBlueprint::
	msgbox Cozy_Text_Blueprint, MSGBOX_SIGN
	return

Cozy_Text_Recruit::
	.string "Heading out? I could come along.\n"
	.string "I know a shortcut to most places.\l"
	.string "It is usually the regular path.\l"
	.string "Want some company?$"

Cozy_Text_Joining::
	.string "COMPANION: Great! You navigate.\n"
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
	.string "COMPANION: Good walking today.\n"
	.string "Very convincing footwork.$"

Cozy_Text_ChatTwo::
	.string "COMPANION: We should pack snacks.\n"
	.string "For emergencies. Like being awake.$"

Cozy_Text_HeadHome::
	.string "Ask your companion to head home?$"

Cozy_Text_GoingHome::
	.string "COMPANION: See you in LITTLEROOT!\n"
	.string "Take a little walk before you\l"
	.string "look for me. I am a slow goodbye.$"

Cozy_Text_AskComment::
	.string "Ask your companion about it?$"

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
	.string "COMPANION: A town so small,\n"
	.string "even the sign knows everyone.$"

Cozy_Text_BirchsLabSign::
	.string "COMPANION: A whole building\n"
	.string "for asking POKéMON questions.\l"
	.string "I usually just ask the POKéMON.$"

Cozy_Text_BrendansHouseSign::
	.string "COMPANION: A name on a house.\n"
	.string "Bold. Now everyone knows\l"
	.string "where to return borrowed things.$"

Cozy_Text_MaysHouseSign::
	.string "COMPANION: Looks cozy.\n"
	.string "That is my professional opinion\l"
	.string "as someone who likes chairs.$"

Cozy_Text_PictureBookShelf::
	.string "COMPANION: Pictures! Finally,\n"
	.string "a book that respects my schedule.$"

Cozy_Text_BookShelf::
	.string "COMPANION: A guide to adventure.\n"
	.string "Chapter one says to pack carefully.\l"
	.string "We have already failed chapter one.$"

Cozy_Text_Vase::
	.string "COMPANION: It lives on sunlight\n"
	.string "and water. Show-off.$"

Cozy_Text_EmptyTrashCan::
	.string "COMPANION: Nothing in there.\n"
	.string "A spotless record. Unlike mine.$"

Cozy_Text_ShopShelf::
	.string "COMPANION: Everything we need.\n"
	.string "And several things I could argue\l"
	.string "we need if you gave me a minute.$"

Cozy_Text_Blueprint::
	.string "COMPANION: I understand this.\n"
	.string "It is a building before it hatches.$"
