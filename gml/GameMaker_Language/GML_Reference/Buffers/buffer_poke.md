# buffer\_poke

With this function you can write data into a buffer at the specified offset, without changing the [seek position](buffer_seek.md). This is different from [buffer\_write](buffer_write.md), which uses the [current seek position](buffer_tell.md) as the offset and advances that with the amount of bytes written.

You supply the function with a buffer, and then the offset position from the buffer start (in bytes) within that buffer to write to, as well as the data type and the value to be written.

 

#### Syntax:

buffer\_poke(buffer, offset, type, value)

| Argument | Type | Description |
| --- | --- | --- |
| buffer | [Buffer](buffer_create.md) | The buffer to use. |
| offset | [Real](../../GML_Overview/Data_Types.md) | The offset position (in bytes) within the buffer to write the given data to. |
| type | [Buffer Data Type Constant](buffer_write.md) | The type of data that is to be written to the buffer (see the list of constants [here](buffer_write.md)). |
| value | [Any](../../GML_Overview/Data_Types.md#variable) | The data to write to the buffer at the given offset, in accordance with the type specified. |

 

#### Returns:

N/A

 

#### Example:

buffer\_poke(buff, 3, buffer\_u8, colour\_get\_blue(image\_blend));

The above code will add the blue component value of the calling instance's [image\_blend](../Asset_Management/Sprites/Sprite_Instance_Variables/image_blend.md) colour into the buffer stored in the variable buff, at the third position in the buffer as an unsigned 8bit value.
