# place\_meeting

With this function you can check a position for a collision with another instance, or all instances of an object, using the collision mask of the instance that runs the code.

When you use this you are effectively asking GameMaker to move the instance to the new position, check for a collision, move back and tell you if a collision was found or not.

This will work for precise collisions, but only if both the instance and the object being checked for have precise collision masks selected. Otherwise, only bounding box collisions are applied.

 
If you need to get the **id** handle of the instance being collided with, you should use [instance\_place()](../../Asset_Management/Instances/instance_place.md).

See: [Collisions](Collisions.md)

 

#### Syntax:

place\_meeting(x, y, obj)

| Argument | Type | Description |
| --- | --- | --- |
| x | [Real](../../../GML_Overview/Data_Types.md) | The x position to check. |
| y | [Real](../../../GML_Overview/Data_Types.md) | The y position to check. |
| obj | [Object Asset](../../../../The_Asset_Editors/Objects.md) or [Object Instance](../../Asset_Management/Instances/Instance_Variables/id.md) or [Tile Map Element ID](../../Asset_Management/Rooms/Tile_Map_Layers/layer_tilemap_get_id.md) or [Array](../../../GML_Overview/Arrays.md) | An object, instance, tile map ID, keywords all/other, or array containing these items |

 

#### Returns:

[Boolean](../../../GML_Overview/Data_Types.md)

 

#### Example 1:

if (keyboard\_check(vk\_left))  

 {  

     if (!place\_meeting(x \- 5, y, obj\_wall))  

     {  

         x \-\= 5;  

     }  

 }

The above code checks to see if there is *not* a collision to the left of the instance and moves the instance if there is none.

#### Example 2:

var \_tilemap \= layer\_tilemap\_get\_id("Tiles\_1");  

  

 if (keyboard\_check(vk\_left))  

 {  

     if !place\_meeting(x \- 5, y, \[obj\_wall, obj\_bush, \_tilemap])  

     {  

         x \-\= 5;  

     }  

 }
 

This is the same logic as the last example, however it uses an array to check for collisions against two types of objects (obj\_wall, obj\_bush) and the Tile Map for a Tile Layer called "Tiles\_1".

As you only need to get your tile map ID once, you can move the first line to the Create event.
