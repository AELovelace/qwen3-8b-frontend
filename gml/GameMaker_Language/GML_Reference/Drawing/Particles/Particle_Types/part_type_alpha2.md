# part\_type\_alpha2

This function can be used to set an alpha value (transparency) gradient for each particle created of the given type. The first alpha is that which all particles will start with, and the second alpha is the one on with which the particle will end with, and a smooth gradient change will occur to the alpha over the particles lifetime from one to the other. This can be from 0 (transparent) to 1 (opaque).

 

#### Syntax:

part\_type\_alpha2(ind, alpha1, alpha2\)

| Argument | Type | Description |
| --- | --- | --- |
| ind | [Particle Type ID](part_type_create.md) | The index of the particle type to change. |
| alpha1 | [Real](../../../../GML_Overview/Data_Types.md) | The start alpha of the particle. |
| alpha2 | [Real](../../../../GML_Overview/Data_Types.md) | The end alpha of the particle. |

 

#### Returns:

N/A

 

#### Example:

part\_type\_alpha2(global.Snow\_Part, 0, 1\);

The above code will set all particles created of the particle type indexed in the global variable "Snow\_Part" to have an alpha value of 0 (transparent) and then fade in to have an alpha of 1 (opaque) at the end of their lifetime.
