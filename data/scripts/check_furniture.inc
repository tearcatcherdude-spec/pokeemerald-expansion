EventScript_PictureBookShelf::
	msgbox Text_PictureBookShelf, MSGBOX_SIGN
	.if !IS_FRLG
	call Cozy_EventScript_InspectPictureBookShelf
	.endif
	end

EventScript_BookShelf::
	msgbox Text_BookShelf, MSGBOX_SIGN
	.if !IS_FRLG
	call Cozy_EventScript_InspectBookShelf
	.endif
	end

EventScript_PokemonCenterBookShelf::
	msgbox Text_PokemonCenterBookShelf, MSGBOX_SIGN
	end

EventScript_Vase::
	msgbox Text_Vase, MSGBOX_SIGN
	.if !IS_FRLG
	call Cozy_EventScript_InspectVase
	.endif
	end

EventScript_EmptyTrashCan::
	msgbox Text_EmptyTrashCan, MSGBOX_SIGN
	.if !IS_FRLG
	call Cozy_EventScript_InspectEmptyTrashCan
	.endif
	end

EventScript_ShopShelf::
	msgbox Text_ShopShelf, MSGBOX_SIGN
	.if !IS_FRLG
	call Cozy_EventScript_InspectShopShelf
	.endif
	end

EventScript_Blueprint::
	msgbox Text_Blueprint, MSGBOX_SIGN
	.if !IS_FRLG
	call Cozy_EventScript_InspectBlueprint
	.endif
	end
