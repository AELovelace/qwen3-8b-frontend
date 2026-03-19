# room\_width

This variable holds the width of the current room in pixels. You can change this variable to change the width of the room at any time.

 

#### Syntax:

room\_width

 

#### Returns:

 

#### Example:

if (bbox\_right \> room\_width)   

 {  

     x \+\= room\_width \- bbox\_right;  

 }

The above code checks to see if the current instance's sprite bounding box is greater than the width of the room, and if it is it moves the instance up.
