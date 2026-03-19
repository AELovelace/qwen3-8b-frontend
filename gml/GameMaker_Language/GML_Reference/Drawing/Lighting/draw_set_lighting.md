# draw\_set\_lighting

This function is used to enable all lighting effects. Default is disabled (false).

 

#### Syntax:

draw\_set\_lighting(enable)

| Argument | Type | Description |
| --- | --- | --- |
| enable | [Boolean](../../../GML_Overview/Data_Types.md) | Whether to enable or disable all lighting (true or false) |

 

#### Returns:

N/A

 

#### Example:

draw\_set\_lighting(true);  

 draw\_light\_define\_direction(1, 0, 1, 0, c\_white);  

 draw\_light\_enable(1, true);

The above code will enable lighting for the whole scene, then define a white directional light in the room space, and then finally turn that light on.
