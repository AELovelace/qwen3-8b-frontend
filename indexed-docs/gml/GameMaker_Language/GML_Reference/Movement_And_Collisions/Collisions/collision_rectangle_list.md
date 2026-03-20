# collision\_rectangle\_list

This function checks a rectangular area for a collision with the given instance(s), instances of the given object and/or tile maps. It returns the number of results found and adds them to the given DS list.

This function is the same as the [collision\_rectangle()](collision_rectangle.md) function, only instead of just detecting one instance / tile map in collision at a time, it will detect multiple instances / tile maps. You supply the x/y positions of the top left and bottom right of the area to check along with the object / tile map to check for, and you can set the check to be precise (in which case all instances being checked will need to have *precise* collision masks) and whether the check should include the calling instance or not.

You supply a [DS list](../../Data_Structures/DS_Lists/DS_Lists.md) too, so the [id](../../Asset_Management/Instances/Instance_Variables/id.md) values of any instances (or tile maps) that are colliding with the calling instance will be added to the end of the given list. You can [clear](../../Data_Structures/DS_Lists/ds_list_clear.md) the list before calling this function so that it only contains results from this function call. You also have the option to order the instances based on their distances from the centre of the rectangular area to their origins. The function returns the number of instances / tile maps found, or 0 if none are found.

 
 

#### Syntax:

collision\_rectangle\_list(x1, y1, x2, y2, obj, prec, notme, list, ordered)

| Argument | Type | Description |
| --- | --- | --- |
| x1 | [Real](../../../GML_Overview/Data_Types.md) | The x coordinate of the left side of the rectangle to check. |
| y1 | [Real](../../../GML_Overview/Data_Types.md) | The y coordinate of the top side of the rectangle to check. |
| x2 | [Real](../../../GML_Overview/Data_Types.md) | The x coordinate of the right side of the rectangle to check. |
| y2 | [Real](../../../GML_Overview/Data_Types.md) | The y coordinate of the bottom side of the rectangle to check. |
| obj | [Object Asset](../../../../The_Asset_Editors/Objects.md) or [Object Instance](../../Asset_Management/Instances/Instance_Variables/id.md) or [Tile Map Element ID](../../Asset_Management/Rooms/Tile_Map_Layers/layer_tilemap_get_id.md) or [Array](../../../GML_Overview/Arrays.md) | An object, instance, tile map ID, keywords all/other, or array containing these items |
| prec | [Boolean](../../../GML_Overview/Data_Types.md) | Whether the check is based on precise collisions (true, which is slower) or its bounding box in general (false, faster). |
| notme | [Boolean](../../../GML_Overview/Data_Types.md) | Whether the calling instance, if relevant, should be excluded (true) or not (false). |
| list | [DS List](../../Data_Structures/DS_Lists/ds_list_create.md) | The DS list to use to store the IDs of colliding instances. |
| ordered | [Boolean](../../../GML_Overview/Data_Types.md) | Whether the list should be ordered by distance (true) or not (false). |

 

#### Returns:

[Real](../../../GML_Overview/Data_Types.md) (The number of instances / tile maps found to be in collision)

 

#### Example:

var \_list \= ds\_list\_create();  

 var \_num \= collision\_rectangle\_list(x \- 100, y \- 100, x \+ 100, y \+ 100, obj\_Enemy, false, true, \_list, false);  

 if (\_num \> 0\)  

 {  

     for (var i \= 0; i \< \_num; \+\+i)  

     {  

         instance\_destroy(\_list\[\| i]);  

     }  

 }  

 ds\_list\_destroy(\_list);

The code above will check a rectangular area 100 pixels around the calling instance position for collisions with instances of "obj\_Enemy". If there are any collisions, then the pre\-created list is looped through and each instance that was in the collision is destroyed.
