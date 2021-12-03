
craftingTable.removeByModid("enderstorage");
craftingTable.removeByModid("immersiveengineering", (name as string) => {
    return name != "crafting/empty_casing";
});
<recipetype:create:milling>.removeByModid("create", (name as string) => {
    return name != "milling/sandstone";
});
<recipetype:create:crushing>.removeByModid("create", (name as string) => {
    return name != "crushing/blaze_rod";
});
#craftingTable.removeRecipe(<item:immersiveengineering:empty_casing>);
#craftingTable.removeByModid("ironchest");
#craftingTable.removeByModid("immersiveengineering");