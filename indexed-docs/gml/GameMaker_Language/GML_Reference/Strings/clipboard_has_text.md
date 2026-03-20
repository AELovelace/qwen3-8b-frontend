# clipboard\_has\_text

This function returns true if the clipboard contains text or false if it does not.

 
 

#### Syntax:

clipboard\_has\_text()

 

#### Returns:

[Boolean](../../GML_Overview/Data_Types.md)

 

#### Example:

if (clipboard\_has\_text())  

 {  

     str \= clipboard\_get\_text();  

     clipboard\_set\_text("");  

 }

The above code checks the clipboard for text and if it contains any, it is read as a string into the variable str. Finally the clipboard is cleared by setting it to an empty string.
