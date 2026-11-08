LivingKanto_Scene0_A::
	lock
	faceplayer
	goto_if_set 0xa8e0, LivingKanto_Scene0_Done
	setflag 0xa8d0
	msgbox LivingKanto_Scene0_Intro, MSGBOX_DEFAULT
	release
	end

LivingKanto_Scene0_B::
	lock
	faceplayer
	goto_if_set 0xa8e0, LivingKanto_Scene0_Done
	goto_if_unset 0xa8d0, LivingKanto_Scene0_Before
	msgbox LivingKanto_Scene0_Resolve, MSGBOX_DEFAULT
	giveitem ITEM_POKE_BALL, 1
	goto_if_eq VAR_RESULT, FALSE, LivingKanto_BagFull
	setflag 0xa8e0
	release
	end

LivingKanto_Scene0_Before::
	msgbox LivingKanto_Scene0_BeforeText, MSGBOX_DEFAULT
	release
	end

LivingKanto_Scene0_Done::
	msgbox LivingKanto_Scene0_After, MSGBOX_DEFAULT
	release
	end

LivingKanto_Scene0_Intro::
	.string "I am sorting rocks by how much\nthey look like BROCK. Ask my\lsister if this one counts.$"

LivingKanto_Scene0_BeforeText::
	.string "He has brought me seventeen rocks\nand one potato.$"

LivingKanto_Scene0_Resolve::
	.string "That is definitely a potato. Take\nthis. He tried to put it in the\lrock collection.$"

LivingKanto_Scene0_After::
	.string "The potato has been moved to the\nlunch collection.$"

LivingKanto_Scene1_A::
	lock
	faceplayer
	goto_if_set 0xa8e1, LivingKanto_Scene1_Done
	setflag 0xa8d1
	msgbox LivingKanto_Scene1_Intro, MSGBOX_DEFAULT
	release
	end

LivingKanto_Scene1_B::
	lock
	faceplayer
	goto_if_set 0xa8e1, LivingKanto_Scene1_Done
	goto_if_unset 0xa8d1, LivingKanto_Scene1_Before
	msgbox LivingKanto_Scene1_Resolve, MSGBOX_DEFAULT
	giveitem ITEM_POTION, 1
	goto_if_eq VAR_RESULT, FALSE, LivingKanto_BagFull
	setflag 0xa8e1
	release
	end

LivingKanto_Scene1_Before::
	msgbox LivingKanto_Scene1_BeforeText, MSGBOX_DEFAULT
	release
	end

LivingKanto_Scene1_Done::
	msgbox LivingKanto_Scene1_After, MSGBOX_DEFAULT
	release
	end

LivingKanto_Scene1_Intro::
	.string "I am inventing a waterproof\numbrella. My friend is handling\ltesting.$"

LivingKanto_Scene1_BeforeText::
	.string "I am waiting for a non-waterproof\numbrella for comparison.$"

LivingKanto_Scene1_Resolve::
	.string "We tested it. It is an umbrella.\nPlease take our emergency drying\lsupplies.$"

LivingKanto_Scene1_After::
	.string "Our next invention is a towel\nwith fewer features.$"

LivingKanto_Scene2_A::
	lock
	faceplayer
	goto_if_set 0xa8e2, LivingKanto_Scene2_Done
	setflag 0xa8d2
	msgbox LivingKanto_Scene2_Intro, MSGBOX_DEFAULT
	release
	end

LivingKanto_Scene2_B::
	lock
	faceplayer
	goto_if_set 0xa8e2, LivingKanto_Scene2_Done
	goto_if_unset 0xa8d2, LivingKanto_Scene2_Before
	msgbox LivingKanto_Scene2_Resolve, MSGBOX_DEFAULT
	giveitem ITEM_SUPER_POTION, 1
	goto_if_eq VAR_RESULT, FALSE, LivingKanto_BagFull
	setflag 0xa8e2
	release
	end

LivingKanto_Scene2_Before::
	msgbox LivingKanto_Scene2_BeforeText, MSGBOX_DEFAULT
	release
	end

LivingKanto_Scene2_Done::
	msgbox LivingKanto_Scene2_After, MSGBOX_DEFAULT
	release
	end

LivingKanto_Scene2_Intro::
	.string "I wrote a sea shanty. Ask my\nfriend why nobody sings the\lsecond verse.$"

LivingKanto_Scene2_BeforeText::
	.string "The second verse is just\ndirections to his house.$"

LivingKanto_Scene2_Resolve::
	.string "We replaced the second verse with\nhumming. Here, thanks for\llistening.$"

LivingKanto_Scene2_After::
	.string "The chorus is now legally\ndistinct from my address.$"

LivingKanto_Scene3_A::
	lock
	faceplayer
	goto_if_set 0xa8e3, LivingKanto_Scene3_Done
	setflag 0xa8d3
	msgbox LivingKanto_Scene3_Intro, MSGBOX_DEFAULT
	release
	end

LivingKanto_Scene3_B::
	lock
	faceplayer
	goto_if_set 0xa8e3, LivingKanto_Scene3_Done
	goto_if_unset 0xa8d3, LivingKanto_Scene3_Before
	msgbox LivingKanto_Scene3_Resolve, MSGBOX_DEFAULT
	giveitem ITEM_ORAN_BERRY, 1
	goto_if_eq VAR_RESULT, FALSE, LivingKanto_BagFull
	setflag 0xa8e3
	release
	end

LivingKanto_Scene3_Before::
	msgbox LivingKanto_Scene3_BeforeText, MSGBOX_DEFAULT
	release
	end

LivingKanto_Scene3_Done::
	msgbox LivingKanto_Scene3_After, MSGBOX_DEFAULT
	release
	end

LivingKanto_Scene3_Intro::
	.string "We are planting flowers for an\nold friend. Could you ask what\lcolor she liked?$"

LivingKanto_Scene3_BeforeText::
	.string "She loved yellow flowers. She\nsaid they looked like little\lsuns.$"

LivingKanto_Scene3_Resolve::
	.string "Yellow it is. Thank you for\nasking. Please take a berry for\lthe road.$"

LivingKanto_Scene3_After::
	.string "The flowers are doing well. We\ncome by every week.$"

LivingKanto_Scene4_A::
	lock
	faceplayer
	goto_if_set 0xa8e4, LivingKanto_Scene4_Done
	setflag 0xa8d4
	msgbox LivingKanto_Scene4_Intro, MSGBOX_DEFAULT
	release
	end

LivingKanto_Scene4_B::
	lock
	faceplayer
	goto_if_set 0xa8e4, LivingKanto_Scene4_Done
	goto_if_unset 0xa8d4, LivingKanto_Scene4_Before
	msgbox LivingKanto_Scene4_Resolve, MSGBOX_DEFAULT
	giveitem ITEM_GREAT_BALL, 1
	goto_if_eq VAR_RESULT, FALSE, LivingKanto_BagFull
	setflag 0xa8e4
	release
	end

LivingKanto_Scene4_Before::
	msgbox LivingKanto_Scene4_BeforeText, MSGBOX_DEFAULT
	release
	end

LivingKanto_Scene4_Done::
	msgbox LivingKanto_Scene4_After, MSGBOX_DEFAULT
	release
	end

LivingKanto_Scene4_Intro::
	.string "I am teaching my friend to save\nmoney. Please ask how lesson one\lwent.$"

LivingKanto_Scene4_BeforeText::
	.string "I bought a very expensive\nnotebook to track my savings.$"

LivingKanto_Scene4_Resolve::
	.string "We have agreed to use both sides\nof the paper. Here, this was our\lstationery budget.$"

LivingKanto_Scene4_After::
	.string "Lesson two is walking past the\ndepartment store.$"

LivingKanto_Scene5_A::
	lock
	faceplayer
	goto_if_set 0xa8e5, LivingKanto_Scene5_Done
	setflag 0xa8d5
	msgbox LivingKanto_Scene5_Intro, MSGBOX_DEFAULT
	release
	end

LivingKanto_Scene5_B::
	lock
	faceplayer
	goto_if_set 0xa8e5, LivingKanto_Scene5_Done
	goto_if_unset 0xa8d5, LivingKanto_Scene5_Before
	msgbox LivingKanto_Scene5_Resolve, MSGBOX_DEFAULT
	giveitem ITEM_REPEL, 1
	goto_if_eq VAR_RESULT, FALSE, LivingKanto_BagFull
	setflag 0xa8e5
	release
	end

LivingKanto_Scene5_Before::
	msgbox LivingKanto_Scene5_BeforeText, MSGBOX_DEFAULT
	release
	end

LivingKanto_Scene5_Done::
	msgbox LivingKanto_Scene5_After, MSGBOX_DEFAULT
	release
	end

LivingKanto_Scene5_Intro::
	.string "I made a nature guide. Ask my\nfriend which animal I missed.$"

LivingKanto_Scene5_BeforeText::
	.string "There is no entry for people who\nlose their nature guides.$"

LivingKanto_Scene5_Resolve::
	.string "A common local species! Thanks.\nTake one of our field supplies.$"

LivingKanto_Scene5_After::
	.string "The guide now includes a map back\nto this bench.$"

LivingKanto_Scene6_A::
	lock
	faceplayer
	goto_if_set 0xa8e6, LivingKanto_Scene6_Done
	setflag 0xa8d6
	msgbox LivingKanto_Scene6_Intro, MSGBOX_DEFAULT
	release
	end

LivingKanto_Scene6_B::
	lock
	faceplayer
	goto_if_set 0xa8e6, LivingKanto_Scene6_Done
	goto_if_unset 0xa8d6, LivingKanto_Scene6_Before
	msgbox LivingKanto_Scene6_Resolve, MSGBOX_DEFAULT
	giveitem ITEM_FRESH_WATER, 1
	goto_if_eq VAR_RESULT, FALSE, LivingKanto_BagFull
	setflag 0xa8e6
	release
	end

LivingKanto_Scene6_Before::
	msgbox LivingKanto_Scene6_BeforeText, MSGBOX_DEFAULT
	release
	end

LivingKanto_Scene6_Done::
	msgbox LivingKanto_Scene6_After, MSGBOX_DEFAULT
	release
	end

LivingKanto_Scene6_Intro::
	.string "My friend claims to predict the\nfuture. Ask what I am having for\llunch.$"

LivingKanto_Scene6_BeforeText::
	.string "Lunch. I predict lunch. I am\nstarting with the reliable\lvisions.$"

LivingKanto_Scene6_Resolve::
	.string "An excellent prediction. Please\naccept this peer-review sample.$"

LivingKanto_Scene6_After::
	.string "Tomorrow we are predicting\nbreakfast.$"

LivingKanto_Scene7_A::
	lock
	faceplayer
	goto_if_set 0xa8e7, LivingKanto_Scene7_Done
	setflag 0xa8d7
	msgbox LivingKanto_Scene7_Intro, MSGBOX_DEFAULT
	release
	end

LivingKanto_Scene7_B::
	lock
	faceplayer
	goto_if_set 0xa8e7, LivingKanto_Scene7_Done
	goto_if_unset 0xa8d7, LivingKanto_Scene7_Before
	msgbox LivingKanto_Scene7_Resolve, MSGBOX_DEFAULT
	giveitem ITEM_BURN_HEAL, 1
	goto_if_eq VAR_RESULT, FALSE, LivingKanto_BagFull
	setflag 0xa8e7
	release
	end

LivingKanto_Scene7_Before::
	msgbox LivingKanto_Scene7_BeforeText, MSGBOX_DEFAULT
	release
	end

LivingKanto_Scene7_Done::
	msgbox LivingKanto_Scene7_After, MSGBOX_DEFAULT
	release
	end

LivingKanto_Scene7_Intro::
	.string "My friend says the volcano is\nasleep. Ask if we should whisper.$"

LivingKanto_Scene7_BeforeText::
	.string "It is geology. It cannot hear us.\nI still said good morning.$"

LivingKanto_Scene7_Resolve::
	.string "We agreed to be polite anyway.\nHere is something for the heat.$"

LivingKanto_Scene7_After::
	.string "Good manners cost nothing. Unlike\nvolcano insurance.$"

LivingKanto_Scene8_A::
	lock
	faceplayer
	goto_if_set 0xa8e8, LivingKanto_Scene8_Done
	setflag 0xa8d8
	msgbox LivingKanto_Scene8_Intro, MSGBOX_DEFAULT
	release
	end

LivingKanto_Scene8_B::
	lock
	faceplayer
	goto_if_set 0xa8e8, LivingKanto_Scene8_Done
	goto_if_unset 0xa8d8, LivingKanto_Scene8_Before
	msgbox LivingKanto_Scene8_Resolve, MSGBOX_DEFAULT
	giveitem ITEM_ORAN_BERRY, 1
	goto_if_eq VAR_RESULT, FALSE, LivingKanto_BagFull
	setflag 0xa8e8
	release
	end

LivingKanto_Scene8_Before::
	msgbox LivingKanto_Scene8_BeforeText, MSGBOX_DEFAULT
	release
	end

LivingKanto_Scene8_Done::
	msgbox LivingKanto_Scene8_After, MSGBOX_DEFAULT
	release
	end

LivingKanto_Scene8_Intro::
	.string "I packed everything for this\nhike. Ask my brother what I\lforgot.$"

LivingKanto_Scene8_BeforeText::
	.string "He packed three pillows and no\nwater.$"

LivingKanto_Scene8_Resolve::
	.string "Water! Right. We have a spare\nsnack, though. Please take it.$"

LivingKanto_Scene8_After::
	.string "We are walking back to buy water.\nThe pillows are staying.$"

LivingKanto_Scene9_A::
	lock
	faceplayer
	goto_if_set 0xa8e9, LivingKanto_Scene9_Done
	setflag 0xa8d9
	msgbox LivingKanto_Scene9_Intro, MSGBOX_DEFAULT
	release
	end

LivingKanto_Scene9_B::
	lock
	faceplayer
	goto_if_set 0xa8e9, LivingKanto_Scene9_Done
	goto_if_unset 0xa8d9, LivingKanto_Scene9_Before
	msgbox LivingKanto_Scene9_Resolve, MSGBOX_DEFAULT
	giveitem ITEM_AWAKENING, 1
	goto_if_eq VAR_RESULT, FALSE, LivingKanto_BagFull
	setflag 0xa8e9
	release
	end

LivingKanto_Scene9_Before::
	msgbox LivingKanto_Scene9_BeforeText, MSGBOX_DEFAULT
	release
	end

LivingKanto_Scene9_Done::
	msgbox LivingKanto_Scene9_After, MSGBOX_DEFAULT
	release
	end

LivingKanto_Scene9_Intro::
	.string "I challenged my friend to a\nstaring contest. Ask who is\lwinning.$"

LivingKanto_Scene9_BeforeText::
	.string "Neither of us remembers who\nstarted. I think it was Tuesday.$"

LivingKanto_Scene9_Resolve::
	.string "We declared a draw. Take this\nprize before somebody asks for a\lrematch.$"

LivingKanto_Scene9_After::
	.string "We are trying a blinking contest.\nMuch faster.$"

LivingKanto_Scene10_A::
	lock
	faceplayer
	goto_if_set 0xa8ea, LivingKanto_Scene10_Done
	setflag 0xa8da
	msgbox LivingKanto_Scene10_Intro, MSGBOX_DEFAULT
	release
	end

LivingKanto_Scene10_B::
	lock
	faceplayer
	goto_if_set 0xa8ea, LivingKanto_Scene10_Done
	goto_if_unset 0xa8da, LivingKanto_Scene10_Before
	msgbox LivingKanto_Scene10_Resolve, MSGBOX_DEFAULT
	giveitem ITEM_GREAT_BALL, 1
	goto_if_eq VAR_RESULT, FALSE, LivingKanto_BagFull
	setflag 0xa8ea
	release
	end

LivingKanto_Scene10_Before::
	msgbox LivingKanto_Scene10_BeforeText, MSGBOX_DEFAULT
	release
	end

LivingKanto_Scene10_Done::
	msgbox LivingKanto_Scene10_After, MSGBOX_DEFAULT
	release
	end

LivingKanto_Scene10_Intro::
	.string "My friend is making bird calls.\nPlease ask which bird that was.$"

LivingKanto_Scene10_BeforeText::
	.string "That was a bicycle brake. I am\nstill practicing the birds.$"

LivingKanto_Scene10_Resolve::
	.string "The PIDGEY seemed impressed.\nHere, take this for being our\laudience.$"

LivingKanto_Scene10_After::
	.string "We have perfected the rare\nsqueaking bicycle.$"

LivingKanto_Scene11_A::
	lock
	faceplayer
	goto_if_set 0xa8eb, LivingKanto_Scene11_Done
	setflag 0xa8db
	msgbox LivingKanto_Scene11_Intro, MSGBOX_DEFAULT
	release
	end

LivingKanto_Scene11_B::
	lock
	faceplayer
	goto_if_set 0xa8eb, LivingKanto_Scene11_Done
	goto_if_unset 0xa8db, LivingKanto_Scene11_Before
	msgbox LivingKanto_Scene11_Resolve, MSGBOX_DEFAULT
	giveitem ITEM_SODA_POP, 1
	goto_if_eq VAR_RESULT, FALSE, LivingKanto_BagFull
	setflag 0xa8eb
	release
	end

LivingKanto_Scene11_Before::
	msgbox LivingKanto_Scene11_BeforeText, MSGBOX_DEFAULT
	release
	end

LivingKanto_Scene11_Done::
	msgbox LivingKanto_Scene11_After, MSGBOX_DEFAULT
	release
	end

LivingKanto_Scene11_Intro::
	.string "I started a relaxing club. Ask\nour treasurer how membership is\lgoing.$"

LivingKanto_Scene11_BeforeText::
	.string "We have two members. Neither\nremembers which one is treasurer.$"

LivingKanto_Scene11_Resolve::
	.string "We voted to have no dues. Here,\ntake the entire refreshment fund.$"

LivingKanto_Scene11_After::
	.string "The next meeting is whenever we\nsit down again.$"

LivingKanto_BagFull::
	msgbox LivingKanto_BagFullText, MSGBOX_DEFAULT
	release
	end

LivingKanto_BagFullText::
	.string "Your BAG looks full. Come back\nwhen there is room. I will keep\lthis for you.$"
