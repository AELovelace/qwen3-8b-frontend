# show\_debug\_message\_ext

This function shows a custom debug message in [The Output Window](../../../Introduction/The_Output_Window.md) and [The Debug Overlay](../Debugging/The_Debug_Overlay.md) at runtime.

The syntax of this function is identical to that of the [string\_ext](string_ext.md) function; aside from a single argument it can also take a [Format String](string.md#h) with placeholders and and array with additional arguments to replace the placeholders with.

 
#### Syntax:

show\_debug\_message\_ext(value\_or\_format, values\_array)

| Argument | Type | Description |
| --- | --- | --- |
| value\_or\_format | [Any](../../GML_Overview/Data_Types.md#variable) (if value) or [String](../../GML_Overview/Data_Types.md) (if format) | The value to be turned into a string. |
| values\_array | [Array](../../GML_Overview/Arrays.md) of [Any](../../GML_Overview/Data_Types.md#variable) | An array containing the values to be inserted at the placeholder positions. |

 

#### Returns:

N/A

 

#### Example 1:

show\_debug\_message\_ext("{0} \- {1}", \[1, "First item"]);

This prints a short message to the Output Log with two values inserted as placeholders.

 

#### Example 2:

numbers \= \[59, 23, 656, 8, 54];  

 array\_sort(numbers, true);  

  

 show\_debug\_message\_ext("The three lowest numbers are: {0}, {1} and {2}", numbers);
 

The above code first defines an array with some numbers, and sorts them in an ascending order. It then uses that array in a show\_debug\_message\_ext() to call to insert its first three numbers into a format string, and then print the resulting string to the Output Log.
