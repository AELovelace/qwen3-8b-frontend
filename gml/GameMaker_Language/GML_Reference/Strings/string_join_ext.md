# string\_join\_ext

This function joins together the string representations of all values in the given array (or part of the array), inserting the given "delimiter" between each value. The function returns the joined string.

Values that are not strings will have the [string()](string.md) function run on them implicitly. See [Conversion From Non\-String Types](string.md#h1) for information on how those data types are converted.

 

#### Syntax:

string\_join\_ext(delimiter, values\_array, \[offset], \[length])

| Argument | Type | Description |
| --- | --- | --- |
| delimiter | [String](../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The string to insert between the values |
| values\_array | [Array](../../../../GameMaker_Language/GML_Overview/Arrays.md) | The array containing the values to join together |
| offset | [Real](../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The offset, or starting index, in the array to start joining elements. Setting a negative value will count from the end of the array. The starting index will then be array\_length(array) \+ offset. See: [Offset And Length](../Variable_Functions/Array_Functions.md#offset_and_length) |
| length | [Real](../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The number of array elements to concatenate, starting at the offset. A negative value will traverse the array backwards (i.e. in descending order of indices, e.g. 2, 1, 0 instead of 2, 3, 4\). See: [Offset And Length](../Variable_Functions/Array_Functions.md#offset_and_length) |

 

#### Returns:

[String](../../../../GameMaker_Language/GML_Overview/Data_Types.md)

 

#### Example 1:

var \_words \= string\_join\_ext(" ", \["This", "example", "joins", "words"]);

The above code joins the words in the [array](../../GML_Overview/Arrays.md) into a single string using a space as the delimiter.

 

#### Example 2:

var \_buffer \= buffer\_create(1, buffer\_grow, 1\);  

 var \_text\_lines \= \["This", "file", "will", "have", "multiple", "lines"];  

 var \_file\_contents \= string\_join\_ext("\\r\\n", \_text\_lines);  

 buffer\_write(\_buffer, buffer\_text, \_file\_contents);  

 buffer\_save(\_buffer, save\_dir \+ "/" \+ "text.txt");  

 buffer\_delete(\_buffer);

The above code first creates a grow [buffer](../Buffers/buffer_create.md) and assigns it to a temporary variable \_buffer. It then creates an array with a number of elements and stores that in another variable \_text\_lines. It then calls string\_join\_ext on the array with a separator "\\r\\n", which results in new lines between all the given strings.

It writes the resulting string to the buffer as a buffer\_text value and then saves the contents of the buffer to a file named "text.txt" in a directory save\_dir. Finally it deletes the buffer to prevent memory leaks.
