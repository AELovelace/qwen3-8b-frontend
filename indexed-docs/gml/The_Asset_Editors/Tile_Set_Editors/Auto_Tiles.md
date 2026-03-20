# Auto Tiles

The **Auto Tile** feature is an incredibly powerful tool that can be used to make level building much easier, whether it is for a top down or side on view project. Essentially, you create an auto tile *library*, and then whenever you lay down a tile from that library it will "connect" with those tiles that are around it to create a seamless wall or platform.

Before you start using the auto tile feature, however, it is very important that you have set up the tile set sprite correctly and that you choose an appropriate type of auto tile. The types available to you are **47 tile** auto tiles, or **16 tile** auto tiles, with (in general) 16 tiles being used for top down or landscapes (since they give nicer transitions) and 47 being used for platformer/side on views or topdown where walls require multiple connections, but that is by no means a hard and fast rule and will depend on how you want your final project to look.

The image below shows a typical 47 tile and 16 tile tile set for autotiling:

Now, just looking at the images doesn't really tell you how they will fit together so we'll open the **Autotile Editor** from the [Tile Set Editor](../Tile_Sets.md) and add them. The Autotile Editor looks like this:

Note that the tile set sprite being used has ALL the tiles we require, and can also have other tiles, since you can pick and choose which ones to be in the auto tile. You can now click  on the 47 tile button in the Templates area to create a new 47 tile library entry and it will bring up the template to use for selecting the tiles you need:

In the template, the light grey area represents the outside edge of the tile being used and the darker grey is the "fill" area. To add a tile into the template, simply click on the first available template cell and then select the tile to add from the left:

If you make a mistake, simply select the autotile that you want to remove and select the "empty" tile from the tile set. After you have added them all in you can check the tiles against the template by clicking the "Show Template" button  at the top, and this will toggle the template overlay on the final autotile, as shown in the image below:

If you want to make a 16 tile autotile, the procedure is exactly the same as that explained above, only instead of using the 47 tile template you use the 16 tile template:

We now have some auto tiles in our auto tile library taken from a tile set. These can be used in the Room Editor by simply creating a tile map layer and then selecting one of the auto tiles from the library (which will select automatically the auto tile brush from the top of the Room Editor) and painting in your room. The tiles will now "auto\-magically" connect up to create properly sequenced tile maps.

Please note that the behaviour of an autotile around the room edges will depend on the **Open Or Closed Edges** button . By default, when an auto tile is placed along the edge of a room, it will choose a tile as if the outside of the room was empty (i.e.: it'll give the room an "edge"). However, if you click this button, the autotile will tile the room as if the area outside was filled with tiles and so choose tiles that blend and have no "edge".
