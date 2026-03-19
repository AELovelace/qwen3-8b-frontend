# tilemap\_set\_width

This function can be used to resize a tile map element.

You give the tile map element ID (which you get when you create a tile map element using [layer\_tilemap\_create()](layer_tilemap_create.md) or when you use the function [layer\_tilemap\_get\_id()](layer_tilemap_get_id.md)), and the new width of the tile map in tile cells.

 

#### Syntax:

tilemap\_set\_width(tilemap\_element\_id, width)

| Argument | Type | Description |
| --- | --- | --- |
| tilemap\_element\_id | [Tile Map Element ID](layer_tilemap_get_id.md) | The unique ID value of the tile map element to set the width of |
| width | [Real](../../../../GML_Overview/Data_Types.md) | The width value (in "cells") |

 

#### Returns:

N/A

 

#### Example:

var lay\_id \= layer\_get\_id("Tiles\_Walls");  

 var map\_id \= layer\_tilemap\_get\_id(lay\_id);  

 if (tilemap\_get\_width(map\_id) !\= room\_width div 16\)  

 {  

     tilemap\_set\_width(map\_id, room\_width div 16\);  

 }

The above code checks the width of a specific tile map and if it is not the correct size then the width is set.
