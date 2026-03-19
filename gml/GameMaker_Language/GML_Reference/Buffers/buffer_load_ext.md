# buffer\_load\_ext

This function loads the buffer data that was previously saved using the [buffer\_save](buffer_save.md) function and related functions into an existing buffer.

You pass the previously created buffer to load into, then the saved buffer file to load, and finally the offset from the start of the buffer (in bytes) that you wish to load the data to.

Please read the [buffer\_load](buffer_load.md) page for platform\-specific notes.

 

#### Syntax:

buffer\_load\_ext(buffer, filename, offset)

| Argument | Type | Description |
| --- | --- | --- |
| buffer | [Buffer](../../../../GameMaker_Language/GML_Reference/Buffers/buffer_create.md) | The buffer to load into. |
| filename | [String](../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The name of the file to load from. |
| offset | [Real](../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The offset within the buffer to load to (in bytes). |

 

#### Returns:

N/A

 

#### Example:

var \_pos \= buffer\_seek(player\_buffer, buffer\_seek\_end, 0\);  

buffer\_load\_ext(player\_buffer, "Data\_Save.sav", \_pos);
 

The above code firsts get the position of the end of the buffer stored in the variable player\_buffer and then loads the data from the given file into that position (note that this example will only work with "grow" or "wrap" buffer types).
