# log2

This function returns the logarithm base 2 of the given number, which is the number of 2's that you need to multiply together to get n.

A common example of use in programming would be to calculate the number of bits that are needed to represent a number. To do this we calculate the log2(x) of the number, round it down and add 1 \- for example log2(100\) returns 6\.643856, which rounded down is 6, to which we add one and it gives us 7\. So we need 7 bits to represent 100\. It can also be used for describing exponential growth or decay, and is often called a *binary logarithm*.

 

#### Syntax:

log2(n)

| Argument | Type | Description |
| --- | --- | --- |
| n | [Real](../../../GML_Overview/Data_Types.md) | The input value |

 

#### Returns:

[Real](../../../GML_Overview/Data_Types.md)

 

#### Example:

colourbits \= floor(log2(colour)) \+ 1;

The above code stores the number of bits needed to represent the value stored in the variable colour.
