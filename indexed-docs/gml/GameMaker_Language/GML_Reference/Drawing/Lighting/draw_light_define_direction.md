# draw\_light\_define\_direction

This function defines a directional light.

The direction is set by the values input for x, y and z. The direction vector is stored normalised and is negated before being sent to the shader.

The lights can also be given a colour, which will also affect the perceived intensity of the light as certain colours appear "darker" than others. You must also give the light an index number which is used in other functions to reference it.

 
 

#### Syntax:

draw\_light\_define\_direction(ind, x, y, z, col)

| Argument | Type | Description |
| --- | --- | --- |
| ind | [Real](../../../GML_Overview/Data_Types.md) | The index number of the light (arbitrary) |
| x | [Real](../../../GML_Overview/Data_Types.md) | The x component of the light vector |
| y | [Real](../../../GML_Overview/Data_Types.md) | The y component of the light vector |
| z | [Real](../../../GML_Overview/Data_Types.md) | The z component of the light vector |
| col | [Colour](../Colour_And_Alpha/Colour_And_Alpha.md) | The colour to use for the light (either a constant, a real or a hex value) |

 

#### Returns:

N/A

 

#### Example:

draw\_set\_lighting(true);  

 draw\_light\_define\_direction(1, 0, 1, 0, c\_white);  

 draw\_light\_enable(1, true);

The above code will enable lighting for the whole scene, then define a white directional light in the room space, and then finally turn that light on.
