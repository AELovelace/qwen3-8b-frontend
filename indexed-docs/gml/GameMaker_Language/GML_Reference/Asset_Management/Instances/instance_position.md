# instance\_position

With this function you can check a position for a collision with another instance or all instances of an object.

 
When you use this, you are checking a single point in the room for instances or tile maps. This check will be done against the bounding box of the instance or against the mask of the instance if that instance has precise collisions checked.

This function will return the ID of the instance or tile map that is first found in collision. If nothing is found, noone is returned.

If you do not need the id of the colliding instance you should consider using [position\_meeting()](../../Movement_And_Collisions/Collisions/position_meeting.md) instead.

See: [Collisions](../../Movement_And_Collisions/Collisions/Collisions.md)

 

#### Syntax:

instance\_position(x, y, obj)

| Argument | Type | Description |
| --- | --- | --- |
| x | [Real](../../../GML_Overview/Data_Types.md) | The x position to check for instances. |
| y | [Real](../../../GML_Overview/Data_Types.md) | The y position to check for instances. |
| obj | [Object Asset](../../../../The_Asset_Editors/Objects.md) or [Object Instance](Instance_Variables/id.md) or [Tile Map Element ID](../Rooms/Tile_Map_Layers/layer_tilemap_get_id.md) or [Array](../../../GML_Overview/Arrays.md) | An object, instance, tile map ID, keywords all/other, or array containing these items |

 

#### Returns:

[Object Instance](Instance_Variables/id.md) or [Tile Map Element ID](../Rooms/Tile_Map_Layers/layer_tilemap_get_id.md)

 

#### Example:

var inst;  

 inst \= instance\_position(mouse\_x, mouse\_y, obj\_Pause\_Button);  

 if (inst !\= noone)  

 {  

     with (inst)  

     {  

         image\_index \= 1;  

     }  

     instance\_create\_layer(room\_width / 2, 0, "Controllers", obj\_Menu);  

 }

The above code will check for a collision with an instance of "obj\_Pause\_Button" at the mouse position, and if there is one it will then use the returned id to set its image\_index to a new value before creating a new instance of the object "obj\_Menu".
