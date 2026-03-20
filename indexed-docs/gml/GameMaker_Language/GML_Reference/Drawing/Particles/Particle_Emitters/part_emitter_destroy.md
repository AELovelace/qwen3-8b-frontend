# part\_emitter\_destroy

This function removes the specified emitter from the given particle system and clears it from memory.

This will also stop any particles from being produced by the given emitter. Existing particles created by this emitter are *not* removed from the particle system.

This function should always be called when the given emitter is no longer needed for the system to prevent memory leaks and errors.

 
 

#### Syntax:

part\_emitter\_destroy( ps, ind )

| Argument | Type | Description |
| --- | --- | --- |
| ps | [Particle System Instance](../Particle_Systems/part_system_create.md) | The particle system to destroy the emitter from. |
| ind | [Particle Emitter ID](part_emitter_create.md) | The index of the emitter to destroy. |

 

#### Returns:

N/A

 

#### Example:

if (part\_emitter\_exists(global.Sname, p\_emit))  

 {  

     part\_emitter\_destroy(global.Sname, p\_emit);  

 }

The above code will check to see if the particle emitter indexed in the variable p\_emit exists in the give particle system and if it does it is destroyed.
