# array\_shuffle\_ext

This function shuffles the existing array *in place*, i.e. it modifies (or *mutates*) the existing array.

 
#### Syntax:

array\_shuffle\_ext(array, \[offset], \[length])

| Argument | Type | Description |
| --- | --- | --- |
| array | [Array](../../GML_Overview/Arrays.md) | The array to shuffle |
| offset | [Real](../../GML_Overview/Data_Types.md) | The offset, or starting index, in the array to start shuffling. Defaults to 0\. Setting a negative value will count from the end of the array. The starting index will then be array\_length(array) \+ offset. See: [Offset And Length](Array_Functions.md#offset_and_length) |
| length | [Real](../../GML_Overview/Data_Types.md) | The number of elements to shuffle. Defaults to array\_length(array). See: [Offset And Length](Array_Functions.md#offset_and_length) |

 

#### Returns:

N/A

 

#### Example:

var \_numbers \= \[1, 2, 3, 4, 5, 6, 7, 8, 9, 10];  

array\_shuffle\_ext(\_numbers);  

 show\_debug\_message(\_numbers);
 

The above code first creates an array \_numbers with the numbers from 1 to 10\. It then shuffles the array using array\_shuffle\_ext. This changes the actual values in the array. Finally the shuffled version is shown in a debug message.
