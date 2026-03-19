# Set Tile Set

With this action you can set a layer to use different [tile sets](#) from those created in the Asset Browser. You give the name of the layer (a string, as defined in the Room Editor), and then
 the tile set resource to use, and all tiles in the room on that layer will be drawn with the new tile set.

 

#### Action Syntax:

#### Arguments:

| Argument | Description |
| --- | --- |
| Layer | The layer on which to set the new tile set. |
| Tileset | The tile set to use for the layer. |

 

#### Example:

The above action block code checks to see if the tiles on the layer "Floor\_Tiles" is using
 the tile set "tl\_PalaceRuins", and if they not, then they are set to use it.
