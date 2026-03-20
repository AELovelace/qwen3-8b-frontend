# gesture\_get\_drag\_time

This function is used to get the time it takes for a [Drag Start Gesture](../../../../The_Asset_Editors/Object_Properties/Gesture_Events.md) event to be triggered by a touch or click. This time will also affect how the **Tap Event** is triggered as a touch/click and release before this time is up will be considered a Tap. The time is measured in seconds and has a default value of 0\.16\.

 

#### **Syntax:**

gesture\_get\_drag\_time();

 

#### Returns:

 (time in seconds)

 

#### Example:

if (gesture\_get\_drag\_time() !\= 0\.16\)   

 {  

     gesture\_drag\_time(0\.16\);  

 }

The above code checks to see if the drag time for gestures is set to 0\.16 seconds and if it is not it sets it to that value.
