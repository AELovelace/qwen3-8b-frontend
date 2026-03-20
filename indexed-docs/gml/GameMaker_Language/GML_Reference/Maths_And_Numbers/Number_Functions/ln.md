# ln

This function returns the natural logarithm of the given value.

The natural logarithm ln(n) is the logarithm with base e (*Euler's number*). It gives the amount of time needed to reach a certain level of continuous growth, where n is the level reached. So if we want to find out how many time units we need to get 20 growth we would use ln(20\) which returns 2\.99 units of time to get that amount of growth.

 

#### Syntax:

ln(n)

 

| Argument | Type | Description |
| --- | --- | --- |
| n | [Real](../../../GML_Overview/Data_Types.md) | The input value |

 

#### Returns:

[Real](../../../GML_Overview/Data_Types.md)

 

#### Example:

alarm\[0] \= ln(age) \* game\_get\_speed(gamespeed\_fps);

The above code uses the natural logarithm of the value stored in the variable age to set an alarm.
