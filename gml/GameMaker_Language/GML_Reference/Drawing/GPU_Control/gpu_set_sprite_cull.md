# gpu\_set\_sprite\_cull

This function sets whether (frustum) culling of sprites and tile maps is enabled globally or not. It is enabled by default.

When enabled, sprites are checked against the view frustum on the CPU and *culled* (i.e. removed) if they're fully outside. Sprites that are culled are not submitted to the GPU (i.e. drawn).

  Sprite culling applies to all sprites that are drawn in your game, either manually using the draw\_sprite\_\* functions, as elements on asset layers or as part of sequences.

Tile maps are culled in a different way than sprites: only the tiles in the tile map that fall into a rectangle defined by the intersection of the room borders and the viewport rectangle are drawn.

 
To determine if a sprite is visible GameMaker calculates a sphere around the sprite and checks if this sphere is inside the view frustum. When the sphere is fully outside of it, the sprite must be, too, and is culled, i.e. not submitted for drawing.

  The sprite's scale factor and the [world matrix](../../Maths_And_Numbers/Matrix_Functions/matrix_set.md "matrix_set()") are taken into account when performing sprite culling.

 

#### Syntax:

gpu\_set\_sprite\_cull(enable)

| Argument | Type | Description |
| --- | --- | --- |
| enable | [Boolean](../../../GML_Overview/Data_Types.md) | Whether to enable sprite culling globally |

 

#### Returns:

N/A

 

#### Example:

Create Event

 gpu\_set\_sprite\_cull(true);

The above code enables sprite frustum culling in the Create event of an object.
