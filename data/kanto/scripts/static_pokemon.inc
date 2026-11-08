EventScript_RemoveStaticMon::
	fadescreenswapbuffers FADE_TO_BLACK
	removeobject KANTO_VAR_LAST_TALKED
	fadescreenswapbuffers FADE_FROM_BLACK
	release
	call Pip_EventScript_NPCReaction
	end

EventScript_MonFlewAway::
	fadescreenswapbuffers FADE_TO_BLACK
	removeobject KANTO_VAR_LAST_TALKED
	fadescreenswapbuffers FADE_FROM_BLACK
	bufferspeciesname STR_VAR_1, KANTO_VAR_0x8004
	msgbox Text_MonFlewAway
	release
	call Pip_EventScript_NPCReaction
	end

EventScript_AwakenSnorlax::
	message Text_PlayedPokeFlute
	waitmessage
	playfanfare MUS_RG_POKE_FLUTE
	waitfanfare
	msgbox Text_SnorlaxWokeUp
	return
