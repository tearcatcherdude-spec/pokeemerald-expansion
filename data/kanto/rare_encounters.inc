@ Optional Kanto rare Pokemon. Capture flags use reserved Kanto bits only.
KantoRare_BELDUM_Interact::
	lock
	faceplayer
	goto_if_set KANTO_FLAG_CAUGHT_RARE_BELDUM, KantoRare_BELDUM_Gone
	goto_if_set FLAG_TEMP_10, KantoRare_BELDUM_Rest
	msgbox KantoRare_BELDUM_Intro, MSGBOX_DEFAULT
	msgbox KantoRare_Text_Invite, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, KantoRare_BELDUM_Decline
	setvar VAR_0x8004, 16
	callnative Script_CozyWorldPrepareRare
	goto_if_eq VAR_RESULT, FALSE, KantoRare_NoHealthyTeam
	msgbox KantoRare_BELDUM_Accept, MSGBOX_DEFAULT
	setwildbattle SPECIES_BELDUM, 6
	callnative Script_CozyWorldTrainRare
	dowildbattle
	specialvar VAR_RESULT, GetBattleOutcome
	goto_if_eq VAR_RESULT, B_OUTCOME_CAUGHT, KantoRare_BELDUM_Caught
	setflag FLAG_TEMP_10
	goto KantoRare_BELDUM_Rest
KantoRare_BELDUM_Caught:
	setflag KANTO_FLAG_CAUGHT_RARE_BELDUM
	removeobject LOCALID_KANTO_RARE_BELDUM
	msgbox KantoRare_BELDUM_CaughtText, MSGBOX_DEFAULT
	release
	end
KantoRare_BELDUM_Decline:
	msgbox KantoRare_BELDUM_DeclineText, MSGBOX_DEFAULT
	release
	end
KantoRare_BELDUM_Rest:
	msgbox KantoRare_BELDUM_RestText, MSGBOX_DEFAULT
	release
	end
KantoRare_BELDUM_Gone:
	release
	end

KantoRare_BELDUM_Intro::
	.string "This BELDUM is hovering beside\nthe road. It keeps turning toward\ltravelers, then back toward town,\las though it has misplaced its\litinerary.$"

KantoRare_BELDUM_Accept::
	.string "It taps the ground twice and\nfloats into position. A friendly\lbattle seems to be its preferred\lintroduction. You can catch it in\lthis battle.$"

KantoRare_BELDUM_DeclineText::
	.string "It resumes inspecting the road.\nThe itinerary remains a work in\lprogress.$"

KantoRare_BELDUM_RestText::
	.string "BELDUM is hovering very still\nafter the match. Let it rest;\lanother visit may suit it better.$"

KantoRare_BELDUM_CaughtText::
	.string "BELDUM gives a small, satisfied\nhum. Its travel arrangements\lappear to be settled.$"

KantoRare_SHINX_Interact::
	lock
	faceplayer
	goto_if_set KANTO_FLAG_CAUGHT_RARE_SHINX, KantoRare_SHINX_Gone
	goto_if_set FLAG_TEMP_10, KantoRare_SHINX_Rest
	msgbox KantoRare_SHINX_Intro, MSGBOX_DEFAULT
	msgbox KantoRare_Text_Invite, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, KantoRare_SHINX_Decline
	setvar VAR_0x8004, 17
	callnative Script_CozyWorldPrepareRare
	goto_if_eq VAR_RESULT, FALSE, KantoRare_NoHealthyTeam
	msgbox KantoRare_SHINX_Accept, MSGBOX_DEFAULT
	setwildbattle SPECIES_SHINX, 5
	callnative Script_CozyWorldTrainRare
	dowildbattle
	specialvar VAR_RESULT, GetBattleOutcome
	goto_if_eq VAR_RESULT, B_OUTCOME_CAUGHT, KantoRare_SHINX_Caught
	setflag FLAG_TEMP_10
	goto KantoRare_SHINX_Rest
KantoRare_SHINX_Caught:
	setflag KANTO_FLAG_CAUGHT_RARE_SHINX
	removeobject LOCALID_KANTO_RARE_SHINX
	msgbox KantoRare_SHINX_CaughtText, MSGBOX_DEFAULT
	release
	end
KantoRare_SHINX_Decline:
	msgbox KantoRare_SHINX_DeclineText, MSGBOX_DEFAULT
	release
	end
KantoRare_SHINX_Rest:
	msgbox KantoRare_SHINX_RestText, MSGBOX_DEFAULT
	release
	end
KantoRare_SHINX_Gone:
	release
	end

KantoRare_SHINX_Intro::
	.string "A SHINX is watching the road to\nthe LEAGUE. Every time a trainer\lpasses, it practices a determined\llittle glare.$"

KantoRare_SHINX_Accept::
	.string "It notices your team and squares\nits paws. Apparently the glare\lrequires a practical exam. You\lcan catch it in this battle.$"

KantoRare_SHINX_DeclineText::
	.string "It returns to glaring at distant\nchampions. Its ambition is\lconsiderably larger than its\lpaws.$"

KantoRare_SHINX_RestText::
	.string "SHINX is taking a break from\nlooking intimidating. Come back\lon another visit.$"

KantoRare_SHINX_CaughtText::
	.string "SHINX gives you one final stern\nlook, then relaxes. You appear to\lhave passed inspection.$"

KantoRare_RIOLU_Interact::
	lock
	faceplayer
	goto_if_set KANTO_FLAG_CAUGHT_RARE_RIOLU, KantoRare_RIOLU_Gone
	goto_if_set FLAG_TEMP_10, KantoRare_RIOLU_Rest
	msgbox KantoRare_RIOLU_Intro, MSGBOX_DEFAULT
	msgbox KantoRare_Text_Invite, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, KantoRare_RIOLU_Decline
	setvar VAR_0x8004, 18
	callnative Script_CozyWorldPrepareRare
	goto_if_eq VAR_RESULT, FALSE, KantoRare_NoHealthyTeam
	msgbox KantoRare_RIOLU_Accept, MSGBOX_DEFAULT
	setwildbattle SPECIES_RIOLU, 12
	callnative Script_CozyWorldTrainRare
	dowildbattle
	specialvar VAR_RESULT, GetBattleOutcome
	goto_if_eq VAR_RESULT, B_OUTCOME_CAUGHT, KantoRare_RIOLU_Caught
	setflag FLAG_TEMP_10
	goto KantoRare_RIOLU_Rest
KantoRare_RIOLU_Caught:
	setflag KANTO_FLAG_CAUGHT_RARE_RIOLU
	removeobject LOCALID_KANTO_RARE_RIOLU
	msgbox KantoRare_RIOLU_CaughtText, MSGBOX_DEFAULT
	release
	end
KantoRare_RIOLU_Decline:
	msgbox KantoRare_RIOLU_DeclineText, MSGBOX_DEFAULT
	release
	end
KantoRare_RIOLU_Rest:
	msgbox KantoRare_RIOLU_RestText, MSGBOX_DEFAULT
	release
	end
KantoRare_RIOLU_Gone:
	release
	end

KantoRare_RIOLU_Intro::
	.string "This RIOLU is practicing its\nfootwork beside MT. MOON. A\lneatly arranged row of pebbles\lappears to be its entire training\lclass.$"

KantoRare_RIOLU_Accept::
	.string "It bows, then points toward your\nteam. A sparring match is the\lnext lesson. You can catch it in\lthis battle.$"

KantoRare_RIOLU_DeclineText::
	.string "RIOLU returns to the pebbles.\nAttendance has been excellent,\lbut their footwork needs work.$"

KantoRare_RIOLU_RestText::
	.string "RIOLU is stretching after the\nmatch. Let it recover before\lanother try.$"

KantoRare_RIOLU_CaughtText::
	.string "RIOLU bows again. The class now\nhas a traveling instructor, or\lpossibly a traveling student.$"

KantoRare_MAREEP_Interact::
	lock
	faceplayer
	goto_if_set KANTO_FLAG_CAUGHT_RARE_MAREEP, KantoRare_MAREEP_Gone
	goto_if_set FLAG_TEMP_10, KantoRare_MAREEP_Rest
	msgbox KantoRare_MAREEP_Intro, MSGBOX_DEFAULT
	msgbox KantoRare_Text_Invite, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, KantoRare_MAREEP_Decline
	setvar VAR_0x8004, 19
	callnative Script_CozyWorldPrepareRare
	goto_if_eq VAR_RESULT, FALSE, KantoRare_NoHealthyTeam
	msgbox KantoRare_MAREEP_Accept, MSGBOX_DEFAULT
	setwildbattle SPECIES_MAREEP, 14
	callnative Script_CozyWorldTrainRare
	dowildbattle
	specialvar VAR_RESULT, GetBattleOutcome
	goto_if_eq VAR_RESULT, B_OUTCOME_CAUGHT, KantoRare_MAREEP_Caught
	setflag FLAG_TEMP_10
	goto KantoRare_MAREEP_Rest
KantoRare_MAREEP_Caught:
	setflag KANTO_FLAG_CAUGHT_RARE_MAREEP
	removeobject LOCALID_KANTO_RARE_MAREEP
	msgbox KantoRare_MAREEP_CaughtText, MSGBOX_DEFAULT
	release
	end
KantoRare_MAREEP_Decline:
	msgbox KantoRare_MAREEP_DeclineText, MSGBOX_DEFAULT
	release
	end
KantoRare_MAREEP_Rest:
	msgbox KantoRare_MAREEP_RestText, MSGBOX_DEFAULT
	release
	end
KantoRare_MAREEP_Gone:
	release
	end

KantoRare_MAREEP_Intro::
	.string "A MAREEP is inspecting the grass\nbeside the bridge. Its wool\lcrackles whenever a passing\ltrainer calls it fluffy.$"

KantoRare_MAREEP_Accept::
	.string "It steps forward, looking hopeful\nand mildly electrified. A battle\lwill decide whether this\lexpedition needs more wool. You\lcan catch it.$"

KantoRare_MAREEP_DeclineText::
	.string "It resumes its inspection. The\ngrass remains undecided about the\lstatic.$"

KantoRare_MAREEP_RestText::
	.string "MAREEP is letting its wool settle\nafter the match. Visit again\lafter some exploring.$"

KantoRare_MAREEP_CaughtText::
	.string "MAREEP settles down with a\ncontented bleat. The expedition\lhas acquired a little more wool.$"

KantoRare_BUNEARY_Interact::
	lock
	faceplayer
	goto_if_set KANTO_FLAG_CAUGHT_RARE_BUNEARY, KantoRare_BUNEARY_Gone
	goto_if_set FLAG_TEMP_10, KantoRare_BUNEARY_Rest
	msgbox KantoRare_BUNEARY_Intro, MSGBOX_DEFAULT
	msgbox KantoRare_Text_Invite, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, KantoRare_BUNEARY_Decline
	setvar VAR_0x8004, 20
	callnative Script_CozyWorldPrepareRare
	goto_if_eq VAR_RESULT, FALSE, KantoRare_NoHealthyTeam
	msgbox KantoRare_BUNEARY_Accept, MSGBOX_DEFAULT
	setwildbattle SPECIES_BUNEARY, 15
	callnative Script_CozyWorldTrainRare
	dowildbattle
	specialvar VAR_RESULT, GetBattleOutcome
	goto_if_eq VAR_RESULT, B_OUTCOME_CAUGHT, KantoRare_BUNEARY_Caught
	setflag FLAG_TEMP_10
	goto KantoRare_BUNEARY_Rest
KantoRare_BUNEARY_Caught:
	setflag KANTO_FLAG_CAUGHT_RARE_BUNEARY
	removeobject LOCALID_KANTO_RARE_BUNEARY
	msgbox KantoRare_BUNEARY_CaughtText, MSGBOX_DEFAULT
	release
	end
KantoRare_BUNEARY_Decline:
	msgbox KantoRare_BUNEARY_DeclineText, MSGBOX_DEFAULT
	release
	end
KantoRare_BUNEARY_Rest:
	msgbox KantoRare_BUNEARY_RestText, MSGBOX_DEFAULT
	release
	end
KantoRare_BUNEARY_Gone:
	release
	end

KantoRare_BUNEARY_Intro::
	.string "This BUNEARY keeps hopping over a\ntiny twig. It pauses after each\ljump as though waiting for\lsomeone to announce the score.$"

KantoRare_BUNEARY_Accept::
	.string "It looks at your team, then takes\na much more serious stance. The\lnext event is a friendly battle.\lYou can catch it.$"

KantoRare_BUNEARY_DeclineText::
	.string "It returns to the twig. The\nobstacle course has a very\lcommitted athlete.$"

KantoRare_BUNEARY_RestText::
	.string "BUNEARY is resting its paws.\nAnother visit will be better for\lanother match.$"

KantoRare_BUNEARY_CaughtText::
	.string "BUNEARY gives the twig one last\ntriumphant hop. The next obstacle\lcourse will be wherever you go.$"

KantoRare_ESPEON_Interact::
	lock
	faceplayer
	goto_if_set KANTO_FLAG_CAUGHT_RARE_ESPEON, KantoRare_ESPEON_Gone
	goto_if_set FLAG_TEMP_10, KantoRare_ESPEON_Rest
	msgbox KantoRare_ESPEON_Intro, MSGBOX_DEFAULT
	msgbox KantoRare_Text_Invite, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, KantoRare_ESPEON_Decline
	setvar VAR_0x8004, 21
	callnative Script_CozyWorldPrepareRare
	goto_if_eq VAR_RESULT, FALSE, KantoRare_NoHealthyTeam
	msgbox KantoRare_ESPEON_Accept, MSGBOX_DEFAULT
	setwildbattle SPECIES_ESPEON, 20
	callnative Script_CozyWorldTrainRare
	dowildbattle
	specialvar VAR_RESULT, GetBattleOutcome
	goto_if_eq VAR_RESULT, B_OUTCOME_CAUGHT, KantoRare_ESPEON_Caught
	setflag FLAG_TEMP_10
	goto KantoRare_ESPEON_Rest
KantoRare_ESPEON_Caught:
	setflag KANTO_FLAG_CAUGHT_RARE_ESPEON
	removeobject LOCALID_KANTO_RARE_ESPEON
	msgbox KantoRare_ESPEON_CaughtText, MSGBOX_DEFAULT
	release
	end
KantoRare_ESPEON_Decline:
	msgbox KantoRare_ESPEON_DeclineText, MSGBOX_DEFAULT
	release
	end
KantoRare_ESPEON_Rest:
	msgbox KantoRare_ESPEON_RestText, MSGBOX_DEFAULT
	release
	end
KantoRare_ESPEON_Gone:
	release
	end

KantoRare_ESPEON_Intro::
	.string "An ESPEON sits in a patch of\nsunlight. It watches travelers\lchoose a direction, then looks\lfaintly disappointed when they\lturn back.$"

KantoRare_ESPEON_Accept::
	.string "It rises before you finish\napproaching. Perhaps it already\lexpected a challenge. You can\lcatch it in this battle.$"

KantoRare_ESPEON_DeclineText::
	.string "It settles back into the\nsunlight. Your change of plans\lseems to have been anticipated.$"

KantoRare_ESPEON_RestText::
	.string "ESPEON is resting quietly in the\nlight. Give it another visit\lbefore another challenge.$"

KantoRare_ESPEON_CaughtText::
	.string "ESPEON takes a leisurely stretch.\nIt appears satisfied with the\ldirection this afternoon has\ltaken.$"

KantoRare_UMBREON_Interact::
	lock
	faceplayer
	goto_if_set KANTO_FLAG_CAUGHT_RARE_UMBREON, KantoRare_UMBREON_Gone
	goto_if_set FLAG_TEMP_10, KantoRare_UMBREON_Rest
	msgbox KantoRare_UMBREON_Intro, MSGBOX_DEFAULT
	msgbox KantoRare_Text_Invite, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, KantoRare_UMBREON_Decline
	setvar VAR_0x8004, 22
	callnative Script_CozyWorldPrepareRare
	goto_if_eq VAR_RESULT, FALSE, KantoRare_NoHealthyTeam
	msgbox KantoRare_UMBREON_Accept, MSGBOX_DEFAULT
	setwildbattle SPECIES_UMBREON, 18
	callnative Script_CozyWorldTrainRare
	dowildbattle
	specialvar VAR_RESULT, GetBattleOutcome
	goto_if_eq VAR_RESULT, B_OUTCOME_CAUGHT, KantoRare_UMBREON_Caught
	setflag FLAG_TEMP_10
	goto KantoRare_UMBREON_Rest
KantoRare_UMBREON_Caught:
	setflag KANTO_FLAG_CAUGHT_RARE_UMBREON
	removeobject LOCALID_KANTO_RARE_UMBREON
	msgbox KantoRare_UMBREON_CaughtText, MSGBOX_DEFAULT
	release
	end
KantoRare_UMBREON_Decline:
	msgbox KantoRare_UMBREON_DeclineText, MSGBOX_DEFAULT
	release
	end
KantoRare_UMBREON_Rest:
	msgbox KantoRare_UMBREON_RestText, MSGBOX_DEFAULT
	release
	end
KantoRare_UMBREON_Gone:
	release
	end

KantoRare_UMBREON_Intro::
	.string "An UMBREON is resting in the\nshade of the rocks. Its rings\lglow softly whenever a trainer\lrushes past without noticing it.$"

KantoRare_UMBREON_Accept::
	.string "It steps out of the shade and\nwaits. This introduction seems to\lrequire patience, then a battle.\lYou can catch it.$"

KantoRare_UMBREON_DeclineText::
	.string "It returns to the shade. The road\nis allowed to be busy without its\lparticipation.$"

KantoRare_UMBREON_RestText::
	.string "UMBREON has settled down after\nthe match. Let it rest before\lanother visit.$"

KantoRare_UMBREON_CaughtText::
	.string "UMBREON gives a quiet nod and\nlets its rings dim. It seems\lcomfortable enough to stop making\lan announcement.$"

KantoRare_LARVITAR_Interact::
	lock
	faceplayer
	goto_if_set KANTO_FLAG_CAUGHT_RARE_LARVITAR, KantoRare_LARVITAR_Gone
	goto_if_set FLAG_TEMP_10, KantoRare_LARVITAR_Rest
	msgbox KantoRare_LARVITAR_Intro, MSGBOX_DEFAULT
	msgbox KantoRare_Text_Invite, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, KantoRare_LARVITAR_Decline
	setvar VAR_0x8004, 23
	callnative Script_CozyWorldPrepareRare
	goto_if_eq VAR_RESULT, FALSE, KantoRare_NoHealthyTeam
	msgbox KantoRare_LARVITAR_Accept, MSGBOX_DEFAULT
	setwildbattle SPECIES_LARVITAR, 17
	callnative Script_CozyWorldTrainRare
	dowildbattle
	specialvar VAR_RESULT, GetBattleOutcome
	goto_if_eq VAR_RESULT, B_OUTCOME_CAUGHT, KantoRare_LARVITAR_Caught
	setflag FLAG_TEMP_10
	goto KantoRare_LARVITAR_Rest
KantoRare_LARVITAR_Caught:
	setflag KANTO_FLAG_CAUGHT_RARE_LARVITAR
	removeobject LOCALID_KANTO_RARE_LARVITAR
	msgbox KantoRare_LARVITAR_CaughtText, MSGBOX_DEFAULT
	release
	end
KantoRare_LARVITAR_Decline:
	msgbox KantoRare_LARVITAR_DeclineText, MSGBOX_DEFAULT
	release
	end
KantoRare_LARVITAR_Rest:
	msgbox KantoRare_LARVITAR_RestText, MSGBOX_DEFAULT
	release
	end
KantoRare_LARVITAR_Gone:
	release
	end

KantoRare_LARVITAR_Intro::
	.string "A LARVITAR has sampled several\nstones near ROCK TUNNEL. It\lappears to be comparing the\lmountain to an extremely large\lmenu.$"

KantoRare_LARVITAR_Accept::
	.string "It notices your team and wipes a\nlittle grit from its mouth.\lPerhaps travel offers a wider\lmenu. You can catch it in this\lbattle.$"

KantoRare_LARVITAR_DeclineText::
	.string "It returns to a particularly\npromising pebble. Your offer has\lbeen filed under after lunch.$"

KantoRare_LARVITAR_RestText::
	.string "LARVITAR is resting beside its\nstone samples. Come back after\lanother walk.$"

KantoRare_LARVITAR_CaughtText::
	.string "LARVITAR gives its favorite\npebble a farewell nibble. Its\lgeological education is becoming\la field trip.$"

KantoRare_HERACROSS_Interact::
	lock
	faceplayer
	goto_if_set KANTO_FLAG_CAUGHT_RARE_HERACROSS, KantoRare_HERACROSS_Gone
	goto_if_set FLAG_TEMP_10, KantoRare_HERACROSS_Rest
	msgbox KantoRare_HERACROSS_Intro, MSGBOX_DEFAULT
	msgbox KantoRare_Text_Invite, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, KantoRare_HERACROSS_Decline
	setvar VAR_0x8004, 24
	callnative Script_CozyWorldPrepareRare
	goto_if_eq VAR_RESULT, FALSE, KantoRare_NoHealthyTeam
	msgbox KantoRare_HERACROSS_Accept, MSGBOX_DEFAULT
	setwildbattle SPECIES_HERACROSS, 17
	callnative Script_CozyWorldTrainRare
	dowildbattle
	specialvar VAR_RESULT, GetBattleOutcome
	goto_if_eq VAR_RESULT, B_OUTCOME_CAUGHT, KantoRare_HERACROSS_Caught
	setflag FLAG_TEMP_10
	goto KantoRare_HERACROSS_Rest
KantoRare_HERACROSS_Caught:
	setflag KANTO_FLAG_CAUGHT_RARE_HERACROSS
	removeobject LOCALID_KANTO_RARE_HERACROSS
	msgbox KantoRare_HERACROSS_CaughtText, MSGBOX_DEFAULT
	release
	end
KantoRare_HERACROSS_Decline:
	msgbox KantoRare_HERACROSS_DeclineText, MSGBOX_DEFAULT
	release
	end
KantoRare_HERACROSS_Rest:
	msgbox KantoRare_HERACROSS_RestText, MSGBOX_DEFAULT
	release
	end
KantoRare_HERACROSS_Gone:
	release
	end

KantoRare_HERACROSS_Intro::
	.string "A HERACROSS is trying to move a\nfallen branch. It keeps stopping\lto let smaller Pokemon cross\lbefore continuing its very\lserious roadworks.$"

KantoRare_HERACROSS_Accept::
	.string "It sets the branch down and turns\ntoward your team. A friendly\lcontest of strength seems fair.\lYou can catch it.$"

KantoRare_HERACROSS_DeclineText::
	.string "It returns to the branch. Public\nworks wait for no beetle.$"

KantoRare_HERACROSS_RestText::
	.string "HERACROSS is resting its horn\nafter the match. Give it another\lvisit before another challenge.$"

KantoRare_HERACROSS_CaughtText::
	.string "HERACROSS nudges the branch\nneatly out of the way before\lturning back to you. The\lroadworks are complete.$"

KantoRare_DRATINI_Interact::
	lock
	faceplayer
	goto_if_set KANTO_FLAG_CAUGHT_RARE_DRATINI, KantoRare_DRATINI_Gone
	goto_if_set FLAG_TEMP_10, KantoRare_DRATINI_Rest
	msgbox KantoRare_DRATINI_Intro, MSGBOX_DEFAULT
	msgbox KantoRare_Text_Invite, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, KantoRare_DRATINI_Decline
	setvar VAR_0x8004, 25
	callnative Script_CozyWorldPrepareRare
	goto_if_eq VAR_RESULT, FALSE, KantoRare_NoHealthyTeam
	msgbox KantoRare_DRATINI_Accept, MSGBOX_DEFAULT
	setwildbattle SPECIES_DRATINI, 27
	callnative Script_CozyWorldTrainRare
	dowildbattle
	specialvar VAR_RESULT, GetBattleOutcome
	goto_if_eq VAR_RESULT, B_OUTCOME_CAUGHT, KantoRare_DRATINI_Caught
	setflag FLAG_TEMP_10
	goto KantoRare_DRATINI_Rest
KantoRare_DRATINI_Caught:
	setflag KANTO_FLAG_CAUGHT_RARE_DRATINI
	removeobject LOCALID_KANTO_RARE_DRATINI
	msgbox KantoRare_DRATINI_CaughtText, MSGBOX_DEFAULT
	release
	end
KantoRare_DRATINI_Decline:
	msgbox KantoRare_DRATINI_DeclineText, MSGBOX_DEFAULT
	release
	end
KantoRare_DRATINI_Rest:
	msgbox KantoRare_DRATINI_RestText, MSGBOX_DEFAULT
	release
	end
KantoRare_DRATINI_Gone:
	release
	end

KantoRare_DRATINI_Intro::
	.string "A DRATINI is watching the ripples\nbeside the bridge. It keeps\lglancing toward travelers as\lthough wondering where the road\lgoes when the water ends.$"

KantoRare_DRATINI_Accept::
	.string "It lifts its head and approaches\nyour team. A battle may be its\lway of asking to find out. You\lcan catch it.$"

KantoRare_DRATINI_DeclineText::
	.string "It returns to the ripples. There\nis no hurry to leave a pleasant\lplace.$"

KantoRare_DRATINI_RestText::
	.string "DRATINI is resting quietly after\nthe match. Another visit will be\lwelcome later.$"

KantoRare_DRATINI_CaughtText::
	.string "DRATINI watches one last circle\nspread across the water. Then its\lattention turns toward the road.$"

KantoRare_MISDREAVUS_Interact::
	lock
	faceplayer
	goto_if_set KANTO_FLAG_CAUGHT_RARE_MISDREAVUS, KantoRare_MISDREAVUS_Gone
	goto_if_set FLAG_TEMP_10, KantoRare_MISDREAVUS_Rest
	msgbox KantoRare_MISDREAVUS_Intro, MSGBOX_DEFAULT
	msgbox KantoRare_Text_Invite, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, KantoRare_MISDREAVUS_Decline
	setvar VAR_0x8004, 26
	callnative Script_CozyWorldPrepareRare
	goto_if_eq VAR_RESULT, FALSE, KantoRare_NoHealthyTeam
	msgbox KantoRare_MISDREAVUS_Accept, MSGBOX_DEFAULT
	setwildbattle SPECIES_MISDREAVUS, 22
	callnative Script_CozyWorldTrainRare
	dowildbattle
	specialvar VAR_RESULT, GetBattleOutcome
	goto_if_eq VAR_RESULT, B_OUTCOME_CAUGHT, KantoRare_MISDREAVUS_Caught
	setflag FLAG_TEMP_10
	goto KantoRare_MISDREAVUS_Rest
KantoRare_MISDREAVUS_Caught:
	setflag KANTO_FLAG_CAUGHT_RARE_MISDREAVUS
	removeobject LOCALID_KANTO_RARE_MISDREAVUS
	msgbox KantoRare_MISDREAVUS_CaughtText, MSGBOX_DEFAULT
	release
	end
KantoRare_MISDREAVUS_Decline:
	msgbox KantoRare_MISDREAVUS_DeclineText, MSGBOX_DEFAULT
	release
	end
KantoRare_MISDREAVUS_Rest:
	msgbox KantoRare_MISDREAVUS_RestText, MSGBOX_DEFAULT
	release
	end
KantoRare_MISDREAVUS_Gone:
	release
	end

KantoRare_MISDREAVUS_Intro::
	.string "A MISDREAVUS is practicing a\nstartling entrance beside a quiet\llane. It keeps stopping whenever\lsomebody looks genuinely upset.$"

KantoRare_MISDREAVUS_Accept::
	.string "It gives you a mischievous look\nand floats closer. A friendly\lbattle seems preferable to\lanother rehearsal. You can catch\lit.$"

KantoRare_MISDREAVUS_DeclineText::
	.string "It drifts back to the lane. Its\nnext rehearsal is considerably\lquieter.$"

KantoRare_MISDREAVUS_RestText::
	.string "MISDREAVUS is taking a quiet\ninterval after the match. Visit\lagain later.$"

KantoRare_MISDREAVUS_CaughtText::
	.string "MISDREAVUS circles you once, then\nmakes an entrance from exactly\lwhere you already knew it was. A\lpromising rehearsal.$"

KantoRare_ABSOL_Interact::
	lock
	faceplayer
	goto_if_set KANTO_FLAG_CAUGHT_RARE_ABSOL, KantoRare_ABSOL_Gone
	goto_if_set FLAG_TEMP_10, KantoRare_ABSOL_Rest
	msgbox KantoRare_ABSOL_Intro, MSGBOX_DEFAULT
	msgbox KantoRare_Text_Invite, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, KantoRare_ABSOL_Decline
	setvar VAR_0x8004, 27
	callnative Script_CozyWorldPrepareRare
	goto_if_eq VAR_RESULT, FALSE, KantoRare_NoHealthyTeam
	msgbox KantoRare_ABSOL_Accept, MSGBOX_DEFAULT
	setwildbattle SPECIES_ABSOL, 30
	callnative Script_CozyWorldTrainRare
	dowildbattle
	specialvar VAR_RESULT, GetBattleOutcome
	goto_if_eq VAR_RESULT, B_OUTCOME_CAUGHT, KantoRare_ABSOL_Caught
	setflag FLAG_TEMP_10
	goto KantoRare_ABSOL_Rest
KantoRare_ABSOL_Caught:
	setflag KANTO_FLAG_CAUGHT_RARE_ABSOL
	removeobject LOCALID_KANTO_RARE_ABSOL
	msgbox KantoRare_ABSOL_CaughtText, MSGBOX_DEFAULT
	release
	end
KantoRare_ABSOL_Decline:
	msgbox KantoRare_ABSOL_DeclineText, MSGBOX_DEFAULT
	release
	end
KantoRare_ABSOL_Rest:
	msgbox KantoRare_ABSOL_RestText, MSGBOX_DEFAULT
	release
	end
KantoRare_ABSOL_Gone:
	release
	end

KantoRare_ABSOL_Intro::
	.string "An ABSOL is carefully moving\nloose stones away from the path.\lIt looks up whenever somebody\lmistakes its serious expression\lfor a threat.$"

KantoRare_ABSOL_Accept::
	.string "It studies your team, then steps\ninto the open. A battle seems to\lbe an invitation to understand\leach other. You can catch it.$"

KantoRare_ABSOL_DeclineText::
	.string "It returns to clearing the path.\nBeing misunderstood has not\lstopped the work.$"

KantoRare_ABSOL_RestText::
	.string "ABSOL is resting beside the\ncleared stones. Let it recover\lbefore another visit.$"

KantoRare_ABSOL_CaughtText::
	.string "ABSOL checks the path once more\nbefore turning to you. It seems\lready to leave the next traveler\la safer road.$"

KantoRare_FEEBAS_Interact::
	lock
	faceplayer
	goto_if_set KANTO_FLAG_CAUGHT_RARE_FEEBAS, KantoRare_FEEBAS_Gone
	goto_if_set FLAG_TEMP_10, KantoRare_FEEBAS_Rest
	msgbox KantoRare_FEEBAS_Intro, MSGBOX_DEFAULT
	msgbox KantoRare_Text_Invite, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, KantoRare_FEEBAS_Decline
	setvar VAR_0x8004, 28
	callnative Script_CozyWorldPrepareRare
	goto_if_eq VAR_RESULT, FALSE, KantoRare_NoHealthyTeam
	msgbox KantoRare_FEEBAS_Accept, MSGBOX_DEFAULT
	setwildbattle SPECIES_FEEBAS, 32
	callnative Script_CozyWorldTrainRare
	dowildbattle
	specialvar VAR_RESULT, GetBattleOutcome
	goto_if_eq VAR_RESULT, B_OUTCOME_CAUGHT, KantoRare_FEEBAS_Caught
	setflag FLAG_TEMP_10
	goto KantoRare_FEEBAS_Rest
KantoRare_FEEBAS_Caught:
	setflag KANTO_FLAG_CAUGHT_RARE_FEEBAS
	removeobject LOCALID_KANTO_RARE_FEEBAS
	msgbox KantoRare_FEEBAS_CaughtText, MSGBOX_DEFAULT
	release
	end
KantoRare_FEEBAS_Decline:
	msgbox KantoRare_FEEBAS_DeclineText, MSGBOX_DEFAULT
	release
	end
KantoRare_FEEBAS_Rest:
	msgbox KantoRare_FEEBAS_RestText, MSGBOX_DEFAULT
	release
	end
KantoRare_FEEBAS_Gone:
	release
	end

KantoRare_FEEBAS_Intro::
	.string "A FEEBAS is making determined\nlittle circuits through the\lwater. It pauses whenever a\ltrainer passes, as though\ldeciding whether to try a much\llonger route.$"

KantoRare_FEEBAS_Accept::
	.string "It swims toward your team with\nunexpected confidence. A battle\lwill be its introduction. You can\lcatch it.$"

KantoRare_FEEBAS_DeclineText::
	.string "It resumes its circuit. A\nfamiliar route can be worth\lanother lap.$"

KantoRare_FEEBAS_RestText::
	.string "FEEBAS is resting in the water\nafter the match. Give it another\lvisit before another challenge.$"

KantoRare_FEEBAS_CaughtText::
	.string "FEEBAS completes one final\ncircuit, then swims back toward\lyou. Its longer journey appears\lto be approved.$"

KantoRare_ROTOM_Interact::
	lock
	faceplayer
	goto_if_set KANTO_FLAG_CAUGHT_RARE_ROTOM, KantoRare_ROTOM_Gone
	goto_if_set FLAG_TEMP_10, KantoRare_ROTOM_Rest
	msgbox KantoRare_ROTOM_Intro, MSGBOX_DEFAULT
	msgbox KantoRare_Text_Invite, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, KantoRare_ROTOM_Decline
	setvar VAR_0x8004, 29
	callnative Script_CozyWorldPrepareRare
	goto_if_eq VAR_RESULT, FALSE, KantoRare_NoHealthyTeam
	msgbox KantoRare_ROTOM_Accept, MSGBOX_DEFAULT
	setwildbattle SPECIES_ROTOM, 33
	callnative Script_CozyWorldTrainRare
	dowildbattle
	specialvar VAR_RESULT, GetBattleOutcome
	goto_if_eq VAR_RESULT, B_OUTCOME_CAUGHT, KantoRare_ROTOM_Caught
	setflag FLAG_TEMP_10
	goto KantoRare_ROTOM_Rest
KantoRare_ROTOM_Caught:
	setflag KANTO_FLAG_CAUGHT_RARE_ROTOM
	removeobject LOCALID_KANTO_RARE_ROTOM
	msgbox KantoRare_ROTOM_CaughtText, MSGBOX_DEFAULT
	release
	end
KantoRare_ROTOM_Decline:
	msgbox KantoRare_ROTOM_DeclineText, MSGBOX_DEFAULT
	release
	end
KantoRare_ROTOM_Rest:
	msgbox KantoRare_ROTOM_RestText, MSGBOX_DEFAULT
	release
	end
KantoRare_ROTOM_Gone:
	release
	end

KantoRare_ROTOM_Intro::
	.string "A ROTOM is hovering beside a\nsilent machine. It keeps making a\lcheerful buzzing noise, then\lwaiting as though expecting the\lmachine to answer.$"

KantoRare_ROTOM_Accept::
	.string "It turns toward your team with a\ndelighted crackle. A battle may\lbe a better conversation. You can\lcatch it.$"

KantoRare_ROTOM_DeclineText::
	.string "It returns to the machine. The\nother participant remains a very\lpoor conversationalist.$"

KantoRare_ROTOM_RestText::
	.string "ROTOM is floating quietly after\nthe match. Let it settle before\lanother visit.$"

KantoRare_ROTOM_CaughtText::
	.string "ROTOM gives the silent machine\none last hopeful buzz. Apparently\lyour team offers a more\lresponsive audience.$"

KantoRare_GIBLE_Interact::
	lock
	faceplayer
	goto_if_set KANTO_FLAG_CAUGHT_RARE_GIBLE, KantoRare_GIBLE_Gone
	goto_if_set FLAG_TEMP_10, KantoRare_GIBLE_Rest
	msgbox KantoRare_GIBLE_Intro, MSGBOX_DEFAULT
	msgbox KantoRare_Text_Invite, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, KantoRare_GIBLE_Decline
	setvar VAR_0x8004, 30
	callnative Script_CozyWorldPrepareRare
	goto_if_eq VAR_RESULT, FALSE, KantoRare_NoHealthyTeam
	msgbox KantoRare_GIBLE_Accept, MSGBOX_DEFAULT
	setwildbattle SPECIES_GIBLE, 29
	callnative Script_CozyWorldTrainRare
	dowildbattle
	specialvar VAR_RESULT, GetBattleOutcome
	goto_if_eq VAR_RESULT, B_OUTCOME_CAUGHT, KantoRare_GIBLE_Caught
	setflag FLAG_TEMP_10
	goto KantoRare_GIBLE_Rest
KantoRare_GIBLE_Caught:
	setflag KANTO_FLAG_CAUGHT_RARE_GIBLE
	removeobject LOCALID_KANTO_RARE_GIBLE
	msgbox KantoRare_GIBLE_CaughtText, MSGBOX_DEFAULT
	release
	end
KantoRare_GIBLE_Decline:
	msgbox KantoRare_GIBLE_DeclineText, MSGBOX_DEFAULT
	release
	end
KantoRare_GIBLE_Rest:
	msgbox KantoRare_GIBLE_RestText, MSGBOX_DEFAULT
	release
	end
KantoRare_GIBLE_Gone:
	release
	end

KantoRare_GIBLE_Intro::
	.string "A GIBLE is comparing a smooth\nstone with a battered bicycle\lpedal. It seems to be considering\lwhether civilization has improved\lthe quality of snacks.$"

KantoRare_GIBLE_Accept::
	.string "It sets the pedal down and faces\nyour team. A traveling partner\lmay offer better research\lopportunities. You can catch it\lin this battle.$"

KantoRare_GIBLE_DeclineText::
	.string "It returns to the comparison. The\nbicycle industry awaits the\lverdict.$"

KantoRare_GIBLE_RestText::
	.string "GIBLE is resting beside its\nsamples. Come back after another\ljourney.$"

KantoRare_GIBLE_CaughtText::
	.string "GIBLE abandons the pedal in favor\nof following you. The bicycle\lindustry has been granted a\ltemporary reprieve.$"

KantoRare_BAGON_Interact::
	lock
	faceplayer
	goto_if_set KANTO_FLAG_CAUGHT_RARE_BAGON, KantoRare_BAGON_Gone
	goto_if_set FLAG_TEMP_10, KantoRare_BAGON_Rest
	msgbox KantoRare_BAGON_Intro, MSGBOX_DEFAULT
	msgbox KantoRare_Text_Invite, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, KantoRare_BAGON_Decline
	setvar VAR_0x8004, 31
	callnative Script_CozyWorldPrepareRare
	goto_if_eq VAR_RESULT, FALSE, KantoRare_NoHealthyTeam
	msgbox KantoRare_BAGON_Accept, MSGBOX_DEFAULT
	setwildbattle SPECIES_BAGON, 34
	callnative Script_CozyWorldTrainRare
	dowildbattle
	specialvar VAR_RESULT, GetBattleOutcome
	goto_if_eq VAR_RESULT, B_OUTCOME_CAUGHT, KantoRare_BAGON_Caught
	setflag FLAG_TEMP_10
	goto KantoRare_BAGON_Rest
KantoRare_BAGON_Caught:
	setflag KANTO_FLAG_CAUGHT_RARE_BAGON
	removeobject LOCALID_KANTO_RARE_BAGON
	msgbox KantoRare_BAGON_CaughtText, MSGBOX_DEFAULT
	release
	end
KantoRare_BAGON_Decline:
	msgbox KantoRare_BAGON_DeclineText, MSGBOX_DEFAULT
	release
	end
KantoRare_BAGON_Rest:
	msgbox KantoRare_BAGON_RestText, MSGBOX_DEFAULT
	release
	end
KantoRare_BAGON_Gone:
	release
	end

KantoRare_BAGON_Intro::
	.string "A BAGON is watching the birds\nabove the island. It makes a\ldetermined little hop whenever\lone passes, then checks whether\lanybody noticed.$"

KantoRare_BAGON_Accept::
	.string "It spots your team and\nstraightens up. A battle seems\llike a more dignified\lintroduction than another hop.\lYou can catch it.$"

KantoRare_BAGON_DeclineText::
	.string "It returns to watching the sky.\nThe dream has not been withdrawn.$"

KantoRare_BAGON_RestText::
	.string "BAGON is resting after the match.\nEven determined dreamers need\lanother visit before another\lbattle.$"

KantoRare_BAGON_CaughtText::
	.string "BAGON watches one last bird cross\nthe sky, then turns proudly\ltoward you. The next part of its\ltraining will have company.$"

KantoRare_NoHealthyTeam:
	msgbox KantoRare_Text_NoHealthyTeam, MSGBOX_DEFAULT
	release
	end

KantoRare_Text_Invite::
	.string "Ask it to join you?$"

KantoRare_Text_NoHealthyTeam::
	.string "Bring a Pokemon able to battle\nbefore offering a tryout.$"

