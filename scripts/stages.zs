import mods.itemstages.ItemStages;

ItemStages.createModRestriction("create", s => {
	var items = [<item:create:copper_ingot>, <item:create:copper_sheet>, <item:create:copper_ore>, <item:create:hand_crank>, <item:create:shaft>, <item:create:andesite_alloy>, <item:create:millstone>, <item:create:cogwheel>];
	for item in items {
		if (item.anyDamage().matches(s)) {
			return true;
		}
	}
	return false;
}, "create");
ItemStages.createModRestriction("immersiveengineering", s => {
	var items = [<item:immersiveengineering:empty_casing>, <item:immersiveengineering:plate_copper>, <item:immersiveengineering:hammer>, <item:immersiveengineering:ingot_copper>, <item:immersiveengineering:ore_copper>, <item:immersiveengineering:dust_saltpeter>, <item:immersiveengineering:dust_sulfur>];
	for item in items {
		if (item.anyDamage().matches(s)) {
			return true;
		}
	}
	return false;
}, "immersiveengineering");


ItemStages.createModRestriction("chisel", "chisel");
ItemStages.createModRestriction("chiselsandbits", "chiselsandbits");

ItemStages.createModRestriction("aquaculture", "pamhc2");
ItemStages.createModRestriction("pamhc2crops", "pamhc2");
ItemStages.createModRestriction("pamhc2foodcore", "pamhc2");
ItemStages.createModRestriction("pamhc2trees", "pamhc2");
ItemStages.createModRestriction("pamhc2foodextended", "pamhc2");

ItemStages.createModRestriction("astralsorcery", "astralsorcery");
ItemStages.createModRestriction("cfm", "cfm");
ItemStages.createModRestriction("comforts", "comforts");
ItemStages.createModRestriction("cookingforblockheads", "cookingforblockheads");
ItemStages.createModRestriction("enderstorage", "enderstorage");
ItemStages.createModRestriction("ironchest", "ironchest");
ItemStages.createModRestriction("storagedrawers", "storagedrawers");
ItemStages.createModRestriction("securitycraft", "securitycraft");