# string\_ext

This function creates a new string, allowing you to insert placeholders in the main "format string", and to specify an array containing the values to be inserted into those placeholders.

The first argument is a [Format String](string.md#h) and the second argument is an array containing values to be inserted into the format string.

## Format String

For information on format strings, see: [string()](string.md)

This function works in a similar manner, but instead of the values being passed as separate arguments, they're passed as an array in the second argument.

 
 

#### Syntax:

string\_ext(value\_or\_format, values)

| Argument | Type | Description |
| --- | --- | --- |
| value\_or\_format | [Any](../../GML_Overview/Data_Types.md#variable) (if value) or [String](../../GML_Overview/Data_Types.md) (if format) | The value to be turned into a string. |
| values | [Array](../../GML_Overview/Arrays.md) | An array of values to be inserted at the placeholder positions. |

 

#### Returns:

[String](../../GML_Overview/Data_Types.md)

 

#### Example:

numbers \= \[59, 23, 656, 8, 54];  

 array\_sort(numbers, true);  

  

 var \_str \= string\_ext("The three lowest numbers are: {0}, {1} and {2}", numbers);
 

The above code first defines an array with some numbers, and sorts them in an ascending order. It then uses that array in a string\_ext() to call to insert its first three numbers into a format string.
