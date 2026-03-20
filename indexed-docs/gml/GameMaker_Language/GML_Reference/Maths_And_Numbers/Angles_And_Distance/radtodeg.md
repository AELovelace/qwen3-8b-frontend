# radtodeg

This function converts an angle in radians to an angle in degrees.

Once you have done your calculations using [sin](sin.md), [cos](cos.md), etc., the result is in radians. This may not always be what you want and so to turn the radians into degrees we use this function. For example, radtodeg(sin(180\)) will return \-45 degrees. This function translates radians into degrees using the formula:

angle\_degrees \= angle\_radians \* 180 / pi;

 

#### Syntax:

radtodeg(rad)

| Argument | Type | Description |
| --- | --- | --- |
| rad | [Real](../../../GML_Overview/Data_Types.md) | The radians to convert |

 

#### Returns:

[Real](../../../GML_Overview/Data_Types.md)

 

#### Example:

val \= radtodeg(pi);

This will set val to 180\.
