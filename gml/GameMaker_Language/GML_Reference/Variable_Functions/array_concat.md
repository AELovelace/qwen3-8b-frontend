# array\_concat

This function takes multiple arrays as arguments, joins them together (in the order of the arguments), and returns the joined array.

 

#### Syntax:

array\_concat(array0, array1, \[array2, ... array\_n])

| Argument | Type | Description |
| --- | --- | --- |
| array0 | [Array](../../GML_Overview/Arrays.md) | The first array to concatenate |
| array1 | [Array](../../GML_Overview/Arrays.md) | The second array to concatenate |
| \[array2, ... array\_n] | [Array](../../GML_Overview/Arrays.md) | Additional arrays to concatenate (one array per argument) |

 

#### Returns:

[Array](../../GML_Overview/Arrays.md) (new array with all arrays concatenated)

 

#### Example:

array\_1 \= \[1, 2, 3];  

 array\_2 \= \[4, 5, 6];  

 array\_3 \= \[7, 8, 9];  

 new\_array \= array\_concat(array\_1, array\_2, array\_3\);

The above code first creates three arrays: array\_1, array\_2 and array\_3. It then joins the arrays together using array\_concat and stores the result in new\_array.
