# string\_set\_byte\_at

This function sets a byte directly in a string (based on the UTF\-8 format) and returns a copy of the string with the changes.

  This function is incredibly slow so consider carefully whether it is necessary and where you use it.

 

#### Syntax:

string\_set\_byte\_at(str, pos, byte)

| Argument | Type | Description |
| --- | --- | --- |
| str | [String](../../GML_Overview/Data_Types.md) | The string to change the byte of. |
| pos | [Real](../../GML_Overview/Data_Types.md) | The position within the string (starting at 1\) to change the byte of. |
| byte | [Real](../../GML_Overview/Data_Types.md) | The new byte value. |

 

#### Returns:

[String](../../GML_Overview/Data_Types.md)

 

#### Example:

str \= string\_set\_byte\_at("hello", 2, 97\);

The above code would change the byte value of the second letter in the string, and so set the variable str to hold "hallo".
