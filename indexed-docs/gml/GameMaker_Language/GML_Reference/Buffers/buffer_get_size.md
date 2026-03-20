# buffer\_get\_size

This function gets the size in bytes of the given buffer.

 

#### Syntax:

buffer\_get\_size(buffer)

| Argument | Type | Description |
| --- | --- | --- |
| buffer | [Buffer](../../../../GameMaker_Language/GML_Reference/Buffers/buffer_create.md) | The buffer to get the size of. |

 

#### Returns:

[Real](../../../../GameMaker_Language/GML_Overview/Data_Types.md)

 

#### Example:

var \_size \= buffer\_get\_size(player\_data);  

 var \_temp \= buffer\_create(\_size, buffer\_fixed, 0\);

The above code creates a new buffer and stores it in a local variable \_temp, with the size of the new buffer being the same as that of the buffer stored in the variable player\_data.
