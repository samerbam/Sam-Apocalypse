
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

craftingTable.removeByModid("tinymobfarm", (name as string) => {
    return name != "tinymobfarm:lasso";
});

loot.modifiers.registerUnconditional("add_spawner_shards", (drops, ctx) => {
    // println("this is a string test");
    // println((drops as string));
    // println((ctx.lootTableId as string));

    if ((ctx.lootTableId as string) == "minecraft:blocks/spawner") {
        drops.add(<item:contenttweaker:spawner_shard>);
    }
    return drops;
});
#craftingTable.removeRecipe(<item:immersiveengineering:empty_casing>);
#craftingTable.removeByModid("ironchest");
#craftingTable.removeByModid("immersiveengineering");