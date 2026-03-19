# string\_replace\_all

You can use this function to parse a string looking for specific substrings, which can then be replaced by the new string that you have specified in all places that they occur.

 

#### Syntax:

string\_replace\_all(str, substr, newstr)

| Argument | Type | Description |
| --- | --- | --- |
| str | [String](../../GML_Overview/Data_Types.md) | The string to be parsed. |
| substr | [String](../../GML_Overview/Data_Types.md) | The substring within the string to be replaced in all instances. |
| newstr | [String](../../GML_Overview/Data_Types.md) | The new substring to replace the previous one(s). |

 

#### Returns:

[String](../../GML_Overview/Data_Types.md)

 

#### Example:

str1 \= "Hexxo Worxd";  

 str2 \= string\_replace\_all(str1, "x", "l");

This will set str2 to str1, but with its instances of "x" replaced with "l", resulting in str2 being "Hello World".
