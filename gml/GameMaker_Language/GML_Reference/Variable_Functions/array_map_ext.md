# array\_map\_ext

This function is similar to [array\_map](array_map.md), but instead of returning a new array, it modifies the original array that was passed as an argument.

You supply a [Callback Function](Array_Functions.md#h2) which runs for all elements in the array. It can return any value which is applied back to the original array, starting at the index given by offset, in the direction given by the sign of the length parameter.

This function returns the new number of valid elements, starting at the given offset position and in the direction set by the length argument. For this function, it's the number of elements modified in the given range.

[Callback Function](../../../assets/snippets/Syntax_predicate_general.hts#)

The callback function you pass into this function should take the following arguments:

#### Syntax:

array\_map\_ext(element, index)

| Argument | Type | Description |
| --- | --- | --- |
| element | [Any](../../../../GameMaker_Language/GML_Overview/Data_Types.md#variable) | The current array element |
| index | [Real](../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The current array index |

This callback function should return a value of [Any](../../../../GameMaker_Language/GML_Overview/Data_Types.md#variable) type that will be applied back to the array element.

 
 

 
 

#### Returns:

[Real](../../../../GameMaker_Language/GML_Overview/Data_Types.md) (the number of valid elements in the array)

 

 
#### Example:

var \_values \= \[7, 4, 11, 9, 12, 21, 17, 1, 2, 3];  

 elements \= array\_map\_ext(\_values, sqr, 2, 5\);

The above code first creates an array values with a set of numbers. It then applies the built\-in [sqr](../Maths_And_Numbers/Number_Functions/sqr.md) function to a range of the array using array\_map\_ext.

After the function has executed the array values will hold in indices 2 to 6 the square of the values that were originally there.
