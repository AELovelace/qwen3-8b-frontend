# bbox\_bottom

This **read only** variable returns the y position (within the room) of the bottom of the bounding box for the instance, where the bounding box is defined by the maximum width and height of the mask for the instance (as set by the [sprite\_index](sprite_index.md) or by the [mask\_index](mask_index.md)). Even when a sprite has a precise collision mask, the bounding box exists and is used for certain things, and so you can use this variable to find it. Please note that when the instance has no sprite assigned the value returned will be the same as the instance Y position.

See: [Bounding Boxes](../../../Movement_And_Collisions/Collisions/Collisions.md#h)

 

#### Syntax:

bbox\_bottom

 

#### Returns:

[Real](../../../../GML_Overview/Data_Types.md) (integer)

 

#### Example:

if (bbox\_bottom \> room\_height)  

 {  

     y \= room\_height \- sprite\_yoffset;  

 }

The above code checks to see if the bounding box of the instance is outside the room and if it is it sets the instance to a new position.
