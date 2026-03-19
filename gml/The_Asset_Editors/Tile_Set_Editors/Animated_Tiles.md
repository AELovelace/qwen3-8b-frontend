# Animated Tiles

Tiles are generally considered to be static cells within the game room, however with GameMaker it is possible to animate them, just as you would a sprite. Why not just use sprites, you ask? Well, sprites have a certain processing overhead due to them being associated with a bounding box and the way in which they are rendered, but tiles have a much lower processing overhead and so are faster to render. This does come at a price however, in that with tile set animations you are limited to creating animations that must be a power of two in length \- ie: of 2, 4, 8, 16, etc... frames \- and they must obviously be created within the tile grid, *and* they must all animate at the same speed (on a per\-tile set basis). However, even with these limitations, animated tiles are a powerful feature that can be used to add life and colour to otherwise static environments and backgrounds.

To create a tile animation you must first have a tile set that has the required tiles all within the one sprite image (but not as sprite frames, so a single large sprite frame with all the animation images within it), and then in the [Tile Set Editor](../Tile_Sets.md) you click on the **Tile Animation** button to bring up the Animation Editor:

The example image above is a single image with all animation frames contained within it, but it should be noted that the image could also contain other non\-animation tiles too, since you can use a single massive tile set and then "cherry pick" the parts of it that you want to create the animation from. For example, you could have a large landscape tile set with trees, earth and water, and within the tile set have multiple tiles to be animated to make the water ripple.

To create a tile animation you first have to add an animation to the animation library by clicking the **Add Animation** button , which will add an empty animation strip to the library and request that you select a number of frames to be used:

You will then be presented with a view of each empty animation frame, with the initial frame highlighted for you:

If you then go back to the tile set image on the left of the editor you can click  on any tile to add it into the animation and the frame will advance to the next one. Clicking on successive tiles will fill up the animation, which you can then preview by clicking on the "play" button beside the frames:

You can set the animation speed in the "**FPS**" field above the animation list. Setting it to 0 will not stop the animation, it will instead make it run as fast as possible.

Once you have done that your animation will become part of the animation library and when you enter the [Room Editor](../Rooms.md) you can select it and place it within the room. Note that if you select any of the tiles from an animation to place in a room, that tile will animate from the selected tile onwards, so you can "desynchronise" an animation by placing separate frames within the room and they will all animate. The only caveat to this is that the animation speed will always be the same, since it is defined for the whole tile set and not individual animations within the library.

A few things to note about tiles that are being used in animations:

- If the tile has its own animation specified (so there is an animation where it is set as the first tile) then it will use that animation.
- If the tile doesn't have its own animation but is used in only one other animation, then it will use that animation starting at the first position that tile is present in the animation.
- If the tile doesn't have its own animation and is used in multiple other animations, then it will not animate at all. You will need to explicitly specify an animation with it as the first tile.
