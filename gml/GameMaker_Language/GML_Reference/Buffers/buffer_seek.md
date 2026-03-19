# buffer\_seek

This function moves the seek position of a buffer, setting it relative to the start, end or current seek position (that which was last used when reading or writing data).

The seek position is the offset (in bytes) from the start of the buffer where new values are [written](buffer_write.md), and from where values are [read](buffer_read.md). It also moves automatically when you read from or write to a buffer.

### Usage Notes

- The "offset" value is the offset (in bytes) to add to the given seek position, for example, if the base is relative and the offset is 4, then the buffer position will move along 4 bytes from its current position. Please note the following:
	- You can use negative values for the offset to seek back through the buffer as well as positive values.
	- If the buffer is of the "wrap" type and you offset past the end of the buffer, the seek position will also wrap.
	- If the buffer is not of the "wrap" type, the seek will clamp to the beginning or end of the buffer, even when the offset would take the seek outside of the buffer limits.

The following constants are accepted as the "base" argument for seeking to:

| [Buffer Seek Constant](buffer_seek.md) | |
| --- | --- |
| Constant | Description |
| buffer\_seek\_start | The start of the buffer |
| buffer\_seek\_relative | A position relative to the current read/write position |
| buffer\_seek\_end | The end of the buffer |

 

#### Syntax:

buffer\_seek(buffer, base, offset)

| Argument | Type | Description |
| --- | --- | --- |
| buffer | [Buffer](buffer_create.md) | The buffer to use. |
| base | [Real](../../GML_Overview/Data_Types.md) | The base position to seek. |
| offset | [Real](../../GML_Overview/Data_Types.md) | The data offset value. |

 

#### Returns:

[Real](../../GML_Overview/Data_Types.md) (the new seek position)

 

#### Example:

buffer\_seek(buff, buffer\_seek\_start, 0\);  

 buffer\_write(buff, buffer\_s16, 0\);  

 buffer\_write(buff, buffer\_s16, x);  

 buffer\_write(buff, buffer\_s16, y);

The above code finds the start of the buffer stored in the variable buff then writes a series of signed 16bit integer values to it.
