# part\_type\_colour1

This function sets the colour of newly created particles of the given type to be a single colour for the total duration of the lifetime of each individual particle.

 
 

#### Syntax:

part\_type\_colour1(ind, colour1\)

| Argument | Type | Description |
| --- | --- | --- |
| ind | [Particle Type ID](part_type_create.md) | The index of the particle type to change. |
| colour1 | [Colour](../../Colour_And_Alpha/Colour_And_Alpha.md) | The single colour to make the particle type. |

 

#### Returns:

N/A

 

#### Example:

part\_type\_colour1(global.Snow\_Part, c\_white);

The above code will set all particles created of the particle type indexed in the global variable Snow\_Part to be white only.
