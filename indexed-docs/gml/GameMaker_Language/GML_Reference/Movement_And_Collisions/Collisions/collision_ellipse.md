# collision\_ellipse

This function checks an elliptical zone around a point for a collision with the given instance(s), instances of the given object and/or tile maps, and returns the first result found.

This collision can be checked as precise or not, and you may also choose to check for the instance running the code itself or not. Consider this image:

Here, the instance in the middle is using a collision ellipse to check for ball objects. Now, the blue ones do *not* have a precise bounding box and as you can see, even if the sprite is not actually touching the ellipse, the collision can still happen (even if you set the precise option in the function to true) as the bounding box of that sprite overlaps the elliptical area defined by collision\_circle. On the other hand, the green balls will only be considered in collision if the actual sprite overlaps the defined ellipse. Remember, for precise collisions to be considered *both* the object sprite and the collision function must have precise marked as on.

 

 
 

#### Syntax:

collision\_ellipse(x1, y1, x2, y2, obj, prec, notme)

| Argument | Type | Description |
| --- | --- | --- |
| x1 | [Real](../../../GML_Overview/Data_Types.md) | The x coordinate of the left side of the ellipse to check. |
| y1 | [Real](../../../GML_Overview/Data_Types.md) | The y coordinate of the top side of the ellipse to check. |
| x2 | [Real](../../../GML_Overview/Data_Types.md) | The x coordinate of the right side of the ellipse to check. |
| y2 | [Real](../../../GML_Overview/Data_Types.md) | The y coordinate of the bottom side of the ellipse to check. |
| obj | [Object Asset](../../../../The_Asset_Editors/Objects.md) or [Object Instance](../../Asset_Management/Instances/Instance_Variables/id.md) or [Tile Map Element ID](../../Asset_Management/Rooms/Tile_Map_Layers/layer_tilemap_get_id.md) or [Array](../../../GML_Overview/Arrays.md) | An object, instance, tile map ID, keywords all/other, or array containing these items |
| prec | [Boolean](../../../GML_Overview/Data_Types.md) | Whether the check is based on precise collisions (true, which is slower) or its bounding box in general (false, faster). |
| notme | [Boolean](../../../GML_Overview/Data_Types.md) | Whether the calling instance, if relevant, should be excluded (true) or not (false). |

 

#### Returns:

[Object Instance](../../Asset_Management/Instances/Instance_Variables/id.md) or [Tile Map Element ID](../../Asset_Management/Rooms/Tile_Map_Layers/layer_tilemap_get_id.md)

 

#### Example:

if (collision\_ellipse(50, 50, 200, 100, obj\_Player, false, true) !\= noone)  

 {  

     instance\_create\_layer(obj\_Player.x, obj\_Player.y, "Effects", obj\_Splash);  

 }

This will check an elliptical zone within the bounds of 50x, 50y and 200x, 100y for the object "obj\_Player". If there is a collision with that object, then it will create an instance of "obj\_Splash" at the x/y coordinates of obj\_Player.
