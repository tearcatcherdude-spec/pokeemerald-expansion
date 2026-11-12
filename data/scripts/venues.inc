Venue_EventScript_Otis::
	lock
	faceplayer
	msgbox Venue_Text_Otis, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, Venue_OtisNo
	msgbox Venue_Text_OtisYes, MSGBOX_DEFAULT
	goto Venue_End
Venue_OtisNo:
	msgbox Venue_Text_OtisNo, MSGBOX_DEFAULT
	goto Venue_End
Venue_EventScript_Taffy::
	msgbox Venue_Text_Taffy, MSGBOX_NPC
	end
Venue_EventScript_Florian::
	lock
	faceplayer
	msgbox Venue_Text_Florian, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, Venue_FlorianNo
	msgbox Venue_Text_FlorianYes, MSGBOX_DEFAULT
	goto Venue_End
Venue_FlorianNo:
	msgbox Venue_Text_FlorianNo, MSGBOX_DEFAULT
	goto Venue_End
Venue_EventScript_Dahlia::
	msgbox Venue_Text_Dahlia, MSGBOX_NPC
	end
Venue_EventScript_Echo::
	lock
	faceplayer
	msgbox Venue_Text_Echo, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, Venue_EchoNo
	msgbox Venue_Text_EchoYes, MSGBOX_DEFAULT
	goto Venue_End
Venue_EchoNo:
	msgbox Venue_Text_EchoNo, MSGBOX_DEFAULT
	goto Venue_End
Venue_EventScript_Fen::
	msgbox Venue_Text_Fen, MSGBOX_NPC
	end
Venue_EventScript_Roux::
	msgbox Venue_Text_Roux, MSGBOX_NPC
	end
Venue_EventScript_Zephyr::
	lock
	faceplayer
	msgbox Venue_Text_Zephyr, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, Venue_ZephyrNo
	playse SE_SELECT
	msgbox Venue_Text_ZephyrYes, MSGBOX_DEFAULT
	goto Venue_End
Venue_ZephyrNo:
	msgbox Venue_Text_ZephyrNo, MSGBOX_DEFAULT
	goto Venue_End
Venue_EventScript_Nettle::
	lock
	faceplayer
	msgbox Venue_Text_Nettle, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, Venue_NettleNo
	msgbox Venue_Text_NettleYes, MSGBOX_DEFAULT
	goto Venue_End
Venue_NettleNo:
	msgbox Venue_Text_NettleNo, MSGBOX_DEFAULT
	goto Venue_End
Venue_EventScript_Orson::
	msgbox Venue_Text_Orson, MSGBOX_NPC
	end
Venue_EventScript_Mosswick::
	msgbox Venue_Text_Mosswick, MSGBOX_NPC
	end
Venue_End:
	release
	end

Venue_Text_Otis:
	.string "OTIS: Should I enter this loaf in\n"
	.string "a BEAUTY CONTEST? Be honest.$"
Venue_Text_OtisYes:
	.string "It has excellent poise. Terrible\n"
	.string "footwork. We are training.$"
Venue_Text_OtisNo:
	.string "Fair. It keeps eating the ribbon.\n"
	.string "Or I do. The evidence is crumbs.$"
Venue_Text_Taffy:
	.string "TAFFY: I iced tiny smiles on these\n"
	.string "cakes so nobody eats alone.\p"
	.string "That one looks like it knows tax\n"
	.string "law. Please eat it first.$"
Venue_Text_Florian:
	.string "FLORIAN: May I name a flower after\n"
	.string "your team? No paperwork involved.$"
Venue_Text_FlorianYes:
	.string "The Brave Little Almost Disaster!\n"
	.string "It blooms after a difficult day.$"
Venue_Text_FlorianNo:
	.string "A private garden. I respect that.\n"
	.string "I will call it Definitely A Plant.$"
Venue_Text_Dahlia:
	.string "DAHLIA: People call these flowers\n"
	.string "dramatic. They are purple.\p"
	.string "I wrote them a twelve-page defense.\n"
	.string "That may have weakened our case.$"
Venue_Text_Echo:
	.string "ECHO: The relay says our password\n"
	.string "is TOO EMOTIONAL. Try please?$"
Venue_Text_EchoYes:
	.string "ACCESS GRANTED. Oh. It just wanted\n"
	.string "someone to ask nicely.$"
Venue_Text_EchoNo:
	.string "Valid. We can stare at the screen\n"
	.string "until it apologizes.$"
Venue_Text_Fen:
	.string "FEN: Clear aisles. Reachable desks.\n"
	.string "That is what good design looks like.\p"
	.string "My map labels this console OOPS.\n"
	.string "An important technical distinction.$"
Venue_Text_Roux:
	.string "ROUX: The bass is a conversation.\n"
	.string "Tonight it is saying BWOM.\p"
	.string "An eloquent speaker. I try not to\n"
	.string "interrupt.$"
Venue_Text_Zephyr:
	.string "ZEPHYR: Want a one-step dance\n"
	.string "lesson? No coolness test.$"
Venue_Text_ZephyrYes:
	.string "Step. Stop. Congratulations!\n"
	.string "That was contemporary confidence.\p"
	.string "Do it badly if you like. The floor\n"
	.string "has signed a silence agreement.$"
Venue_Text_ZephyrNo:
	.string "Watching counts. You brought your\n"
	.string "own rhythm; no rush to share it.$"
Venue_Text_Nettle:
	.string "NETTLE: Would you like to hear\n"
	.string "a truly shocking tea secret?$"
Venue_Text_NettleYes:
	.string "The tiny spoon is just a spoon.\n"
	.string "I have been furious for decades.$"
Venue_Text_NettleNo:
	.string "Wise. Some truths are too small\n"
	.string "to stir a decent cup.$"
Venue_Text_Orson:
	.string "ORSON: I wrote a poem about a cup.\n"
	.string "It has a handle on its feelings.\p"
	.string "You can sit quietly here. Nobody\n"
	.string "has to earn a peaceful minute.$"
Venue_Text_Mosswick:
	.string "MOSSWICK: He looks suspicious. His\n"
	.string "lesson notes are beautifully neat.\p"
	.string "I checked. Even the MAGIKARP page.\n"
	.string "It has a tiny diagram of a tail.$"
