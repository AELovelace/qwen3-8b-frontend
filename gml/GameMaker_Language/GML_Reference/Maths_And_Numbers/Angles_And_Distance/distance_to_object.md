# distance\_to\_object

This function calculates the distance from the edge of the bounding box of the calling instance to the nearest edge of the nearest instance of the object specified.

The object can be an object index or a specific instance ID as well as the [*keyword*](../../../GML_Overview/Instance_Keywords.md) [other](../../../GML_Overview/Instance Keywords/other.md), and the distance is returned in pixels.

  If either of the objects have no sprite or no mask defined, the results will be incorrect.

 

#### **Syntax:**

distance\_to\_object(obj)

| Argument | Type | Description |
| --- | --- | --- |
| obj | [Object Asset](../../../../The_Asset_Editors/Objects.md) or [Object Instance](../../Asset_Management/Instances/Instance_Variables/id.md) | The object to check for |

 

#### Returns:

[Real](../../../GML_Overview/Data_Types.md)

 

#### Example:

if (distance\_to\_object(obj\_player) \< range)  

 {  

     can\_shoot \= true;  

 }

The above code will check for the distance to the player object and if it is less than the value stored in the variable range the variable can\_shoot is set to true.
