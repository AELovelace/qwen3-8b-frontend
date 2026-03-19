# layer\_tilemap\_get\_colmask

This function gets the sprite used as the collision mask for the given tile map element.

The collision mask can be set with [layer\_tilemap\_set\_colmask](layer_tilemap_set_colmask.md).

 

#### Syntax:

layer\_tilemap\_get\_colmask(tilemap\_element\_id)

| Argument | Type | Description |
| --- | --- | --- |
| tilemap\_element\_id | [Tile Map Element ID](layer_tilemap_get_id.md) | The tile map element |

 

#### Returns:

[Sprite Asset](../../../../../The_Asset_Editors/Sprites.md)

 

#### Example:

var \_id \= layer\_tilemap\_get\_id("Solid");  

 var \_mask \= layer\_tilemap\_get\_colmask(\_id);

This code gets the ID of the tile map element on a layer and then gets the collision mask sprite of this tile map using layer\_tilemap\_get\_colmask.
