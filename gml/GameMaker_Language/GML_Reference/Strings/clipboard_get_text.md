# clipboard\_get\_text

This function returns a string of the text contained on the clipboard. If no text is stored it will return an empty string "".

 
 

#### Syntax:

clipboard\_get\_text()

 

#### Returns:

[String](../../GML_Overview/Data_Types.md)

 

#### Example:

if (clipboard\_has\_text())  

 {  

     str \= clipboard\_get\_text();  

     clipboard\_set\_text("");  

 }

The above code checks the clipboard for text and if it contains any, it is read as a string into the variable str. Finally the clipboard is cleared by setting it to an empty string.
