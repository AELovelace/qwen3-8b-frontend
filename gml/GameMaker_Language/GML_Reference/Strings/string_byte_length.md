# string\_byte\_length

This function returns the number of bytes in a string. Due to their being held as UTF8, this will *not* be equal to the [number of characters](string_length.md) in the string.

 

#### Syntax:

string\_byte\_length(string)

| Argument | Type | Description |
| --- | --- | --- |
| string | [String](../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The string to measure the number of bytes of. |

 

#### Returns:

[Real](../../../../GameMaker_Language/GML_Overview/Data_Types.md)

 

#### Example:

bytesize \= string\_byte\_length("Hello World");

This would set bytesize to the number of bytes in "Hello World".
