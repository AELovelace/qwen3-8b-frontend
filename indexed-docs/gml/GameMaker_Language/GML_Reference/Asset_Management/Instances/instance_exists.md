# instance\_exists

This function can be used in two ways depending on what you wish to check. You can give it an object index to check for, in which case this function will return true if any active instances of the specified object exist in the current room, or you can also supply it with an instance id, in which case this function will return true if that specific instance exists and is active in the current room.

  This function does *not* take into account those instances that have been deactivated using the [instance deactivate](Deactivating_Instances/Deactivating_Instances.md) functions.

 

#### Syntax:

instance\_exists(obj)

| Argument | Type | Description |
| --- | --- | --- |
| obj | [Object Instance](Instance_Variables/id.md) or [Object Asset](../../../../The_Asset_Editors/Objects.md) | The object or instance to check for the existence of |

 

#### Returns:

[Boolean](../../../GML_Overview/Data_Types.md)

 

#### Example:

if (!instance\_exists(obj\_enemy))  

 {  

     score \+\= 200;  

     room\_goto(rm\_hiscores);  

 }

The above code checks to see if any instances of an object obj\_enemy exist and if not it adds to the variable score and changes room.
