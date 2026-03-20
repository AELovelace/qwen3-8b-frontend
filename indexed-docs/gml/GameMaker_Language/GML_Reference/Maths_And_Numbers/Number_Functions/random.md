# random

This function returns a random floating\-point (decimal) number between 0\.0 (inclusive) and the specified upper limit (inclusive).

For example, random(100\) will return a value from 0 to 100\.00, but that value can be 22\.56473! You can also use real numbers and not integers in this function like this \- random(0\.5\), which will return a value between 0 and 0\.500\.

 
#### Syntax:

random(n)

| Argument | Type | Description |
| --- | --- | --- |
| n | [Real](../../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The upper range from which the random number will be selected. |

 

#### Returns:

[Real](../../../../../GameMaker_Language/GML_Overview/Data_Types.md)

 

#### Example:

if (random(10\) \>\= 9\)  

 {  

     score \+\= 100;  

 }

This will produce approximately a one in ten chance of adding 100 to the score.
