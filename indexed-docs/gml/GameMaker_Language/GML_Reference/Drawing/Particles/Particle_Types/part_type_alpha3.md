# part\_type\_alpha3

This function can be used to set a three alpha (transparency) value gradient for each particle created of the given type.

The first alpha is that which all particles will start with, and the second alpha is the one that will be blended to half way through its lifetime and the third alpha is the one with which the particle will end with. A smooth gradient change will occur through the alphas over the particle's lifetime from one to the other.

 

#### Syntax:

part\_type\_alpha3(ind, alpha1, alpha2, alpha3\)

| Argument | Type | Description |
| --- | --- | --- |
| ind | [Particle Type ID](part_type_create.md) | The index of the particle type to change. |
| alpha1 | [Real](../../../../GML_Overview/Data_Types.md) | The starting alpha of the particle. |
| alpha2 | [Real](../../../../GML_Overview/Data_Types.md) | The halfway point alpha of the particle. |
| alpha3 | [Real](../../../../GML_Overview/Data_Types.md) | The ending alpha of the particle. |

 

#### Returns:

N/A

 

#### Example:

part\_type\_alpha3( part\_Health, 0\.5, 1, 0\);

The above code will make all particles created of the type indexed in the variable part\_Health have an alpha blend from 0\.5 to 1 to 0 over their lifetime.
