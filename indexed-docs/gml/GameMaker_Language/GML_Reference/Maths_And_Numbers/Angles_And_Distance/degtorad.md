# degtorad

This function converts an angle in degrees to an angle in radians.

In GM all the standard trigonometric functions work in radians, but most people work in degrees and this means that to convert your degrees into radians you need to use this function. For example, degtorad(180\) returns 3\.14159265 radians. This function translates degrees into radians using the formula:

angle\_radians \= angle\_degrees \* pi / 180;

 

#### Syntax:

degtorad(deg)

| Argument | Type | Description |
| --- | --- | --- |
| deg | [Real](../../../GML_Overview/Data_Types.md) | The degrees to convert |

 

#### Returns:

[Real](../../../GML_Overview/Data_Types.md)

 

#### Example:

val \= degtorad(90\);

This will set val to pi/2\.
