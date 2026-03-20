# string\_digits

You can use this function to parse a given string and get any numbers from it. For example, say you have this text \- "I am 81 years old". With this function you would get a return string of "81".

 

#### Syntax:

string\_digits(string)

| Argument | Type | Description |
| --- | --- | --- |
| string | [String](../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The string to get the digits from. |

 

#### Returns:

[String](../../../../GameMaker_Language/GML_Overview/Data_Types.md)

 

#### Example:

var t\_str \= string\_digits(input\_str);  

 age \= real(t\_str);

The above code will take the input string, strip it of all characters other than numbers and then set the variable age to hold the real number value of the return string (so, if the input string was \- for example \- "I am 18", the function would return "18").
