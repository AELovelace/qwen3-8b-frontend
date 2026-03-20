# part\_system\_automatic\_draw

This function can be used to switch off the drawing of a particle system so that any updates done to the system (automatic or otherwise) will not be seen.

This is a purely visual option and when set to false you will not be able to see the particles as they are not drawn, but they still exist and are changing position, colour, etc. as they would normally. When automatic drawing is off, you can *explicitly* order GameMaker to draw the current state of the particle system using the function [part\_system\_drawit](part_system_drawit.md), and if you set this function to true again you can switch automatic drawing back on.

 
 

#### Syntax:

part\_system\_automatic\_draw(ind, automatic)

| Argument | Type | Description |
| --- | --- | --- |
| ind | [Particle System Instance](part_system_create.md) | The particle system to change. |
| automatic | [Boolean](../../../../GML_Overview/Data_Types.md) | Whether automatic drawing is on (true) or not (false). |

 

#### Returns:

N/A

 

#### Example:

part\_system\_automatic\_draw(global.Sname, false);

The above code switches off automatic drawing for the particle system indexed in the global variable Sname.
