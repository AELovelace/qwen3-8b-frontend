# buffer\_save\_ext

This function saves (part of) the contents of a buffer to a file, ready to be read back into memory using the [buffer\_load](buffer_load.md) function.  

The "offset" defines the start position within the buffer for saving (in bytes), and the "size" is the size of the buffer area to be saved from that offset onwards (also in bytes).

 

#### Syntax:

buffer\_save\_ext(buffer, filename, offset, size)

| Argument | Type | Description |
| --- | --- | --- |
| buffer | [Buffer](buffer_create.md) | The buffer to save. |
| filename | [String](../../GML_Overview/Data_Types.md) | The name of the file to save as. |
| offset | [Real](../../GML_Overview/Data_Types.md) | The offset within the buffer to save from (in bytes). |
| size | [Real](../../GML_Overview/Data_Types.md) | The size of the buffer area to save (in bytes). |

 

#### Returns:

N/A

 

#### Example:

buffer\_save\_ext(buff, "Player\_Save.sav", 0, 16384\);

This function saves part of the current contents of the buffer stored in the variable buff to a file.
