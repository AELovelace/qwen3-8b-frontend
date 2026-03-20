# part\_type\_exists

This function checks if the given particle type exists in the game or not.

Note that if the variable being checked is an uninitialised variable (that a particle type would otherwise have its index assigned to) this will throw an error.

 

#### Syntax:

part\_type\_exists(ind)

| Argument | Type | Description |
| --- | --- | --- |
| ind | [Particle Type ID](part_type_create.md) | The index of the particle type to check for. |

 

#### Returns:

[Boolean](../../../../GML_Overview/Data_Types.md)

 

#### Example:

if (!part\_type\_exists(global.p1\))  

 {  

     global.p1 \= part\_type\_create();  

 }

The above code checks to see if the global variable p1 stores the index of a particle type and if it does not it creates one.
