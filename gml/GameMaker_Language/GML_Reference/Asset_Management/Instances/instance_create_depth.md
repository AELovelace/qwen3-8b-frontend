# instance\_create\_depth

With this function you can create a new instance of the specified object at any given point within the room and at the depth specified. The depth can be any value, where the lower the depth the "nearer" to the camera things will be drawn and the higher the depth the further away, so an instance at depth \-200 will be drawn over an instance at depth \+300 (for example).

Note that this function will actually create a room layer for the instance, since all instances *must* be on a layer in the room, but since this is a *managed* layer (i.e.: not one that you have created through code or in the room, but one that GameMaker has created automatically). You cannot access that layer, and the [layer](Instance_Variables/layer.md) instance variable will hold an invalid handle (\-1).

 
  This function behaves differently when you call it after calling a room\-changing function in the same event. See the note on [room\_goto](../Rooms/room_goto.md) for details.

This function returns the [id](Instance_Variables/id.md) of the new instance which can then be stored in a variable and used to access that instance. Note that this function will also call the [Create Event](../../../../The_Asset_Editors/Object_Properties/Object_Events.md) of the instance being created *before* continuing with the code or actions for the event that called the function.

 
 

#### Syntax:

instance\_create\_depth(x, y, depth, obj, \[var\_struct])

| Argument | Type | Description |
| --- | --- | --- |
| x | [Real](../../../GML_Overview/Data_Types.md) | The x position the instance of the given object will be created at |
| y | [Real](../../../GML_Overview/Data_Types.md) | The y position the instance of the given object will be created at |
| depth | [Real](../../../GML_Overview/Data_Types.md) | The depth to assign the created instance to |
| obj | [Object Asset](../../../../The_Asset_Editors/Objects.md) | The object to create an instance of |
| var\_struct | [Struct](../../../GML_Overview/Structs.md) | A struct with variables to assign to the new instance |

 

#### Returns:

[Object Instance](Instance_Variables/id.md)

 

#### Example 1:

var \_inst \= instance\_create\_depth(x, y, \-100, obj\_bullet);  

 with (\_inst)  

 {  

     speed \= other.shoot\_speed;  

     direction \= other.image\_angle;  

 }

The above code creates a new instance of the object obj\_bullet at \-100 depth, and stores the instance ID in a variable. This variable is then used to assign speed and direction to the new instance.

This will first create the instance, run its Create event, and *then* assign values to its variables.

If you want to assign some variables *before* the Create event runs, see the example below.

 

#### Example 2:

var inst \= instance\_create\_depth(x, y, \-100, obj\_bullet,  

 {  

     speed : shoot\_speed,  

     direction : image\_angle  

 });

The above code creates an instance of obj\_bullet, and passes in a struct as the last argument.

That struct has variables for the speed and direction. It pulls its values from the calling instance, without the need to use other.

These variables are applied to the new instance before its Create event runs.

You're not limited to a struct literal, as you can also pass in a variable that stores an existing struct, or create a [new](../../../GML_Overview/Language_Features/new.md) struct from a [constructor](../../../GML_Overview/Structs.md#constr).
