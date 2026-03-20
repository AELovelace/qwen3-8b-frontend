# part\_system\_get\_info

This function returns information about the given particle system instance. See info of the returned struct on [particle\_get\_info](../particle_get_info.md).

 

#### Syntax:

part\_system\_get\_info(partsys)

| Argument | Type | Description |
| --- | --- | --- |
| partsys | [Particle System Instance](part_system_create.md) | The particle system instance for which to retrieve the info |

 

#### Returns:

[Particle System Info Struct](../particle_get_info.md#particle_system_info_struct)

 

#### Example:

var \_info \= part\_system\_get\_info(ps\_trail);  

 var \_readable \= json\_stringify(\_info, true);  

 show\_debug\_message(\_readable);

The above code calls part\_system\_get\_info to retrieve information about a particle system instance stored in a variable ps\_trail. It then converts the returned struct's contents to a prettified JSON string and outputs this string's contents in a debug message.
