# max

This function returns the maximum of the input values, of which it can have as many as you require (note that more arguments will mean that the function will be slower to parse). For example, max(12, 96, 32, 75\) will return 96 as that is the highest of all the input values.

 

#### Syntax:

max(val1, val2, ... max\_val)

| Argument | Type | Description |
| --- | --- | --- |
| val0 ... max\_val | [Real](../../../GML_Overview/Data_Types.md) | The values to compare |

 

#### Returns:

[Real](../../../GML_Overview/Data_Types.md)

 

#### Example:

x \= max(x, 0\);

This will stop the player from exiting the left of the room. This works by constantly setting its x to either itself or 0, whichever is larger. If the player exits the left, its x would be smaller than 0 (i.e. negative), so it'll get set straight back.
