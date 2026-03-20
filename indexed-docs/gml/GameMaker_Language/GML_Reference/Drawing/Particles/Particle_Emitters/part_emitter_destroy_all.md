# part\_emitter\_destroy\_all

This function removes all defined emitters from the given particle system and clears them from memory.

This will also stop any particles from being produced by the emitters. Existing particles created by the emitters are *not* removed from the system.

This function should always be called when the emitters are no longer needed for the system to prevent memory leaks and errors.

 
 

#### Syntax:

part\_emitter\_destroy\_all( ps )

| Argument | Type | Description |
| --- | --- | --- |
| ps | [Particle System Instance](../Particle_Systems/part_system_create.md) | The particle system to destroy all emitters from. |

 

#### Returns:

N/A

 

#### Example:

if (lives \=\= 0\)  

 {  

     part\_emitter\_destroy\_all(global.Sname);  

     room\_goto(rm\_Menu);  

 }

The above code checks the built\-in global variable [lives](../../../../GML_Overview/Variables/Builtin_Global_Variables/lives.md) and if it is 0, it destroys all particle emitters and then changes room.
