# tileset\_get\_info

This function returns a [struct](../../../GML_Overview/Structs.md#struct) containing information on a tile set.

The returned struct contains the following variables: 

  This returns information for the texture page that is [generated for the Tile Set](tileset_get_texture.md) when the game is compiled, so some values (e.g. dimensions, the number of columns) may be different at runtime compared to the source sprite's [texture](../Sprites/Sprite_Information/sprite_get_texture.md) used for the Tile Set.

[Tile Set Info Struct](tileset_get_info.md)

| Variable Name | Data Type | Description |
| --- | --- | --- |
| width | [Real](../../../GML_Overview/Data_Types.md) | The width of the tile set texture area on its texture page (in pixels) |
| height | [Real](../../../GML_Overview/Data_Types.md) | The height of the tile set texture area on its texture page (in pixels) |
| texture | [Texture](../Sprites/Sprite_Information/sprite_get_texture.md) | The texture page for the tile set |
| tile\_width | [Real](../../../GML_Overview/Data_Types.md) | The width of a single tile (in pixels) |
| tile\_height | [Real](../../../GML_Overview/Data_Types.md) | The height of a single tile (in pixels) |
| tile\_horizontal\_separator | [Real](../../../GML_Overview/Data_Types.md) | The number of pixels horizontally on each side of each tile (making the space between two tiles 2 \* tile\_horizontal\_separator) |
| tile\_vertical\_separator | [Real](../../../GML_Overview/Data_Types.md) | The number of pixels vertically on each side of each tile (making the space between two tiles 2 \* tile\_vertical\_separator) |
| tile\_border\_x | [Real](../../../GML_Overview/Data_Types.md) | The number of pixels added left and right of every tile for the output border on the texture page |
| tile\_border\_y | [Real](../../../GML_Overview/Data_Types.md) | The number of pixels added above and below every tile for the output border on the texture page |
| tile\_columns | [Real](../../../GML_Overview/Data_Types.md) | The number of columns on each row of the tile set on the texture page |
| tile\_count | [Real](../../../GML_Overview/Data_Types.md) | The number of tiles |
| frame\_count | [Real](../../../GML_Overview/Data_Types.md) | The number of frames of animation per animation |
| frame\_length\_ms | [int64 (signed 64\-bit integer)](../../../GML_Overview/Data_Types.md) | The number of milliseconds for frame animation |
| frames | [Struct](../../../GML_Overview/Structs.md) | A struct containing all the animation frames. Each tile number has a key in the struct, each entry is an array of the frames to use (each array should be frame\_count long). |

 

#### Syntax:

tileset\_get\_info(index)

| Argument | Type | Description |
| --- | --- | --- |
| index | [Tile Set Asset](../../../../The_Asset_Editors/Tile_Sets.md) | The tile set to get the info from |

 

#### Returns:

[Tile Set Info Struct](tileset_get_info.md) (in case of a valid [Tile Set Asset](../../../../The_Asset_Editors/Tile_Sets.md)) or [undefined](../../../GML_Overview/Data_Types.md) (no valid tile set given)

 

#### Example 1: Showing the output

var \_info \= tileset\_get\_info(ts\_Forest);  

 show\_debug\_message(\_info);

The above code calls tileset\_get\_info to get information about an existing tile set ts\_Forest and stores the result in a temporary variable \_info. The info is then shown in a debug message.

 

#### Example 2: Finding the top\-left corner position of a tile

// tnumber is the number of the tile that you want to find  

 var \_tnumber \= 7;  

 var \_ts\_info \= tileset\_get\_info(ts\_Forest);  

 if (is\_undefined(\_ts\_info) \=\= false)  

 {  

     var \_twidth \= \_ts\_info.tile\_width \+ 2 \* \_ts\_info.tile\_horizontal\_separator;  

     var \_theight \= \_ts\_info.tile\_height \+ 2 \* \_ts\_info.tile\_vertical\_separator;  

     var \_tile\_x \= (\_tnumber mod \_ts\_info.tile\_columns) \* \_twidth;  

     var \_tile\_y \= (\_tnumber div \_ts\_info.tile\_columns) \* \_theight;  

     show\_debug\_message("The top\-left coordinates of tile index {0} are: ({1}, {2})", \_tnumber, \_tile\_x, \_tile\_y);  

 }  

 else  

 {  

     show\_debug\_message("No valid tile set was provided to the function");  

 }

The above code finds the coordinates of the top\-left corner of the given tile index. First the index of the tile is defined and stored in a temporary variable \_tnumber. Then tileset\_get\_info is called on an existing tile set ts\_Forest and the returned struct is stored in \_ts\_info. Next an if statement checks if the variable contains a valid struct (accessing the variables in the next steps will throw errors otherwise).  

 If it does, some variables are calculated. \_twidth and \_theight are the total width and height of a tile on the tile set, including the border on both sides (\_ts\_info.tile\_horizontal\_separator and \_ts\_info.tile\_vertical\_separator) \_tile\_x is the remainder of the tile index divided by the number of columns and \_tile\_y is the number of times \_ts\_info.tile\_columns fits into the tile index. After this, a debug message is shown with the top\-left coordinates (the separator offsets not yet included).  

 If the case an invalid tile set was provided to the function a different debug message is shown.
