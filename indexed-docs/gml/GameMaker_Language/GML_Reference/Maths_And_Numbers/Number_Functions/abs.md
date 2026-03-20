# abs

This function returns the absolute value of the input argument, so if it's a positive value then it will remain the same, but if it's negative it will be multiplied by \-1 to make it positive.

 

#### **Syntax:**

abs(val)

 

| Argument | Type | Description |
| --- | --- | --- |
| val | [Real](../../../GML_Overview/Data_Types.md) | The number to turn absolute. |

 

#### Returns:

[Real](../../../GML_Overview/Data_Types.md)

 

#### Example:

x \+\= abs(x \- mouse\_x);

This will add an amount equal to the absolute value of the difference between the current x position of the instance and the mouse x position.
