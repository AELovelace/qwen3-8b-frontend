# part\_system\_colour

This function changes the blend colour and alpha that the given particle system is rendered with. This is similar to [image\_blend](../../../Asset_Management/Sprites/Sprite_Instance_Variables/image_blend.md) and [image\_alpha](../../../Asset_Management/Sprites/Sprite_Instance_Variables/image_alpha.md) in instances.

 

#### Syntax:

part\_system\_colour(ind, colour, alpha)

| Argument | Type | Description |
| --- | --- | --- |
| ind | [Particle System Instance](part_system_create.md) | The particle system to change. |
| colour | [Colour](../../Colour_And_Alpha/Colour_And_Alpha.md) | The new colour of the particle system. |
| alpha | [Real](../../../../GML_Overview/Data_Types.md) | The new alpha of the particle system. |

 

#### Returns:

N/A

 

#### Example:

part\_system\_colour(pt\_sys, c\_red, 0\.5\);

This changes the colour of a particle system to red, with an alpha of 0\.5\.
