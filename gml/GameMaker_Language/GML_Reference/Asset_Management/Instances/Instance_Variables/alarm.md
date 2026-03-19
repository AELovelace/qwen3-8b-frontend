# alarm

This 1\-dimensional [array](../../../../GML_Overview/Arrays.md) is used to get the current value for any alarms that the instance may have, or it can be used to set those alarms. There are twelve alarms built into each instance of an object, and each one has its own [event](../../../../../The_Asset_Editors/Object_Properties/Object_Events.md) that will run when this variable reaches 0\.

Alarms are counted down at the start of each step, **after** the Begin Step event but **before** the main Step event, and before anything is rendered for the frame. This means that if you set an alarm to 1 in the Begin Step event, its event will run in that same frame (as the alarm will be counted down to 0 after Begin Step has finished), but if you set an alarm to 1 in the Step event, it will run in the next frame.

It should be noted that the alarm is not finished when it reaches 0 (although the event has been triggered) as the next step it will go down to \-1, so if you need to stop an alarm for any reason you should set its array value to \-1 *not* 0\. Alarm times are calculated in *game steps*, with a value of 30 being 30 steps, 60 being 60 steps, etc.

  An alarm with no actions or code in it will not run. However, even with just a comment and no code, the alarm will count down.

You can set the alarm array directly (and retrieve the current alarm value directly by using the array too), but under some circumstances this is not the most appropriate method, so you can also use the function [alarm\_set](../alarm_set.md) to set an alarm, and the function [alarm\_get](../alarm_get.md) to get the value of an alarm.

 
 

#### Syntax:

alarm\[index]

 

#### Holds:

[Real](../../../../GML_Overview/Data_Types.md) (\-1 if the alarm isn't running)

 

#### Example:

Create Event

can\_shoot \= true;

Alarm 0 Event

can\_shoot \= true;

Step Event

if (can\_shoot)  

 {  

     if (keyboard\_check\_pressed(vk\_space))  

     {  

         can\_shoot \= false;  

         alarm\[0] \= game\_get\_speed(gamespeed\_fps);  

         instance\_create\_layer(x, y, "Bullets", obj\_bullet);  

     }  

 }

The above code checks a variable can\_shoot in the Step event. If this variable is true, a key press of the Space key is then checked and if that is true the variable is finally set to false, alarm\[0] is set and an instance of obj\_bullet is created. When the alarm reaches 0, the can\_shoot variable is set back to true. Note that this variable is first initialised to true in the Create event.
