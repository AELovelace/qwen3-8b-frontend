# Set Tile Index At Pixel

 

With this action you can set a tile on a given layer to a new index. The layer is specified from the layer name given (a string, as used to name the layer in the Room Editor), and then you give an x and y position to get the tile to set. The x and
 y position can be flagged as being relative to the position of the calling instance, and the tile being set will be the one that the given position falls within in the room and the tile set used will be the one assigned to the layer in the room
 editor. Finally you supply the tile index to set the tile to (tiles are indexed from left to right from top to bottom, with 0 at the top left). Note you can always set the tile index to 0 to clear the tile.

 

#### Action Syntax:

#### Arguments:

| Argument | Description |
| --- | --- |
| Layer | The layer to set the tile on |
| x | The x position to check |
| y | The y position to check |
| Tile | The new index of the tile to use |

 

#### Example:

The above action block code checks for a mouse left button press and
 if one is detected it gets the index of the tile cell that the position of the mouse falls within. This tile index is then checked and if it is not 0, it is set to 0\.
