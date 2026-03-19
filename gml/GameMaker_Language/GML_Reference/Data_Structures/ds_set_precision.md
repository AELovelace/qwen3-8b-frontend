# ds\_set\_precision

This function sets the precision value to be used by the data structure functions for comparing values.

When comparing values, for example when searching in a map or sorting a list, GameMaker must decide when two values are equal. For strings and integer values this is clear but for real numbers, due to floating point round\-off errors, seemingly equal numbers can easily become unequal. For example, it's possible that (5 / 3\) \* 3 will *not* be equal to 5! To help avoid this, a precision value is used on all real number functions, and when the *difference between two numbers is smaller* than this precision they are considered equal. The default precision of 0\.0000001 is used for all data structure functions unless changed by this function.

  This precision is used in all data structures but not in other comparisons in GML!

 

#### Syntax:

ds\_set\_precision(prec)

| Argument | Type | Description |
| --- | --- | --- |
| prec | [Real](../../GML_Overview/Data_Types.md) | The precision value (default 0\.0000001) |

 

#### Returns:

N/A

 

#### Example:

ds\_set\_precision(0\.0001\);

The above code will change the default precision setting for all data structure functions.
