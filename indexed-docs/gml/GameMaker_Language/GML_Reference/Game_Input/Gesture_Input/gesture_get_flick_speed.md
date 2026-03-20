# gesture\_get\_flick\_speed

This function is used to get the speed required for a [Flick Gesture](../../../../The_Asset_Editors/Object_Properties/Gesture_Events.md) event to be triggered when a touch or click is released. The speed is measured in inches per second and has a default value of 2\.0\.

 

#### **Syntax:**

gesture\_get\_flick\_speed();

 

#### Returns:

 (inches per second)

 

#### Example:

if (gesture\_get\_flick\_speed() !\= 2\)   

 {  

     gesture\_flick\_speed(2\);  

 }

The above code checks to see if the flick speed for gestures is set to 2 inches per second and if it is not it sets it to that value.
