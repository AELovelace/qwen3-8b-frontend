# position\_meeting

With this function you can check a position for a collision with another instance or all instances of an object. When you use this you are checking a single point in the room for an instance or an object. This check will be done against the bounding box of the instance or against the mask of the instance if that instance has precise collisions checked. If you need to get the unique [id](../../Asset_Management/Instances/Instance_Variables/id.md) of the instance being collided with you should use [instance\_position](../../Asset_Management/Instances/instance_position.md).

 
 

#### Syntax:

position\_meeting(x, y, obj)

| Argument | Type | Description |
| --- | --- | --- |
| x | [Real](../../../GML_Overview/Data_Types.md) | The x position to check |
| y | [Real](../../../GML_Overview/Data_Types.md) | The y position to check |
| obj | [Object Asset](../../../../The_Asset_Editors/Objects.md) or [Object Instance](../../Asset_Management/Instances/Instance_Variables/id.md) or [Tile Map Element ID](../../Asset_Management/Rooms/Tile_Map_Layers/layer_tilemap_get_id.md) or [Array](../../../GML_Overview/Arrays.md) | An object, instance, tile map ID, keywords all/other, or array containing these items |

 

#### Returns:

[Boolean](../../../GML_Overview/Data_Types.md)

 

#### Example:

if (mouse\_check\_button(mb\_left))  

 {  

     if (!position\_meeting(mouse\_x, mouse\_y, all))  

     {  

         instance\_create\_layer(mouse\_x, mouse\_y, "Walls", obj\_wall);  

     }  

 }

The above code checks for the left mouse button, and if it is pressed it checks the mouse (x, y) position for a collision with any instance. If there is none, then an instance of obj\_wall is created.
