# floor

This function takes any real number and rounds it down to the nearest integer.

This is similar to the [round](round.md) function, but it only rounds *down*, no matter what the decimal value, so floor(5\.99999\) will return 5, as will floor(5\.2\), floor(5\.6457\), etc.

 

#### Syntax:

floor(n)

| Argument | Type | Description |
| --- | --- | --- |
| n | [Real](../../../GML_Overview/Data_Types.md) | The number to floor |

 

#### Returns:

[Real](../../../GML_Overview/Data_Types.md)

 

#### Example:

val \= floor( 3\.9 );

This will set val to 3\.
