# buffer\_exists

This function checks whether the given buffer exists in memory or not. If it does, the function will return true, otherwise it will return false.

 

#### Syntax:

buffer\_exists(buffer)

| Argument | Type | Description |
| --- | --- | --- |
| buffer | [Buffer](buffer_create.md) | The buffer to check. |

 

#### Returns:

[Boolean](../../GML_Overview/Data_Types.md)

 

#### Example:

if (buffer\_exists(buff))  

 {  

     buffer\_delete(buff);  

 }

The above code checks to see if the variable buff holds a buffer and if it does, the buffer is deleted.
