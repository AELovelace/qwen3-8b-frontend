# collision\_rectangle

This function checks a rectangular area for a collision with the given instance(s), instances of the given object and/or tile maps, and returns the first result found.

This collision can be checked as precise or not, and you may also choose to check for the instance running the code itself or not. Consider this image:

Here, the instance in the middle is using a collision rectangle to check for ball objects. Now, the blue ones do *not* have a precise bounding box and as you can see, even if the sprite is not actually touching the rectangle, the collision will still happen (even if you set the precise option in the function to true) as the bounding box of that sprite overlaps the collision\_rectangle. On the other hand, the green balls will only be considered in collision if the actual sprite overlaps the rectangle. Remember, for precise collisions to be considered *both* the object sprite and the collision function must have precise marked as on.

 

 
 

#### Syntax:

collision\_rectangle(x1, y1, x2, y2, obj, prec, notme)

| Argument | Type | Description |
| --- | --- | --- |
| x1 | [Real](../../../GML_Overview/Data_Types.md) | The x coordinate of the left side of the rectangle to check. |
| y1 | [Real](../../../GML_Overview/Data_Types.md) | The y coordinate of the top side of the rectangle to check. |
| x2 | [Real](../../../GML_Overview/Data_Types.md) | The x coordinate of the right side of the rectangle to check. |
| y2 | [Real](../../../GML_Overview/Data_Types.md) | The y coordinate of the bottom side of the rectangle to check. |
| obj | [Object Asset](../../../../The_Asset_Editors/Objects.md) or [Object Instance](../../Asset_Management/Instances/Instance_Variables/id.md) or [Tile Map Element ID](../../Asset_Management/Rooms/Tile_Map_Layers/layer_tilemap_get_id.md) or [Array](../../../GML_Overview/Arrays.md) | An object, instance, tile map ID, keywords all/other, or array containing these items |
| prec | [Boolean](../../../GML_Overview/Data_Types.md) | Whether the check is based on precise collisions (true, which is slower) or its bounding box in general (false, faster). |
| notme | [Boolean](../../../GML_Overview/Data_Types.md) | Whether the calling instance, if relevant, should be excluded (true) or not (false). |

 

#### Returns:

[Object Instance](../../Asset_Management/Instances/Instance_Variables/id.md) or [Tile Map Element ID](../../Asset_Management/Rooms/Tile_Map_Layers/layer_tilemap_get_id.md)

 

#### Example:

var inst;  

 inst \= collision\_rectangle(50, 50, 200, 100, obj\_Ball, false, true);  

 if (inst !\= noone)  

 {  

     instance\_destroy(inst);  

 }

This short code uses collision\_rectangle check an area in the room from 50x, 50y (top left of the rectangle) to 200x, 200y (bottom right of the rectangle) for an instance of an object called "obj\_ball". It stores the return value in a temporary variable which is then checked to see if that value is an instance id, or the keyword [**noone**](../../../GML_Overview/Instance_Keywords.md). If it is *not* **noone** then it uses the stored instance id to destroy the object.
