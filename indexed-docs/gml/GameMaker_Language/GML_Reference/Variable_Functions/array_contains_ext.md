# array\_contains\_ext

This function checks if the given array (or a part of it) contains any or all of the given values.

The matchAll argument determines if *all* values should be present in the array (true) or if *any one* of the values will do (false).

The values array may contain duplicates. When matchAll is enabled, this allows you to check exactly how many occurrences of a value exist in the original array.

  To check if an array not just *contains* a value but rather contains a value *that satisfies a certain condition*, use [array\_any](array_any.md).

 

#### Syntax:

array\_contains\_ext(array, values, \[matchAll], \[offset], \[length])

| Argument | Type | Description |
| --- | --- | --- |
| array | [Array](../../GML_Overview/Arrays.md) | The array in which to look for the values |
| values | [Array](../../GML_Overview/Arrays.md) | An array containing the values to look for. Add a value multiple times with the matchAll argument set to true to require that a value occurs multiple times (see Example 2\). Order isn't taken into account, i.e. the values don't have to occur in the array in the order they're listed here. |
| matchAll | [Boolean](../../GML_Overview/Data_Types.md) | Whether all values should be present in the array (true) or any of the values will do (false). The default is false. |
| offset | [Real](../../GML_Overview/Data_Types.md) | The offset, or starting index, in the array. Defaults to 0\. Setting a negative value will count from the end of the array. The starting index will then be array\_length(array) \+ offset. See: [Offset And Length](Array_Functions.md#offset_and_length) |
| length | [Real](../../GML_Overview/Data_Types.md) | The number of elements to traverse. The default is array\_length() \- 1. A negative value will traverse the array backwards (i.e. in descending order of indices, e.g. 2, 1, 0 instead of 2, 3, 4\). See: [Offset And Length](Array_Functions.md#offset_and_length) |

 

#### Returns:

[Boolean](../../GML_Overview/Data_Types.md)

 

#### Example 1: Check if any of the given values is present in an array

hand \= \["1", "1", "4", "J", "J", "Q", "7", "10", "K", "8", "7", "8", "5"];  

 var \_high\_cards \= \["A", "K", "Q", "J"];  

 var \_any\_high\_cards \= array\_contains\_ext(hand, \_high\_cards);  

 show\_debug\_message(\_any\_high\_cards);

The above code first creates an array hand with 13 values. It then defines another array \_high\_cards that defines which are considered "high" cards. Next the hand array is checked for any of these using array\_contains\_ext and the result is stored in a temporary variable \_any\_high\_cards. Finally a debug message shows the value of the variable \_any\_high\_cards.

 

#### Example 2: Check if all values are present in an array

inputs \= \["left", "right", "left", "left", "up", "down", "right"];  

 var \_required\_inputs \= \["left", "left", "left"];  

 var \_input\_valid \= array\_contains\_ext(inputs, \_required\_inputs, true);  

 show\_debug\_message(\_input\_valid);

The above code creates an array containing a sequence of inputs. Then it creates another array which contains the inputs that make the sequence valid (i.e. having *only* three occurrences of "left"). It then calls array\_contains\_ext to validate the inputs array, stores the result in a variable and prints it to the output log.
