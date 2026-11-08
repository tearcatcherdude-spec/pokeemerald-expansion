@ Authored Hoenn scenes. Original terrain and event positions stay intact.

World_EventScript_Rare0_0::
	lock
	faceplayer
	goto_if_set FLAG_TEMP_10, World_Rare0_Rest
	msgbox World_Rare0_Intro, MSGBOX_DEFAULT
	msgbox World_Text_Invite, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, World_Rare0_Decline
	setvar VAR_0x8004, 0
	callnative Script_CozyWorldPrepareRare
	goto_if_eq VAR_RESULT, FALSE, World_Rare_NoTeam
	msgbox World_Rare0_Accept, MSGBOX_DEFAULT
	setwildbattle SPECIES_SENTRET, 5
	callnative Script_CozyWorldTrainRare
	dowildbattle
	specialvar VAR_RESULT, GetBattleOutcome
	goto_if_eq VAR_RESULT, B_OUTCOME_CAUGHT, World_Rare0_Caught
	setflag FLAG_TEMP_10
	msgbox World_Rare0_RestText, MSGBOX_DEFAULT
	release
	end
World_Rare0_Caught:
	setflag FLAG_WORLD_CAUGHT_SENTRET
	removeobject LOCALID_LIVING_Rare0_0
	msgbox World_Text_Caught, MSGBOX_DEFAULT
	setvar VAR_0x8004, 21
	call World_EventScript_PipReaction
	release
	end
World_Rare0_Decline:
	msgbox World_Rare0_DeclineText, MSGBOX_DEFAULT
	release
	end
World_Rare0_Rest:
	msgbox World_Rare0_RestText, MSGBOX_DEFAULT
	release
	end

World_Rare0_Intro::
	.string "This SENTRET stands on its tail to\ninspect the crossroads. It seems to\lbe interviewing travelers about the\lquality of their snacks.$"


World_Rare0_Accept::
	.string "It checks your pockets, then settles\ninto a battle stance. A tryout,\lapparently. You can catch it in this\lbattle.$"


World_Rare0_DeclineText::
	.string "It returns to surveying the road. The\nsnack research continues.$"


World_Rare0_RestText::
	.string "It is resting its tail. Perhaps come\nback after taking a walk.$"


World_Pip_21::
	.string "PIP: It has a better recruitment\nprocess than I did.$"


World_EventScript_Rare1_0::
	lock
	faceplayer
	goto_if_set FLAG_TEMP_10, World_Rare1_Rest
	msgbox World_Rare1_Intro, MSGBOX_DEFAULT
	msgbox World_Text_Invite, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, World_Rare1_Decline
	setvar VAR_0x8004, 1
	callnative Script_CozyWorldPrepareRare
	goto_if_eq VAR_RESULT, FALSE, World_Rare_NoTeam
	msgbox World_Rare1_Accept, MSGBOX_DEFAULT
	setwildbattle SPECIES_SHINX, 7
	callnative Script_CozyWorldTrainRare
	dowildbattle
	specialvar VAR_RESULT, GetBattleOutcome
	goto_if_eq VAR_RESULT, B_OUTCOME_CAUGHT, World_Rare1_Caught
	setflag FLAG_TEMP_10
	msgbox World_Rare1_RestText, MSGBOX_DEFAULT
	release
	end
World_Rare1_Caught:
	setflag FLAG_WORLD_CAUGHT_SHINX
	removeobject LOCALID_LIVING_Rare1_0
	msgbox World_Text_Caught, MSGBOX_DEFAULT
	setvar VAR_0x8004, 22
	call World_EventScript_PipReaction
	release
	end
World_Rare1_Decline:
	msgbox World_Rare1_DeclineText, MSGBOX_DEFAULT
	release
	end
World_Rare1_Rest:
	msgbox World_Rare1_RestText, MSGBOX_DEFAULT
	release
	end

World_Rare1_Intro::
	.string "This SHINX is practicing a fearsome\nroar. Each attempt surprises it\lslightly more than the listener.$"


World_Rare1_Accept::
	.string "It notices you watching and wants a\nproper audience. Win its trust in a\lwild battle; you can catch it.$"


World_Rare1_DeclineText::
	.string "It tries again, a little louder. You\ntactfully look impressed.$"


World_Rare1_RestText::
	.string "It is taking a quiet break between\nvery small roars. Come back later.$"


World_Pip_22::
	.string "PIP: That was a brave noise. We should\nnot mention the squeak.$"


World_EventScript_Rare2_0::
	lock
	faceplayer
	goto_if_set FLAG_TEMP_10, World_Rare2_Rest
	msgbox World_Rare2_Intro, MSGBOX_DEFAULT
	msgbox World_Text_Invite, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, World_Rare2_Decline
	setvar VAR_0x8004, 2
	callnative Script_CozyWorldPrepareRare
	goto_if_eq VAR_RESULT, FALSE, World_Rare_NoTeam
	msgbox World_Rare2_Accept, MSGBOX_DEFAULT
	setwildbattle SPECIES_EEVEE, 10
	callnative Script_CozyWorldTrainRare
	dowildbattle
	specialvar VAR_RESULT, GetBattleOutcome
	goto_if_eq VAR_RESULT, B_OUTCOME_CAUGHT, World_Rare2_Caught
	setflag FLAG_TEMP_10
	msgbox World_Rare2_RestText, MSGBOX_DEFAULT
	release
	end
World_Rare2_Caught:
	setflag FLAG_WORLD_CAUGHT_EEVEE
	removeobject LOCALID_LIVING_Rare2_0
	msgbox World_Text_Caught, MSGBOX_DEFAULT
	setvar VAR_0x8004, 23
	call World_EventScript_PipReaction
	release
	end
World_Rare2_Decline:
	msgbox World_Rare2_DeclineText, MSGBOX_DEFAULT
	release
	end
World_Rare2_Rest:
	msgbox World_Rare2_RestText, MSGBOX_DEFAULT
	release
	end

World_Rare2_Intro::
	.string "This EEVEE appears to be weighing\nthe pros and cons of being wild\lversus having a trainer. The trainer\lcolumn currently contains regular\lmeals.$"


World_Rare2_Accept::
	.string "It adds adventure to the list, then\nchallenges you to a battle. You can\lcatch it if you are ready.$"


World_Rare2_DeclineText::
	.string "It resumes the debate. Being able to\nnap wherever it likes remains a\lpowerful argument.$"


World_Rare2_RestText::
	.string "It has put the debate on hold for a\nnap. Try visiting again later.$"


World_Pip_23::
	.string "PIP: A carefully considered career\nmove. I respect the lunch clause.$"


World_EventScript_Rare3_0::
	lock
	faceplayer
	goto_if_set FLAG_TEMP_10, World_Rare3_Rest
	msgbox World_Rare3_Intro, MSGBOX_DEFAULT
	msgbox World_Text_Invite, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, World_Rare3_Decline
	setvar VAR_0x8004, 3
	callnative Script_CozyWorldPrepareRare
	goto_if_eq VAR_RESULT, FALSE, World_Rare_NoTeam
	msgbox World_Rare3_Accept, MSGBOX_DEFAULT
	setwildbattle SPECIES_MAREEP, 12
	callnative Script_CozyWorldTrainRare
	dowildbattle
	specialvar VAR_RESULT, GetBattleOutcome
	goto_if_eq VAR_RESULT, B_OUTCOME_CAUGHT, World_Rare3_Caught
	setflag FLAG_TEMP_10
	msgbox World_Rare3_RestText, MSGBOX_DEFAULT
	release
	end
World_Rare3_Caught:
	setflag FLAG_WORLD_CAUGHT_MAREEP
	removeobject LOCALID_LIVING_Rare3_0
	msgbox World_Text_Caught, MSGBOX_DEFAULT
	setvar VAR_0x8004, 24
	call World_EventScript_PipReaction
	release
	end
World_Rare3_Decline:
	msgbox World_Rare3_DeclineText, MSGBOX_DEFAULT
	release
	end
World_Rare3_Rest:
	msgbox World_Rare3_RestText, MSGBOX_DEFAULT
	release
	end

World_Rare3_Intro::
	.string "This MAREEP keeps rubbing against a\nrock, then looking offended when its\lwool crackles. It seems to blame the\lrock.$"


World_Rare3_Accept::
	.string "It approaches you cautiously.\nPerhaps traveling together would\lmean fewer arguments with rocks. It\lwants a battle first; you can catch\lit.$"


World_Rare3_DeclineText::
	.string "It returns to the rock. Negotiations\nare not going well.$"


World_Rare3_RestText::
	.string "Its wool is settling down. Give it a\nlittle time before another battle.$"


World_Pip_24::
	.string "PIP: We could introduce it to a very\nunderstanding sweater.$"


World_EventScript_Rare4_0::
	lock
	faceplayer
	goto_if_set FLAG_TEMP_10, World_Rare4_Rest
	msgbox World_Rare4_Intro, MSGBOX_DEFAULT
	msgbox World_Text_Invite, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, World_Rare4_Decline
	setvar VAR_0x8004, 4
	callnative Script_CozyWorldPrepareRare
	goto_if_eq VAR_RESULT, FALSE, World_Rare_NoTeam
	msgbox World_Rare4_Accept, MSGBOX_DEFAULT
	setwildbattle SPECIES_RIOLU, 15
	callnative Script_CozyWorldTrainRare
	dowildbattle
	specialvar VAR_RESULT, GetBattleOutcome
	goto_if_eq VAR_RESULT, B_OUTCOME_CAUGHT, World_Rare4_Caught
	setflag FLAG_TEMP_10
	msgbox World_Rare4_RestText, MSGBOX_DEFAULT
	release
	end
World_Rare4_Caught:
	setflag FLAG_WORLD_CAUGHT_RIOLU
	removeobject LOCALID_LIVING_Rare4_0
	msgbox World_Text_Caught, MSGBOX_DEFAULT
	setvar VAR_0x8004, 25
	call World_EventScript_PipReaction
	release
	end
World_Rare4_Decline:
	msgbox World_Rare4_DeclineText, MSGBOX_DEFAULT
	release
	end
World_Rare4_Rest:
	msgbox World_Rare4_RestText, MSGBOX_DEFAULT
	release
	end

World_Rare4_Intro::
	.string "This RIOLU mirrors the footsteps of\ntrainers leaving the GYM. It appears\lto be searching for a partner who will\lpractice rather than just pose.$"


World_Rare4_Accept::
	.string "It bows to you. A friendly battle\nseems to be its interview. You can\lcatch it during the match.$"


World_Rare4_DeclineText::
	.string "It bows again and returns to its\nfootwork. No hard feelings.$"


World_Rare4_RestText::
	.string "It is stretching after the match.\nCome back after a walk.$"


World_Pip_25::
	.string "PIP: I have been practicing standing\nsupportively. Perhaps it will count.$"


World_EventScript_Rare5_0::
	lock
	faceplayer
	goto_if_set FLAG_TEMP_10, World_Rare5_Rest
	msgbox World_Rare5_Intro, MSGBOX_DEFAULT
	msgbox World_Text_Invite, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, World_Rare5_Decline
	setvar VAR_0x8004, 5
	callnative Script_CozyWorldPrepareRare
	goto_if_eq VAR_RESULT, FALSE, World_Rare_NoTeam
	msgbox World_Rare5_Accept, MSGBOX_DEFAULT
	setwildbattle SPECIES_TOGEPI, 17
	callnative Script_CozyWorldTrainRare
	dowildbattle
	specialvar VAR_RESULT, GetBattleOutcome
	goto_if_eq VAR_RESULT, B_OUTCOME_CAUGHT, World_Rare5_Caught
	setflag FLAG_TEMP_10
	msgbox World_Rare5_RestText, MSGBOX_DEFAULT
	release
	end
World_Rare5_Caught:
	setflag FLAG_WORLD_CAUGHT_TOGEPI
	removeobject LOCALID_LIVING_Rare5_0
	msgbox World_Text_Caught, MSGBOX_DEFAULT
	setvar VAR_0x8004, 26
	call World_EventScript_PipReaction
	release
	end
World_Rare5_Decline:
	msgbox World_Rare5_DeclineText, MSGBOX_DEFAULT
	release
	end
World_Rare5_Rest:
	msgbox World_Rare5_RestText, MSGBOX_DEFAULT
	release
	end

World_Rare5_Intro::
	.string "This TOGEPI has gathered several\nfallen petals. It appears to be\lmaking the quietest parade in the\lworld.$"


World_Rare5_Accept::
	.string "It gives you one petal and bounces\ninto a playful battle stance. You can\lcatch it in this battle.$"


World_Rare5_DeclineText::
	.string "It adds another petal to the parade.\nYou have been allowed to watch.$"


World_Rare5_RestText::
	.string "The parade has stopped for a nap.\nPlease visit again later.$"


World_Pip_26::
	.string "PIP: A parade with no drums. Quiet\nClub will be delighted.$"


World_EventScript_Rare6_0::
	lock
	faceplayer
	goto_if_set FLAG_TEMP_10, World_Rare6_Rest
	msgbox World_Rare6_Intro, MSGBOX_DEFAULT
	msgbox World_Text_Invite, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, World_Rare6_Decline
	setvar VAR_0x8004, 6
	callnative Script_CozyWorldPrepareRare
	goto_if_eq VAR_RESULT, FALSE, World_Rare_NoTeam
	msgbox World_Rare6_Accept, MSGBOX_DEFAULT
	setwildbattle SPECIES_WOOPER, 18
	callnative Script_CozyWorldTrainRare
	dowildbattle
	specialvar VAR_RESULT, GetBattleOutcome
	goto_if_eq VAR_RESULT, B_OUTCOME_CAUGHT, World_Rare6_Caught
	setflag FLAG_TEMP_10
	msgbox World_Rare6_RestText, MSGBOX_DEFAULT
	release
	end
World_Rare6_Caught:
	setflag FLAG_WORLD_CAUGHT_WOOPER
	removeobject LOCALID_LIVING_Rare6_0
	msgbox World_Text_Caught, MSGBOX_DEFAULT
	setvar VAR_0x8004, 27
	call World_EventScript_PipReaction
	release
	end
World_Rare6_Decline:
	msgbox World_Rare6_DeclineText, MSGBOX_DEFAULT
	release
	end
World_Rare6_Rest:
	msgbox World_Rare6_RestText, MSGBOX_DEFAULT
	release
	end

World_Rare6_Intro::
	.string "This WOOPER is sitting beside a\npuddle with a leaf on its head. It\llooks deeply satisfied with its\lrecent promotion to pond supervisor.$"


World_Rare6_Accept::
	.string "It seems willing to supervise your\ntravels instead. A wild battle will\lsettle the appointment; you can\lcatch it.$"


World_Rare6_DeclineText::
	.string "It nods at the puddle. Important\nwork remains.$"


World_Rare6_RestText::
	.string "The supervisor is on a break. Come\nback after some exploring.$"


World_Pip_27::
	.string "PIP: I would happily report to\nsomeone with that expression.$"


World_EventScript_Rare7_0::
	lock
	faceplayer
	goto_if_set FLAG_TEMP_10, World_Rare7_Rest
	msgbox World_Rare7_Intro, MSGBOX_DEFAULT
	msgbox World_Text_Invite, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, World_Rare7_Decline
	setvar VAR_0x8004, 7
	callnative Script_CozyWorldPrepareRare
	goto_if_eq VAR_RESULT, FALSE, World_Rare_NoTeam
	msgbox World_Rare7_Accept, MSGBOX_DEFAULT
	setwildbattle SPECIES_HOUNDOUR, 23
	callnative Script_CozyWorldTrainRare
	dowildbattle
	specialvar VAR_RESULT, GetBattleOutcome
	goto_if_eq VAR_RESULT, B_OUTCOME_CAUGHT, World_Rare7_Caught
	setflag FLAG_TEMP_10
	msgbox World_Rare7_RestText, MSGBOX_DEFAULT
	release
	end
World_Rare7_Caught:
	setflag FLAG_WORLD_CAUGHT_HOUNDOUR
	removeobject LOCALID_LIVING_Rare7_0
	msgbox World_Text_Caught, MSGBOX_DEFAULT
	setvar VAR_0x8004, 28
	call World_EventScript_PipReaction
	release
	end
World_Rare7_Decline:
	msgbox World_Rare7_DeclineText, MSGBOX_DEFAULT
	release
	end
World_Rare7_Rest:
	msgbox World_Rare7_RestText, MSGBOX_DEFAULT
	release
	end

World_Rare7_Intro::
	.string "This HOUNDOUR is guarding a patch of\nwarm ground. It has apparently\ldecided the patch is a very small hot\lspring and it is the attendant.$"


World_Rare7_Accept::
	.string "It sniffs your shoes and steps\nforward. It wants to test a\lprospective traveling partner in\lbattle. You can catch it.$"


World_Rare7_DeclineText::
	.string "It resumes its duties. The patch is in\nsafe paws.$"


World_Rare7_RestText::
	.string "It is cooling off after the battle.\nGive it some time.$"


World_Pip_28::
	.string "PIP: It has the same job as the towel\nmarshal, with more actual authority.$"


World_EventScript_Rare8_0::
	lock
	faceplayer
	goto_if_set FLAG_TEMP_10, World_Rare8_Rest
	msgbox World_Rare8_Intro, MSGBOX_DEFAULT
	msgbox World_Text_Invite, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, World_Rare8_Decline
	setvar VAR_0x8004, 8
	callnative Script_CozyWorldPrepareRare
	goto_if_eq VAR_RESULT, FALSE, World_Rare_NoTeam
	msgbox World_Rare8_Accept, MSGBOX_DEFAULT
	setwildbattle SPECIES_GIBLE, 25
	callnative Script_CozyWorldTrainRare
	dowildbattle
	specialvar VAR_RESULT, GetBattleOutcome
	goto_if_eq VAR_RESULT, B_OUTCOME_CAUGHT, World_Rare8_Caught
	setflag FLAG_TEMP_10
	msgbox World_Rare8_RestText, MSGBOX_DEFAULT
	release
	end
World_Rare8_Caught:
	setflag FLAG_WORLD_CAUGHT_GIBLE
	removeobject LOCALID_LIVING_Rare8_0
	msgbox World_Text_Caught, MSGBOX_DEFAULT
	setvar VAR_0x8004, 29
	call World_EventScript_PipReaction
	release
	end
World_Rare8_Decline:
	msgbox World_Rare8_DeclineText, MSGBOX_DEFAULT
	release
	end
World_Rare8_Rest:
	msgbox World_Rare8_RestText, MSGBOX_DEFAULT
	release
	end

World_Rare8_Intro::
	.string "This GIBLE is trying to fit a round\nstone into a square gap. It looks\lprepared to change the stone, the\lgap, or possibly the mountain.$"


World_Rare8_Accept::
	.string "It notices your team and becomes\ninterested in a more portable\lproject. It challenges you; you can\lcatch it during battle.$"


World_Rare8_DeclineText::
	.string "It returns to the stone with renewed\nand slightly alarming determination.$"


World_Rare8_RestText::
	.string "It is resting beside its project. Try\nagain on another visit.$"


World_Pip_29::
	.string "PIP: Let us avoid promising it any\nload-bearing walls.$"


World_EventScript_Rare9_0::
	lock
	faceplayer
	goto_if_set FLAG_TEMP_10, World_Rare9_Rest
	msgbox World_Rare9_Intro, MSGBOX_DEFAULT
	msgbox World_Text_Invite, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, World_Rare9_Decline
	setvar VAR_0x8004, 9
	callnative Script_CozyWorldPrepareRare
	goto_if_eq VAR_RESULT, FALSE, World_Rare_NoTeam
	msgbox World_Rare9_Accept, MSGBOX_DEFAULT
	setwildbattle SPECIES_MUNCHLAX, 26
	callnative Script_CozyWorldTrainRare
	dowildbattle
	specialvar VAR_RESULT, GetBattleOutcome
	goto_if_eq VAR_RESULT, B_OUTCOME_CAUGHT, World_Rare9_Caught
	setflag FLAG_TEMP_10
	msgbox World_Rare9_RestText, MSGBOX_DEFAULT
	release
	end
World_Rare9_Caught:
	setflag FLAG_WORLD_CAUGHT_MUNCHLAX
	removeobject LOCALID_LIVING_Rare9_0
	msgbox World_Text_Caught, MSGBOX_DEFAULT
	setvar VAR_0x8004, 30
	call World_EventScript_PipReaction
	release
	end
World_Rare9_Decline:
	msgbox World_Rare9_DeclineText, MSGBOX_DEFAULT
	release
	end
World_Rare9_Rest:
	msgbox World_Rare9_RestText, MSGBOX_DEFAULT
	release
	end

World_Rare9_Intro::
	.string "This MUNCHLAX has sorted its lunch\ninto now and later. It keeps moving\litems from later into now, which\lappears to be a serious\ladministrative problem.$"


World_Rare9_Accept::
	.string "It studies your bag and decides a\ntrainer might help with provisions. It\lwants a battle first; you can catch\lit.$"


World_Rare9_DeclineText::
	.string "It resumes the sorting. The later pile\nis in considerable trouble.$"


World_Rare9_RestText::
	.string "Lunch has become a nap. Come back on\nanother visit.$"


World_Pip_30::
	.string "PIP: I understand its filing system\nrather too well.$"


World_EventScript_Rare10_0::
	lock
	faceplayer
	goto_if_set FLAG_TEMP_10, World_Rare10_Rest
	msgbox World_Rare10_Intro, MSGBOX_DEFAULT
	msgbox World_Text_Invite, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, World_Rare10_Decline
	setvar VAR_0x8004, 10
	callnative Script_CozyWorldPrepareRare
	goto_if_eq VAR_RESULT, FALSE, World_Rare_NoTeam
	msgbox World_Rare10_Accept, MSGBOX_DEFAULT
	setwildbattle SPECIES_DRATINI, 29
	callnative Script_CozyWorldTrainRare
	dowildbattle
	specialvar VAR_RESULT, GetBattleOutcome
	goto_if_eq VAR_RESULT, B_OUTCOME_CAUGHT, World_Rare10_Caught
	setflag FLAG_TEMP_10
	msgbox World_Rare10_RestText, MSGBOX_DEFAULT
	release
	end
World_Rare10_Caught:
	setflag FLAG_WORLD_CAUGHT_DRATINI
	removeobject LOCALID_LIVING_Rare10_0
	msgbox World_Text_Caught, MSGBOX_DEFAULT
	setvar VAR_0x8004, 31
	call World_EventScript_PipReaction
	release
	end
World_Rare10_Decline:
	msgbox World_Rare10_DeclineText, MSGBOX_DEFAULT
	release
	end
World_Rare10_Rest:
	msgbox World_Rare10_RestText, MSGBOX_DEFAULT
	release
	end

World_Rare10_Intro::
	.string "This DRATINI is watching raindrops\nmake circles in the water. It seems\lreluctant to leave, but keeps\lglancing toward the road.$"


World_Rare10_Accept::
	.string "It swims closer. Perhaps it wants to\nsee what makes circles somewhere\lelse. It offers you a battle; you can\lcatch it.$"


World_Rare10_DeclineText::
	.string "It settles back by the bank. You\nwatch a few more circles together.$"


World_Rare10_RestText::
	.string "It is sheltering quietly after the\nbattle. Visit again later.$"


World_Pip_31::
	.string "PIP: We can take the long way if it\nwants. There are usually more\lpuddles.$"


World_EventScript_Rare11_0::
	lock
	faceplayer
	goto_if_set FLAG_TEMP_10, World_Rare11_Rest
	msgbox World_Rare11_Intro, MSGBOX_DEFAULT
	msgbox World_Text_Invite, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, World_Rare11_Decline
	setvar VAR_0x8004, 11
	callnative Script_CozyWorldPrepareRare
	goto_if_eq VAR_RESULT, FALSE, World_Rare_NoTeam
	msgbox World_Rare11_Accept, MSGBOX_DEFAULT
	setwildbattle SPECIES_CROAGUNK, 32
	callnative Script_CozyWorldTrainRare
	dowildbattle
	specialvar VAR_RESULT, GetBattleOutcome
	goto_if_eq VAR_RESULT, B_OUTCOME_CAUGHT, World_Rare11_Caught
	setflag FLAG_TEMP_10
	msgbox World_Rare11_RestText, MSGBOX_DEFAULT
	release
	end
World_Rare11_Caught:
	setflag FLAG_WORLD_CAUGHT_CROAGUNK
	removeobject LOCALID_LIVING_Rare11_0
	msgbox World_Text_Caught, MSGBOX_DEFAULT
	setvar VAR_0x8004, 32
	call World_EventScript_PipReaction
	release
	end
World_Rare11_Decline:
	msgbox World_Rare11_DeclineText, MSGBOX_DEFAULT
	release
	end
World_Rare11_Rest:
	msgbox World_Rare11_RestText, MSGBOX_DEFAULT
	release
	end

World_Rare11_Intro::
	.string "This CROAGUNK is performing to an\naudience of mushrooms. The\lmushrooms have maintained a very\lprofessional silence.$"


World_Rare11_Accept::
	.string "It turns to you and takes a\ntheatrical battle pose. An audition\lwith a live audience! You can catch it\lin this battle.$"


World_Rare11_DeclineText::
	.string "It returns to the mushrooms. Their\nreview remains difficult to read.$"


World_Rare11_RestText::
	.string "The performer is taking an interval.\nTry again later.$"


World_Pip_32::
	.string "PIP: I will clap at the end. Somebody\nought to.$"


World_EventScript_Rare12_0::
	lock
	faceplayer
	goto_if_set FLAG_TEMP_10, World_Rare12_Rest
	msgbox World_Rare12_Intro, MSGBOX_DEFAULT
	msgbox World_Text_Invite, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, World_Rare12_Decline
	setvar VAR_0x8004, 12
	callnative Script_CozyWorldPrepareRare
	goto_if_eq VAR_RESULT, FALSE, World_Rare_NoTeam
	msgbox World_Rare12_Accept, MSGBOX_DEFAULT
	setwildbattle SPECIES_PORYGON, 33
	callnative Script_CozyWorldTrainRare
	dowildbattle
	specialvar VAR_RESULT, GetBattleOutcome
	goto_if_eq VAR_RESULT, B_OUTCOME_CAUGHT, World_Rare12_Caught
	setflag FLAG_TEMP_10
	msgbox World_Rare12_RestText, MSGBOX_DEFAULT
	release
	end
World_Rare12_Caught:
	setflag FLAG_WORLD_CAUGHT_PORYGON
	removeobject LOCALID_LIVING_Rare12_0
	msgbox World_Text_Caught, MSGBOX_DEFAULT
	setvar VAR_0x8004, 33
	call World_EventScript_PipReaction
	release
	end
World_Rare12_Decline:
	msgbox World_Rare12_DeclineText, MSGBOX_DEFAULT
	release
	end
World_Rare12_Rest:
	msgbox World_Rare12_RestText, MSGBOX_DEFAULT
	release
	end

World_Rare12_Intro::
	.string "This PORYGON is facing a sign, turning\naround, then facing it again. It\lappears to be deciding whether going\loutside was a software update.$"


World_Rare12_Accept::
	.string "It focuses on your bag. A journey may\noffer useful data. It initiates a wild\lbattle; you can catch it.$"


World_Rare12_DeclineText::
	.string "It resumes studying the sign. The\noutdoors remains under evaluation.$"


World_Rare12_RestText::
	.string "It appears to be processing the last\nbattle. Come back after a walk.$"


World_Pip_33::
	.string "PIP: It has been outside longer than\nsome people I know and is still taking\lnotes.$"


World_EventScript_Rare13_0::
	lock
	faceplayer
	goto_if_set FLAG_TEMP_10, World_Rare13_Rest
	msgbox World_Rare13_Intro, MSGBOX_DEFAULT
	msgbox World_Text_Invite, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, World_Rare13_Decline
	setvar VAR_0x8004, 13
	callnative Script_CozyWorldPrepareRare
	goto_if_eq VAR_RESULT, FALSE, World_Rare_NoTeam
	msgbox World_Rare13_Accept, MSGBOX_DEFAULT
	setwildbattle SPECIES_ELEKID, 35
	callnative Script_CozyWorldTrainRare
	dowildbattle
	specialvar VAR_RESULT, GetBattleOutcome
	goto_if_eq VAR_RESULT, B_OUTCOME_CAUGHT, World_Rare13_Caught
	setflag FLAG_TEMP_10
	msgbox World_Rare13_RestText, MSGBOX_DEFAULT
	release
	end
World_Rare13_Caught:
	setflag FLAG_WORLD_CAUGHT_ELEKID
	removeobject LOCALID_LIVING_Rare13_0
	msgbox World_Text_Caught, MSGBOX_DEFAULT
	setvar VAR_0x8004, 34
	call World_EventScript_PipReaction
	release
	end
World_Rare13_Decline:
	msgbox World_Rare13_DeclineText, MSGBOX_DEFAULT
	release
	end
World_Rare13_Rest:
	msgbox World_Rare13_RestText, MSGBOX_DEFAULT
	release
	end

World_Rare13_Intro::
	.string "This ELEKID keeps pointing at the\nSPACE CENTER, then winding its arms.\lIt seems convinced the rocket needs\lan enthusiastic hand crank.$"


World_Rare13_Accept::
	.string "It demonstrates its power and waits\nfor you. A battle seems to be its\lpractical exam; you can catch it.$"


World_Rare13_DeclineText::
	.string "It returns to monitoring the launch\nfacilities. Nobody has requested a\lhand crank yet.$"


World_Rare13_RestText::
	.string "It is recharging after the\ndemonstration. Visit again later.$"


World_Pip_34::
	.string "PIP: I hope they find a job for it\nbefore it finds a socket.$"


World_EventScript_Rare14_0::
	lock
	faceplayer
	goto_if_set FLAG_TEMP_10, World_Rare14_Rest
	msgbox World_Rare14_Intro, MSGBOX_DEFAULT
	msgbox World_Text_Invite, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, World_Rare14_Decline
	setvar VAR_0x8004, 14
	callnative Script_CozyWorldPrepareRare
	goto_if_eq VAR_RESULT, FALSE, World_Rare_NoTeam
	msgbox World_Rare14_Accept, MSGBOX_DEFAULT
	setwildbattle SPECIES_LARVITAR, 38
	callnative Script_CozyWorldTrainRare
	dowildbattle
	specialvar VAR_RESULT, GetBattleOutcome
	goto_if_eq VAR_RESULT, B_OUTCOME_CAUGHT, World_Rare14_Caught
	setflag FLAG_TEMP_10
	msgbox World_Rare14_RestText, MSGBOX_DEFAULT
	release
	end
World_Rare14_Caught:
	setflag FLAG_WORLD_CAUGHT_LARVITAR
	removeobject LOCALID_LIVING_Rare14_0
	msgbox World_Text_Caught, MSGBOX_DEFAULT
	setvar VAR_0x8004, 35
	call World_EventScript_PipReaction
	release
	end
World_Rare14_Decline:
	msgbox World_Rare14_DeclineText, MSGBOX_DEFAULT
	release
	end
World_Rare14_Rest:
	msgbox World_Rare14_RestText, MSGBOX_DEFAULT
	release
	end

World_Rare14_Intro::
	.string "This LARVITAR has taken one bite\nfrom several stones. It appears to be\lreviewing the local geology, with\lstrong opinions about the texture.$"


World_Rare14_Accept::
	.string "It looks at your team with interest.\nPerhaps travel would broaden its\lmenu. It wants a battle first; you can\lcatch it.$"


World_Rare14_DeclineText::
	.string "It returns to its reviews. One pebble\nreceives an unusually thoughtful\lnod.$"


World_Rare14_RestText::
	.string "The reviewer is resting. Please come\nback on another visit.$"


World_Pip_35::
	.string "PIP: I will ask before borrowing\nanything from its lunch bag.$"


World_EventScript_Rare15_0::
	lock
	faceplayer
	goto_if_set FLAG_TEMP_10, World_Rare15_Rest
	msgbox World_Rare15_Intro, MSGBOX_DEFAULT
	msgbox World_Text_Invite, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, World_Rare15_Decline
	setvar VAR_0x8004, 15
	callnative Script_CozyWorldPrepareRare
	goto_if_eq VAR_RESULT, FALSE, World_Rare_NoTeam
	msgbox World_Rare15_Accept, MSGBOX_DEFAULT
	setwildbattle SPECIES_DEINO, 42
	callnative Script_CozyWorldTrainRare
	dowildbattle
	specialvar VAR_RESULT, GetBattleOutcome
	goto_if_eq VAR_RESULT, B_OUTCOME_CAUGHT, World_Rare15_Caught
	setflag FLAG_TEMP_10
	msgbox World_Rare15_RestText, MSGBOX_DEFAULT
	release
	end
World_Rare15_Caught:
	setflag FLAG_WORLD_CAUGHT_DEINO
	removeobject LOCALID_LIVING_Rare15_0
	msgbox World_Text_Caught, MSGBOX_DEFAULT
	setvar VAR_0x8004, 36
	call World_EventScript_PipReaction
	release
	end
World_Rare15_Decline:
	msgbox World_Rare15_DeclineText, MSGBOX_DEFAULT
	release
	end
World_Rare15_Rest:
	msgbox World_Rare15_RestText, MSGBOX_DEFAULT
	release
	end

World_Rare15_Intro::
	.string "This DEINO has been carefully\nfollowing its own footsteps in a\lcircle. It seems determined to find\lthe trainer whose trail smells\lexactly like itself.$"


World_Rare15_Accept::
	.string "It hears you and approaches. Maybe\nfollowing a real companion would be\leasier. It challenges you; you can\lcatch it.$"


World_Rare15_DeclineText::
	.string "It returns to the trail, still hopeful.\nYou leave its path clear.$"


World_Rare15_RestText::
	.string "It is resting after the battle. Come\nback on another visit.$"


World_Pip_36::
	.string "PIP: Getting lost is easier with\nsomeone who will admit it. I can\lprovide references.$"


World_EventScript_Scene0_0::
	lock
	faceplayer
	goto_if_set FLAG_WORLD_SCENE_0, World_Scene0_Done

	msgbox World_Scene0_Intro, MSGBOX_DEFAULT

	setflag FLAG_WORLD_SCENE_0
World_Scene0_Done:
	msgbox World_Scene0_DoneText, MSGBOX_DEFAULT
	setvar VAR_0x8004, 0
	call World_EventScript_PipReaction
	release
	end
World_EventScript_Scene0_1::
	lock
	faceplayer
	goto_if_set FLAG_WORLD_SCENE_0, World_Scene0_PartnerAfter
	msgbox World_Scene0_Before, MSGBOX_DEFAULT
	release
	end
World_Scene0_PartnerAfter:
	msgbox World_Scene0_After, MSGBOX_DEFAULT
	setvar VAR_0x8004, 0
	call World_EventScript_PipReaction
	release
	end

World_Scene0_Intro::
	.string "MAP CLUB: We are drawing a map of\ntown. Our first disagreement is\lwhether my house should be larger.$"


World_Scene0_Before::
	.string "MAP CLUB SECRETARY: His house is the\nsame size as mine. He has drawn a\lsecond floor containing his\lconfidence.$"


World_Scene0_DoneText::
	.string "MAP CLUB: We voted to use actual\nmeasurements. Democracy has been\ldifficult for my house.$"


World_Scene0_After::
	.string "MAP CLUB SECRETARY: The map is now\naccurate. His confidence has been\lmoved to the margins.$"


World_Pip_0::
	.string "PIP: A very small town has still\nmanaged to invent a planning dispute.$"


World_EventScript_Scene1_0::
	lock
	faceplayer
	goto_if_set FLAG_WORLD_SCENE_1, World_Scene1_Done

	msgbox World_Scene1_Intro, MSGBOX_DEFAULT

	giveitem ITEM_POTION, 1
	goto_if_eq VAR_RESULT, FALSE, World_RewardFull

	setflag FLAG_WORLD_SCENE_1
World_Scene1_Done:
	msgbox World_Scene1_DoneText, MSGBOX_DEFAULT
	setvar VAR_0x8004, 1
	call World_EventScript_PipReaction
	release
	end
World_EventScript_Scene1_1::
	lock
	faceplayer
	goto_if_set FLAG_WORLD_SCENE_1, World_Scene1_PartnerAfter
	msgbox World_Scene1_Before, MSGBOX_DEFAULT
	release
	end
World_Scene1_PartnerAfter:
	msgbox World_Scene1_After, MSGBOX_DEFAULT
	setvar VAR_0x8004, 1
	call World_EventScript_PipReaction
	release
	end

World_Scene1_Intro::
	.string "POND INSPECTOR: We check the pond\nevery morning. Still wet. We do not\llike to rush a conclusion.$"


World_Scene1_Before::
	.string "ASSISTANT INSPECTOR: I record the\nfindings. The notebook is getting\lsurprisingly damp.$"


World_Scene1_DoneText::
	.string "POND INSPECTOR: Another conclusive\ninspection. Please take a POTION. For\lworking under these conditions.$"


World_Scene1_After::
	.string "ASSISTANT INSPECTOR: He calls it\nfieldwork. We are standing four steps\lfrom his kitchen.$"


World_Pip_1::
	.string "PIP: A job with clear expectations\nand a nearby kitchen. Tempting.$"


World_EventScript_Scene2_0::
	lock
	faceplayer
	goto_if_set FLAG_WORLD_SCENE_2, World_Scene2_Done

	msgbox World_Scene2_Intro, MSGBOX_DEFAULT

	setflag FLAG_WORLD_SCENE_2
World_Scene2_Done:
	msgbox World_Scene2_DoneText, MSGBOX_DEFAULT
	setvar VAR_0x8004, 2
	call World_EventScript_PipReaction
	release
	end
World_EventScript_Scene2_1::
	lock
	faceplayer
	goto_if_set FLAG_WORLD_SCENE_2, World_Scene2_PartnerAfter
	msgbox World_Scene2_Before, MSGBOX_DEFAULT
	release
	end
World_Scene2_PartnerAfter:
	msgbox World_Scene2_After, MSGBOX_DEFAULT
	setvar VAR_0x8004, 2
	call World_EventScript_PipReaction
	release
	end

World_Scene2_Intro::
	.string "DEVON INTERN: My invention sorts\nrocks by how interesting they are. It\lcurrently puts all of them first.$"


World_Scene2_Before::
	.string "SCHOOL STUDENT: I suggested a\nsecond setting called less\linteresting. The machine looked\ldisappointed.$"


World_Scene2_DoneText::
	.string "DEVON INTERN: We have renamed it the\nRock Appreciation Device. It now\lworks perfectly.$"


World_Scene2_After::
	.string "SCHOOL STUDENT: My science teacher\nsays changing the question is\lsometimes science.$"


World_Pip_2::
	.string "PIP: They fixed it by being kinder to\nrocks. I approve of the new\lspecification.$"


World_EventScript_Scene3_0::
	lock
	faceplayer
	goto_if_set FLAG_WORLD_SCENE_3, World_Scene3_Done

	msgbox World_Scene3_Intro, MSGBOX_DEFAULT

	giveitem ITEM_GREAT_BALL, 1
	goto_if_eq VAR_RESULT, FALSE, World_RewardFull

	setflag FLAG_WORLD_SCENE_3
World_Scene3_Done:
	msgbox World_Scene3_DoneText, MSGBOX_DEFAULT
	setvar VAR_0x8004, 3
	call World_EventScript_PipReaction
	release
	end
World_EventScript_Scene3_1::
	lock
	faceplayer
	goto_if_set FLAG_WORLD_SCENE_3, World_Scene3_PartnerAfter
	msgbox World_Scene3_Before, MSGBOX_DEFAULT
	release
	end
World_Scene3_PartnerAfter:
	msgbox World_Scene3_After, MSGBOX_DEFAULT
	setvar VAR_0x8004, 3
	call World_EventScript_PipReaction
	release
	end

World_Scene3_Intro::
	.string "TRENDSETTER: The next big trend is\nstanding normally. You are doing it\lalready. A natural talent.$"


World_Scene3_Before::
	.string "FORMER TRENDSETTER: I popularized\nsitting. We had creative differences.$"


World_Scene3_DoneText::
	.string "TRENDSETTER: Please accept a GREAT\nBALL. You have helped normalize\lstanding normally.$"


World_Scene3_After::
	.string "FORMER TRENDSETTER: I am planning a\ncomeback. It involves lying down.$"


World_Pip_3::
	.string "PIP: We have somehow become early\nadopters of our own legs.$"


World_EventScript_Scene4_0::
	lock
	faceplayer
	goto_if_set FLAG_WORLD_SCENE_4, World_Scene4_Done

	msgbox World_Scene4_Intro, MSGBOX_YESNO

	goto_if_eq VAR_RESULT, NO, World_RequestDeclined
	checkitem ITEM_ORAN_BERRY, 1
	goto_if_eq VAR_RESULT, FALSE, World_RequestMissing
	checkitemspace ITEM_PECHA_BERRY, 1
	goto_if_eq VAR_RESULT, FALSE, World_RewardFull
	giveitem ITEM_PECHA_BERRY, 1
	goto_if_eq VAR_RESULT, FALSE, World_RewardFull
	removeitem ITEM_ORAN_BERRY, 1

	setflag FLAG_WORLD_SCENE_4
World_Scene4_Done:
	msgbox World_Scene4_DoneText, MSGBOX_DEFAULT
	setvar VAR_0x8004, 4
	call World_EventScript_PipReaction
	release
	end
World_EventScript_Scene4_1::
	lock
	faceplayer
	goto_if_set FLAG_WORLD_SCENE_4, World_Scene4_PartnerAfter
	msgbox World_Scene4_Before, MSGBOX_DEFAULT
	release
	end
World_Scene4_PartnerAfter:
	msgbox World_Scene4_After, MSGBOX_DEFAULT
	setvar VAR_0x8004, 4
	call World_EventScript_PipReaction
	release
	end

World_Scene4_Intro::
	.string "PICNIC PLANNER: We budgeted for a\npicnic, then spent the budget on a\lclipboard. Do you have an ORAN BERRY?\lWe can swap a PECHA BERRY.$"


World_Scene4_Before::
	.string "PICNIC TREASURER: I approved the\nclipboard. It has made recording our\lhunger much easier.$"


World_Scene4_DoneText::
	.string "PICNIC PLANNER: A real picnic\ningredient! You have been entered\lunder essential personnel.$"


World_Scene4_After::
	.string "PICNIC TREASURER: The berry has its\nown line on the clipboard. The\lclipboard remains inedible.$"


World_Pip_4::
	.string "PIP: I would have started with lunch\nand worked backward. A radical\lapproach.$"


World_EventScript_Scene5_0::
	lock
	faceplayer
	goto_if_set FLAG_WORLD_SCENE_5, World_Scene5_Done

	msgbox World_Scene5_Intro, MSGBOX_DEFAULT

	setflag FLAG_WORLD_SCENE_5
World_Scene5_Done:
	msgbox World_Scene5_DoneText, MSGBOX_DEFAULT
	setvar VAR_0x8004, 5
	call World_EventScript_PipReaction
	release
	end
World_EventScript_Scene5_1::
	lock
	faceplayer
	goto_if_set FLAG_WORLD_SCENE_5, World_Scene5_PartnerAfter
	msgbox World_Scene5_Before, MSGBOX_DEFAULT
	release
	end
World_Scene5_PartnerAfter:
	msgbox World_Scene5_After, MSGBOX_DEFAULT
	setvar VAR_0x8004, 5
	call World_EventScript_PipReaction
	release
	end

World_Scene5_Intro::
	.string "BIKE COUNTER: I count the bicycles\npassing through. One just came back.\lDoes that count as two?$"


World_Scene5_Before::
	.string "COUNT AUDITOR: I audit the count. We\nare both afraid to ask where the\lrider went.$"


World_Scene5_DoneText::
	.string "BIKE COUNTER: We agreed to count\njourneys instead. The bicycle remains\lunder investigation.$"


World_Scene5_After::
	.string "COUNT AUDITOR: The rider said he\nforgot his wallet. A devastating\ldevelopment for our methodology.$"


World_Pip_5::
	.string "PIP: I like a mystery that can be\nsolved by checking your other\lpocket.$"


World_EventScript_Scene6_0::
	lock
	faceplayer
	goto_if_set FLAG_WORLD_SCENE_6, World_Scene6_Done

	msgbox World_Scene6_Intro, MSGBOX_DEFAULT

	setflag FLAG_WORLD_SCENE_6
World_Scene6_Done:
	msgbox World_Scene6_DoneText, MSGBOX_DEFAULT
	setvar VAR_0x8004, 6
	call World_EventScript_PipReaction
	release
	end
World_EventScript_Scene6_1::
	lock
	faceplayer
	goto_if_set FLAG_WORLD_SCENE_6, World_Scene6_PartnerAfter
	msgbox World_Scene6_Before, MSGBOX_DEFAULT
	release
	end
World_Scene6_PartnerAfter:
	msgbox World_Scene6_After, MSGBOX_DEFAULT
	setvar VAR_0x8004, 6
	call World_EventScript_PipReaction
	release
	end

World_Scene6_Intro::
	.string "QUIET CLUB: Welcome to Quiet Club. We\nmeet here so nobody has to make an\lexcuse to be quiet.$"


World_Scene6_Before::
	.string "LOUD TREASURER: I collect dues.\nSilently. I have lost three members\lby clearing my throat.$"


World_Scene6_DoneText::
	.string "QUIET CLUB: You can stay as long as\nyou like. There is no speech at the\lend.$"


World_Scene6_After::
	.string "LOUD TREASURER: The dues are\noptional. This was not made clear by\lmy extremely serious little box.$"


World_Pip_6::
	.string "PIP: We can just stand here a moment.\nThat can be the activity.$"


World_EventScript_Scene7_0::
	lock
	faceplayer
	goto_if_set FLAG_WORLD_SCENE_7, World_Scene7_Done

	msgbox World_Scene7_Intro, MSGBOX_DEFAULT

	giveitem ITEM_SUPER_POTION, 1
	goto_if_eq VAR_RESULT, FALSE, World_RewardFull

	setflag FLAG_WORLD_SCENE_7
World_Scene7_Done:
	msgbox World_Scene7_DoneText, MSGBOX_DEFAULT
	setvar VAR_0x8004, 7
	call World_EventScript_PipReaction
	release
	end
World_EventScript_Scene7_1::
	lock
	faceplayer
	goto_if_set FLAG_WORLD_SCENE_7, World_Scene7_PartnerAfter
	msgbox World_Scene7_Before, MSGBOX_DEFAULT
	release
	end
World_Scene7_PartnerAfter:
	msgbox World_Scene7_After, MSGBOX_DEFAULT
	setvar VAR_0x8004, 7
	call World_EventScript_PipReaction
	release
	end

World_Scene7_Intro::
	.string "ASH SWEEPER: I sweep this spot. She\npredicts when the ash will return. We\lare both having a busy career.$"


World_Scene7_Before::
	.string "ASH FORECASTER: Soon. That is my\nforecast. It has been remarkably\lconsistent.$"


World_Scene7_DoneText::
	.string "ASH SWEEPER: Take a SUPER POTION.\nGetting up and trying again is worth\llooking after.$"


World_Scene7_After::
	.string "ASH FORECASTER: I have revised the\nforecast to shortly. Professional\ldevelopment.$"


World_Pip_7::
	.string "PIP: They know it will come back. They\nare still taking care of the place.$"


World_EventScript_Scene8_0::
	lock
	faceplayer
	goto_if_set FLAG_WORLD_SCENE_8, World_Scene8_Done

	msgbox World_Scene8_Intro, MSGBOX_DEFAULT

	setflag FLAG_WORLD_SCENE_8
World_Scene8_Done:
	msgbox World_Scene8_DoneText, MSGBOX_DEFAULT
	setvar VAR_0x8004, 8
	call World_EventScript_PipReaction
	release
	end
World_EventScript_Scene8_1::
	lock
	faceplayer
	goto_if_set FLAG_WORLD_SCENE_8, World_Scene8_PartnerAfter
	msgbox World_Scene8_Before, MSGBOX_DEFAULT
	release
	end
World_Scene8_PartnerAfter:
	msgbox World_Scene8_After, MSGBOX_DEFAULT
	setvar VAR_0x8004, 8
	call World_EventScript_PipReaction
	release
	end

World_Scene8_Intro::
	.string "TOWEL MARSHAL: That towel has\nreserved a place in the spring for\ltwenty minutes. Its trainer has not\larrived.$"


World_Scene8_Before::
	.string "TOWEL OWNER: I am its trainer. I am\nwaiting for the towel to invite me.$"


World_Scene8_DoneText::
	.string "TOWEL MARSHAL: We resolved the\nsituation. The towel has retired from\lcompetitive reservation.$"


World_Scene8_After::
	.string "TOWEL OWNER: It is now drying on a\nrock. A much more suitable career.$"


World_Pip_8::
	.string "PIP: I am pleased they found an\narrangement that respected the\ltowel.$"


World_EventScript_Scene9_0::
	lock
	faceplayer
	goto_if_set FLAG_WORLD_SCENE_9, World_Scene9_Done

	msgbox World_Scene9_Intro, MSGBOX_DEFAULT

	setflag FLAG_WORLD_SCENE_9
World_Scene9_Done:
	msgbox World_Scene9_DoneText, MSGBOX_DEFAULT
	setvar VAR_0x8004, 9
	call World_EventScript_PipReaction
	release
	end
World_EventScript_Scene9_1::
	lock
	faceplayer
	goto_if_set FLAG_WORLD_SCENE_9, World_Scene9_PartnerAfter
	msgbox World_Scene9_Before, MSGBOX_DEFAULT
	release
	end
World_Scene9_PartnerAfter:
	msgbox World_Scene9_After, MSGBOX_DEFAULT
	setvar VAR_0x8004, 9
	call World_EventScript_PipReaction
	release
	end

World_Scene9_Intro::
	.string "FLOOR TESTER: I test the\nfloorboards. The tree tests my\lpatience. We have a healthy\lprofessional relationship.$"


World_Scene9_Before::
	.string "TREE NEIGHBOR: The tree was here\nfirst. I keep offering to mediate.$"


World_Scene9_DoneText::
	.string "FLOOR TESTER: We agreed the creaking\nis a greeting. The house is now\lextremely welcoming.$"


World_Scene9_After::
	.string "TREE NEIGHBOR: He has started saying\nhello back. I believe this is progress.$"


World_Pip_9::
	.string "PIP: If our house greeted us that\noften, I would feel obliged to bring\lit a snack.$"


World_EventScript_Scene10_0::
	lock
	faceplayer
	goto_if_set FLAG_WORLD_SCENE_10, World_Scene10_Done

	msgbox World_Scene10_Intro, MSGBOX_DEFAULT

	setflag FLAG_WORLD_SCENE_10
World_Scene10_Done:
	msgbox World_Scene10_DoneText, MSGBOX_DEFAULT
	setvar VAR_0x8004, 10
	call World_EventScript_PipReaction
	release
	end
World_EventScript_Scene10_1::
	lock
	faceplayer
	goto_if_set FLAG_WORLD_SCENE_10, World_Scene10_PartnerAfter
	msgbox World_Scene10_Before, MSGBOX_DEFAULT
	release
	end
World_Scene10_PartnerAfter:
	msgbox World_Scene10_After, MSGBOX_DEFAULT
	setvar VAR_0x8004, 10
	call World_EventScript_PipReaction
	release
	end

World_Scene10_Intro::
	.string "ART CRITIC: A masterpiece needs\nmystery. This painting has it. I\lcannot tell which way is up.$"


World_Scene10_Before::
	.string "PAINTER: It is a picture of my lunch.\nHe is holding it sideways.$"


World_Scene10_DoneText::
	.string "ART CRITIC: I have reclassified it as\nan ambitious still life.$"


World_Scene10_After::
	.string "PAINTER: He asked to buy it. I said\nthe sandwich was extra.$"


World_Pip_10::
	.string "PIP: I am trying to have a profound\nresponse to the tomato.$"


World_EventScript_Scene11_0::
	lock
	faceplayer
	goto_if_set FLAG_WORLD_SCENE_11, World_Scene11_Done

	msgbox World_Scene11_Intro, MSGBOX_YESNO

	goto_if_eq VAR_RESULT, NO, World_RequestDeclined
	checkitem ITEM_STAR_PIECE, 1
	goto_if_eq VAR_RESULT, FALSE, World_RequestMissing
	checkitemspace ITEM_ULTRA_BALL, 1
	goto_if_eq VAR_RESULT, FALSE, World_RewardFull
	giveitem ITEM_ULTRA_BALL, 1
	goto_if_eq VAR_RESULT, FALSE, World_RewardFull
	removeitem ITEM_STAR_PIECE, 1

	setflag FLAG_WORLD_SCENE_11
World_Scene11_Done:
	msgbox World_Scene11_DoneText, MSGBOX_DEFAULT
	setvar VAR_0x8004, 11
	call World_EventScript_PipReaction
	release
	end
World_EventScript_Scene11_1::
	lock
	faceplayer
	goto_if_set FLAG_WORLD_SCENE_11, World_Scene11_PartnerAfter
	msgbox World_Scene11_Before, MSGBOX_DEFAULT
	release
	end
World_Scene11_PartnerAfter:
	msgbox World_Scene11_After, MSGBOX_DEFAULT
	setvar VAR_0x8004, 11
	call World_EventScript_PipReaction
	release
	end

World_Scene11_Intro::
	.string "JUNIOR ASTRONOMER: We built a ladder\nto study the stars. Early results\lsuggest we need a taller ladder.$"


World_Scene11_Before::
	.string "LADDER ASSISTANT: I hold it steady.\nScience is mostly making sure\lsomeone does not fall.$"


World_Scene11_DoneText::
	.string "JUNIOR ASTRONOMER: A STAR PIECE\nwould help our display. We can offer\lan ULTRA BALL. It has excellent\lastronaut colors.$"


World_Scene11_After::
	.string "LADDER ASSISTANT: We do know a STAR\nPIECE is not an actual star. The\ldisplay label is very careful about\lthat.$"


World_Pip_11::
	.string "PIP: A small piece of wonder is easier\nto carry than a very large ladder.$"


World_EventScript_Scene12_0::
	lock
	faceplayer
	goto_if_set FLAG_WORLD_SCENE_12, World_Scene12_Done

	msgbox World_Scene12_Intro, MSGBOX_DEFAULT

	giveitem ITEM_FRESH_WATER, 1
	goto_if_eq VAR_RESULT, FALSE, World_RewardFull

	setflag FLAG_WORLD_SCENE_12
World_Scene12_Done:
	msgbox World_Scene12_DoneText, MSGBOX_DEFAULT
	setvar VAR_0x8004, 12
	call World_EventScript_PipReaction
	release
	end
World_EventScript_Scene12_1::
	lock
	faceplayer
	goto_if_set FLAG_WORLD_SCENE_12, World_Scene12_PartnerAfter
	msgbox World_Scene12_Before, MSGBOX_DEFAULT
	release
	end
World_Scene12_PartnerAfter:
	msgbox World_Scene12_After, MSGBOX_DEFAULT
	setvar VAR_0x8004, 12
	call World_EventScript_PipReaction
	release
	end

World_Scene12_Intro::
	.string "STAIR COMMITTEE: We are requesting a\nbench halfway up the stairs. The\lpetition has reached a landing.$"


World_Scene12_Before::
	.string "STAIR COMMITTEE CHAIR: I am the\nchair. It is a title, which has caused\lsome disappointment.$"


World_Scene12_DoneText::
	.string "STAIR COMMITTEE: We rested on the\nlanding and discovered we had\laccidentally held a meeting.$"


World_Scene12_After::
	.string "STAIR COMMITTEE CHAIR: The minutes\nsay everyone should bring water.\lPlease take ours for the road.$"


World_Pip_12::
	.string "PIP: A meeting that ends with\neveryone feeling better. Remarkable.$"


World_EventScript_Scene13_0::
	lock
	faceplayer
	goto_if_set FLAG_WORLD_SCENE_13, World_Scene13_Done

	msgbox World_Scene13_Intro, MSGBOX_DEFAULT

	setflag FLAG_WORLD_SCENE_13
World_Scene13_Done:
	msgbox World_Scene13_DoneText, MSGBOX_DEFAULT
	setvar VAR_0x8004, 13
	call World_EventScript_PipReaction
	release
	end
World_EventScript_Scene13_1::
	lock
	faceplayer
	goto_if_set FLAG_WORLD_SCENE_13, World_Scene13_PartnerAfter
	msgbox World_Scene13_Before, MSGBOX_DEFAULT
	release
	end
World_Scene13_PartnerAfter:
	msgbox World_Scene13_After, MSGBOX_DEFAULT
	setvar VAR_0x8004, 13
	call World_EventScript_PipReaction
	release
	end

World_Scene13_Intro::
	.string "MAIL SORTER: I found a message in a\nbottle. It says please return bottle.$"


World_Scene13_Before::
	.string "BOTTLE OWNER: That is mine. I have\ndeveloped a very slow postal service.$"


World_Scene13_DoneText::
	.string "MAIL SORTER: The bottle is home. We\nare discussing whether to charge it\lpostage.$"


World_Scene13_After::
	.string "BOTTLE OWNER: I have written thank\nyou on a piece of paper. We may never\lsee that bottle again.$"


World_Pip_13::
	.string "PIP: A reply is nice. Perhaps we could\nhand this one over.$"


World_EventScript_Scene14_0::
	lock
	faceplayer
	goto_if_set FLAG_WORLD_SCENE_14, World_Scene14_Done

	msgbox World_Scene14_Intro, MSGBOX_DEFAULT

	giveitem ITEM_FULL_RESTORE, 1
	goto_if_eq VAR_RESULT, FALSE, World_RewardFull

	setflag FLAG_WORLD_SCENE_14
World_Scene14_Done:
	msgbox World_Scene14_DoneText, MSGBOX_DEFAULT
	setvar VAR_0x8004, 14
	call World_EventScript_PipReaction
	release
	end
World_EventScript_Scene14_1::
	lock
	faceplayer
	goto_if_set FLAG_WORLD_SCENE_14, World_Scene14_PartnerAfter
	msgbox World_Scene14_Before, MSGBOX_DEFAULT
	release
	end
World_Scene14_PartnerAfter:
	msgbox World_Scene14_After, MSGBOX_DEFAULT
	setvar VAR_0x8004, 14
	call World_EventScript_PipReaction
	release
	end

World_Scene14_Intro::
	.string "FINISH LINE CREW: I welcome people\nat the end of their journey. She\lkeeps saying this is also a beginning.$"


World_Scene14_Before::
	.string "START LINE CREW: Somebody has to\nmake sure there is a beginning to go\lback to.$"


World_Scene14_DoneText::
	.string "FINISH LINE CREW: Take a FULL\nRESTORE. You can decide what this\lplace means after you have had a\lrest.$"


World_Scene14_After::
	.string "START LINE CREW: You are allowed to\ncome here twice. Or leave and come\lback ready.$"


World_Pip_14::
	.string "PIP: I do not mind which line this is. I\nam glad we reached it together.$"


World_EventScript_Scene15_0::
	lock
	faceplayer
	goto_if_set FLAG_WORLD_SCENE_15, World_Scene15_Done

	msgbox World_Scene15_Intro, MSGBOX_DEFAULT

	setflag FLAG_WORLD_SCENE_15
World_Scene15_Done:
	msgbox World_Scene15_DoneText, MSGBOX_DEFAULT
	setvar VAR_0x8004, 15
	call World_EventScript_PipReaction
	release
	end
World_EventScript_Scene15_1::
	lock
	faceplayer
	goto_if_set FLAG_WORLD_SCENE_15, World_Scene15_PartnerAfter
	msgbox World_Scene15_Before, MSGBOX_DEFAULT
	release
	end
World_Scene15_PartnerAfter:
	msgbox World_Scene15_After, MSGBOX_DEFAULT
	setvar VAR_0x8004, 15
	call World_EventScript_PipReaction
	release
	end

World_Scene15_Intro::
	.string "BUG LISTENER: I am listening for bug\ncalls. My friend has been translating.$"


World_Scene15_Before::
	.string "BUG TRANSLATOR: That one said leaf.\nThe previous one also said leaf.\lStrong theme.$"


World_Scene15_DoneText::
	.string "BUG LISTENER: We heard a new call!\nShe says it means slightly different\lleaf.$"


World_Scene15_After::
	.string "BUG TRANSLATOR: I believe in being\nprecise.$"


World_Pip_15::
	.string "PIP: I understood none of it, but\ntheir enthusiasm is quite convincing.$"


World_EventScript_Scene16_0::
	lock
	faceplayer
	goto_if_set FLAG_WORLD_SCENE_16, World_Scene16_Done

	msgbox World_Scene16_Intro, MSGBOX_DEFAULT

	setflag FLAG_WORLD_SCENE_16
World_Scene16_Done:
	msgbox World_Scene16_DoneText, MSGBOX_DEFAULT
	setvar VAR_0x8004, 16
	call World_EventScript_PipReaction
	release
	end
World_EventScript_Scene16_1::
	lock
	faceplayer
	goto_if_set FLAG_WORLD_SCENE_16, World_Scene16_PartnerAfter
	msgbox World_Scene16_Before, MSGBOX_DEFAULT
	release
	end
World_Scene16_PartnerAfter:
	msgbox World_Scene16_After, MSGBOX_DEFAULT
	setvar VAR_0x8004, 16
	call World_EventScript_PipReaction
	release
	end

World_Scene16_Intro::
	.string "WALK ORGANIZER: I organize walks. He\nkeeps arriving early and finishing\lbefore we start.$"


World_Scene16_Before::
	.string "WALK PARTICIPANT: I thought the\nmeeting point was the destination. I\lam very good at the travel part.$"


World_Scene16_DoneText::
	.string "WALK ORGANIZER: We are walking\ntogether now. I have confiscated the\lschedule.$"


World_Scene16_After::
	.string "WALK PARTICIPANT: The walk is much\nnicer with someone to point out the\lsea.$"


World_Pip_16::
	.string "PIP: We can point out the sea too. It\nhas put a lot of effort into being\lvisible.$"


World_EventScript_Scene17_0::
	lock
	faceplayer
	goto_if_set FLAG_WORLD_SCENE_17, World_Scene17_Done

	msgbox World_Scene17_Intro, MSGBOX_YESNO

	goto_if_eq VAR_RESULT, NO, World_RequestDeclined
	checkitem ITEM_ANTIDOTE, 1
	goto_if_eq VAR_RESULT, FALSE, World_RequestMissing
	checkitemspace ITEM_GREAT_BALL, 1
	goto_if_eq VAR_RESULT, FALSE, World_RewardFull
	giveitem ITEM_GREAT_BALL, 1
	goto_if_eq VAR_RESULT, FALSE, World_RewardFull
	removeitem ITEM_ANTIDOTE, 1

	setflag FLAG_WORLD_SCENE_17
World_Scene17_Done:
	msgbox World_Scene17_DoneText, MSGBOX_DEFAULT
	setvar VAR_0x8004, 17
	call World_EventScript_PipReaction
	release
	end
World_EventScript_Scene17_1::
	lock
	faceplayer
	goto_if_set FLAG_WORLD_SCENE_17, World_Scene17_PartnerAfter
	msgbox World_Scene17_Before, MSGBOX_DEFAULT
	release
	end
World_Scene17_PartnerAfter:
	msgbox World_Scene17_After, MSGBOX_DEFAULT
	setvar VAR_0x8004, 17
	call World_EventScript_PipReaction
	release
	end

World_Scene17_Intro::
	.string "SHADE SURVEYOR: We are comparing the\nshade under the cycling road to the\lsun beside it.$"


World_Scene17_Before::
	.string "SUN SURVEYOR: The shade is winning. I\nwould like the experiment to be over.$"


World_Scene17_DoneText::
	.string "SHADE SURVEYOR: An ANTIDOTE? My\npartner brushed a poison barb\lcollecting samples. We have a GREAT\lBALL to trade.$"


World_Scene17_After::
	.string "SUN SURVEYOR: The samples were\nentirely avoidable. I wish this to be\lin the report.$"


World_Pip_17::
	.string "PIP: An excellent time for the report\nto include an apology.$"


World_EventScript_Scene18_0::
	lock
	faceplayer
	goto_if_set FLAG_WORLD_SCENE_18, World_Scene18_Done

	msgbox World_Scene18_Intro, MSGBOX_DEFAULT

	setflag FLAG_WORLD_SCENE_18
World_Scene18_Done:
	msgbox World_Scene18_DoneText, MSGBOX_DEFAULT
	setvar VAR_0x8004, 18
	call World_EventScript_PipReaction
	release
	end
World_EventScript_Scene18_1::
	lock
	faceplayer
	goto_if_set FLAG_WORLD_SCENE_18, World_Scene18_PartnerAfter
	msgbox World_Scene18_Before, MSGBOX_DEFAULT
	release
	end
World_Scene18_PartnerAfter:
	msgbox World_Scene18_After, MSGBOX_DEFAULT
	setvar VAR_0x8004, 18
	call World_EventScript_PipReaction
	release
	end

World_Scene18_Intro::
	.string "DESERT GUIDE: My trainee has\nidentified every sand dune as the\lsame sand dune.$"


World_Scene18_Before::
	.string "GUIDE TRAINEE: They are all made of\nsand. I stand by my findings.$"


World_Scene18_DoneText::
	.string "DESERT GUIDE: He identified a rock.\nWe are celebrating this development.$"


World_Scene18_After::
	.string "GUIDE TRAINEE: It was a very decisive\nrock.$"


World_Pip_18::
	.string "PIP: Sometimes progress looks\nexactly like noticing one new thing.$"


World_EventScript_Scene19_0::
	lock
	faceplayer
	goto_if_set FLAG_WORLD_SCENE_19, World_Scene19_Done

	msgbox World_Scene19_Intro, MSGBOX_DEFAULT

	setflag FLAG_WORLD_SCENE_19
World_Scene19_Done:
	msgbox World_Scene19_DoneText, MSGBOX_DEFAULT
	setvar VAR_0x8004, 19
	call World_EventScript_PipReaction
	release
	end
World_EventScript_Scene19_1::
	lock
	faceplayer
	goto_if_set FLAG_WORLD_SCENE_19, World_Scene19_PartnerAfter
	msgbox World_Scene19_Before, MSGBOX_DEFAULT
	release
	end
World_Scene19_PartnerAfter:
	msgbox World_Scene19_After, MSGBOX_DEFAULT
	setvar VAR_0x8004, 19
	call World_EventScript_PipReaction
	release
	end

World_Scene19_Intro::
	.string "FOOTPRINT KEEPER: I preserve\nfootprints in the ash. She keeps\lwalking through my collection.$"


World_Scene19_Before::
	.string "FOOTPRINT MAKER: He set up the\ncollection on the path. I have\lexplained my position with several\lfootprints.$"


World_Scene19_DoneText::
	.string "FOOTPRINT KEEPER: We moved the\ncollection beside the path. It is less\lpopular, but much safer.$"


World_Scene19_After::
	.string "FOOTPRINT MAKER: I have donated one\nfootprint. By appointment.$"


World_Pip_19::
	.string "PIP: A museum with room left over for\nwalking. I like their compromise.$"


World_EventScript_Scene20_0::
	lock
	faceplayer
	goto_if_set FLAG_WORLD_SCENE_20, World_Scene20_Done

	msgbox World_Scene20_Intro, MSGBOX_YESNO

	goto_if_eq VAR_RESULT, NO, World_RequestDeclined
	checkitem ITEM_REPEL, 1
	goto_if_eq VAR_RESULT, FALSE, World_RequestMissing
	checkitemspace ITEM_SUPER_POTION, 1
	goto_if_eq VAR_RESULT, FALSE, World_RewardFull
	giveitem ITEM_SUPER_POTION, 1
	goto_if_eq VAR_RESULT, FALSE, World_RewardFull
	removeitem ITEM_REPEL, 1

	setflag FLAG_WORLD_SCENE_20
World_Scene20_Done:
	msgbox World_Scene20_DoneText, MSGBOX_DEFAULT
	setvar VAR_0x8004, 20
	call World_EventScript_PipReaction
	release
	end
World_EventScript_Scene20_1::
	lock
	faceplayer
	goto_if_set FLAG_WORLD_SCENE_20, World_Scene20_PartnerAfter
	msgbox World_Scene20_Before, MSGBOX_DEFAULT
	release
	end
World_Scene20_PartnerAfter:
	msgbox World_Scene20_After, MSGBOX_DEFAULT
	setvar VAR_0x8004, 20
	call World_EventScript_PipReaction
	release
	end

World_Scene20_Intro::
	.string "RAIN RESEARCHER: We are checking\nwhether the rain stops if nobody\lcomplains about it.$"


World_Scene20_Before::
	.string "DRY SOCK OWNER: I have lasted eleven\nseconds. My socks would like a REPEL\lfor the walk home. We can trade a\lSUPER POTION.$"


World_Scene20_DoneText::
	.string "RAIN RESEARCHER: The trial has ended.\nThe rain did not, but morale has\limproved.$"


World_Scene20_After::
	.string "DRY SOCK OWNER: We are renaming it a\nstudy of the restorative properties\lof dry socks.$"


World_Pip_20::
	.string "PIP: A negative result is still a\nresult. A dry sock is still a treasure.$"


World_EventScript_PipReaction::
	callnative Script_CozyWorldPipReaction
	compare VAR_RESULT, TRUE
	call_if_eq World_EventScript_ShowPip
	return
World_EventScript_ShowPip:
	msgbox gStringVar4, MSGBOX_DEFAULT
	return
World_Rare_NoTeam:
	msgbox World_Text_NoTeam, MSGBOX_DEFAULT
	release
	end
World_RequestDeclined:
	msgbox World_Text_Declined, MSGBOX_DEFAULT
	release
	end
World_RequestMissing:
	msgbox World_Text_Missing, MSGBOX_DEFAULT
	release
	end
World_RewardFull:
	msgbox World_Text_Full, MSGBOX_DEFAULT
	release
	end

World_Text_Invite::
	.string "Ask it to join you? It will want a wild\nbattle first. Bring POKE BALLS if you\lwant to catch it.$"


World_Text_Caught::
	.string "Your new traveling companion seems\npleased with the arrangement.$"


World_Text_NoTeam::
	.string "You need a healthy POKEMON with you\nfor a friendly battle. It will wait\lhere.$"


World_Text_Declined::
	.string "No rush. We will be here if you change\nyour mind.$"


World_Text_Missing::
	.string "It looks like you do not have one with\nyou. Come back whenever it suits you.$"


World_Text_Full::
	.string "Your BAG cannot hold the reward.\nNothing was taken. Come back after\lmaking some room.$"

