# dtan

This function returns the tangent of an angle in degrees. In a right\-angled triangle the tangent is defined as *tan(val) \= opposite / adjacent*, where val is one of the three angles.

 
  A vast number of values (90, or \-90 for example) will error with this function due to their returning infinity, a graph representation of this would produce *asymptotes* at these values.

 

#### Syntax:

dtan(val)

| Argument | Type | Description |
| --- | --- | --- |
| val | [Real](../../../GML_Overview/Data_Types.md) | The angle (in degrees) to return the tangent of |

 

#### Returns:

[Real](../../../GML_Overview/Data_Types.md)

 

#### Example:

val \= dtan(45\);

This will set val to 1\.
