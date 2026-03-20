# clipboard\_set\_text

This function sets the clipboard to hold the defined string. You can set it to an empty string "" to effectively clear the clipboard of text.

 
 

#### Syntax:

clipboard\_set\_text(string)

| Argument | Type | Description |
| --- | --- | --- |
| string | [String](../../GML_Overview/Data_Types.md) | The text (as a string) to set the clipboard to hold. |

 

#### Returns:

N/A

 

#### Example:

if (clipboard\_has\_text())  

 {  

     str \= clipboard\_get\_text();  

     clipboard\_set\_text("");  

 }

The above code checks the clipboard for text and if it contains any, it is read as a string into the variable str. Finally the clipboard is cleared by setting it to an empty string.
