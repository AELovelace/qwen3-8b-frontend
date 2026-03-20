# collision\_line

This function checks along a line for a collision with the given instance(s), instances of the given object and/or tile maps, and returns the first result found.

 

This check can be either precise or not, but for precise collisions to be enabled, the object or instance that you are checking for *must* also have precise collisions enabled for their sprite. If not, the default check is based on bounding boxes. The following image illustrates how this works:

Remember, for precise collisions to be considered *both* the object sprite and the collision function must have precise marked as on. It should also be noted that the return value of the function can be the id of *any one* of the instances considered to be in collision along the line, so if three instances overlap the defined line, any one of their ids could be the return value of the function.

 
 

#### Syntax:

collision\_line(x1, y1, x2, y2, obj, prec, notme)

| Argument | Type | Description |
| --- | --- | --- |
| x1 | [Real](../../../GML_Overview/Data_Types.md) | The x coordinate of the start of the line. |
| y1 | [Real](../../../GML_Overview/Data_Types.md) | The y coordinate of the start of the line. |
| x2 | [Real](../../../GML_Overview/Data_Types.md) | The x coordinate of the end of the line. |
| y2 | [Real](../../../GML_Overview/Data_Types.md) | The y coordinate of the end of the line. |
| obj | [Object Asset](../../../../The_Asset_Editors/Objects.md) or [Object Instance](../../Asset_Management/Instances/Instance_Variables/id.md) or [Tile Map Element ID](../../Asset_Management/Rooms/Tile_Map_Layers/layer_tilemap_get_id.md) or [Array](../../../GML_Overview/Arrays.md) | An object, instance, tile map ID, keywords all/other, or array containing these items |
| prec | [Boolean](../../../GML_Overview/Data_Types.md) | Whether the check is based on precise collisions (true, which is slower) or its bounding box in general (false, faster). |
| notme | [Boolean](../../../GML_Overview/Data_Types.md) | Whether the calling instance, if relevant, should be excluded (true) or not (false). |

 

#### Returns:

[Object Instance](../../Asset_Management/Instances/Instance_Variables/id.md) or [Tile Map Element ID](../../Asset_Management/Rooms/Tile_Map_Layers/layer_tilemap_get_id.md)

 

#### Example:

with (obj\_Enemy)  

 {  

     if (collision\_line(100, 400, 100, 600, id, false, false) !\= noone) instance\_destroy();  

 }

This code gets all instances of "obj\_Enemy" to check along a line from 100x, 400y to 100x, 600y for a collision with themselves, and if there is one then they are destroyed.
