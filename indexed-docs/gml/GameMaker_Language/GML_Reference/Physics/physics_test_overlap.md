# physics\_test\_overlap

This function can be used to check if the physical body of the calling instance (i.e. any of its bound fixtures) overlaps, or *will* overlap, when rotated and placed at a given position in the room.

The angle argument is the angle of rotation that the calling instance has (or will have) at the position to be checked, and the obj argument can be either a single instance ID, an object index or one of the keywords [all](../../GML_Overview/Instance Keywords/all.md) or [other](../../GML_Overview/Instance Keywords/other.md).

 

#### Syntax:

physics\_test\_overlap(xpos, ypos, angle, obj)

| Argument | Type | Description |
| --- | --- | --- |
| xpos | [Real](../../GML_Overview/Data_Types.md) | The x position in the room to check |
| ypos | [Real](../../GML_Overview/Data_Types.md) | The y position in the room to check |
| angle | [Real](../../GML_Overview/Data_Types.md) | The angle to check (of the calling instance) |
| obj | [Object Asset](../../../The_Asset_Editors/Objects.md) or [Object Instance](../Asset_Management/Instances/Instance_Variables/id.md) | The object index or instance ID to check for, or one of the keywords [all](../../GML_Overview/Instance Keywords/all.md) or [other](../../GML_Overview/Instance Keywords/other.md) |

 

#### Returns:

[Boolean](../../GML_Overview/Data_Types.md)

 

#### Example:

if physics\_test\_overlap(x\+20, y\-35, 0, obj\_bomb)  

 {  

     alarm\[0] \= game\_get\_speed(gamespeed\_fps);  

     ignited \= true;  

 }

The above code will check a position for a physics fixture overlap, and if there is one, it sets a variable and an alarm.
