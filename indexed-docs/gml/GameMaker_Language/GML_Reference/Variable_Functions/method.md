# method

With this function you can bind an existing function (or method) to the given instance or struct, creating a new [method variable](../../GML_Overview/Method_Variables.md) that can be used later.

You supply the instance ID to use (an instance that is active in the room, and not an object index) or a struct reference, as well as the function ID (or method reference) that you want to bind. The function will return a new [method](#) which can be called from the variable it is assigned to (see the code example below).

The returned method will be "bound" to the given instance or struct, meaning it will always execute in the scope of that instance/struct.

You can bind built\-in functions as well as user\-defined functions/methods, and you can also supply undefined as the instance/struct argument meaning that the current [self](../../GML_Overview/Instance Keywords/self.md) scope will be used for the binding.

  The method function is implicitly called when defining new [Method Variables](../../GML_Overview/Method_Variables.md) (to assign the new function to self) and when defining new struct and array literals. Due to this, you may see extra calls to the method function in [The Debugger](../../../IDE_Tools/The_Debugger.md) in addition to any explicit calls, which are made implicitly to define the aforementioned resources.

 

#### Syntax:

method(struct\_ref\_or\_instance\_id, func)

| Argument | Type | Description |
| --- | --- | --- |
| struct\_ref\_or\_instance\_id | [Struct](../../GML_Overview/Structs.md) or [Object Instance](../Asset_Management/Instances/Instance_Variables/id.md) | The unique reference or ID value of the struct or instance to use (can be self or undefined) |
| func | [Script Function](../../GML_Overview/Script_Functions.md) or [Method](../../GML_Overview/Method_Variables.md) | The ID of the function (or method reference) to use |

 

#### Returns:

[Method](../../GML_Overview/Method_Variables.md)

 

#### Example:

var \_inst \= instance\_position(mouse\_x, mouse\_y, obj\_enemy);  

 if (instance\_exists(\_inst))  

 {  

     enemy\_func \= method(\_inst, enemy\_ai);  

 }

The above code will check if an enemy instance exists at the mouse position. If it does then the enemy\_ai method is bound to the enemy instance and returned as a new method variable enemy\_func.
