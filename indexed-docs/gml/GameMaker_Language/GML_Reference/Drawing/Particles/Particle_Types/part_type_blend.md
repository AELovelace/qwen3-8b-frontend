# part\_type\_blend

This function you can make your particles be drawn with an additive blend mode (true) or not (false).

Additive blending is a special blend mode that adds the luminosity values of each particle as they overlap, so that light colours will gradually get brighter (until they appear white) as they overlap, and dark colours become more and more transparent with black being almost invisible. This function can give some beautiful particle effects but may not always be necessary. For example, a smoke trail would have additive blending off to keep the effect gray, but a flame effect would probably have it on to make the particles more translucent and brighter.

 

#### Syntax:

part\_type\_blend(ind, additive)

| Argument | Type | Description |
| --- | --- | --- |
| ind | [Particle Type ID](part_type_create.md) | The index of the particle type to change. |
| additive | [Boolean](../../../../GML_Overview/Data_Types.md) | Whether the particles should be blended additively (true) or normally (false). |

 

#### Returns:

N/A

 

#### Example:

part\_type\_blend(part\_fire, true);

The above code will set all particles created of the particle type indexed in the variable part\_fire to have an additive blend mode.
