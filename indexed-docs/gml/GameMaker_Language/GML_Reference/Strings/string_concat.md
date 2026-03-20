# string\_concat

This function concatenates (joins together) the string representations of all arguments that are passed to it, and returns the result as a new string.

Arguments that are not strings will have the [string()](string.md) function run on them implicitly. See [Conversion From Non\-String Types](string.md#h1) for information on how those data types are converted.

If you want to join strings with certain characters between them, use [string\_join()](string_join.md).

 

#### Syntax:

string\_concat(value1 \[, value2, ... max\_val])

| Argument | Type | Description |
| --- | --- | --- |
| value1 | [Any](../../../../GameMaker_Language/GML_Overview/Data_Types.md#variable) | The first value to concatenate |
| \[, value2, ... max\_val] | [Any](../../../../GameMaker_Language/GML_Overview/Data_Types.md#variable) | Additional values to concatenate |

 

#### Returns:

[String](../../../../GameMaker_Language/GML_Overview/Data_Types.md)

 

#### Example:

result \= string\_concat("W", "o", "r", "d", "s");

The above code calls string\_concat on a series of letters to make a word. The new string is stored in a variable result.
