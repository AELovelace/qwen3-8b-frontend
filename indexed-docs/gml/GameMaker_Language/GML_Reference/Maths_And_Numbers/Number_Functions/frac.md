# frac

This function returns the fractional part of n, that is, the part behind the decimal dot. It will return *only* the decimals behind the dot of a value (including the sign), so frac(3\.125\) will return 0\.125, frac(\-6\.921\) will return \-0\.921, etc.

 

#### Syntax:

frac(n)

| Argument | Type | Description |
| --- | --- | --- |
| n | [Real](../../../GML_Overview/Data_Types.md) | The number to change |

 

#### Returns:

[Real](../../../GML_Overview/Data_Types.md)

 

#### Example:

val \= frac(3\.4\);

This will set val to 0\.4\.
