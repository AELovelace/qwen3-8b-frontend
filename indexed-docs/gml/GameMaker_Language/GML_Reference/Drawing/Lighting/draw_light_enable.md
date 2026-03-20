# draw\_light\_enable

This function is used to enable a defined light. When you define a positional or a directional light you must assign it an index number which is then used by this function to switch the light on or off. Default is disabled (false).

 
 

#### Syntax:

draw\_light\_enable(ind, enable)

| Argument | Type | Description |
| --- | --- | --- |
| ind | [Real](../../../GML_Overview/Data_Types.md) | The index number of the light (from 0 to 7\) |
| enable | [Boolean](../../../GML_Overview/Data_Types.md) | Enable or disable all lighting (true or false) |

 

#### Returns:

N/A

 

#### Example:

draw\_set\_lighting(true);  

 draw\_light\_define\_direction(1, 0, 1, 0, c\_white);  

 draw\_light\_enable(1, true);

The above code will enable lighting for the whole scene, then define a white directional light in the room space, and then finally turn that light on.
