# buffer\_write

This function can be used to write data to a previously created buffer. The data you write must be in agreement with the "type" argument of this function, meaning that you can't try to write a string as an unsigned 16bit integer, for example.

The function will write your given value at the buffer's [current seek position](buffer_tell.md).

The following constants can be used to define the data type:

 
The function will return 0 if it succeeds or one of the following constants in case of failure:

| [Buffer Error Constant](buffer_write.md) | | |
| --- | --- | --- |
| Constant | Description | Value |
| buffer\_error\_general | A general buffer error. | \-1 |
| buffer\_error\_out\_of\_space | The buffer doesn't have enough space for the size of the type being written. | \-2 |
| buffer\_error\_invalid\_type | Attempting to write an invalid type to a buffer. For example, submitting a string value for a buffer\_u16 type or a buffer\_f16 into a "fast" buffer that only takes buffer\_u8 values. | \-4 |

 

#### Syntax:

buffer\_write(buffer, type, value)

| Argument | Type | Description |
| --- | --- | --- |
| buffer | [Buffer](buffer_create.md) | The buffer to write to. |
| type | [Real](../../GML_Overview/Data_Types.md) | The type of data to be written to the buffer (see the list of constants above). |
| value | [Real](../../GML_Overview/Data_Types.md) | The data to write. |

 

#### Returns:

[Real](../../GML_Overview/Data_Types.md) (0 if success) or [Buffer Error Constant](buffer_write.md) (if it fails)

 

#### Example:

buffer\_seek(buff, buffer\_seek\_start, 0\);  

buffer\_write(buff, buffer\_s16, 0\);  

buffer\_write(buff, buffer\_s16, x);  

buffer\_write(buff, buffer\_s16, y);
 

The above code finds the start of the buffer stored in the variable buff then writes a series of signed 16bit integer values to it.
