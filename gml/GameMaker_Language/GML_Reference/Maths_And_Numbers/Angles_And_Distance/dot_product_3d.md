# dot\_product\_3d

This function returns the dot product of two 3D vectors specified as (x1, y1, z1\) and (x2, y2, z2\).

The dot product is a value expressing the angular relationship between two vectors and is found by taking two vectors, multiplying them together and then adding the results. The name "dot product" is derived from the centered dot "·" that is often used to designate this operation (the alternative name "scalar product" emphasises the scalar rather than vector nature of the result).

The actual mathematical formula can be written like this:

In 2D, the dot product of vectors a\[x1,y1] and b\[x2,y2] is x1x2 \+ y1y2, so in 3D, the dot product of vectors a\[x1,y1,z1] and b\[x1,y1,z1] is x1x2 \+ y1y2 \+ z1z2. So, the dot\_product\_3d in GameMaker is calculated as:

a · b \= (x1\*x2\) \+ (y1\*y2\) \+ (z1\*z2\);

The curious thing about the dot product is the relationship it has to the angle formed by the input vectors which can be expressed as:

a · b \= (length of a) \* (length of b) \* cos(angle)

That is to say, the dot product of two vectors will be equal to the cosine of the angle between those vectors, multiplied by the lengths of each of them. Here is an image to illustrate:

  See [Vectors](../../../../Additional_Information/Vectors.md) for more information.

There are a few things that we can now state from any two vectors in relation to the result of their dot product:

- If a and b are perpendicular (at 90 degrees to each other), the result of the dot product will be zero, because cos(ang) will be zero
- If the angle between a and b are less than 90 degrees, the dot product will be positive (greater than zero), as cos(ang) will be positive
- If the angle between a and b are greater than 90 degrees, the dot product will be negative (less than zero), as cos(ang) will be negative

So what does this mean for those of us that make games? Well, this mathematical relationship can be used in quite a few circumstances, but the best way to see it is to build an actual scenario and see for yourself what is going on. One of the simplest ways to do this is to generate a simple "height" check for an enemy in, say, a platform game so that the enemy will "see" the player if they are above the plane formed by the enemy *normal* vector and the 3d floor.

Basically, we are getting the vector normal from the enemy perpendicular to the floor and then we are getting the vector of the player to the enemy. We will then get the dot\_product of these vectors, and if the result is positive the player is "above" the enemy floor plane and if it is negative he is below. The actual code to get this working is supplied in the example below.

 

#### **Syntax:**

dot\_product\_3d(x1, y1, z1, x2, y2, z2\)

| Argument | Type | Description |
| --- | --- | --- |
| x1 | [Real](../../../GML_Overview/Data_Types.md) | The x coordinate of the first vector |
| y1 | [Real](../../../GML_Overview/Data_Types.md) | The y coordinate of the first vector |
| z1 | [Real](../../../GML_Overview/Data_Types.md) | The z coordinate of the first vector |
| x2 | [Real](../../../GML_Overview/Data_Types.md) | The x coordinate of the second vector |
| y2 | [Real](../../../GML_Overview/Data_Types.md) | The y coordinate of the second vector |
| z2 | [Real](../../../GML_Overview/Data_Types.md) | The z coordinate of the second vector |

 

#### Returns:

[Real](../../../GML_Overview/Data_Types.md)

 

#### Example:

var \_x1, \_y1, \_z1, \_x2, \_y2, \_z2;  

 \_x1 \= 0;  

 \_y1 \= 1;  

 \_z1 \= 0;  

 \_x2 \= obj\_player.x \- x;  

 \_y2 \= obj\_player.y \- y;  

 \_z2 \= obj\_player.z \- z;  

 if (dot\_product\_3d(\_x1, \_y1, \_z1, \_x2, \_y2, \_z2\) \> 0\)  

 {  

     above \= true;  

 }  

 else  

 {  

     above \= false;  

 }

The above code creates a vector normal along the instance's y (up) axis, and then gets the vector of the player instance (referenced through obj\_player) to itself. Finally it calculates the dot product of these two vectors and, if it is greater than 0, sets the variable above to true, and if it is less than or equal to 0, sets the variable to false.
