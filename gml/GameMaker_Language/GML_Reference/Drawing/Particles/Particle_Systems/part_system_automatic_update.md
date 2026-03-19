# part\_system\_automatic\_update

This function controls whether GameMaker should update the particle system automatically or not.

Normally you would not need to use this function as the default value of true (automatic update is on) is what you wish to happen. However, for special effects or for pausing the game, you can set this to false and it will prevent any updates being carried out on the given particle system unless *explicitly* commanded by the use of the function [part\_system\_update](part_system_update.md) or you use this function again to turn automatic updates on. No updating means that particles created in this system will no longer change position, colour or any other parameter and that emitters will cease to work too, "freezing" the system at the exact point in which the automatic update was set to false.

 
 

#### Syntax:

part\_system\_automatic\_update(ind, automatic)

| Argument | Type | Description |
| --- | --- | --- |
| ind | [Particle System Instance](part_system_create.md) | The particle system to change. |
| automatic | [Boolean](../../../../GML_Overview/Data_Types.md) | Whether automatic updating is on (true) or not (false). |

 

#### Returns:

N/A

 

#### Example:

if (global.pause)  

 {  

     part\_system\_automatic\_update(global.Sname, false);  

 }

The above code will switch off the particle updates if the global variable pause is true.
