
craftingTable.removeByModid("enderstorage");
craftingTable.removeByModid("immersiveengineering", (name as string) => {
    return name != "crafting/empty_casing";
});
<recipetype:create:milling>.removeRecipe(<item:create:standstone>);
#craftingTable.removeRecipe(<item:immersiveengineering:empty_casing>);
#craftingTable.removeByModid("ironchest");
#craftingTable.removeByModid("immersiveengineering");