# array\_shuffle

This function returns a **new** array in which the elements of the original array (or a range of it) are randomly reordered.

When [Offset And Length](Array_Functions.md#offset_and_length) are provided, the returned array will have the same number of elements as are in the range of the original array, given by these values.

  See [array\_shuffle\_ext](array_shuffle_ext.md) for the function that changes the original array in place.

 
#### Syntax:

array\_shuffle(array, \[offset], \[length])

| Argument | Type | Description |
| --- | --- | --- |
| array | [Array](../../../../GameMaker_Language/GML_Overview/Arrays.md) | The array to shuffle |
| offset | [Real](../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The offset, or starting index, in the array to start shuffling. Defaults to 0\. Setting a negative value will count from the end of the array. The starting index will then be array\_length(array) \+ offset. See: [Offset And Length](Array_Functions.md#offset_and_length) |
| length | [Real](../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The number of elements to shuffle. Defaults to (array\_length(array) \- 1. See: [Offset And Length](Array_Functions.md#offset_and_length) |

 

#### Returns:

[Array](../../../../GameMaker_Language/GML_Overview/Arrays.md)

 

#### Example:

var \_array \= \["Everyday", "I", "'m", "shuffling"];  

 var \_array\_shuffled \= array\_shuffle(\_array);  

 show\_debug\_message(\_array\_shuffled);

The above code first creates an array \_array with a couple of words in it. It then shuffles the array using array\_shuffle and returns the result as a new array, which is stored in \_array\_shuffled. Finally a debug message shows the contents of the shuffled array.
