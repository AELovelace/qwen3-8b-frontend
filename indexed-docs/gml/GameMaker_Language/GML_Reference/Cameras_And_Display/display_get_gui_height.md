# display\_get\_gui\_height

This function gets the height (in pixels) of the GUI as used in the [Draw GUI Event](../../../The_Asset_Editors/Object_Properties/Draw_Events.md).

 
 

#### Syntax:

display\_get\_gui\_height()

 

#### Returns:

[Real](../../GML_Overview/Data_Types.md)

 

#### Example:

Draw GUI Event

var \_height \= display\_get\_gui\_height();  

 var \_valign \= draw\_get\_valign();  

 draw\_set\_valign(fa\_bottom);  

 draw\_text(5, \_height \- 5, "I am drawn in the bottom\-left corner of the GUI");  

 draw\_set\_valign(\_valign);

The above code draws a text in the GUI: it first gets the GUI height using display\_get\_gui\_height and then sets the vertical text alignment to fa\_bottom, then draws a line of text using [draw\_text](../Drawing/Text/draw_text.md) and finally resets the vertical text alignment to its previous value.
