# animcurve\_get\_channel

This function returns a [struct](../../../GML_Overview/Structs.md) containing the channel data for the channel specified in an animation curve asset or struct (as returned by [animcurve\_get](animcurve_get.md)).

You supply the animation curve ID or struct as well as the channel name or index, and the function will return a struct with the following format:

 
The first required argument is the Animation Curve as it was defined in [The Asset Browser](../../../../Introduction/The_Asset_Browser.md), or the struct pointer as returned by the function [animcurve\_create](animcurve_create.md).

The second required argument is a string that refers to the channel as it was defined in the Animation Curve asset, or you can supply an index value, which is from 0 to *n\-1*, where *n\-1* is the last channel in the curve asset (e.g.: if an animation curve has 4 channels, they will be indexed from 0 to 3\).

Note that passing an index value will require less processing than passing in a channel name. If the function fails (i.e.: no channel exists with the given name or index) then you will get an error.

### 'points' Array

The points member of the returned struct contains an array, which contains all of the channel's points as structs.

One point struct has the following variables:

 
The points member only allows you to get and set the array variable. You cannot run [Array Functions](../../Variable_Functions/Array_Functions.md) on the points array to modify it.

To modify the points array, store it in a variable, which will create a copy. Then modify that copy with the array functions, and apply that copy back to the points member in the struct.

var \_points\_copy \= channel\_struct.points;  

  

 array\_delete(\_points\_copy, 0, 1\);  

  

 channel\_struct.points \= \_points\_copy;
 

 

 

#### Syntax:

animcurve\_get\_channel(curve\_struct\_or\_id, channel\_name\_or\_index)

| Argument | Type | Description |
| --- | --- | --- |
| curve\_struct\_or\_id | [Animation Curve Struct](animcurve_get.md) or [Animation Curve Asset](../../../../The_Asset_Editors/Animation_Curves.md) | The ID or struct pointer of the animation curve to target |
| channel\_name\_or\_index | [String](../../../GML_Overview/Data_Types.md) or [Real](../../../GML_Overview/Data_Types.md) | The channel name (a string) or the channel index (an integer) |

 

#### Returns:

[Animation Curve Channel Struct](animcurve_get_channel.md)

 

#### Example:

var \_channel\_data \= animcurve\_get\_channel(ac\_ButtonTween, 0\);  

 var \_points \= \_channel\_data.points;  

 for (var i \= 0; i \< array\_length(\_points); \+\+i)  

 {  

     \_points\[i].value \+\= 1;  

 }

The above code retrieves the channel struct for channel 0 in the curve asset ac\_ButtonTween, then loops through the points on the channel curve and adds one to their value.
