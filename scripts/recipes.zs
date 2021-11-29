
craftingTable.removeByModid("enderstorage");
craftingTable.removeByModid("immersiveengineering", (name as string) => {
    return name != "crafting/empty_casing";
});
craftingTable.removeByModid("create", (name as string) => {
    return name != "milling/sandstone";
});
#craftingTable.removeRecipe(<item:immersiveengineering:empty_casing>);
#craftingTable.removeByModid("ironchest");
#craftingTable.removeByModid("immersiveengineering");