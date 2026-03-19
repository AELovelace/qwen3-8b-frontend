# Set Tile Data In Cell

With this action you can set the tile data for a tile cell on a [tile map](#) layer. The tile data is simply a value that reflects the index of the tile along with the flip, mirror, and rotate values, as well as any custom tile masks that you have used. With this action you first supply the layer to target using the name of the layer (a string) as defined in the room editor, and then the column and row on the tile map layer to set the tile\-data for. The "cell" is the area on the tile map grid that holds the tile you want to set the data for, so if your tiles are 16x16, for example, and the room is 1024x768 the tile map will have 64 columns and 48 rows.

 
The final argument for the action is the tile\-data itself. You would normally retrieve the tile data for the tile map cell using the action [Get Tile Data In Cell](Get_Tile_Data_In_Cell.md) and then manipulate it using the action [Set Tile Data Transform](Set_Tile_Data_Transform.md) before setting it again with this action. For more information on tile data, please see the GML section on [Tile Map Functions](../../../GameMaker_Language/GML_Reference/Asset_Management/Rooms/Tile_Map_Layers/Tile_Map_Layers.md).

 

#### Action Syntax:

#### Arguments:

| Argument | Description |
| --- | --- |
| Layer | The layer with the tile map to target |
| Columns | The cell column position along the horizontal axis to set the tile\-data for |
| Row | The cell row position along the vertical axis to set the tile\-data |
| Data | The tile data to use for setting the cell |

 

#### Example:

The above action block code loops through every tile cell in the room, retrieves the tile data for the cell, mirrors it, then sets the cell again.
