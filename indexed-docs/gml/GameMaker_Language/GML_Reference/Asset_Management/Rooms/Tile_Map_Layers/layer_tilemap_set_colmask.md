# layer\_tilemap\_set\_colmask

This function sets the sprite to be used as the collision mask for the given tile map element.

### Usage Notes

- The dimensions of the mask sprite must match the dimensions of the sprite being used for the tile set.
- The sprite should have precise collisions enabled in [The Sprite Editor](../../../../../The_Asset_Editors/Sprites.md).
- The collision mask sprite can be set per tile map, i.e. the same tile on a tile set can have a different collision mask on different tile maps.

 

#### Syntax:

layer\_tilemap\_set\_colmask(tilemap\_element\_id, sprite)

| Argument | Type | Description |
| --- | --- | --- |
| tilemap\_element\_id | [Tile Map Element ID](layer_tilemap_get_id.md) | The tile map element |
| sprite | [Sprite Asset](../../../../../The_Asset_Editors/Sprites.md) | The sprite to use as the collision mask for the tile map |

 

#### Returns:

N/A

 

#### Example:

var \_id \= layer\_tilemap\_get\_id("Solid");  

 layer\_tilemap\_set\_colmask(\_id, spr\_solid);

The code above gets the ID of the tile map element on a layer and then sets the sprite to be used as the collision mask for this tile map.
