# view\_visible

This variable can be used to find out if a particular viewport is currently visible or not. You can also set this variable to effectively turn "on" or "off" a view by setting the value to true (visible) or false (invisible). Note that even if you have a viewport set to visible, if viewports are not enabled (using the built\-in variable [view\_enabled](view_enabled.md) or enabling them in [The Room Editor](../../../../The_Asset_Editors/Rooms.md)) then they will not be drawn to the screen.

 
 

#### Syntax:

view\_visible\[0 ... 7]

 

#### Returns:

[Boolean](../../../GML_Overview/Data_Types.md) (true: enabled, false: disabled)

 

#### Example:

if (!view\_visible\[0])  

 {  

     view\_visible\[0] \= true;  

 }

The above code checks to see if view\[0] is visible or not and if it is not, it then sets it to be visible.
