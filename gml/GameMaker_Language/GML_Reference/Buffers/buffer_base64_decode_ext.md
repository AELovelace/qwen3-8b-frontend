# buffer\_base64\_decode\_ext

This function decodes a base64 encoded string (created using the [buffer\_base64\_encode](buffer_base64_encode.md) function) into a buffer.

Unlike the function [buffer\_base64\_decode](buffer_base64_decode.md), this will *not* create a buffer for you, but rather you should already have created the buffer (see [buffer\_create](buffer_create.md)), which you would then use with this function. The "offset" is the position within the buffer to decode the given string (in bytes).

 

#### Syntax:

buffer\_base64\_decode\_ext(buffer, string, offset)

| Argument | Type | Description |
| --- | --- | --- |
| buffer | [Buffer](../../../../GameMaker_Language/GML_Reference/Buffers/buffer_create.md) | The buffer to decode the string into. |
| string | [String](../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The base64 encoded string to decode. |
| offset | [Real](../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The data offset value. |

 

#### Returns:

N/A

 

#### Example:

buff \= buffer\_create(16384, buffer\_grow, 2\);  

 ini\_open("Save.ini");  

 var \_str \= ini\_read\_string("Save", "Slot1", "");  

 buffer\_base64\_decode\_ext(buff, \_str, 0\);  

 ini\_close();

The above code will create a buffer and store it in the variable buff, then open an INI file and read a string from it into the local variable \_str. This string is then decoded into the newly created buffer before closing the INI file again.
