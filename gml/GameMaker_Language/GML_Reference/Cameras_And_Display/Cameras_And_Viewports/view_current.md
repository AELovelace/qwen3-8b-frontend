# view\_current

This **read\-only** variable holds the index of the current viewport being rendered, or 0 outside of the regular [Draw Events](../../../../The_Asset_Editors/Object_Properties/Draw_Events.md).

The value will change during the Draw event when you have various views as the Draw event is called *once for each viewport in succession*. So when (for example) you are using viewport\[0] and viewport\[1] in your game room, the [Draw Events](../../../../The_Asset_Editors/Object_Properties/Draw_Events.md) for *ALL* instances will be run twice, once for each port, and with this variable you can check to see what view is currently being drawn. In general, this is used to only render specific details to a single viewport when multiple are visible in the room at the same time. See the example code below.

 

#### Syntax:

view\_current

 

#### Returns:

[Real](../../../GML_Overview/Data_Types.md) (viewport index from 0 to 7 in the regular Draw events, 0 otherwise)

 

#### Example:

if (view\_current \=\= 0\)  

 {  

     var \_xx \= camera\_get\_view\_x(view\_camera\[0]);  

     var \_yy \= camera\_get\_view\_y(view\_camera\[0]);  

     draw\_text(\_xx \+ 32, \_yy \+ 32, "Player 1");  

 }  

 else  

 {  

     var \_xx \= camera\_get\_view\_x(view\_camera\[1]);  

     var \_yy \= camera\_get\_view\_y(view\_camera\[1]);  

     draw\_text(\_xx \+ 32, \_yy \+ 32, "Player 2");  

 }

The above code checks to see which view is currently being drawn and then draws a different text to each view based on the return value.
