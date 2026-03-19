# part\_system\_exists

This function checks to see if the given particle system instance exists in the game or not.

Note that if the variable being checked is an uninitialised variable (that a particle system would otherwise have its index assigned to) this will throw an error.

 

#### Syntax:

part\_system\_exists(ind)

| Argument | Type | Description |
| --- | --- | --- |
| ind | [Particle System Instance](part_system_create.md) | The particle system to check for |

 

#### Returns:

[Boolean](../../../../GML_Overview/Data_Types.md)

 

#### Example:

if (!part\_system\_exists(global.Sname))  

 {  

     global.Sname \= part\_system\_create();  

 }

The above code checks to see if the particle system referenced in the global variable exists and if it does not it is created.
