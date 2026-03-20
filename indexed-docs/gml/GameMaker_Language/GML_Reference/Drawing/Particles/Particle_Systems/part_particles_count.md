# part\_particles\_count

This function returns the number of particles that currently exist in the given particle system.

 

#### Syntax:

part\_particles\_count(ind)

| Argument | Type | Description |
| --- | --- | --- |
| ind | [Particle System Instance](part_system_create.md) | The particle system. |

 

#### Returns:

[Real](../../../../GML_Overview/Data_Types.md)

 

#### Example:

if (part\_particles\_count(Sname) \=\= 0\)  

 {  

     part\_system\_destroy(Sname);  

     instance\_destroy();  

 }

The above code will check the number of particles in the local particle system indexed in the variable Sname and if there are none, it will destroy the system and then the instance.
