# irandom\_range

This function returns a random integer value within the given range (both inclusive).

The function is similar to [random\_range()](random_range.md) only with integer values as the input. You supply the low value for the range as well as the high value, and the function will return a random integer value within (and including) the given range. For example, irandom\_range(10, 35\) will return an integer between 10 and 35 *inclusive*.

As with the [irandom()](irandom.md) function, real numbers can be used, in which case they will be rounded down to the nearest integer, e.g.: irandom\_range(6\.2,9\.9\) will give a value between 6 and 9\.

 
#### Syntax:

irandom\_range(n1, n2\)

| Argument | Type | Description |
| --- | --- | --- |
| n1 | [Real](../../../GML_Overview/Data_Types.md) | The low end of the range from which the random number will be selected. |
| n2 | [Real](../../../GML_Overview/Data_Types.md) | The high end of the range from which the random number will be selected. |

 

#### Returns:

[Real](../../../GML_Overview/Data_Types.md)

 

#### Example:

score \+\= irandom\_range(500, 600\);

This will add an integer value anywhere between 500 and 600 (inclusive) to the total score.
