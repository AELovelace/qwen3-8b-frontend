# part\_particles\_clear

This function clears all particles currently created by the system from the room.

It does *not* reset or remove the particle types themselves, just their visual representation, and if you have any object streaming particles from an emitter, these particles disappear but will begin to appear again the next step after calling this code.

 

#### Syntax:

part\_particles\_clear(ind)

| Argument | Type | Description |
| --- | --- | --- |
| ind | [Particle System Instance](part_system_create.md) | The particle system. |

 

#### Returns:

N/A

 

#### Example:

if (lives \<\= 0\)  

 {  

     part\_particles\_clear(global.Sname);  

     room\_goto(rm\_intro);  

 }

The above code will check the value of the variable [lives](../../../../GML_Overview/Variables/Builtin_Global_Variables/lives.md) and if it is equal to 0, it clears all particles from the system and then changes room.
