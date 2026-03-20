# string\_concat\_ext

This function concatenates (joins together) the string representations of all elements in the given array, and returns the result as a new string.

Values that are not strings will have the [string()](string.md) function run on them implicitly. See [Conversion From Non\-String Types](string.md#h1) for information on how those data types are converted.

 

#### Syntax:

string\_concat\_ext(values\_array, \[offset], \[length])

| Argument | Type | Description |
| --- | --- | --- |
| values\_array | [Array](../../../../GameMaker_Language/GML_Overview/Arrays.md) | The array of values to concatenate |
| offset | [Real](../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The offset, or starting index, in the array to start concatenating elements. Setting a negative value will count from the end of the array. The starting index will then be array\_length(array) \+ offset. See: [Offset And Length](../Variable_Functions/Array_Functions.md#offset_and_length) |
| length | [Real](../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The number of array elements to concatenate, starting at the offset. A negative value will traverse the array backwards (i.e. in descending order of indices, e.g. 2, 1, 0 instead of 2, 3, 4\). See: [Offset And Length](../Variable_Functions/Array_Functions.md#offset_and_length) |

 

#### Returns:

[String](../../../../GameMaker_Language/GML_Overview/Data_Types.md)

 

#### Example:

var \_some\_letters \= \["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"];  

 var \_concat \= string\_concat\_ext(\_some\_letters, \-5, \-3\);

The above code first creates an array with the first ten letters of the alphabet and stores it in a temporary variable \_some\_letters. It then calls string\_concat\_ext on this array with an offset (starting position) of \-5 (at the position of the letter "f") and a length of \-3 (3 elements going from right to left).
