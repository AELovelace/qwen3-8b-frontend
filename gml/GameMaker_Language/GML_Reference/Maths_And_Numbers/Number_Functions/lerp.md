# lerp

With this function you can find the value that equates to the position between two other values for a given percentage.

So if you do, for example:

lerp(0, 10, 0\.5\)

you would get the return value of 5, which is 50% of the input values. You can extrapolate using this function too, by supplying a positive or negative value for the interpolation amount so that doing something like:

lerp(0, 10, 2\)

will return a value of 20\.

 

#### Syntax:

lerp(a, b, amt)

| Argument | Type | Description |
| --- | --- | --- |
| a | [Real](../../../GML_Overview/Data_Types.md) | The first value. |
| b | [Real](../../../GML_Overview/Data_Types.md) | The second value. |
| amt | [Real](../../../GML_Overview/Data_Types.md) | The amount to interpolate. |

 

#### Returns:

[Real](../../../GML_Overview/Data_Types.md)

 

#### Example:

var \_gamespeed \= game\_get\_speed(gamespeed\_fps);  

 xx \= lerp(x, x \+ hspeed, \_gamespeed);  

 yy \= lerp(y, y \+ vspeed, \_gamespeed);

The above code uses the linear interpolation function to predict where an instance would have moved to after one second of game time.
