# dot\_product\_normalised

This function returns the normalised dot product of two 2D vectors specified as (x1, y1\) and (x2, y2\).

The dot product is a value expressing the angular relationship between two vectors and is found by taking two vectors, multiplying them together and then adding the results. The name "dot product" is derived from the centered dot "·" that is often used to designate this operation (the alternative name "scalar product" emphasises the scalar rather than vector nature of the result).

The actual mathematical formula can be written like this:

So, in 2D the dot product of vectors a\[x1,y1] and b\[x2,2] is x1x2 \+ y1y2, meaning that the dot\_product in GameMaker is calculated as:

a · b \= (x1\*x2\)\+(y1\*y2\);

What about the *normalised* dot product? The normalised dot product has been corrected in such a way as to bring the return value into the range of \-1 and 1 (see the section on [Vectors](../../../../Additional_Information/Vectors.md) for more detailed information), which is exceptionally useful in many circumstances, particularly when dealing with lighting and other 3D functions.

 

#### **Syntax:**

dot\_product\_normalised(x1, y1, x2, y2\)

| Argument | Type | Description |
| --- | --- | --- |
| x1 | [Real](../../../GML_Overview/Data_Types.md) | The x coordinate of the first vector |
| y1 | [Real](../../../GML_Overview/Data_Types.md) | The y coordinate of the first vector |
| x2 | [Real](../../../GML_Overview/Data_Types.md) | The x coordinate of the second vector |
| y2 | [Real](../../../GML_Overview/Data_Types.md) | The y coordinate of the second vector |

 

#### Returns:

[Real](../../../GML_Overview/Data_Types.md)

 

#### Example:

var \_x1 \= lengthdir\_x(1, image\_angle);  

 var \_y1 \= lengthdir\_y(1, image\_angle);  

 var \_x2 \= obj\_player.x \- x;  

 var \_y2 \= obj\_player.y \- y;  

 if (dot\_product\_normalised(\_x1, \_y1, \_x2, \_y2\) \> 0\)  

 {  

     seen \= true;  

 }  

 else  

 {  

     seen \= false;  

 }

The above code creates a vector using the instance's [image\_angle](../../Asset_Management/Sprites/Sprite_Instance_Variables/image_angle.md), and then gets the vector of the player instance (referenced through obj\_player) to itself. Finally it calculates the dot product of these two vectors and, if it is greater than 0, sets the variable seen to true, and if it is equal to or less than 0, it sets it to false.
