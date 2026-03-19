# irandom

This function returns a random integer (whole number) value. So, for example, to get a random number from 0 to 9 you can use irandom(9\) and it will return a number from 0 to 9 *inclusive*.

Floats can also be used but the upper value after the point will be excluded, so irandom(9\.7\) will return a value from 0 to 9 only. The function has an upper bound of $7fffffffffffffffLL, so care should be taken if using very large numbers.

 
#### Syntax:

irandom(n)

| Argument | Type | Description |
| --- | --- | --- |
| n | [Real](../../../GML_Overview/Data_Types.md) | The upper range from which the random number will be selected. |

 

#### Returns:

[Real](../../../GML_Overview/Data_Types.md)

 

#### Example:

if (irandom(9\) \=\= 1\)  

 {  

     score \+\= 100;  

 }

This will produce a one in ten (since 0 is included) chance of adding 100 to the score.
