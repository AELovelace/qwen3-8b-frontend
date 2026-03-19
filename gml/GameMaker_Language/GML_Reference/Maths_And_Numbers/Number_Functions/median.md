# median

This function returns the median of the input values, that is, the middle value, or the larger of the two middle values when the number of arguments is even.

The function can have as many arguments as required (note that more arguments will mean that the function will be slower to parse) which must all be real values. This means that, for example, median(43, 12, 25, 19, 6\) would return 19 as it is the middle value between all the rest.

 

#### Syntax:

median(val1, val2, ... max\_val)

| Argument | Type | Description |
| --- | --- | --- |
| val0 ... max\_val | [Real](../../../GML_Overview/Data_Types.md) | The values to compare |

 

#### Returns:

[Real](../../../GML_Overview/Data_Types.md)

 

#### Example:

x \= median(0, x, room\_width);  

 y \= median(0, y, room\_height);

This will stop the player from exiting any side of the room, by using median as a clamp. If the player, for instance, moves to the left of the room boundary, its x will be smaller than 0\. This will mean the middle number of the first of the medians will be 0, so the player will be jumped to (0, y).
