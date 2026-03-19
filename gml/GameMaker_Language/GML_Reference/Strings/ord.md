# ord

This function takes a single character input string and returns the Unicode (UTF\-8\) value for that character. Note that when used with the [keyboard\_check\*](../Game_Input/Keyboard_Input/Keyboard_Input.md) functions, the input string can only be one character in length and can only be a number from 0 to 9 or a *capitalised* Roman character from A to Z.

 

#### Syntax:

ord(string)

| Argument | Type | Description |
| --- | --- | --- |
| string | [String](../../GML_Overview/Data_Types.md) | The string of which to find the Unicode value. |

 

#### Returns:

[Real](../../GML_Overview/Data_Types.md)

 

#### Example:

if (keyboard\_check(ord("W")))  

 {  

     y \-\= 4;  

 }

This will move the calling instance four pixels upwards if the key W is held down.
