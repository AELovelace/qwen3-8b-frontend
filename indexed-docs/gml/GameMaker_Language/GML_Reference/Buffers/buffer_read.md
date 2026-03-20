# buffer\_read

This function reads a piece of data of the given type from the given buffer at the buffer's current [seek position](buffer_seek.md).

After the function has executed the seek position is advanced by the number of bytes read. The next buffer\_read will be done at this new position and will read the next byte(s) of data.

Since the function only reads the contents starting from the buffer's current [seek position](buffer_seek.md), you must ensure this is set correctly before calling the function \- otherwise, you will get either incorrect results or nothing at all being returned.

  You can use [buffer\_peek](buffer_peek.md) to get a value anywhere in the buffer without changing the seek position.

The return value depends on the type of data that you are reading, which can be one of the following constants:

 
If the function succeeds, it will return a value of the given type. If it fails, however, it will cause a [runner error](../../../Additional_Information/Errors/Runner_Errors.md).

  Using the incorrect data type for the data being read will result in erroneous values being returned.

  Reading a buffer\_s32 or buffer\_u32 on HTML5 returns the value as a [Real](../../GML_Overview/Data_Types.md), which is a 64\-bit double, as int32 is not supported on that platform.

 

#### Syntax:

buffer\_read(buffer, type)

| Argument | Type | Description |
| --- | --- | --- |
| buffer | [Buffer](buffer_create.md) | The buffer to read from. |
| type | [Buffer Data Type Constant](buffer_write.md) | The type of data to be read from the buffer (see the list of constants above). |

 

#### Returns:

[Real](../../GML_Overview/Data_Types.md), [Boolean](../../GML_Overview/Data_Types.md) or [String](../../GML_Overview/Data_Types.md)

 

#### Example:

buffer \= buffer\_create(10240, buffer\_grow, 1\);  

  

 // buffer\_seek(buffer, buffer\_seek\_start, 0\);  

 buffer\_write(buffer, buffer\_string, "Hello World");  

  

 buffer\_seek(buffer, buffer\_seek\_start, 0\);  

 result \= buffer\_read(buffer, buffer\_string);  

  

 show\_debug\_message("Result \= " \+ result);
 

The above code creates a buffer, writes a string to it and reads it back.

First a new grow buffer with an initial size of 10240 bytes is created using [buffer\_create](buffer_create.md). At this point you can explicitly call [buffer\_seek](buffer_seek.md) to set the seek position to 0, but this isn't necessary since a newly created buffer's seek position is 0\. Next the string "Hello World" is written to the buffer with a call to [buffer\_write](buffer_write.md). This advances the seek position by 12 bytes: 11 bytes for the characters of the string followed by a final null byte. After this, the string is read back from the buffer. To read the correct data, the seek position is first set back to 0 with a call to [buffer\_seek](buffer_seek.md). The data is then read into a variable result using [buffer\_read](buffer_read.md), which is shown in a debug message.
