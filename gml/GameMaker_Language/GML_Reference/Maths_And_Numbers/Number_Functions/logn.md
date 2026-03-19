# logn

This function returns the logarithm base n of the given number, which is the number of times that you need to multiply n by itself to get the value.

This function is similar to the [log2](log2.md) and [log10](log10.md) functions, only you stipulate the log base value. For example, logn(5,25\) will return how many 5's we need to multiply to get 25 (which is 2\).

 

#### Syntax:

logn(n, val)

| Argument | Type | Description |
| --- | --- | --- |
| n | [Real](../../../GML_Overview/Data_Types.md) | The log base |
| val | [Real](../../../GML_Overview/Data_Types.md) | The input value |

 

#### Returns:

[Real](../../../GML_Overview/Data_Types.md)

 

#### Example:

logval \= logn(5, num);

The above code gets the log5 of the value stored in num.
