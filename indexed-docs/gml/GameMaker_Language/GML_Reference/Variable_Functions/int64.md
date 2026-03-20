# int64

This function will attempt to convert a given value into a signed 64\-bit integer, where the value *must* be either a real, a string, an int64, an int32, or a ptr. Anything else will cause the game to crash with an error message. You can check to see if a variable holds an int64 using the function [is\_int64()](is_int64.md).

 

#### Syntax:

int64(val)

| Argument | Type | Description |
| --- | --- | --- |
| val | [Real](../../GML_Overview/Data_Types.md), [String](../../GML_Overview/Data_Types.md), or [Pointer](../../GML_Overview/Data_Types.md) | The value to convert. |

 

#### Returns:

[int64 (signed 64\-bit integer)](../../GML_Overview/Data_Types.md)

 

#### Example:

steam\_handle \= int64(global.fileReadString);

The above code converts the value held in the global variable to a 64bit integer.
