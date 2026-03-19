# buffer\_base64\_decode

This function decodes a base64 encoded string (created using the [buffer\_base64\_encode](buffer_base64_encode.md) function) into a new buffer.

The buffer is created as a 1 byte aligned "grow" buffer.

 
 

#### Syntax:

buffer\_base64\_decode(string)

| Argument | Type | Description |
| --- | --- | --- |
| string | [String](../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The base64 encoded string to decode |

 

#### Returns:

[Buffer](../../../../GameMaker_Language/GML_Reference/Buffers/buffer_create.md)

 

#### Example:

ini\_open("Save.ini");  

 buff \= buffer\_base64\_decode(ini\_read\_string("Save", "Slot1", ""));  

 ini\_close();

The above code will open an INI file and then read a string from it into the buffer\_base64\_decode function. The function will return a buffer, which is stored in the variable buff, containing the data previously encoded and saved. The INI file is then closed.
