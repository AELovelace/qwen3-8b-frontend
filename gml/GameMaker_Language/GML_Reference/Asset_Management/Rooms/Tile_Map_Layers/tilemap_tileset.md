# tilemap\_tileset

Using this function you can change the tile set asset assigned to a given tile map element on a layer.

You give the tile map element ID (which you get when you create a tile map element using [layer\_tilemap\_create()](layer_tilemap_create.md) or when you use the function [layer\_tilemap\_get\_id()](layer_tilemap_get_id.md)), and then supply a tile set index and the tile map will be given the new sprite.

 

#### Syntax:

tilemap\_tileset(tilemap\_element\_id, tileset\_index)

| Argument | Type | Description |
| --- | --- | --- |
| tilemap\_element\_id | [Tile Map Element ID](layer_tilemap_get_id.md) | The unique ID value of the tile map element to change |
| tileset\_index | [Tile Set Asset](../../../../../The_Asset_Editors/Tile_Sets.md) | The new tile set index to use |

 

#### Returns:

N/A

 

#### Example:

var lay\_id \= layer\_get\_id("Tiles\_trees");  

 var tile\_id \= layer\_tilemap\_get\_id(lay\_id);  

 if (tilemap\_get\_tileset(tile\_id) !\= ts\_Nighttime)  

 {  

     tilemap\_tileset(tile\_id, ts\_Nighttime);  

 }

The above code checks the current tile set assigned to the tile map on the layer "Tiles\_trees" and if it is not "ts\_Nighttime" then that tile set is assigned to the tile map.
