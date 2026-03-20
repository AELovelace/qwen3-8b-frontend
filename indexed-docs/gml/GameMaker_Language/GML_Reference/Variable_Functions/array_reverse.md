# array\_reverse

This function returns a **new** array with all the elements from the given array (or a range of it) in a reversed order.

You can also reverse only a part of the array by supplying [Offset And Length](Array_Functions.md#offset_and_length) values. In this case the returned array will have a length corresponding to the range given by these values (e.g. if offset and length refer to a range of 5 elements then the new array will contain 5 elements).

 

#### Syntax:

array\_reverse(array, \[offset], \[length])

| Argument | Type | Description |
| --- | --- | --- |
| array | [Array](../../../../GameMaker_Language/GML_Overview/Arrays.md) | The array to reverse |
| offset | [Real](../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The offset, or the starting index, in the array. Setting a negative value will count from the end of the array. The starting index will then be array\_length(array) \+ offset. See: [Offset And Length](Array_Functions.md#offset_and_length) |
| length | [Real](../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The number of elements to traverse. A negative value will traverse the array backwards (i.e. in descending order of indices, e.g. 2 \> 1 \> 0 instead of 0 \> 1 \> 2\). See: [Offset And Length](Array_Functions.md#offset_and_length) |

 

#### Returns:

[Array](../../../../GameMaker_Language/GML_Overview/Arrays.md)

 

#### Example:

countdown \= \[5, 4, 3, 2, 1, 0];  

  

 countdown\_reverse \= array\_reverse(countdown);
 

The above code creates an array countdown. It then creates an array countdown\_reverse with the same elements but reversed.
