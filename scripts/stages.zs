import mods.itemstages.ItemStages;

ItemStages.createModRestriction("create", s => {
	if (<item:create:copper_ingot>.matches(s)) {
		return true;
	}
	if (<item:create:copper_sheet>.matches(s)) {
		return true;
	}
	if (<item:create:copper_ore>.matches(s)) {
		return true;
	}
	return false;
}, "create");
ItemStages.createModRestriction("chisel", "chisel");
ItemStages.createModRestriction("chiselsandbits", "chiselsandbits");

ItemStages.createModRestriction("aquaculture", "pamhc2");
ItemStages.createModRestriction("pamhc2crops", "pamhc2");
ItemStages.createModRestriction("pamhc2foodcore", "pamhc2");
ItemStages.createModRestriction("pamhc2trees", "pamhc2");
ItemStages.createModRestriction("pamhc2foodextended", "pamhc2");

ItemStages.createModRestriction("astralsorcery", "astralsorcery");
ItemStages.createModRestriction("cfm", "cfm");
ItemStages.createModRestriction("immersiveengineering", s => {
	# s => <item:minecraft:stick>.matches(s), "one"
	# println((s as string));
	if (<item:immersiveengineering:empty_casing>.matches(s)) {
		return true;
	}
	if (<item:immersiveengineering:plate_copper>.matches(s)) {
		return true;
	}
	if (<item:immersiveengineering:hammer>.anyDamage().matches(s)) {
		return true;
	}
	if (<item:immersiveengineering:ingot_copper>.matches(s)) {
		return true;
	}
	if (<item:immersiveengineering:ore_copper>.matches(s)) {
		return true;
	}
	return false;
}, "immersiveengineering");
ItemStages.createModRestriction("comforts", "comforts");
ItemStages.createModRestriction("cookingforblockheads", "cookingforblockheads");
ItemStages.createModRestriction("enderstorage", "enderstorage");
ItemStages.createModRestriction("ironchest", "ironchest");
ItemStages.createModRestriction("storagedrawers", "storagedrawers");
ItemStages.createModRestriction("securitycraft", "securitycraft");