# weak\_ref\_create

With this function you can create a [weak reference](#) to a [struct](../../GML_Overview/Structs.md) or [instance](../../../Quick_Start_Guide/Objects_And_Instances.md) which can then be used to check if it is still "alive" (referenced) or not in the game. You supply the reference to the struct or instance you want to track, and the function will return another struct which is a weak reference to that struct.

### Usage Notes

- You can check whether a reference is "strong" or "weak" by using the function [instanceof](../Variable_Functions/instanceof.md), as a strong reference will return either "struct" or the name of the constructor function that created the struct, or "weakref" if it's a weak reference.
- The weak reference struct will have a variable ref which can be accessed to get the strong reference to the struct in question, unless it has been garbage collected, in which case it will return undefined.
- Passing an instance is the same as passing the self variable of that instance, as the returned weak ref points to that self struct

 

#### Syntax:

weak\_ref\_create(struct\_to\_track)

| Argument | Type | Description |
| --- | --- | --- |
| struct\_to\_track | [Struct](../../GML_Overview/Structs.md) or [Object Instance](../Asset_Management/Instances/Instance_Variables/id.md) | The struct or instance that you want to create a weak reference for |

 

#### Returns:

[Struct Weak Reference](weak_ref_create.md)

 

#### Example:

inventory\_ref \= weak\_ref\_create(inventory);

The above code creates a weak reference to a struct and stores it in an instance variable for later use.
