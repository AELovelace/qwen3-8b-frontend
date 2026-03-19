# buffer\_save

This function saves the contents of a buffer to a file, ready to be read back into memory using the [buffer\_load](buffer_load.md) function.

 

  On HTML5 the contents of the buffer will be saved as base64 encoded strings when using this function.

 

#### Syntax:

buffer\_save(buffer, filename)

| Argument | Type | Description |
| --- | --- | --- |
| buffer | [Buffer](buffer_create.md) | The buffer to save. |
| filename | [String](../../GML_Overview/Data_Types.md) | The name of the file to save as. |

 

#### Returns:

N/A

 

#### Example:

buffer\_save(buff, "Player\_Save.sav");

The above code saves the current contents of the buffer stored in the variable buff to a file.
