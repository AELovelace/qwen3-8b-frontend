# array\_push

With this function you can push a value (or values) onto the end of an array without having to know the length of the array. The function requires you to provide a variable that holds the array as well as at least *one* value to push, although you can optionally provide further arguments and they will all be pushed onto the array in consecutive order.

 

#### Syntax:

array\_push(variable, value, \[value], \[value], \[etc...])

| Argument | Type | Description |
| --- | --- | --- |
| variable | [Array](../../../../GameMaker_Language/GML_Overview/Arrays.md) | The variable that holds the array. |
| value | [Any](../../../../GameMaker_Language/GML_Overview/Data_Types.md#variable) | The value to push onto the end of the array |
| \[value], \[value], \[etc...] | [Any](../../../../GameMaker_Language/GML_Overview/Data_Types.md#variable) | OPTIONAL Further values to be pushed onto the array |

 

#### Returns:

N/A

 

#### Example:

array\_push(score\_array, obj\_Player1\.scr, obj\_Player2\.scr, obj\_Player3\.scr, obj\_Player4\.scr);

The above code will push four values onto the end of the given array.
