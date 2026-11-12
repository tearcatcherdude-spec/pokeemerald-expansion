Variety_EventScript_BARNABY_HOENN::
	lock
	faceplayer
	goto_if_set (TRAINER_FLAGS_START + VARIETY_TRAINER_BARNABY_HOENN), Variety_EventScript_BARNABY_HOENN_Post
	goto_if_unset (TRAINER_FLAGS_START + VARIETY_TRAINER_BARNABY_KANTO), Variety_EventScript_BARNABY_HOENN_Battle
	msgbox Variety_Text_BARNABY_Reunion, MSGBOX_DEFAULT
Variety_EventScript_BARNABY_HOENN_Battle::
	trainerbattle_single VARIETY_TRAINER_BARNABY_HOENN, Variety_Text_BARNABY_Intro, Variety_Text_BARNABY_Defeat
Variety_EventScript_BARNABY_HOENN_Post::
	msgbox Variety_Text_BARNABY_Post, MSGBOX_AUTOCLOSE
	release
	end

Variety_EventScript_BARNABY_KANTO::
	lock
	faceplayer
	goto_if_set (TRAINER_FLAGS_START + VARIETY_TRAINER_BARNABY_KANTO), Variety_EventScript_BARNABY_KANTO_Post
	goto_if_unset (TRAINER_FLAGS_START + VARIETY_TRAINER_BARNABY_HOENN), Variety_EventScript_BARNABY_KANTO_Battle
	msgbox Variety_Text_BARNABY_Reunion, MSGBOX_DEFAULT
Variety_EventScript_BARNABY_KANTO_Battle::
	trainerbattle_single VARIETY_TRAINER_BARNABY_KANTO, Variety_Text_BARNABY_Intro, Variety_Text_BARNABY_Defeat
Variety_EventScript_BARNABY_KANTO_Post::
	msgbox Variety_Text_BARNABY_Post, MSGBOX_AUTOCLOSE
	release
	end

Variety_Text_BARNABY_Intro::
	.string "BARNABY BARGAIN! My potions cure\nexhaustion, doubt, and having\lmoney!\pA demonstration battle is free.\nThe demonstration is mandatory.$"

Variety_Text_BARNABY_Defeat::
	.string "A refund? On a free demonstration?$"

Variety_Text_BARNABY_Post::
	.string "My potion is water with\nconfidence.\lThe confidence is locally sourced.\pI am revising the label.\nApparently confidence needs\ltesting.$"

Variety_Text_BARNABY_Reunion::
	.string "A returning customer! Or witness!\nI've updated the label since we\lmet.$"

Variety_EventScript_VESPER_HOENN::
	lock
	faceplayer
	goto_if_set (TRAINER_FLAGS_START + VARIETY_TRAINER_VESPER_HOENN), Variety_EventScript_VESPER_HOENN_Post
	goto_if_unset (TRAINER_FLAGS_START + VARIETY_TRAINER_VESPER_KANTO), Variety_EventScript_VESPER_HOENN_Battle
	msgbox Variety_Text_VESPER_Reunion, MSGBOX_DEFAULT
Variety_EventScript_VESPER_HOENN_Battle::
	trainerbattle_single VARIETY_TRAINER_VESPER_HOENN, Variety_Text_VESPER_Intro, Variety_Text_VESPER_Defeat
Variety_EventScript_VESPER_HOENN_Post::
	msgbox Variety_Text_VESPER_Post, MSGBOX_AUTOCLOSE
	release
	end

Variety_EventScript_VESPER_KANTO::
	lock
	faceplayer
	goto_if_set (TRAINER_FLAGS_START + VARIETY_TRAINER_VESPER_KANTO), Variety_EventScript_VESPER_KANTO_Post
	goto_if_unset (TRAINER_FLAGS_START + VARIETY_TRAINER_VESPER_HOENN), Variety_EventScript_VESPER_KANTO_Battle
	msgbox Variety_Text_VESPER_Reunion, MSGBOX_DEFAULT
Variety_EventScript_VESPER_KANTO_Battle::
	trainerbattle_single VARIETY_TRAINER_VESPER_KANTO, Variety_Text_VESPER_Intro, Variety_Text_VESPER_Defeat
Variety_EventScript_VESPER_KANTO_Post::
	msgbox Variety_Text_VESPER_Post, MSGBOX_AUTOCLOSE
	release
	end

Variety_Text_VESPER_Intro::
	.string "VESPER VALE, phantom thief.\nI have stolen your attention!\pPlease keep watching. My escape\nplan depends on applause.$"

Variety_Text_VESPER_Defeat::
	.string "You stole my dramatic exit!$"

Variety_Text_VESPER_Post::
	.string "I only steal discarded trinkets.\nMostly bottle caps.\pThe calling cards cost more than\nthe entire criminal enterprise.$"

Variety_Text_VESPER_Reunion::
	.string "You again! I'd steal this reunion,\nbut I haven't paid for the cards.$"

Variety_EventScript_MARLO_HOENN::
	lock
	faceplayer
	goto_if_set (TRAINER_FLAGS_START + VARIETY_TRAINER_MARLO_HOENN), Variety_EventScript_MARLO_HOENN_Post
	goto_if_unset (TRAINER_FLAGS_START + VARIETY_TRAINER_MARLO_KANTO), Variety_EventScript_MARLO_HOENN_Battle
	msgbox Variety_Text_MARLO_Reunion, MSGBOX_DEFAULT
Variety_EventScript_MARLO_HOENN_Battle::
	trainerbattle_single VARIETY_TRAINER_MARLO_HOENN, Variety_Text_MARLO_Intro, Variety_Text_MARLO_Defeat
Variety_EventScript_MARLO_HOENN_Post::
	msgbox Variety_Text_MARLO_Post, MSGBOX_AUTOCLOSE
	release
	end

Variety_EventScript_MARLO_KANTO::
	lock
	faceplayer
	goto_if_set (TRAINER_FLAGS_START + VARIETY_TRAINER_MARLO_KANTO), Variety_EventScript_MARLO_KANTO_Post
	goto_if_unset (TRAINER_FLAGS_START + VARIETY_TRAINER_MARLO_HOENN), Variety_EventScript_MARLO_KANTO_Battle
	msgbox Variety_Text_MARLO_Reunion, MSGBOX_DEFAULT
Variety_EventScript_MARLO_KANTO_Battle::
	trainerbattle_single VARIETY_TRAINER_MARLO_KANTO, Variety_Text_MARLO_Intro, Variety_Text_MARLO_Defeat
Variety_EventScript_MARLO_KANTO_Post::
	msgbox Variety_Text_MARLO_Post, MSGBOX_AUTOCLOSE
	release
	end

Variety_Text_MARLO_Intro::
	.string "MARLO MIRTH presents: a battle\nwith a completely impartial judge!\pThe judge is me in a different\nhat.$"

Variety_Text_MARLO_Defeat::
	.string "The judge requests a recess!$"

Variety_Text_MARLO_Post::
	.string "I awarded myself second place.\nYou may have first.\pThere were only two contestants,\nbut I still made the podium.$"

Variety_Text_MARLO_Reunion::
	.string "My esteemed former opponent!\nThe judge has bought a second hat.$"

Variety_EventScript_CLATTER_HOENN::
	lock
	faceplayer
	goto_if_set (TRAINER_FLAGS_START + VARIETY_TRAINER_CLATTER_HOENN), Variety_EventScript_CLATTER_HOENN_Post
	goto_if_unset (TRAINER_FLAGS_START + VARIETY_TRAINER_CLATTER_KANTO), Variety_EventScript_CLATTER_HOENN_Battle
	msgbox Variety_Text_CLATTER_Reunion, MSGBOX_DEFAULT
Variety_EventScript_CLATTER_HOENN_Battle::
	trainerbattle_single VARIETY_TRAINER_CLATTER_HOENN, Variety_Text_CLATTER_Intro, Variety_Text_CLATTER_Defeat
Variety_EventScript_CLATTER_HOENN_Post::
	msgbox Variety_Text_CLATTER_Post, MSGBOX_AUTOCLOSE
	release
	end

Variety_EventScript_CLATTER_KANTO::
	lock
	faceplayer
	goto_if_set (TRAINER_FLAGS_START + VARIETY_TRAINER_CLATTER_KANTO), Variety_EventScript_CLATTER_KANTO_Post
	goto_if_unset (TRAINER_FLAGS_START + VARIETY_TRAINER_CLATTER_HOENN), Variety_EventScript_CLATTER_KANTO_Battle
	msgbox Variety_Text_CLATTER_Reunion, MSGBOX_DEFAULT
Variety_EventScript_CLATTER_KANTO_Battle::
	trainerbattle_single VARIETY_TRAINER_CLATTER_KANTO, Variety_Text_CLATTER_Intro, Variety_Text_CLATTER_Defeat
Variety_EventScript_CLATTER_KANTO_Post::
	msgbox Variety_Text_CLATTER_Post, MSGBOX_AUTOCLOSE
	release
	end

Variety_Text_CLATTER_Intro::
	.string "SIR CLATTER! Rule one: no running!\nRule two: no reading rule one!\pRule three: battle the official\nwho has misplaced his whistle!$"

Variety_Text_CLATTER_Defeat::
	.string "I appeal to a higher helmet!$"

Variety_Text_CLATTER_Post::
	.string "I wrote these rules to help\npeople.\lThen I ran out of useful rules.\pTomorrow: fewer rules.\nThat one is compulsory.$"

Variety_Text_CLATTER_Reunion::
	.string "A familiar challenger! You will\nfind the regulations much shorter.$"

Variety_EventScript_MOSSWICK_HOENN::
	lock
	faceplayer
	goto_if_set (TRAINER_FLAGS_START + VARIETY_TRAINER_MOSSWICK_HOENN), Variety_EventScript_MOSSWICK_HOENN_Post
	goto_if_unset (TRAINER_FLAGS_START + VARIETY_TRAINER_MOSSWICK_KANTO), Variety_EventScript_MOSSWICK_HOENN_Battle
	msgbox Variety_Text_MOSSWICK_Reunion, MSGBOX_DEFAULT
Variety_EventScript_MOSSWICK_HOENN_Battle::
	trainerbattle_single VARIETY_TRAINER_MOSSWICK_HOENN, Variety_Text_MOSSWICK_Intro, Variety_Text_MOSSWICK_Defeat
Variety_EventScript_MOSSWICK_HOENN_Post::
	msgbox Variety_Text_MOSSWICK_Post, MSGBOX_AUTOCLOSE
	release
	end

Variety_EventScript_MOSSWICK_KANTO::
	lock
	faceplayer
	goto_if_set (TRAINER_FLAGS_START + VARIETY_TRAINER_MOSSWICK_KANTO), Variety_EventScript_MOSSWICK_KANTO_Post
	goto_if_unset (TRAINER_FLAGS_START + VARIETY_TRAINER_MOSSWICK_HOENN), Variety_EventScript_MOSSWICK_KANTO_Battle
	msgbox Variety_Text_MOSSWICK_Reunion, MSGBOX_DEFAULT
Variety_EventScript_MOSSWICK_KANTO_Battle::
	trainerbattle_single VARIETY_TRAINER_MOSSWICK_KANTO, Variety_Text_MOSSWICK_Intro, Variety_Text_MOSSWICK_Defeat
Variety_EventScript_MOSSWICK_KANTO_Post::
	msgbox Variety_Text_MOSSWICK_Post, MSGBOX_AUTOCLOSE
	release
	end

Variety_Text_MOSSWICK_Intro::
	.string "MOSSWICK! Behold my smoke bomb!\n...That is a perfectly normal\lspore.\pQuick! A battle before anyone\nnotices my grand entrance failed!$"

Variety_Text_MOSSWICK_Defeat::
	.string "My grand exit is also a sneeze!$"

Variety_Text_MOSSWICK_Post::
	.string "My mushrooms refuse to prank\nanyone.\lThey have formed an ethics panel.\pI am the only member under review.$"

Variety_Text_MOSSWICK_Reunion::
	.string "Ah! My previous grand-entrance\nwitness! The mushrooms remember\lyou.$"

Variety_EventScript_NYXIE_HOENN::
	lock
	faceplayer
	goto_if_set (TRAINER_FLAGS_START + VARIETY_TRAINER_NYXIE_HOENN), Variety_EventScript_NYXIE_HOENN_Post
	goto_if_unset (TRAINER_FLAGS_START + VARIETY_TRAINER_NYXIE_KANTO), Variety_EventScript_NYXIE_HOENN_Battle
	msgbox Variety_Text_NYXIE_Reunion, MSGBOX_DEFAULT
Variety_EventScript_NYXIE_HOENN_Battle::
	trainerbattle_single VARIETY_TRAINER_NYXIE_HOENN, Variety_Text_NYXIE_Intro, Variety_Text_NYXIE_Defeat
Variety_EventScript_NYXIE_HOENN_Post::
	msgbox Variety_Text_NYXIE_Post, MSGBOX_AUTOCLOSE
	release
	end

Variety_EventScript_NYXIE_KANTO::
	lock
	faceplayer
	goto_if_set (TRAINER_FLAGS_START + VARIETY_TRAINER_NYXIE_KANTO), Variety_EventScript_NYXIE_KANTO_Post
	goto_if_unset (TRAINER_FLAGS_START + VARIETY_TRAINER_NYXIE_HOENN), Variety_EventScript_NYXIE_KANTO_Battle
	msgbox Variety_Text_NYXIE_Reunion, MSGBOX_DEFAULT
Variety_EventScript_NYXIE_KANTO_Battle::
	trainerbattle_single VARIETY_TRAINER_NYXIE_KANTO, Variety_Text_NYXIE_Intro, Variety_Text_NYXIE_Defeat
Variety_EventScript_NYXIE_KANTO_Post::
	msgbox Variety_Text_NYXIE_Post, MSGBOX_AUTOCLOSE
	release
	end

Variety_Text_NYXIE_Intro::
	.string "I'm NYXIE. This parasol is for\nmaintaining an air of mystery.\pIt also keeps ash out of my hair.\nLet us duel with practical\lelegance.$"

Variety_Text_NYXIE_Defeat::
	.string "A most inconvenient sunrise.$"

Variety_Text_NYXIE_Post::
	.string "I like quiet places. Not because\nI'm tragic. They're simply quiet.\pPeople keep offering me tissues\nwhen I just want a bench.$"

Variety_Text_NYXIE_Reunion::
	.string "We've met. How lovely to skip\nthe part about the parasol.$"

Variety_EventScript_SABLE_HOENN::
	lock
	faceplayer
	goto_if_set (TRAINER_FLAGS_START + VARIETY_TRAINER_SABLE_HOENN), Variety_EventScript_SABLE_HOENN_Post
	goto_if_unset (TRAINER_FLAGS_START + VARIETY_TRAINER_SABLE_KANTO), Variety_EventScript_SABLE_HOENN_Battle
	msgbox Variety_Text_SABLE_Reunion, MSGBOX_DEFAULT
Variety_EventScript_SABLE_HOENN_Battle::
	trainerbattle_single VARIETY_TRAINER_SABLE_HOENN, Variety_Text_SABLE_Intro, Variety_Text_SABLE_Defeat
Variety_EventScript_SABLE_HOENN_Post::
	msgbox Variety_Text_SABLE_Post, MSGBOX_AUTOCLOSE
	release
	end

Variety_EventScript_SABLE_KANTO::
	lock
	faceplayer
	goto_if_set (TRAINER_FLAGS_START + VARIETY_TRAINER_SABLE_KANTO), Variety_EventScript_SABLE_KANTO_Post
	goto_if_unset (TRAINER_FLAGS_START + VARIETY_TRAINER_SABLE_HOENN), Variety_EventScript_SABLE_KANTO_Battle
	msgbox Variety_Text_SABLE_Reunion, MSGBOX_DEFAULT
Variety_EventScript_SABLE_KANTO_Battle::
	trainerbattle_single VARIETY_TRAINER_SABLE_KANTO, Variety_Text_SABLE_Intro, Variety_Text_SABLE_Defeat
Variety_EventScript_SABLE_KANTO_Post::
	msgbox Variety_Text_SABLE_Post, MSGBOX_AUTOCLOSE
	release
	end

Variety_Text_SABLE_Intro::
	.string "SABLE. I started a protest against\nbeing told to keep off the grass.\pThen the grass asked us to move.\nBattle me while we reconsider.$"

Variety_Text_SABLE_Defeat::
	.string "The grass has a strong argument.$"

Variety_Text_SABLE_Post::
	.string "Being loud is easy. Listening\nwithout planning your next shout?\pThat's the part I'm practicing.\nDon't tell the band.$"

Variety_Text_SABLE_Reunion::
	.string "Hey, it's you. I've been\npracticing the listening part.$"

Variety_EventScript_OPALINE_HOENN::
	lock
	faceplayer
	goto_if_set (TRAINER_FLAGS_START + VARIETY_TRAINER_OPALINE_HOENN), Variety_EventScript_OPALINE_HOENN_Post
	goto_if_unset (TRAINER_FLAGS_START + VARIETY_TRAINER_OPALINE_KANTO), Variety_EventScript_OPALINE_HOENN_Battle
	msgbox Variety_Text_OPALINE_Reunion, MSGBOX_DEFAULT
Variety_EventScript_OPALINE_HOENN_Battle::
	trainerbattle_single VARIETY_TRAINER_OPALINE_HOENN, Variety_Text_OPALINE_Intro, Variety_Text_OPALINE_Defeat
Variety_EventScript_OPALINE_HOENN_Post::
	msgbox Variety_Text_OPALINE_Post, MSGBOX_AUTOCLOSE
	release
	end

Variety_EventScript_OPALINE_KANTO::
	lock
	faceplayer
	goto_if_set (TRAINER_FLAGS_START + VARIETY_TRAINER_OPALINE_KANTO), Variety_EventScript_OPALINE_KANTO_Post
	goto_if_unset (TRAINER_FLAGS_START + VARIETY_TRAINER_OPALINE_HOENN), Variety_EventScript_OPALINE_KANTO_Battle
	msgbox Variety_Text_OPALINE_Reunion, MSGBOX_DEFAULT
Variety_EventScript_OPALINE_KANTO_Battle::
	trainerbattle_single VARIETY_TRAINER_OPALINE_KANTO, Variety_Text_OPALINE_Intro, Variety_Text_OPALINE_Defeat
Variety_EventScript_OPALINE_KANTO_Post::
	msgbox Variety_Text_OPALINE_Post, MSGBOX_AUTOCLOSE
	release
	end

Variety_Text_OPALINE_Intro::
	.string "OPALINE. Yes, black lace and pink\nribbons can be on the same team.\pMy POKEMON settled the argument\nby eating both fashion magazines.$"

Variety_Text_OPALINE_Defeat::
	.string "A tasteful, devastating defeat.$"

Variety_Text_OPALINE_Post::
	.string "I design outfits for shy trainers.\nOne pocket is for emergency\lcourage.\pIt's usually full of biscuits.\nCourage travels surprisingly well.$"

Variety_Text_OPALINE_Reunion::
	.string "Oh, hello again. I restocked\nthe emergency courage pocket.$"

Variety_EventScript_CINDER_HOENN::
	lock
	faceplayer
	goto_if_set (TRAINER_FLAGS_START + VARIETY_TRAINER_CINDER_HOENN), Variety_EventScript_CINDER_HOENN_Post
	goto_if_unset (TRAINER_FLAGS_START + VARIETY_TRAINER_CINDER_KANTO), Variety_EventScript_CINDER_HOENN_Battle
	msgbox Variety_Text_CINDER_Reunion, MSGBOX_DEFAULT
Variety_EventScript_CINDER_HOENN_Battle::
	trainerbattle_single VARIETY_TRAINER_CINDER_HOENN, Variety_Text_CINDER_Intro, Variety_Text_CINDER_Defeat
Variety_EventScript_CINDER_HOENN_Post::
	msgbox Variety_Text_CINDER_Post, MSGBOX_AUTOCLOSE
	release
	end

Variety_EventScript_CINDER_KANTO::
	lock
	faceplayer
	goto_if_set (TRAINER_FLAGS_START + VARIETY_TRAINER_CINDER_KANTO), Variety_EventScript_CINDER_KANTO_Post
	goto_if_unset (TRAINER_FLAGS_START + VARIETY_TRAINER_CINDER_HOENN), Variety_EventScript_CINDER_KANTO_Battle
	msgbox Variety_Text_CINDER_Reunion, MSGBOX_DEFAULT
Variety_EventScript_CINDER_KANTO_Battle::
	trainerbattle_single VARIETY_TRAINER_CINDER_KANTO, Variety_Text_CINDER_Intro, Variety_Text_CINDER_Defeat
Variety_EventScript_CINDER_KANTO_Post::
	msgbox Variety_Text_CINDER_Post, MSGBOX_AUTOCLOSE
	release
	end

Variety_Text_CINDER_Intro::
	.string "CINDER. Mechanic. That buzzing\nis my diagnostic equipment.\pIf it starts singing, duck.\nLet's test the battle function\lfirst.$"

Variety_Text_CINDER_Defeat::
	.string "Diagnosis: needs less exploding.$"

Variety_Text_CINDER_Post::
	.string "I repair old machines because\nsomeone once cared enough to build\lthem.\pAlso, new machines have far fewer\ninteresting things wrong with\lthem.$"

Variety_Text_CINDER_Reunion::
	.string "Familiar face, new testing ground.\nThe equipment still buzzes.$"

Variety_EventScript_DAHLIA_HOENN::
	lock
	faceplayer
	goto_if_set (TRAINER_FLAGS_START + VARIETY_TRAINER_DAHLIA_HOENN), Variety_EventScript_DAHLIA_HOENN_Post
	goto_if_unset (TRAINER_FLAGS_START + VARIETY_TRAINER_DAHLIA_KANTO), Variety_EventScript_DAHLIA_HOENN_Battle
	msgbox Variety_Text_DAHLIA_Reunion, MSGBOX_DEFAULT
Variety_EventScript_DAHLIA_HOENN_Battle::
	trainerbattle_single VARIETY_TRAINER_DAHLIA_HOENN, Variety_Text_DAHLIA_Intro, Variety_Text_DAHLIA_Defeat
Variety_EventScript_DAHLIA_HOENN_Post::
	msgbox Variety_Text_DAHLIA_Post, MSGBOX_AUTOCLOSE
	release
	end

Variety_EventScript_DAHLIA_KANTO::
	lock
	faceplayer
	goto_if_set (TRAINER_FLAGS_START + VARIETY_TRAINER_DAHLIA_KANTO), Variety_EventScript_DAHLIA_KANTO_Post
	goto_if_unset (TRAINER_FLAGS_START + VARIETY_TRAINER_DAHLIA_HOENN), Variety_EventScript_DAHLIA_KANTO_Battle
	msgbox Variety_Text_DAHLIA_Reunion, MSGBOX_DEFAULT
Variety_EventScript_DAHLIA_KANTO_Battle::
	trainerbattle_single VARIETY_TRAINER_DAHLIA_KANTO, Variety_Text_DAHLIA_Intro, Variety_Text_DAHLIA_Defeat
Variety_EventScript_DAHLIA_KANTO_Post::
	msgbox Variety_Text_DAHLIA_Post, MSGBOX_AUTOCLOSE
	release
	end

Variety_Text_DAHLIA_Intro::
	.string "DAHLIA NOCT. These flowers are\nnot wilting. They're brooding.\pA little battle should improve\ntheir circulation and their\lreviews.$"

Variety_Text_DAHLIA_Defeat::
	.string "We shall brood constructively.$"

Variety_Text_DAHLIA_Post::
	.string "People buy cheerful flowers for\nsad friends. Sometimes a dark\lbloom\lis the first honest thing in the\lroom.\pI still include care instructions.\nHonesty also needs watering.$"

Variety_Text_DAHLIA_Reunion::
	.string "We meet again. The flowers have\nhad time to develop their\lopinions.$"

Variety_EventScript_ECHO_HOENN::
	lock
	faceplayer
	goto_if_set (TRAINER_FLAGS_START + VARIETY_TRAINER_ECHO_HOENN), Variety_EventScript_ECHO_HOENN_Post
	goto_if_unset (TRAINER_FLAGS_START + VARIETY_TRAINER_ECHO_KANTO), Variety_EventScript_ECHO_HOENN_Battle
	msgbox Variety_Text_ECHO_Reunion, MSGBOX_DEFAULT
Variety_EventScript_ECHO_HOENN_Battle::
	trainerbattle_single VARIETY_TRAINER_ECHO_HOENN, Variety_Text_ECHO_Intro, Variety_Text_ECHO_Defeat
Variety_EventScript_ECHO_HOENN_Post::
	msgbox Variety_Text_ECHO_Post, MSGBOX_AUTOCLOSE
	release
	end

Variety_EventScript_ECHO_KANTO::
	lock
	faceplayer
	goto_if_set (TRAINER_FLAGS_START + VARIETY_TRAINER_ECHO_KANTO), Variety_EventScript_ECHO_KANTO_Post
	goto_if_unset (TRAINER_FLAGS_START + VARIETY_TRAINER_ECHO_HOENN), Variety_EventScript_ECHO_KANTO_Battle
	msgbox Variety_Text_ECHO_Reunion, MSGBOX_DEFAULT
Variety_EventScript_ECHO_KANTO_Battle::
	trainerbattle_single VARIETY_TRAINER_ECHO_KANTO, Variety_Text_ECHO_Intro, Variety_Text_ECHO_Defeat
Variety_EventScript_ECHO_KANTO_Post::
	msgbox Variety_Text_ECHO_Post, MSGBOX_AUTOCLOSE
	release
	end

Variety_Text_ECHO_Intro::
	.string "ECHO. Arcade champion. My strategy\nis flawless if this is turn one.\pAfter that, I call it an exciting\nnew difficulty setting.$"

Variety_Text_ECHO_Defeat::
	.string "I found the difficulty setting.$"

Variety_Text_ECHO_Post::
	.string "I used to reset every losing game.\nThen I never learned the last\llevel.\pI'm keeping this loss.\nIt has useful information in it.$"

Variety_Text_ECHO_Reunion::
	.string "Hey! I kept our last match.\nLet's see what I learned from it.$"

Variety_EventScript_BRIAR_HOENN::
	lock
	faceplayer
	goto_if_set (TRAINER_FLAGS_START + VARIETY_TRAINER_BRIAR_HOENN), Variety_EventScript_BRIAR_HOENN_Post
	goto_if_unset (TRAINER_FLAGS_START + VARIETY_TRAINER_BRIAR_KANTO), Variety_EventScript_BRIAR_HOENN_Battle
	msgbox Variety_Text_BRIAR_Reunion, MSGBOX_DEFAULT
Variety_EventScript_BRIAR_HOENN_Battle::
	trainerbattle_single VARIETY_TRAINER_BRIAR_HOENN, Variety_Text_BRIAR_Intro, Variety_Text_BRIAR_Defeat
Variety_EventScript_BRIAR_HOENN_Post::
	msgbox Variety_Text_BRIAR_Post, MSGBOX_AUTOCLOSE
	release
	end

Variety_EventScript_BRIAR_KANTO::
	lock
	faceplayer
	goto_if_set (TRAINER_FLAGS_START + VARIETY_TRAINER_BRIAR_KANTO), Variety_EventScript_BRIAR_KANTO_Post
	goto_if_unset (TRAINER_FLAGS_START + VARIETY_TRAINER_BRIAR_HOENN), Variety_EventScript_BRIAR_KANTO_Battle
	msgbox Variety_Text_BRIAR_Reunion, MSGBOX_DEFAULT
Variety_EventScript_BRIAR_KANTO_Battle::
	trainerbattle_single VARIETY_TRAINER_BRIAR_KANTO, Variety_Text_BRIAR_Intro, Variety_Text_BRIAR_Defeat
Variety_EventScript_BRIAR_KANTO_Post::
	msgbox Variety_Text_BRIAR_Post, MSGBOX_AUTOCLOSE
	release
	end

Variety_Text_BRIAR_Intro::
	.string "BRIAR. My jacket has thorns.\nMy team has thorns.\pMy sandwich was a logistical\nerror.\lLet's battle before lunch.$"

Variety_Text_BRIAR_Defeat::
	.string "A prickly situation, resolved.$"

Variety_Text_BRIAR_Post::
	.string "I plant flowers in forgotten\nplaces.\lThe council calls it unauthorized.\pThe COMBEE call it lunch.\nI value both forms of feedback.$"

Variety_Text_BRIAR_Reunion::
	.string "You again! The COMBEE remember\nyour contribution to field\ltesting.$"

Variety_EventScript_FABLE_HOENN::
	lock
	faceplayer
	goto_if_set (TRAINER_FLAGS_START + VARIETY_TRAINER_FABLE_HOENN), Variety_EventScript_FABLE_HOENN_Post
	goto_if_unset (TRAINER_FLAGS_START + VARIETY_TRAINER_FABLE_KANTO), Variety_EventScript_FABLE_HOENN_Battle
	msgbox Variety_Text_FABLE_Reunion, MSGBOX_DEFAULT
Variety_EventScript_FABLE_HOENN_Battle::
	trainerbattle_single VARIETY_TRAINER_FABLE_HOENN, Variety_Text_FABLE_Intro, Variety_Text_FABLE_Defeat
Variety_EventScript_FABLE_HOENN_Post::
	msgbox Variety_Text_FABLE_Post, MSGBOX_AUTOCLOSE
	release
	end

Variety_EventScript_FABLE_KANTO::
	lock
	faceplayer
	goto_if_set (TRAINER_FLAGS_START + VARIETY_TRAINER_FABLE_KANTO), Variety_EventScript_FABLE_KANTO_Post
	goto_if_unset (TRAINER_FLAGS_START + VARIETY_TRAINER_FABLE_HOENN), Variety_EventScript_FABLE_KANTO_Battle
	msgbox Variety_Text_FABLE_Reunion, MSGBOX_DEFAULT
Variety_EventScript_FABLE_KANTO_Battle::
	trainerbattle_single VARIETY_TRAINER_FABLE_KANTO, Variety_Text_FABLE_Intro, Variety_Text_FABLE_Defeat
Variety_EventScript_FABLE_KANTO_Post::
	msgbox Variety_Text_FABLE_Post, MSGBOX_AUTOCLOSE
	release
	end

Variety_Text_FABLE_Intro::
	.string "FABLE. I'm collecting stories.\nEvery good one needs a challenge.\pYou look like a reasonable middle\nchapter. Shall we begin?$"

Variety_Text_FABLE_Defeat::
	.string "An unexpectedly strong edit.$"

Variety_Text_FABLE_Post::
	.string "I leave the endings of my stories\nblank until I meet the people\lagain.\pPeople deserve a chance to\nsurprise\lthe person writing about them.$"

Variety_Text_FABLE_Reunion::
	.string "A returning character!\nI saved a blank page for this.$"

Variety_EventScript_TAFFY_HOENN::
	lock
	faceplayer
	goto_if_set (TRAINER_FLAGS_START + VARIETY_TRAINER_TAFFY_HOENN), Variety_EventScript_TAFFY_HOENN_Post
	goto_if_unset (TRAINER_FLAGS_START + VARIETY_TRAINER_TAFFY_KANTO), Variety_EventScript_TAFFY_HOENN_Battle
	msgbox Variety_Text_TAFFY_Reunion, MSGBOX_DEFAULT
Variety_EventScript_TAFFY_HOENN_Battle::
	trainerbattle_single VARIETY_TRAINER_TAFFY_HOENN, Variety_Text_TAFFY_Intro, Variety_Text_TAFFY_Defeat
Variety_EventScript_TAFFY_HOENN_Post::
	msgbox Variety_Text_TAFFY_Post, MSGBOX_AUTOCLOSE
	release
	end

Variety_EventScript_TAFFY_KANTO::
	lock
	faceplayer
	goto_if_set (TRAINER_FLAGS_START + VARIETY_TRAINER_TAFFY_KANTO), Variety_EventScript_TAFFY_KANTO_Post
	goto_if_unset (TRAINER_FLAGS_START + VARIETY_TRAINER_TAFFY_HOENN), Variety_EventScript_TAFFY_KANTO_Battle
	msgbox Variety_Text_TAFFY_Reunion, MSGBOX_DEFAULT
Variety_EventScript_TAFFY_KANTO_Battle::
	trainerbattle_single VARIETY_TRAINER_TAFFY_KANTO, Variety_Text_TAFFY_Intro, Variety_Text_TAFFY_Defeat
Variety_EventScript_TAFFY_KANTO_Post::
	msgbox Variety_Text_TAFFY_Post, MSGBOX_AUTOCLOSE
	release
	end

Variety_Text_TAFFY_Intro::
	.string "TAFFY! My team is adorable!\nAlso extensively trained!\pPlease admire the ribbons before\nexperiencing the consequences.$"

Variety_Text_TAFFY_Defeat::
	.string "The consequences were mutual!$"

Variety_Text_TAFFY_Post::
	.string "Cute isn't the opposite of strong.\nMy JIGGLYPUFF can lift my\lsuitcase.\pGetting it to pack sensibly\nremains\la much more difficult operation.$"

Variety_Text_TAFFY_Reunion::
	.string "There you are! New ribbons,\nsame extremely determined team!$"

Variety_EventScript_ROUX_HOENN::
	lock
	faceplayer
	goto_if_set (TRAINER_FLAGS_START + VARIETY_TRAINER_ROUX_HOENN), Variety_EventScript_ROUX_HOENN_Post
	goto_if_unset (TRAINER_FLAGS_START + VARIETY_TRAINER_ROUX_KANTO), Variety_EventScript_ROUX_HOENN_Battle
	msgbox Variety_Text_ROUX_Reunion, MSGBOX_DEFAULT
Variety_EventScript_ROUX_HOENN_Battle::
	trainerbattle_single VARIETY_TRAINER_ROUX_HOENN, Variety_Text_ROUX_Intro, Variety_Text_ROUX_Defeat
Variety_EventScript_ROUX_HOENN_Post::
	msgbox Variety_Text_ROUX_Post, MSGBOX_AUTOCLOSE
	release
	end

Variety_EventScript_ROUX_KANTO::
	lock
	faceplayer
	goto_if_set (TRAINER_FLAGS_START + VARIETY_TRAINER_ROUX_KANTO), Variety_EventScript_ROUX_KANTO_Post
	goto_if_unset (TRAINER_FLAGS_START + VARIETY_TRAINER_ROUX_HOENN), Variety_EventScript_ROUX_KANTO_Battle
	msgbox Variety_Text_ROUX_Reunion, MSGBOX_DEFAULT
Variety_EventScript_ROUX_KANTO_Battle::
	trainerbattle_single VARIETY_TRAINER_ROUX_KANTO, Variety_Text_ROUX_Intro, Variety_Text_ROUX_Defeat
Variety_EventScript_ROUX_KANTO_Post::
	msgbox Variety_Text_ROUX_Post, MSGBOX_AUTOCLOSE
	release
	end

Variety_Text_ROUX_Intro::
	.string "ROUX. Bass player. Nobody notices\nyou until you stop playing.\pMy team would like to demonstrate\nbeing very difficult to ignore.$"

Variety_Text_ROUX_Defeat::
	.string "That's our experimental ending.$"

Variety_Text_ROUX_Post::
	.string "I used to play louder when I felt\nleft out. Now I ask for a solo.\pIt works better.\nThe neighbors wrote to thank me.$"

Variety_Text_ROUX_Reunion::
	.string "Oh, hey. I've been working\non a new solo since our last\lmatch.$"

Variety_EventScript_HUGO_HOENN::
	lock
	faceplayer
	goto_if_set (TRAINER_FLAGS_START + VARIETY_TRAINER_HUGO_HOENN), Variety_EventScript_HUGO_HOENN_Post
	goto_if_unset (TRAINER_FLAGS_START + VARIETY_TRAINER_HUGO_KANTO), Variety_EventScript_HUGO_HOENN_Battle
	msgbox Variety_Text_HUGO_Reunion, MSGBOX_DEFAULT
Variety_EventScript_HUGO_HOENN_Battle::
	trainerbattle_single VARIETY_TRAINER_HUGO_HOENN, Variety_Text_HUGO_Intro, Variety_Text_HUGO_Defeat
Variety_EventScript_HUGO_HOENN_Post::
	msgbox Variety_Text_HUGO_Post, MSGBOX_AUTOCLOSE
	release
	end

Variety_EventScript_HUGO_KANTO::
	lock
	faceplayer
	goto_if_set (TRAINER_FLAGS_START + VARIETY_TRAINER_HUGO_KANTO), Variety_EventScript_HUGO_KANTO_Post
	goto_if_unset (TRAINER_FLAGS_START + VARIETY_TRAINER_HUGO_HOENN), Variety_EventScript_HUGO_KANTO_Battle
	msgbox Variety_Text_HUGO_Reunion, MSGBOX_DEFAULT
Variety_EventScript_HUGO_KANTO_Battle::
	trainerbattle_single VARIETY_TRAINER_HUGO_KANTO, Variety_Text_HUGO_Intro, Variety_Text_HUGO_Defeat
Variety_EventScript_HUGO_KANTO_Post::
	msgbox Variety_Text_HUGO_Post, MSGBOX_AUTOCLOSE
	release
	end

Variety_Text_HUGO_Intro::
	.string "HUGO BOULDER. Our lunch committee\nhas reached a difficult question.\pIs soup a beverage? We have agreed\nto settle nothing and battle\linstead.$"

Variety_Text_HUGO_Defeat::
	.string "The soup remains under review.$"

Variety_Text_HUGO_Post::
	.string "OTIS says soup needs a spoon.\nBASTIAN says the ocean disagrees.\pI study stars. None of them\nhave volunteered to chair this\lmeeting.$"

Variety_Text_HUGO_Reunion::
	.string "A familiar face! Excellent.\nThe soup debate needs fresh\levidence.$"

Variety_EventScript_OTIS_HOENN::
	lock
	faceplayer
	goto_if_set (TRAINER_FLAGS_START + VARIETY_TRAINER_OTIS_HOENN), Variety_EventScript_OTIS_HOENN_Post
	goto_if_unset (TRAINER_FLAGS_START + VARIETY_TRAINER_OTIS_KANTO), Variety_EventScript_OTIS_HOENN_Battle
	msgbox Variety_Text_OTIS_Reunion, MSGBOX_DEFAULT
Variety_EventScript_OTIS_HOENN_Battle::
	trainerbattle_single VARIETY_TRAINER_OTIS_HOENN, Variety_Text_OTIS_Intro, Variety_Text_OTIS_Defeat
Variety_EventScript_OTIS_HOENN_Post::
	msgbox Variety_Text_OTIS_Post, MSGBOX_AUTOCLOSE
	release
	end

Variety_EventScript_OTIS_KANTO::
	lock
	faceplayer
	goto_if_set (TRAINER_FLAGS_START + VARIETY_TRAINER_OTIS_KANTO), Variety_EventScript_OTIS_KANTO_Post
	goto_if_unset (TRAINER_FLAGS_START + VARIETY_TRAINER_OTIS_HOENN), Variety_EventScript_OTIS_KANTO_Battle
	msgbox Variety_Text_OTIS_Reunion, MSGBOX_DEFAULT
Variety_EventScript_OTIS_KANTO_Battle::
	trainerbattle_single VARIETY_TRAINER_OTIS_KANTO, Variety_Text_OTIS_Intro, Variety_Text_OTIS_Defeat
Variety_EventScript_OTIS_KANTO_Post::
	msgbox Variety_Text_OTIS_Post, MSGBOX_AUTOCLOSE
	release
	end

Variety_Text_OTIS_Intro::
	.string "OTIS CRUMB. Baker, treasurer,\nand keeper of the emergency\lbiscuits.\pThis battle is not an emergency.\nThe biscuits disagree.$"

Variety_Text_OTIS_Defeat::
	.string "A perfectly valid biscuit\nemergency!$"

Variety_Text_OTIS_Post::
	.string "The six of us split the bill\nevenly.\lORSON writes a poem on the\lreceipt.\pThe waiter has asked us to stop\nclaiming poetry as legal tender.$"

Variety_Text_OTIS_Reunion::
	.string "Hello again! I've saved you\na metaphorical biscuit. Let's\lbattle.$"

Variety_EventScript_BASTIAN_HOENN::
	lock
	faceplayer
	goto_if_set (TRAINER_FLAGS_START + VARIETY_TRAINER_BASTIAN_HOENN), Variety_EventScript_BASTIAN_HOENN_Post
	goto_if_unset (TRAINER_FLAGS_START + VARIETY_TRAINER_BASTIAN_KANTO), Variety_EventScript_BASTIAN_HOENN_Battle
	msgbox Variety_Text_BASTIAN_Reunion, MSGBOX_DEFAULT
Variety_EventScript_BASTIAN_HOENN_Battle::
	trainerbattle_single VARIETY_TRAINER_BASTIAN_HOENN, Variety_Text_BASTIAN_Intro, Variety_Text_BASTIAN_Defeat
Variety_EventScript_BASTIAN_HOENN_Post::
	msgbox Variety_Text_BASTIAN_Post, MSGBOX_AUTOCLOSE
	release
	end

Variety_EventScript_BASTIAN_KANTO::
	lock
	faceplayer
	goto_if_set (TRAINER_FLAGS_START + VARIETY_TRAINER_BASTIAN_KANTO), Variety_EventScript_BASTIAN_KANTO_Post
	goto_if_unset (TRAINER_FLAGS_START + VARIETY_TRAINER_BASTIAN_HOENN), Variety_EventScript_BASTIAN_KANTO_Battle
	msgbox Variety_Text_BASTIAN_Reunion, MSGBOX_DEFAULT
Variety_EventScript_BASTIAN_KANTO_Battle::
	trainerbattle_single VARIETY_TRAINER_BASTIAN_KANTO, Variety_Text_BASTIAN_Intro, Variety_Text_BASTIAN_Defeat
Variety_EventScript_BASTIAN_KANTO_Post::
	msgbox Variety_Text_BASTIAN_Post, MSGBOX_AUTOCLOSE
	release
	end

Variety_Text_BASTIAN_Intro::
	.string "BASTIAN TIDE. Marine botanist.\nI asked whether the salad was\llocal.\pThey showed me the kitchen.\nLet's battle while I refine the\lquestion.$"

Variety_Text_BASTIAN_Defeat::
	.string "A remarkably vigorous ecosystem!$"

Variety_Text_BASTIAN_Post::
	.string "I brought seaweed for the\ncommittee.\lFLORIAN arranged it in a vase.\pIt does look lovely.\nIt also tastes considerably less\llovely.$"

Variety_Text_BASTIAN_Reunion::
	.string "We meet again! I have collected\nseveral more complicated salad\lquestions.$"

Variety_EventScript_MONTY_HOENN::
	lock
	faceplayer
	goto_if_set (TRAINER_FLAGS_START + VARIETY_TRAINER_MONTY_HOENN), Variety_EventScript_MONTY_HOENN_Post
	goto_if_unset (TRAINER_FLAGS_START + VARIETY_TRAINER_MONTY_KANTO), Variety_EventScript_MONTY_HOENN_Battle
	msgbox Variety_Text_MONTY_Reunion, MSGBOX_DEFAULT
Variety_EventScript_MONTY_HOENN_Battle::
	trainerbattle_single VARIETY_TRAINER_MONTY_HOENN, Variety_Text_MONTY_Intro, Variety_Text_MONTY_Defeat
Variety_EventScript_MONTY_HOENN_Post::
	msgbox Variety_Text_MONTY_Post, MSGBOX_AUTOCLOSE
	release
	end

Variety_EventScript_MONTY_KANTO::
	lock
	faceplayer
	goto_if_set (TRAINER_FLAGS_START + VARIETY_TRAINER_MONTY_KANTO), Variety_EventScript_MONTY_KANTO_Post
	goto_if_unset (TRAINER_FLAGS_START + VARIETY_TRAINER_MONTY_HOENN), Variety_EventScript_MONTY_KANTO_Battle
	msgbox Variety_Text_MONTY_Reunion, MSGBOX_DEFAULT
Variety_EventScript_MONTY_KANTO_Battle::
	trainerbattle_single VARIETY_TRAINER_MONTY_KANTO, Variety_Text_MONTY_Intro, Variety_Text_MONTY_Defeat
Variety_EventScript_MONTY_KANTO_Post::
	msgbox Variety_Text_MONTY_Post, MSGBOX_AUTOCLOSE
	release
	end

Variety_Text_MONTY_Intro::
	.string "MONTY MALLOW. Skater. Our meeting\nminutes contain no actual minutes.\pI timed them. Forty-seven seconds.\nWe have plenty of room for a\lbattle.$"

Variety_Text_MONTY_Defeat::
	.string "A new personal best at losing!$"

Variety_Text_MONTY_Post::
	.string "I proposed wheels on the table.\nHUGO proposed thinking first.\pFor the sake of the soup,\nwe have reached a compromise:\lchairs.$"

Variety_Text_MONTY_Reunion::
	.string "Hey! You remember the routine.\nThis time I've timed the\lintroduction.$"

Variety_EventScript_FLORIAN_HOENN::
	lock
	faceplayer
	goto_if_set (TRAINER_FLAGS_START + VARIETY_TRAINER_FLORIAN_HOENN), Variety_EventScript_FLORIAN_HOENN_Post
	goto_if_unset (TRAINER_FLAGS_START + VARIETY_TRAINER_FLORIAN_KANTO), Variety_EventScript_FLORIAN_HOENN_Battle
	msgbox Variety_Text_FLORIAN_Reunion, MSGBOX_DEFAULT
Variety_EventScript_FLORIAN_HOENN_Battle::
	trainerbattle_single VARIETY_TRAINER_FLORIAN_HOENN, Variety_Text_FLORIAN_Intro, Variety_Text_FLORIAN_Defeat
Variety_EventScript_FLORIAN_HOENN_Post::
	msgbox Variety_Text_FLORIAN_Post, MSGBOX_AUTOCLOSE
	release
	end

Variety_EventScript_FLORIAN_KANTO::
	lock
	faceplayer
	goto_if_set (TRAINER_FLAGS_START + VARIETY_TRAINER_FLORIAN_KANTO), Variety_EventScript_FLORIAN_KANTO_Post
	goto_if_unset (TRAINER_FLAGS_START + VARIETY_TRAINER_FLORIAN_HOENN), Variety_EventScript_FLORIAN_KANTO_Battle
	msgbox Variety_Text_FLORIAN_Reunion, MSGBOX_DEFAULT
Variety_EventScript_FLORIAN_KANTO_Battle::
	trainerbattle_single VARIETY_TRAINER_FLORIAN_KANTO, Variety_Text_FLORIAN_Intro, Variety_Text_FLORIAN_Defeat
Variety_EventScript_FLORIAN_KANTO_Post::
	msgbox Variety_Text_FLORIAN_Post, MSGBOX_AUTOCLOSE
	release
	end

Variety_Text_FLORIAN_Intro::
	.string "FLORIAN BLOOM. I've arranged the\nflowers in order of battle\lreadiness.\pThe centerpiece is undefeated.\nI would like to catch up.$"

Variety_Text_FLORIAN_Defeat::
	.string "The centerpiece keeps its title.$"

Variety_Text_FLORIAN_Post::
	.string "We meet because six people can\nmake a bad week feel much smaller.\pAlso, OTIS brings bread.\nWe are allowed two reasons.$"

Variety_Text_FLORIAN_Reunion::
	.string "It's good to see you again.\nThe centerpiece has been training\ltoo.$"

Variety_EventScript_ORSON_HOENN::
	lock
	faceplayer
	goto_if_set (TRAINER_FLAGS_START + VARIETY_TRAINER_ORSON_HOENN), Variety_EventScript_ORSON_HOENN_Post
	goto_if_unset (TRAINER_FLAGS_START + VARIETY_TRAINER_ORSON_KANTO), Variety_EventScript_ORSON_HOENN_Battle
	msgbox Variety_Text_ORSON_Reunion, MSGBOX_DEFAULT
Variety_EventScript_ORSON_HOENN_Battle::
	trainerbattle_single VARIETY_TRAINER_ORSON_HOENN, Variety_Text_ORSON_Intro, Variety_Text_ORSON_Defeat
Variety_EventScript_ORSON_HOENN_Post::
	msgbox Variety_Text_ORSON_Post, MSGBOX_AUTOCLOSE
	release
	end

Variety_EventScript_ORSON_KANTO::
	lock
	faceplayer
	goto_if_set (TRAINER_FLAGS_START + VARIETY_TRAINER_ORSON_KANTO), Variety_EventScript_ORSON_KANTO_Post
	goto_if_unset (TRAINER_FLAGS_START + VARIETY_TRAINER_ORSON_HOENN), Variety_EventScript_ORSON_KANTO_Battle
	msgbox Variety_Text_ORSON_Reunion, MSGBOX_DEFAULT
Variety_EventScript_ORSON_KANTO_Battle::
	trainerbattle_single VARIETY_TRAINER_ORSON_KANTO, Variety_Text_ORSON_Intro, Variety_Text_ORSON_Defeat
Variety_EventScript_ORSON_KANTO_Post::
	msgbox Variety_Text_ORSON_Post, MSGBOX_AUTOCLOSE
	release
	end

Variety_Text_ORSON_Intro::
	.string "ORSON VELVET! I have composed\na sonnet to this humble sandwich.\pIt has fourteen lines and mustard.\nYour battle shall be its final\lstanza!$"

Variety_Text_ORSON_Defeat::
	.string "Alas! A devastating enjambment!$"

Variety_Text_ORSON_Post::
	.string "The others let me read my poems.\nI let them finish lunch first.\pArt needs an audience.\nAn audience needs a sandwich.$"

Variety_Text_ORSON_Reunion::
	.string "My worthy rival returns!\nThe sandwich has acquired a\lsequel!$"

Variety_EventScript_KESTREL_HOENN::
	lock
	faceplayer
	goto_if_set (TRAINER_FLAGS_START + VARIETY_TRAINER_KESTREL_HOENN), Variety_EventScript_KESTREL_HOENN_Post
	goto_if_unset (TRAINER_FLAGS_START + VARIETY_TRAINER_KESTREL_KANTO), Variety_EventScript_KESTREL_HOENN_Battle
	msgbox Variety_Text_KESTREL_Reunion, MSGBOX_DEFAULT
Variety_EventScript_KESTREL_HOENN_Battle::
	trainerbattle_single VARIETY_TRAINER_KESTREL_HOENN, Variety_Text_KESTREL_Intro, Variety_Text_KESTREL_Defeat
Variety_EventScript_KESTREL_HOENN_Post::
	msgbox Variety_Text_KESTREL_Post, MSGBOX_AUTOCLOSE
	release
	end

Variety_EventScript_KESTREL_KANTO::
	lock
	faceplayer
	goto_if_set (TRAINER_FLAGS_START + VARIETY_TRAINER_KESTREL_KANTO), Variety_EventScript_KESTREL_KANTO_Post
	goto_if_unset (TRAINER_FLAGS_START + VARIETY_TRAINER_KESTREL_HOENN), Variety_EventScript_KESTREL_KANTO_Battle
	msgbox Variety_Text_KESTREL_Reunion, MSGBOX_DEFAULT
Variety_EventScript_KESTREL_KANTO_Battle::
	trainerbattle_single VARIETY_TRAINER_KESTREL_KANTO, Variety_Text_KESTREL_Intro, Variety_Text_KESTREL_Defeat
Variety_EventScript_KESTREL_KANTO_Post::
	msgbox Variety_Text_KESTREL_Post, MSGBOX_AUTOCLOSE
	release
	end

Variety_Text_KESTREL_Intro::
	.string "KESTREL. Weather courier.\nToday's forecast: scattered\lchallenges.\pOne is approaching from directly\nin front of you. Battle now!$"

Variety_Text_KESTREL_Defeat::
	.string "An unforeseen pressure drop!$"

Variety_Text_KESTREL_Post::
	.string "I deliver weather reports by hand.\nIf I arrive soaked, I am also\lthe supporting evidence.\pNobody tips for that part.$"

Variety_Text_KESTREL_Reunion::
	.string "You again! Forecast update:\na strong chance of a second\lbattle.$"

Variety_EventScript_JUNIPER_HOENN::
	lock
	faceplayer
	goto_if_set (TRAINER_FLAGS_START + VARIETY_TRAINER_JUNIPER_HOENN), Variety_EventScript_JUNIPER_HOENN_Post
	goto_if_unset (TRAINER_FLAGS_START + VARIETY_TRAINER_JUNIPER_KANTO), Variety_EventScript_JUNIPER_HOENN_Battle
	msgbox Variety_Text_JUNIPER_Reunion, MSGBOX_DEFAULT
Variety_EventScript_JUNIPER_HOENN_Battle::
	trainerbattle_single VARIETY_TRAINER_JUNIPER_HOENN, Variety_Text_JUNIPER_Intro, Variety_Text_JUNIPER_Defeat
Variety_EventScript_JUNIPER_HOENN_Post::
	msgbox Variety_Text_JUNIPER_Post, MSGBOX_AUTOCLOSE
	release
	end

Variety_EventScript_JUNIPER_KANTO::
	lock
	faceplayer
	goto_if_set (TRAINER_FLAGS_START + VARIETY_TRAINER_JUNIPER_KANTO), Variety_EventScript_JUNIPER_KANTO_Post
	goto_if_unset (TRAINER_FLAGS_START + VARIETY_TRAINER_JUNIPER_HOENN), Variety_EventScript_JUNIPER_KANTO_Battle
	msgbox Variety_Text_JUNIPER_Reunion, MSGBOX_DEFAULT
Variety_EventScript_JUNIPER_KANTO_Battle::
	trainerbattle_single VARIETY_TRAINER_JUNIPER_KANTO, Variety_Text_JUNIPER_Intro, Variety_Text_JUNIPER_Defeat
Variety_EventScript_JUNIPER_KANTO_Post::
	msgbox Variety_Text_JUNIPER_Post, MSGBOX_AUTOCLOSE
	release
	end

Variety_Text_JUNIPER_Intro::
	.string "JUNIPER. Climber. Three points\nof contact at all times!\pUnless you're throwing a BALL.\nThen the lecture becomes a battle.$"

Variety_Text_JUNIPER_Defeat::
	.string "A safe and educational landing!$"

Variety_Text_JUNIPER_Post::
	.string "I used to climb to prove I wasn't\nafraid. I was afraid the whole\ltime.\pNow I check the ropes and climb\nbecause I like the view.$"

Variety_Text_JUNIPER_Reunion::
	.string "Good to see you! I've checked\nthe ropes. Your team looks ready\ltoo.$"

Variety_EventScript_SOLACE_HOENN::
	lock
	faceplayer
	goto_if_set (TRAINER_FLAGS_START + VARIETY_TRAINER_SOLACE_HOENN), Variety_EventScript_SOLACE_HOENN_Post
	goto_if_unset (TRAINER_FLAGS_START + VARIETY_TRAINER_SOLACE_KANTO), Variety_EventScript_SOLACE_HOENN_Battle
	msgbox Variety_Text_SOLACE_Reunion, MSGBOX_DEFAULT
Variety_EventScript_SOLACE_HOENN_Battle::
	trainerbattle_single VARIETY_TRAINER_SOLACE_HOENN, Variety_Text_SOLACE_Intro, Variety_Text_SOLACE_Defeat
Variety_EventScript_SOLACE_HOENN_Post::
	msgbox Variety_Text_SOLACE_Post, MSGBOX_AUTOCLOSE
	release
	end

Variety_EventScript_SOLACE_KANTO::
	lock
	faceplayer
	goto_if_set (TRAINER_FLAGS_START + VARIETY_TRAINER_SOLACE_KANTO), Variety_EventScript_SOLACE_KANTO_Post
	goto_if_unset (TRAINER_FLAGS_START + VARIETY_TRAINER_SOLACE_HOENN), Variety_EventScript_SOLACE_KANTO_Battle
	msgbox Variety_Text_SOLACE_Reunion, MSGBOX_DEFAULT
Variety_EventScript_SOLACE_KANTO_Battle::
	trainerbattle_single VARIETY_TRAINER_SOLACE_KANTO, Variety_Text_SOLACE_Intro, Variety_Text_SOLACE_Defeat
Variety_EventScript_SOLACE_KANTO_Post::
	msgbox Variety_Text_SOLACE_Post, MSGBOX_AUTOCLOSE
	release
	end

Variety_Text_SOLACE_Intro::
	.string "SOLACE. I make wind chimes.\nEach one has a different voice.\pMy team would like to test the\nacoustics of a friendly battle.$"

Variety_Text_SOLACE_Defeat::
	.string "A very persuasive final note.$"

Variety_Text_SOLACE_Post::
	.string "My first chime was made from\nbroken cups after we moved house.\pI wanted something familiar to\nmake\la sound in a place that wasn't\lyet.$"

Variety_Text_SOLACE_Reunion::
	.string "Hello again. I've tuned the\nchimes since our last meeting.$"

Variety_EventScript_IDRIS_HOENN::
	lock
	faceplayer
	goto_if_set (TRAINER_FLAGS_START + VARIETY_TRAINER_IDRIS_HOENN), Variety_EventScript_IDRIS_HOENN_Post
	goto_if_unset (TRAINER_FLAGS_START + VARIETY_TRAINER_IDRIS_KANTO), Variety_EventScript_IDRIS_HOENN_Battle
	msgbox Variety_Text_IDRIS_Reunion, MSGBOX_DEFAULT
Variety_EventScript_IDRIS_HOENN_Battle::
	trainerbattle_single VARIETY_TRAINER_IDRIS_HOENN, Variety_Text_IDRIS_Intro, Variety_Text_IDRIS_Defeat
Variety_EventScript_IDRIS_HOENN_Post::
	msgbox Variety_Text_IDRIS_Post, MSGBOX_AUTOCLOSE
	release
	end

Variety_EventScript_IDRIS_KANTO::
	lock
	faceplayer
	goto_if_set (TRAINER_FLAGS_START + VARIETY_TRAINER_IDRIS_KANTO), Variety_EventScript_IDRIS_KANTO_Post
	goto_if_unset (TRAINER_FLAGS_START + VARIETY_TRAINER_IDRIS_HOENN), Variety_EventScript_IDRIS_KANTO_Battle
	msgbox Variety_Text_IDRIS_Reunion, MSGBOX_DEFAULT
Variety_EventScript_IDRIS_KANTO_Battle::
	trainerbattle_single VARIETY_TRAINER_IDRIS_KANTO, Variety_Text_IDRIS_Intro, Variety_Text_IDRIS_Defeat
Variety_EventScript_IDRIS_KANTO_Post::
	msgbox Variety_Text_IDRIS_Post, MSGBOX_AUTOCLOSE
	release
	end

Variety_Text_IDRIS_Intro::
	.string "IDRIS. Sky watcher. I have named\nthat cloud after my greatest\lrival.\pIt keeps changing shape to avoid\nthe rematch. You seem more\lreliable.$"

Variety_Text_IDRIS_Defeat::
	.string "The cloud will be unbearable now.$"

Variety_Text_IDRIS_Post::
	.string "I chart the sky for travelers who\ncan't see the stars from their\lrooms.\pSome nights all I can send is:\ncloudy, but still up there.$"

Variety_Text_IDRIS_Reunion::
	.string "My cloud rival has competition!\nWelcome back to the ground\ldivision.$"

Variety_EventScript_FEN_HOENN::
	lock
	faceplayer
	goto_if_set (TRAINER_FLAGS_START + VARIETY_TRAINER_FEN_HOENN), Variety_EventScript_FEN_HOENN_Post
	goto_if_unset (TRAINER_FLAGS_START + VARIETY_TRAINER_FEN_KANTO), Variety_EventScript_FEN_HOENN_Battle
	msgbox Variety_Text_FEN_Reunion, MSGBOX_DEFAULT
Variety_EventScript_FEN_HOENN_Battle::
	trainerbattle_single VARIETY_TRAINER_FEN_HOENN, Variety_Text_FEN_Intro, Variety_Text_FEN_Defeat
Variety_EventScript_FEN_HOENN_Post::
	msgbox Variety_Text_FEN_Post, MSGBOX_AUTOCLOSE
	release
	end

Variety_EventScript_FEN_KANTO::
	lock
	faceplayer
	goto_if_set (TRAINER_FLAGS_START + VARIETY_TRAINER_FEN_KANTO), Variety_EventScript_FEN_KANTO_Post
	goto_if_unset (TRAINER_FLAGS_START + VARIETY_TRAINER_FEN_HOENN), Variety_EventScript_FEN_KANTO_Battle
	msgbox Variety_Text_FEN_Reunion, MSGBOX_DEFAULT
Variety_EventScript_FEN_KANTO_Battle::
	trainerbattle_single VARIETY_TRAINER_FEN_KANTO, Variety_Text_FEN_Intro, Variety_Text_FEN_Defeat
Variety_EventScript_FEN_KANTO_Post::
	msgbox Variety_Text_FEN_Post, MSGBOX_AUTOCLOSE
	release
	end

Variety_Text_FEN_Intro::
	.string "FEN. Cartographer. This map says\nthe path is perfectly smooth.\pMy chair and I have filed a\ndetailed\lobjection. Battle while the ink\ldries?$"

Variety_Text_FEN_Defeat::
	.string "I'll mark that as a tough route!$"

Variety_Text_FEN_Post::
	.string "A good map tells you more than\nwhere the stairs are. It tells you\lwhich way you can actually go.\pMine includes benches, ramps,\nand the best places to watch\lbirds.$"

Variety_Text_FEN_Reunion::
	.string "Oh, hello! I've added our last\nmeeting to the interesting-routes\lnotes.$"

Variety_EventScript_TARO_HOENN::
	lock
	faceplayer
	goto_if_set (TRAINER_FLAGS_START + VARIETY_TRAINER_TARO_HOENN), Variety_EventScript_TARO_HOENN_Post
	goto_if_unset (TRAINER_FLAGS_START + VARIETY_TRAINER_TARO_KANTO), Variety_EventScript_TARO_HOENN_Battle
	msgbox Variety_Text_TARO_Reunion, MSGBOX_DEFAULT
Variety_EventScript_TARO_HOENN_Battle::
	trainerbattle_single VARIETY_TRAINER_TARO_HOENN, Variety_Text_TARO_Intro, Variety_Text_TARO_Defeat
Variety_EventScript_TARO_HOENN_Post::
	msgbox Variety_Text_TARO_Post, MSGBOX_AUTOCLOSE
	release
	end

Variety_EventScript_TARO_KANTO::
	lock
	faceplayer
	goto_if_set (TRAINER_FLAGS_START + VARIETY_TRAINER_TARO_KANTO), Variety_EventScript_TARO_KANTO_Post
	goto_if_unset (TRAINER_FLAGS_START + VARIETY_TRAINER_TARO_HOENN), Variety_EventScript_TARO_KANTO_Battle
	msgbox Variety_Text_TARO_Reunion, MSGBOX_DEFAULT
Variety_EventScript_TARO_KANTO_Battle::
	trainerbattle_single VARIETY_TRAINER_TARO_KANTO, Variety_Text_TARO_Intro, Variety_Text_TARO_Defeat
Variety_EventScript_TARO_KANTO_Post::
	msgbox Variety_Text_TARO_Post, MSGBOX_AUTOCLOSE
	release
	end

Variety_Text_TARO_Intro::
	.string "TARO. Tailor. I can repair a cape\nwhile its owner is still posing.\pMy team calls that multitasking.\nLet's add a battle to the\lschedule.$"

Variety_Text_TARO_Defeat::
	.string "That strategy needs a new lining.$"

Variety_Text_TARO_Post::
	.string "Every patch on my coat came from\nsomeone who taught me something.\pThis elbow was a lesson in\nnot sewing while wearing the coat.$"

Variety_Text_TARO_Reunion::
	.string "A familiar face! The coat has\na new patch and I have a new plan.$"

Variety_EventScript_COSMO_HOENN::
	lock
	faceplayer
	goto_if_set (TRAINER_FLAGS_START + VARIETY_TRAINER_COSMO_HOENN), Variety_EventScript_COSMO_HOENN_Post
	goto_if_unset (TRAINER_FLAGS_START + VARIETY_TRAINER_COSMO_KANTO), Variety_EventScript_COSMO_HOENN_Battle
	msgbox Variety_Text_COSMO_Reunion, MSGBOX_DEFAULT
Variety_EventScript_COSMO_HOENN_Battle::
	trainerbattle_single VARIETY_TRAINER_COSMO_HOENN, Variety_Text_COSMO_Intro, Variety_Text_COSMO_Defeat
Variety_EventScript_COSMO_HOENN_Post::
	msgbox Variety_Text_COSMO_Post, MSGBOX_AUTOCLOSE
	release
	end

Variety_EventScript_COSMO_KANTO::
	lock
	faceplayer
	goto_if_set (TRAINER_FLAGS_START + VARIETY_TRAINER_COSMO_KANTO), Variety_EventScript_COSMO_KANTO_Post
	goto_if_unset (TRAINER_FLAGS_START + VARIETY_TRAINER_COSMO_HOENN), Variety_EventScript_COSMO_KANTO_Battle
	msgbox Variety_Text_COSMO_Reunion, MSGBOX_DEFAULT
Variety_EventScript_COSMO_KANTO_Battle::
	trainerbattle_single VARIETY_TRAINER_COSMO_KANTO, Variety_Text_COSMO_Intro, Variety_Text_COSMO_Defeat
Variety_EventScript_COSMO_KANTO_Post::
	msgbox Variety_Text_COSMO_Post, MSGBOX_AUTOCLOSE
	release
	end

Variety_Text_COSMO_Intro::
	.string "COSMO! Master of the night sky!\nAssistant manager of this\lafternoon!\pFor my next trick, a constellation\nmade entirely of POKEMON battles!$"

Variety_Text_COSMO_Defeat::
	.string "The stars request a brief\ninterval.$"

Variety_Text_COSMO_Post::
	.string "I learned the constellations wrong\nand spent years calling one 'the\lsock.'\pChildren remember it better that\nway.\lThe sock is staying.$"

Variety_Text_COSMO_Reunion::
	.string "My returning star! Tonight's\nprogram includes a second\lperformance!$"

Variety_EventScript_NETTLE_HOENN::
	lock
	faceplayer
	goto_if_set (TRAINER_FLAGS_START + VARIETY_TRAINER_NETTLE_HOENN), Variety_EventScript_NETTLE_HOENN_Post
	goto_if_unset (TRAINER_FLAGS_START + VARIETY_TRAINER_NETTLE_KANTO), Variety_EventScript_NETTLE_HOENN_Battle
	msgbox Variety_Text_NETTLE_Reunion, MSGBOX_DEFAULT
Variety_EventScript_NETTLE_HOENN_Battle::
	trainerbattle_single VARIETY_TRAINER_NETTLE_HOENN, Variety_Text_NETTLE_Intro, Variety_Text_NETTLE_Defeat
Variety_EventScript_NETTLE_HOENN_Post::
	msgbox Variety_Text_NETTLE_Post, MSGBOX_AUTOCLOSE
	release
	end

Variety_EventScript_NETTLE_KANTO::
	lock
	faceplayer
	goto_if_set (TRAINER_FLAGS_START + VARIETY_TRAINER_NETTLE_KANTO), Variety_EventScript_NETTLE_KANTO_Post
	goto_if_unset (TRAINER_FLAGS_START + VARIETY_TRAINER_NETTLE_HOENN), Variety_EventScript_NETTLE_KANTO_Battle
	msgbox Variety_Text_NETTLE_Reunion, MSGBOX_DEFAULT
Variety_EventScript_NETTLE_KANTO_Battle::
	trainerbattle_single VARIETY_TRAINER_NETTLE_KANTO, Variety_Text_NETTLE_Intro, Variety_Text_NETTLE_Defeat
Variety_EventScript_NETTLE_KANTO_Post::
	msgbox Variety_Text_NETTLE_Post, MSGBOX_AUTOCLOSE
	release
	end

Variety_Text_NETTLE_Intro::
	.string "NETTLE. Tea connoisseur.\nThis cup needs three more minutes.\pYou look like a two-minute battle.\nDo try to surprise me.$"

Variety_Text_NETTLE_Defeat::
	.string "I'll put the kettle on again.$"

Variety_Text_NETTLE_Post::
	.string "People ask for the secret to a\nlong\llife. I tell them: let the tea\lcool.\pIt's not the whole secret,\nbut it prevents a very silly\lending.$"

Variety_Text_NETTLE_Reunion::
	.string "You again. This time I've\nput on enough water for another\lpot.$"

Variety_EventScript_MIRI_HOENN::
	lock
	faceplayer
	goto_if_set (TRAINER_FLAGS_START + VARIETY_TRAINER_MIRI_HOENN), Variety_EventScript_MIRI_HOENN_Post
	goto_if_unset (TRAINER_FLAGS_START + VARIETY_TRAINER_MIRI_KANTO), Variety_EventScript_MIRI_HOENN_Battle
	msgbox Variety_Text_MIRI_Reunion, MSGBOX_DEFAULT
Variety_EventScript_MIRI_HOENN_Battle::
	trainerbattle_single VARIETY_TRAINER_MIRI_HOENN, Variety_Text_MIRI_Intro, Variety_Text_MIRI_Defeat
Variety_EventScript_MIRI_HOENN_Post::
	msgbox Variety_Text_MIRI_Post, MSGBOX_AUTOCLOSE
	release
	end

Variety_EventScript_MIRI_KANTO::
	lock
	faceplayer
	goto_if_set (TRAINER_FLAGS_START + VARIETY_TRAINER_MIRI_KANTO), Variety_EventScript_MIRI_KANTO_Post
	goto_if_unset (TRAINER_FLAGS_START + VARIETY_TRAINER_MIRI_HOENN), Variety_EventScript_MIRI_KANTO_Battle
	msgbox Variety_Text_MIRI_Reunion, MSGBOX_DEFAULT
Variety_EventScript_MIRI_KANTO_Battle::
	trainerbattle_single VARIETY_TRAINER_MIRI_KANTO, Variety_Text_MIRI_Intro, Variety_Text_MIRI_Defeat
Variety_EventScript_MIRI_KANTO_Post::
	msgbox Variety_Text_MIRI_Post, MSGBOX_AUTOCLOSE
	release
	end

Variety_Text_MIRI_Intro::
	.string "MIRI. Accordion player. I know\ntwelve songs and thirty apologies.\pMy team knows a battle\narrangement.\lPlease hold your applause until we\lstop.$"

Variety_Text_MIRI_Defeat::
	.string "That was the extended apology mix.$"

Variety_Text_MIRI_Post::
	.string "I play requests for sailors.\nMostly songs that remind them of\lhome.\pI pretend not to notice when they\nsing the wrong words very\lcarefully.$"

Variety_Text_MIRI_Reunion::
	.string "Oh, hello! I've learned a new\narrangement and two more\lapologies.$"

Variety_EventScript_ZEPHYR_HOENN::
	lock
	faceplayer
	goto_if_set (TRAINER_FLAGS_START + VARIETY_TRAINER_ZEPHYR_HOENN), Variety_EventScript_ZEPHYR_HOENN_Post
	goto_if_unset (TRAINER_FLAGS_START + VARIETY_TRAINER_ZEPHYR_KANTO), Variety_EventScript_ZEPHYR_HOENN_Battle
	msgbox Variety_Text_ZEPHYR_Reunion, MSGBOX_DEFAULT
Variety_EventScript_ZEPHYR_HOENN_Battle::
	trainerbattle_single VARIETY_TRAINER_ZEPHYR_HOENN, Variety_Text_ZEPHYR_Intro, Variety_Text_ZEPHYR_Defeat
Variety_EventScript_ZEPHYR_HOENN_Post::
	msgbox Variety_Text_ZEPHYR_Post, MSGBOX_AUTOCLOSE
	release
	end

Variety_EventScript_ZEPHYR_KANTO::
	lock
	faceplayer
	goto_if_set (TRAINER_FLAGS_START + VARIETY_TRAINER_ZEPHYR_KANTO), Variety_EventScript_ZEPHYR_KANTO_Post
	goto_if_unset (TRAINER_FLAGS_START + VARIETY_TRAINER_ZEPHYR_HOENN), Variety_EventScript_ZEPHYR_KANTO_Battle
	msgbox Variety_Text_ZEPHYR_Reunion, MSGBOX_DEFAULT
Variety_EventScript_ZEPHYR_KANTO_Battle::
	trainerbattle_single VARIETY_TRAINER_ZEPHYR_KANTO, Variety_Text_ZEPHYR_Intro, Variety_Text_ZEPHYR_Defeat
Variety_EventScript_ZEPHYR_KANTO_Post::
	msgbox Variety_Text_ZEPHYR_Post, MSGBOX_AUTOCLOSE
	release
	end

Variety_Text_ZEPHYR_Intro::
	.string "ZEPHYR. Street dancer. That\nstumble\lwas part of the routine.\pSo is this battle.\nPlease don't ask about the next\lstumble.$"

Variety_Text_ZEPHYR_Defeat::
	.string "A daring return to floor level!$"

Variety_Text_ZEPHYR_Post::
	.string "I teach dance to people who say\nthey have two left feet.\pMy SPINDA has four directions\nand none of them are right. We\lmanage.$"

Variety_Text_ZEPHYR_Reunion::
	.string "Welcome back! I've practiced\nthe bit where I stay upright.$"

Variety_EventScript_ELDEN_HOENN::
	lock
	faceplayer
	goto_if_set (TRAINER_FLAGS_START + VARIETY_TRAINER_ELDEN_HOENN), Variety_EventScript_ELDEN_HOENN_Post
	goto_if_unset (TRAINER_FLAGS_START + VARIETY_TRAINER_ELDEN_KANTO), Variety_EventScript_ELDEN_HOENN_Battle
	msgbox Variety_Text_ELDEN_Reunion, MSGBOX_DEFAULT
Variety_EventScript_ELDEN_HOENN_Battle::
	trainerbattle_single VARIETY_TRAINER_ELDEN_HOENN, Variety_Text_ELDEN_Intro, Variety_Text_ELDEN_Defeat
Variety_EventScript_ELDEN_HOENN_Post::
	msgbox Variety_Text_ELDEN_Post, MSGBOX_AUTOCLOSE
	release
	end

Variety_EventScript_ELDEN_KANTO::
	lock
	faceplayer
	goto_if_set (TRAINER_FLAGS_START + VARIETY_TRAINER_ELDEN_KANTO), Variety_EventScript_ELDEN_KANTO_Post
	goto_if_unset (TRAINER_FLAGS_START + VARIETY_TRAINER_ELDEN_HOENN), Variety_EventScript_ELDEN_KANTO_Battle
	msgbox Variety_Text_ELDEN_Reunion, MSGBOX_DEFAULT
Variety_EventScript_ELDEN_KANTO_Battle::
	trainerbattle_single VARIETY_TRAINER_ELDEN_KANTO, Variety_Text_ELDEN_Intro, Variety_Text_ELDEN_Defeat
Variety_EventScript_ELDEN_KANTO_Post::
	msgbox Variety_Text_ELDEN_Post, MSGBOX_AUTOCLOSE
	release
	end

Variety_Text_ELDEN_Intro::
	.string "ELDEN GLIMMER. Photographer.\nI've waited an hour for perfect\llight.\pMy team has decided to manufacture\nsome. A battle should do it.$"

Variety_Text_ELDEN_Defeat::
	.string "Wonderful! Slightly overexposed!$"

Variety_Text_ELDEN_Post::
	.string "I used to chase rare photographs.\nNow I return to the same small\lpond.\pSomething changes every evening.\nYou have to stay long enough to\lnotice.$"

Variety_Text_ELDEN_Reunion::
	.string "Good to see you again.\nDifferent place, different light.$"

