# arctan2

This function returns the inverse tangent (in radians) of a value given as a ratio y/x, where y \= opposite side of triangle and x \= adjacent side of triangle.

Unlike [arctan](arctan.md), the function arctan2(y, x) is valid for all angles and so may be used to convert a vector to an angle without risking division by zero, and it also returns a result in the correct quadrant.

  The value returned is in radians, not degrees.

 

#### Syntax:

arctan2(y, x)

| Argument | Type | Description |
| --- | --- | --- |
| y | [Real](../../../GML_Overview/Data_Types.md) | The y coordinate |
| x | [Real](../../../GML_Overview/Data_Types.md) | The x coordinate |

 

#### Returns:

[Real](../../../GML_Overview/Data_Types.md)

 

#### Example:

val \= arctan2(1, 1\);

This will set val to the correct angle, in this case 0\.79\.
