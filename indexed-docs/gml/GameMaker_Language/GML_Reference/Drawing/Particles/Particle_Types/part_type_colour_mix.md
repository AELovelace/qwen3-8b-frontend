# part\_type\_colour\_mix

This function sets the colour of newly created particles of the given type to be a random blend of two colours.

 
 

#### Syntax:

part\_type\_colour\_mix(ind, colour1, colour2\)

| Argument | Type | Description |
| --- | --- | --- |
| ind | [Particle Type ID](part_type_create.md) | The index of the particle type to change. |
| colour1 | [Colour](../../Colour_And_Alpha/Colour_And_Alpha.md) | The first colour the blend will take from. |
| colour2 | [Colour](../../Colour_And_Alpha/Colour_And_Alpha.md) | The second colour the blend will take from. |

 

#### Returns:

N/A

 

#### Example:

part\_type\_colour\_mix(global.P\_Damage, c\_red, c\_yellow);

The above code will set the colour for each particle emitted of the particle type indexed in the global variable P\_Damage to be a random mix between the colours red and yellow.
