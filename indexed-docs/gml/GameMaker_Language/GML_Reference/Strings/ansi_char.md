# ansi\_char

This function returns a string containing the character with raw BYTE value set. This will not, *and should not*, be displayed, but it will save correctly to disk for use in encoding.

 

#### Syntax:

ansi\_char(val)

| Argument | Type | Description |
| --- | --- | --- |
| val | [Real](../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The raw byte value. |

 

#### Returns:

[String](../../../../GameMaker_Language/GML_Overview/Data_Types.md) (Single character)

 

#### Example:

var str1 \= ansi\_char($EF);  

 var str2 \= ansi\_char($BB);  

 var str3 \= ansi\_char($BF);  

 file\_text\_write\_string(global.saveFile, str1 \+ str2 \+ str3\);

The above code creates a string from raw byte data and writes it to a (previously opened) file.
