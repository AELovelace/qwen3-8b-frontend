# array\_all

This function is used to check if all of the elements in the given array match the same condition. You check that by passing a [Predicate Function](Array_Functions.md#h) that runs on each element of the given array, and returns true or false.

This function returns true if your predicate function returns true for *all* of the elements in the given array range, otherwise it returns false.

 
  

 
#### Returns:

[Boolean](../../../../GameMaker_Language/GML_Overview/Data_Types.md) (whether the function returned **true** for all elements in the array or range)

 

#### Example:

function is\_even(element, index)  

 {  

     return (element mod 2 \=\= 0\);  

 }  

 values \= \[2, 4, 8, 10, 12, 14, 18, 22, 46];  

 var all\_elements\_are\_even \= array\_all(values, is\_even);

The above code first defines a function is\_even that returns true if the value is even.

It then creates an array values and adds some numbers to it.

Finally it calls array\_all on the array and stores the result in a temporary variable all\_elements\_are\_even. As all values in the array are even, all\_elements\_are\_even will be set to true.
