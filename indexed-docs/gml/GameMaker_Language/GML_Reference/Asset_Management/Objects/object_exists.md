# object\_exists

This function returns whether the specified value is an object asset (true) or not (false). Note that this checks to see if an object is present in the Asset Browser, and not actually in the game room. For that you should use the function [instance\_exists()](../Instances/instance_exists.md).

 

#### Syntax:

object\_exists(obj)

| Argument | Type | Description |
| --- | --- | --- |
| obj | [Object Asset](../../../../The_Asset_Editors/Objects.md) | The index of the object to check. |

 

#### Returns:

[Boolean](../../../GML_Overview/Data_Types.md)

 

#### Example:

function destroy\_all\_instances(\_object)  

 {  

     if (!object\_exists(\_object)) return;  

       

     with (\_object)  

     {  

         instance\_create\_layer(x, y, layer, obj\_explosion);  

         instance\_destroy();  

     }  

 }

This function destroys all instances of the given object. It does a check first and in case an invalid object asset has been passed, it ends the function. Otherwise, it continues with execution and for each instance of the object, it creates an explosion instance in its location and destroys the instance.
