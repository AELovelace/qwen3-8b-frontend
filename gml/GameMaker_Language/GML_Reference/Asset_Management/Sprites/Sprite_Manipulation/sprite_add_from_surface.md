# sprite\_add\_from\_surface

This function works in exactly the same way as [sprite\_create\_from\_surface()](sprite_create_from_surface.md) only instead of creating a new sprite from the area of the indexed surface that you select, it adds the defined area of the surface as a new sub\-image to a previously created sprite (this means that you cannot add it directly to a sprite from the resource tree, but rather only to one previously created from a surface, or one that has been duplicated from a resource sprite using [sprite\_duplicate()](sprite_duplicate.md)).

It should be noted that the memory used when adding a sprite in this way will be larger than you may expect. This is because GameMaker will store the sprite as a texture page *and* it will also be stored in GPU memory, so the total memory will be larger than would be expected for an image file of the same sprite.

 
 

#### Syntax:

sprite\_add\_from\_surface(index, surface, x, y, w, h, removeback, smooth)

| Argument | Type | Description |
| --- | --- | --- |
| index | [Sprite Asset](../../../../../The_Asset_Editors/Sprites.md) | The index of the sprite to add the new image to. |
| surface | [Surface](../../../Drawing/Surfaces/surface_create.md) | The index of the surface from which we get the image. |
| x | [Real](../../../../GML_Overview/Data_Types.md) | The x position to copy from. |
| y | [Real](../../../../GML_Overview/Data_Types.md) | The y position to copy from. |
| w | [Real](../../../../GML_Overview/Data_Types.md) | The width of the area to be copied (from the x position). |
| h | [Real](../../../../GML_Overview/Data_Types.md) | The height of the area to be copied (from the y position). |
| removeback | [Boolean](../../../../GML_Overview/Data_Types.md) | Indicates whether to make all pixels with the background colour (left\-bottom pixel) transparent. |
| smooth | [Boolean](../../../../GML_Overview/Data_Types.md) | Indicates whether to smooth the edges. |

 

#### Returns:

N/A

 

#### Example:

spr\_custom \= sprite\_create\_from\_surface(surf, 0, 0, 32, 32, true, true, 16, 16\);  

 var i;  

 for (i \= 1; i \< 8; i \+\= 1\)  

 {  

     sprite\_add\_from\_surface(spr\_custom, surf, i, 0, 32, 32, false, false);  

 }

The above code creates a sprite from the surface indexed in the variable "surf", assigning its index to the variable "spr\_Custom", and then uses a for loop to move across the surface and capture various sections which are added into the sprite as sub\-images.
