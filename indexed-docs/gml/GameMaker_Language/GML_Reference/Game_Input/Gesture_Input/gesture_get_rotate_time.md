# gesture\_get\_rotate\_time

This function is used to get the time within which a pair of touches must be rotating in a consistent direction for a [Rotate Start Gesture](../../../../The_Asset_Editors/Object_Properties/Gesture_Events.md) to be triggered. The time is measured in seconds and has a default value of 0\.16s.

**IMPORTANT!** Currently for a 60fps game you can only set this to a maximum of one second otherwise no rotations will be detected. This will increase for a lower framrate, for example a 30fps game can have a maximum time of 2 seconds.

 

#### **Syntax:**

gesture\_get\_rotate\_time();

 

#### Returns:

 (inches)

 

#### Example:

if (gesture\_get\_rotate\_time() !\= 0\.1\)   

 {  

     gesture\_rotate\_time(0\.1\);  

 }

The above code checks to see if the rotate time for gestures is set to 0\.1 seconds and if it is not it sets it to that value.
