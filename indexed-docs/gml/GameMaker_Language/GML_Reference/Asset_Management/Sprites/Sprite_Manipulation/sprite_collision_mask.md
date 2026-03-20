# sprite\_collision\_mask

With this function you can set the properties of the collision mask that a sprite should have. For information on sprite masks, see: [Collision Mask](../../../../../The_Asset_Editors/Sprites.md#p)

You can supply one of the following bbox modes for the bboxmode argument:

 
If you select either automatic or full image as the bounding box mode, then the individual bounding box values can be set to 0\. However for a user defined mask, you will have to set these values. The different bounding box values are always relative to the top left corner of the sprite (irrespective of the x and y origin) which is considered position (0, 0\).

Setting the kind of mask sets the general shape for the mask itself, but note that anything other than a rectangular mask will require more processing power when resolving collisions, with a subsequent drop in performance. In general, you should only use mask types other than rectangular when absolutely necessary.

  This function does not permit the **rotated rectangle** collision mask kind.

  Spine sprites can only use the bboxmode\_fullimage and bboxmode\_manual modes, using bboxkind\_rectangular on either mode, or bboxkind\_spine only in full image mode.

The kind of mask that can be set will be one of the following constants, passed into the kind argument:

| [Bounding Box Kind (Shape) Constant](sprite_collision_mask.md) | |
| --- | --- |
| Constant | Description |
| bboxkind\_rectangular | A rectangular (non\-rotating) rectangle collision mask shape, usable for Spine sprites |
| bboxkind\_ellipse | An elliptical collision mask shape |
| bboxkind\_diamond | A diamond collision mask shape |
| bboxkind\_precise | A precise collision mask, where the mask will conform to the non\-transparent pixels of the sprite, based on the tolerance value given (see below)) |
| bboxkind\_spine | Apart from rectangle, this is the only valid option for Spine sprites. It enables more precise collision checking against the mesh in the sprite. |

  

 Finally, tolerance is used to define how precise the mask is (when used with a "full image" mask, this will have no effect), with a tolerance of 0 meaning that the mask will follow every single pixel that has a transparency over 0, while other values will shift the collision mask perimeter depending on the transparency of the pixels.

  This function will only work on added sprites or duplicated sprites and **not** directly on pre\-made assets. You can duplicate sprites using the function [sprite\_duplicate()](sprite_duplicate.md).

 

#### Syntax:

sprite\_collision\_mask(ind, sepmasks, bboxmode, bbleft, bbtop, bbright, bbbottom, kind, tolerance)

| Argument | Type | Description |
| --- | --- | --- |
| ind | [Sprite Asset](../../../../../The_Asset_Editors/Sprites.md) | The index of the sprite to set the bounding box of. |
| sepmasks | [Boolean](../../../../GML_Overview/Data_Types.md) | Whether to create collision masks for each sub\-image of the sprite (true), or one mask for all (false). |
| bboxmode | [Real](../../../../GML_Overview/Data_Types.md) | What kind of bounding box to use. |
| bbleft | [Real](../../../../GML_Overview/Data_Types.md) | The maximum left position of the bounding box. |
| bbtop | [Real](../../../../GML_Overview/Data_Types.md) | The maximum top position of the bounding box. |
| bbright | [Real](../../../../GML_Overview/Data_Types.md) | The maximum right position of the bounding box. |
| bbbottom | [Real](../../../../GML_Overview/Data_Types.md) | The maximum bottom position of the bounding box. |
| kind | [Bounding Box Kind (Shape) Constant](sprite_collision_mask.md) | The kind of mask, a constant (see the table in the description). |
| tolerance | [Real](../../../../GML_Overview/Data_Types.md) | Indicates the tolerance in the transparency value (0\=no tolerance, 255\=full tolerance). |

 

#### Returns

N/A

 

#### Example:

sprite \= sprite\_add("sprite\_5\.png", 5, false, false, 0, 0\);  

 sprite\_collision\_mask(sprite, true, bboxmode\_fullimage, 0, 0, 0, 0, bboxkind\_precise, 0\);

The above code loads a sprite from an external source and stores the new index in the variable "sprite". The code then sets the new sprite to have a precise collision mask for each of its sub\-images.
