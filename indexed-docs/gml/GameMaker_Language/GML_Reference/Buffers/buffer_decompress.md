# buffer\_decompress

This function returns a new buffer with the decompressed data of a buffer that stores data using [zlib compression](https://en.wikipedia.org/wiki/Zlib).

You supply the buffer to decompress, and the function will return a new buffer that contains the uncompressed data. If the decompression failed (for example, you supplied a buffer that wasn't compressed) then the function will instead return an invalid handle (\-1).

 

#### Syntax:

buffer\_decompress(buffer)

| Argument | Type | Description |
| --- | --- | --- |
| buffer | [Buffer](buffer_create.md) | The index of the buffer to decompress. |

 

#### Returns:

[Buffer](buffer_create.md) (or an invalid buffer handle \-1 in case the buffer couldn't be decompressed)

 

#### Example:

var \_cmpBuff \= buffer\_load("Player\_Save.sav");  

 var \_srcBuff \= buffer\_decompress(\_cmpBuff);  

 global.DataString \= buffer\_read(\_srcBuff, buffer\_string);

The above code first loads a saved buffer, then decompresses it and finally reads the string data from the decompressed buffer into a global variable.
