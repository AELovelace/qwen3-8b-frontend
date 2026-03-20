# image\_number

This **read only** variable can be used to get the number of sub\-images in a sprite that has been assigned to an instance (if you need the number of sub\-images for a sprite other than the one assigned to the instance you should use [sprite\_get\_number()](../Sprite_Information/sprite_get_number.md)). Please note that when there is (for example) 1 sub\-image this variable will return "1" but the image\_index of that sub\-image is 0\.

 

#### Syntax:

image\_number

 

#### Returns:

 (single precision floating point value)

 

#### Example:

if (image\_speed \> 0\)   

 {  

     if image\_index \> image\_number \- 1 instance\_destroy();  

 }

The above code checks to see if the sprite is animating, and if it is it then checks to see if the current image\_index is greater than the number of sub\-images and if it is it destroys the instance.
