# array\_find\_index

This function is used to find the index of the first array element that satisfies a condition.

You supply a [Predicate Function](Array_Functions.md#h) which runs for all elements in the array. It should return either true or false based on a condition.

As soon as the predicate function returns true for an element, the function stops and returns the index of that element.

If the predicate doesn't return true on any element, the function returns \-1.

 
  If you use an offset of \-1 and a negative length (\-infinity), then this function will search backwards from the end of the array, essentially letting you find the last element in the array that satisfies the predicate condition.

 
#### Returns:

[Real](../../../../GameMaker_Language/GML_Overview/Data_Types.md) (the index of the first element found or \-1 if nothing was found)

 

#### Example:

var \_f \= function(\_element, \_index)  

 {  

     return (\_element \> 0\);  

 }  

  

 var \_array \= \[\-1, \-8, \-2, \-4, 0, 3, 8, 7, 5];  

 var \_index \= array\_find\_index(\_array, \_f);
 

The above code first creates a function that takes an array element and its index as the input. The function returns true if the element is greater than 0 and false if not. An array with values is then created.

Finally an index is found using array\_find\_index and stored in a temporary variable index. This variable will contain the value 5, as the first positive value in the array, 3, is at array index 5\.
