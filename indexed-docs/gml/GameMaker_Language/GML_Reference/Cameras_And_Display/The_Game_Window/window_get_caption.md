# window\_get\_caption

This function returns the caption of the window (this is the text that appears on the top of the window, next to its icon).

 

#### Syntax:

window\_get\_caption()

 

#### Returns:

[String](../../../GML_Overview/Data_Types.md)

 

#### Example:

if (window\_get\_caption() !\= "")  

 {  

     window\_set\_caption("");  

 }

The above code will check the windows caption to see if it has text or not, and if it does, sets it to an empty string so that no caption is displayed.
