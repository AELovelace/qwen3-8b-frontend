# gesture\_get\_pinch\_distance

This function is used to get the distance within which you have to touch/click the screen and move with two fingers before you trigger a [Pinch Gesture](../../../../The_Asset_Editors/Object_Properties/Gesture_Events.md). The distance is measured in inches and has a default value of 0\.1\.

 

#### **Syntax:**

gesture\_get\_pinch\_distance();

 

#### Returns:

 (inches)

 

#### Example:

if (gesture\_get\_pinch\_distance() !\= 0\.1\)   

 {  

     gesture\_pinch\_distance(0\.1\);  

 }

The above code checks to see if the pinch distance for gestures is set to 0\.1 inches and if it is not it sets it to that value.
