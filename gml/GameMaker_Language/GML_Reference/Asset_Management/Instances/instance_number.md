# instance\_number

With this function you can find out how many active instances of the specified object exists in the room. When checking using this function, if the object is a **parent**, then *all child objects will also be included in the return value*, and also note that those instances which have been deactivated with the [instance deactivate](Deactivating_Instances/Deactivating_Instances.md) functions will *not* be included in this check.

 

#### Syntax:

instance\_number(obj)

| Argument | Type | Description |
| --- | --- | --- |
| obj | [Object Asset](../../../../The_Asset_Editors/Objects.md) | The object to get the number of instances of, or the keyword all to count all instances |

 

#### Returns:

[Real](../../../GML_Overview/Data_Types.md)

 

#### Example:

if (instance\_number(object\_index) \< 50\)   

 {  

     instance\_create\_layer(random(room\_width), random(room\_height), "Instances", object\_index);  

 }

The above code will check the number of instances that are created form the same object as the current instance and then if there are less than 50, create another one at a random position within the room.
