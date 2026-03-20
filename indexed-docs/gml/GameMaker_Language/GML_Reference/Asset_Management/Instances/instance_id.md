# instance\_id

This **read\-only variable acts as an** [array](../../../GML_Overview/Arrays.md) that holds the [ids](Instance_Variables/id.md) of all *active* instances within the room. This means that if you have used any of the [Instance Deactivate](Deactivating_Instances/Deactivating_Instances.md) functions those instances that have been deactivated will not be included in this array.

  This variable does not hold a real GML array, so you cannot run any [array functions](I:/GameMaker-Manual/Manual/contents/GameMaker_Language/GML_Reference/Variable_Functions/Array_Functions.md) on it or serialise it (convert it to a string). The only operation you can run on it is accessing a value at an index, with the instance\_id\[index] syntax. If you return the value of the variable itself, it will return an invalid handle with a value of [noone](../../../GML_Overview/Instance Keywords/noone.md) (\-4\).

As you cannot run [array\_length](../../Variable_Functions/array_length.md) on this function, use [instance\_number](instance_number.md)(all) to get the number of instances in the room. Any entries outside of this range will return [noone](../../../GML_Overview/Instance Keywords/noone.md).

 

#### Syntax:

instance\_id\[index]

 

#### Returns:

[Object Instance](Instance_Variables/id.md)

 

#### Example:

for (var i \= 0; i \< instance\_count; i\+\+)  

 {  

     with (instance\_id\[i]) speed \+\= 0\.1;  

 }

The above code will loop through all instances within the room and add 0\.1 to their speed.
