# angle\_difference

This function returns the smallest difference between the two specified angles, where the difference is calculated from the source angle towards the destination angle.

The returned value will be between \-180 and 180 degrees (where a positive angle is anti\-clockwise and a negative angle is clockwise).

The relationship between the "source" and "destination" angles is such that the difference that you get by calling angle\_difference(dest, src), when added back to the src value, gives you the dest angle (although the exact numeric values may differ). You can use a similar technique to move the source angle towards the destination angle gradually every step, where you add, say, 10% of the returned difference back to src to move it a little bit towards dest (this is demonstrated in the example below).

 

#### **Syntax:**

angle\_difference(dest, src)

| Argument | Type | Description |
| --- | --- | --- |
| dest | [Real](../../../GML_Overview/Data_Types.md) | The destination or target angle (in degrees) |
| src | [Real](../../../GML_Overview/Data_Types.md) | The source angle (in degrees) |

 

#### Returns:

[Real](../../../GML_Overview/Data_Types.md)

 

#### Example:

var \_dir \= point\_direction(x, y, mouse\_x, mouse\_y);  

 var \_diff \= angle\_difference(\_dir, image\_angle);  

 image\_angle \+\= \_diff \* 0\.1;

The above code will get the direction from the instance to the mouse cursor, then get the difference between that angle and the current [image\_angle](../../Asset_Management/Sprites/Sprite_Instance_Variables/image_angle.md), using this value to gradually rotate the instance towards the mouse.

Interactive Example
