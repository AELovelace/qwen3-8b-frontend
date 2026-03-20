# Get Tile Data Transform

With this action you can find out if the tile data for a tile has been transformed in one of three ways: flipped, mirrored or rotated. The tile data is simply a value that reflects the index of the tile along with the transforms applied, and you will normally want to get the tile data first using either [Get Tile Data In Cell](Get_Tile_Data_In_Cell.md) or [Get Tile Data At Pixel](Get_Tile_Data_At_Pixel.md) before using this action. The action will return true if the chosen transform has been applied to the tile\-data, or false otherwise, and the returned value will then be stored in the target variable which can have been created previously or can be a new temporary one (if you check the "Temp" check\-box). For more information on tile data, please see the GML section on [Tile Map Functions](../../../GameMaker_Language/GML_Reference/Asset_Management/Rooms/Tile_Map_Layers/Tile_Map_Layers.md).

 

#### Action Syntax:

#### Arguments:

| Argument | Description |
| --- | --- |
| Tile | The tile\-data for the tile to get the transform from |
| Transform | The transform to check |

 

#### Example:

 

The above action block code gets the tile data at the mouse position and then checks to see if the tile has had a rotation transform applied to it. If it has then the transform is reset and the tile data sets the tile at the position again.
