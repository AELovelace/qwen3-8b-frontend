# string\_lettersdigits

This function will return a copy of a given string with everything but its letters and digits removed, which means it can be used to remove any unwanted characters (like "\#" or "?") from, for example, a login name or a password.

  This function only returns the 26 letter English alphabet from A \- Z (upper or lower case) and the numbers 0 \- 9\.

 

#### Syntax:

string\_lettersdigits(string)

| Argument | Type | Description |
| --- | --- | --- |
| string | [String](../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The string to convert to letters and digits. |

 

#### Returns:

[String](../../../../GameMaker_Language/GML_Overview/Data_Types.md)

 

#### Example:

if (string\_length(password) \> string\_length(string\_lettersdigits(password)))  

 {  

     draw\_text(32,32, "Invalid Password! Only Letters and numbers please!");  

 }

The above code will check the length of a string against the length of the same string, but with all symbols removed. If they are not the same a message is drawn on the screen.
