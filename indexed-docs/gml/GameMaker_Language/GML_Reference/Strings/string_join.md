# string\_join

This function joins together the string representations of all arguments that are passed to it, inserting the given "delimiter" between each argument. The function returns the joined string.

Arguments that are not strings will have the [string()](string.md) function run on them implicitly. See [Conversion From Non\-String Types](string.md#h1) for information on how those data types are converted.

 

#### Syntax:

string\_join(delimiter, value1 \[, value2, ... max\_val])

| Argument | Type | Description |
| --- | --- | --- |
| delimiter | [String](../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The string to insert between the values |
| value1 | [Any](../../../../GameMaker_Language/GML_Overview/Data_Types.md#variable) | The first value to join |
| \[, value2, ... max\_val] | [Any](../../../../GameMaker_Language/GML_Overview/Data_Types.md#variable) | The other values to join |

 

#### Returns:

[String](../../../../GameMaker_Language/GML_Overview/Data_Types.md)

 

#### Example:

countdown\_message \= string\_join("... ", "Ready", "Set", "Go!");

The above code calls string\_join to create a new string from a few phrases, joined together by the string "... ". The result is stored in a variable named countdown\_message.
