# string\_last\_pos\_ext

This function will return the character position of an instance of a sub\-string within a string, searching backwards through the string from the position given as the starting position. The function will return 0 if the search string is not found, or the position of the first character of the search string if it is. Keep in mind that for legacy support strings are indexed from 1, so 1 is the first position in the string, not 0 as you may expect.

 

#### Syntax:

string\_last\_pos\_ext(substr, str, start\_pos)

| Argument | Type | Description |
| --- | --- | --- |
| substr | [String](../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The substring to look for in the string. |
| str | [String](../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The string. |
| start\_pos | [Real](../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The starting position to search from. |

 

#### Returns:

[Real](../../../../GameMaker_Language/GML_Overview/Data_Types.md)

 

#### Example:

if (string\_last\_pos\_ext(",", text, 20\) !\= 0\)  

 {  

     string\_insert(name, text, string\_last\_pos\_ext(",", text, 20\));  

 }

The above code searches the string stored in the variable "text" for a comma before the 20th character, and if it finds one it inserts the substring "name" at that position.
