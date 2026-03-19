# collision\_circle

This function checks a circular zone around a point for a collision with the given instance(s), instances of the given object and/or tile maps, and returns the first result found.

This check can be either precise or not, but for precise collisions to be enabled, the object or instance that you are checking for *must* also have precise collisions enabled for their sprite. If not, the default check is based on bounding boxes. The following image illustrates how this works:

Here, the instance in the middle is using a collision circle to check for ball objects. Now, the blue ones do *not* have a precise bounding box and as you can see, even if the sprite is not actually touching the circle, the collision can still happen (even if you set the precise option in the function to true) as the bounding box of that sprite overlaps the circular area defined by collision\_circle. On the other hand, the green balls will only be considered in collision if the actual sprite overlaps with the defined circle. Remember, for precise collisions to be considered *both* the object sprite and the collision function must have precise marked as on.

 

 
 

#### Syntax:

collision\_circle(x1, y1, rad, obj, prec, notme)

 

| Argument | Type | Description |
| --- | --- | --- |
| x1 | [Real](../../../GML_Overview/Data_Types.md) | The x coordinate of the center of the circle to check. |
| y1 | [Real](../../../GML_Overview/Data_Types.md) | The y coordinate of the center of the circle to check. |
| rad | [Real](../../../GML_Overview/Data_Types.md) | The radius (distance in pixels from its center to its edge). |
| obj | [Object Asset](../../../../The_Asset_Editors/Objects.md) or [Object Instance](../../Asset_Management/Instances/Instance_Variables/id.md) or [Tile Map Element ID](../../Asset_Management/Rooms/Tile_Map_Layers/layer_tilemap_get_id.md) or [Array](../../../GML_Overview/Arrays.md) | An object, instance, tile map ID, keywords all/other, or array containing these items |
| prec | [Boolean](../../../GML_Overview/Data_Types.md) | Whether the check is based on pixel\-perfect collisions (true \= slow) or its bounding box in general (false \= fast). |
| notme | [Boolean](../../../GML_Overview/Data_Types.md) | Whether the calling instance, if relevant, should be excluded (true) or not (false). |

 

#### Returns:

[Object Instance](../../Asset_Management/Instances/Instance_Variables/id.md) or [Tile Map Element ID](../../Asset_Management/Rooms/Tile_Map_Layers/layer_tilemap_get_id.md)

 

#### Example:

if (collision\_circle(x, y, 20, obj\_Cursor, false, true) !\= noone)  

 {  

     image\_index \= 1;  

 }  

 else image\_index \= 0;

The code above will check a circular are with a 20pixel radius for a collision with "obj\_Cursor" and if there is one it will set the image\_index of the object running the code to 1, but if there is not it will set the image\_index of the object to 0\.
