# buffer\_md5

This function takes the input data from (part of) a given buffer and returns the 32\-character hexadecimal MD5 hash that is unique to that data. In this way you can generate a secure key which can be stored and used to check the integrity of the information being sent to (or received from) an external server (for example).

 
When applying this to buffers using this function you must specify the buffer to use, then an offset value (in bytes) for where to begin, and then a size (again in bytes) for the region to be hashed.

 

#### Syntax:

buffer\_md5(buffer, offset, size)

| Argument | Type | Description |
| --- | --- | --- |
| buffer | [Buffer](buffer_create.md) | The buffer to use |
| offset | [Real](../../GML_Overview/Data_Types.md) | The data offset value |
| size | [Real](../../GML_Overview/Data_Types.md) | The size of the buffer |

 

#### Returns:

[String](../../GML_Overview/Data_Types.md)

 

#### Example:

check\_string \= buffer\_md5(buff, 0, buffer\_get\_size(buff));

The above code will create an MD5 hash for the full data stored in the buffer stored in the variable buff, and store the returned hash in the variable check\_string.
