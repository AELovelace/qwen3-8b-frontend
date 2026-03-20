# device\_get\_tilt\_x

This function returns a value between \-1 and 1 depending on the angle of "tilt" of the device. The actual correlation between degrees of tilt and the value returned depends on the device and OS that it uses, but generally a value of 1 or \-1 is the same as \+/\-90°. The image below shows how each of the available functions relates to the device:

 
 

#### Syntax:

device\_get\_tilt\_x()

 

#### Returns:

[Real](../../../GML_Overview/Data_Types.md)

 

#### Example:

if (display\_get\_orientation() \=\= display\_landscape)  

 {  

     x \+\= sign(device\_get\_tilt\_y());  

 }  

 else  

 {  

     x \+\= sign(device\_get\_tilt\_x());  

 }

The above code checks the orientation of the display and then uses the corresponding tilt value to move the player along the x axis.
