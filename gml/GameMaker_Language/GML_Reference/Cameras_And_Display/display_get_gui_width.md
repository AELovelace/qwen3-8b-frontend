# display\_get\_gui\_width

This function gets the width (in pixels) of the GUI as used in the [Draw GUI Event](../../../The_Asset_Editors/Object_Properties/Draw_Events.md).

 
 

#### Syntax:

display\_get\_gui\_width()

 

#### Returns:

[Real](../../GML_Overview/Data_Types.md)

 

#### Example:

Draw GUI Event

var \_width \= display\_get\_gui\_width();  

 var \_halign \= draw\_get\_halign();  

 draw\_set\_halign(fa\_right);  

 draw\_text(\_width \- 5, 5, "This text is drawn in the top\-right corner of the GUI");  

 draw\_set\_halign(\_halign);

The above code draws a text in the GUI: it first gets the GUI width using display\_get\_gui\_width and then sets the horizontal text alignment to fa\_right, then draws a line of text using [draw\_text](../Drawing/Text/draw_text.md) and finally resets the horizontal text alignment to its previous value.
