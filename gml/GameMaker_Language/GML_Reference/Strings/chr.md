# chr

This function returns a string containing the character which relates to the input Unicode code for displaying. This character depends on the current drawing fonts character set code page and if no font is set, it will use the default code page for the machine.

 

#### Syntax:

chr(val)

| Argument | Type | Description |
| --- | --- | --- |
| val | [Real](../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The Unicode code value to get the string from |

 

#### Returns:

[String](../../../../GameMaker_Language/GML_Overview/Data_Types.md)

 

#### Example:

mystring \= chr(53\) \+ chr(48\);

This would set mystring to "50" (a string, not an integer) as chr(53\) is "5" and chr(48\) is "0".
