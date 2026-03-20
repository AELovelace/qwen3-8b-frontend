# collision\_point

This function checks a point for a collision with the given instance(s), instances of the given object and/or tile maps, and returns the first result found.

 

This check can be either precise or not, but for precise collisions to be enabled, the object or instance that you are checking for *must* also have precise collisions enabled for their sprite. If not, the default check is based on bounding boxes. The following image illustrates how this works:

Remember, for precise collisions to be considered *both* the object sprite and the collision function must have precise marked as on. It should also be noted that the return value of the function can be the id of *any one* of the instances considered to be in collision, so if three instance overlap at that point, any one of their ids could be the return value of the function.

 
 

#### Syntax:

collision\_point(x, y, obj, prec, notme)

| Argument | Type | Description |
| --- | --- | --- |
| x | [Real](../../../GML_Overview/Data_Types.md) | The x coordinate of the point to check. |
| y | [Real](../../../GML_Overview/Data_Types.md) | The y coordinate of the point to check. |
| obj | [Object Asset](../../../../The_Asset_Editors/Objects.md) or [Object Instance](../../Asset_Management/Instances/Instance_Variables/id.md) or [Tile Map Element ID](../../Asset_Management/Rooms/Tile_Map_Layers/layer_tilemap_get_id.md) or [Array](../../../GML_Overview/Arrays.md) | An object, instance, tile map ID, keywords all/other, or array containing these items |
| prec | [Boolean](../../../GML_Overview/Data_Types.md) | Whether the check is based on precise collisions (true, which is slower) or its bounding box in general (false, faster). |
| notme | [Boolean](../../../GML_Overview/Data_Types.md) | Whether the calling instance, if relevant, should be excluded (true) or not (false). |

 

#### Returns:

[Object Instance](../../Asset_Management/Instances/Instance_Variables/id.md) or [Tile Map Element ID](../../Asset_Management/Rooms/Tile_Map_Layers/layer_tilemap_get_id.md)

 

#### Example:

if (collision\_point(x, y, obj\_Cursor, false, true) !\= noone)  

 {  

     score \+\= 10;  

 }

Here we are checking the point at the position of the object that has the code for the object "obj\_Cursor". If there is one, then we add 10 onto the score variable.
