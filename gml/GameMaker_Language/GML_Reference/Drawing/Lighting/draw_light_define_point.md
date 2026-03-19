# draw\_light\_define\_point

This function defines a positional light.

You can define the x, y and z position of the light, the light range and its colour (which will also affect the perceived intensity of the light as certain colours appear "darker" than others). You must also give the light an index number which is used in other functions to reference it.

 
 

#### Syntax:

draw\_light\_define\_point(ind, x, y, z, range, col)

| Argument | Type | Description |
| --- | --- | --- |
| ind | [Real](../../../GML_Overview/Data_Types.md) | The index number of the light (arbitrary) |
| x | [Real](../../../GML_Overview/Data_Types.md) | The x component of the light position |
| y | [Real](../../../GML_Overview/Data_Types.md) | The y component of the light position |
| z | [Real](../../../GML_Overview/Data_Types.md) | The z component of the light position |
| range | [Real](../../../GML_Overview/Data_Types.md) | The light range (in pixels) |
| col | [Colour](../Colour_And_Alpha/Colour_And_Alpha.md) | The colour to use for the light (either a constant, a real or a hex value) |

 

#### Returns:

N/A

 

#### Example:

draw\_set\_lighting(true);  

 draw\_light\_define\_point(1, 200, 123, 50, 2000, c\_white);  

 draw\_light\_enable(1, true);

The above code will enable lighting for the whole scene, then define a white light at a specific point in the room space, and then finally turn that light on.
