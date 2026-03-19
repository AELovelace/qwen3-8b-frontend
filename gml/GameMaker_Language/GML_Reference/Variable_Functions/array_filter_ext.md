# array\_filter\_ext

This function is similar to [array\_filter](array_filter.md), but instead of returning a new array, it modifies the original array that was passed as an argument.

You supply a [Predicate Function](Array_Functions.md#h) which runs for all elements in the array. It should return either true or false based on a condition.

The first element for which the predicate function returns true is written at the index given by offset, others are written to subsequent indices (in the direction given by the sign of the length parameter).

This function returns the new number of valid elements, starting at the given offset position and in the direction set by the length argument. For this function, it's the number of elements for which the predicate returned true, and were written back to the array.

 
 
 
#### Returns:

[Real](../../../../GameMaker_Language/GML_Overview/Data_Types.md) (the number of valid elements in the array)

 

#### Example:

var \_is\_even \= function(\_element, \_index) {  

     return (\_element mod 2\) \=\= 0;  

 }  

  

 var \_values \= \[1, 2, 3, 4, 5, 6, 7, 8, 9];  

 var \_valid\_elements \= array\_filter\_ext(\_values, \_is\_even, \-2, \-infinity);
 

The above code first defines a function \_is\_even that takes element and index parameters and returns true when the element is an even number.

An array values is then initialised with the digits from 1 to 9\.

Finally array\_filter\_ext is called on this array with the predicate function. It takes a starting index of \-2 (the second\-last index) and a length of [\-infinity](../../GML_Overview/Data_Types.md). This will start checking at 8 and go backwards to the beginning of the array.

From there the function finds 4 even numbers (8, 6, 4, 2), so it returns 4 as the new valid number of elements.

Since this function mutates the original array, \_values becomes \[1, 2, 3, 4, **2, 4, 6, 8,** 9], writing the even numbers into the array from the index where it started searching.
