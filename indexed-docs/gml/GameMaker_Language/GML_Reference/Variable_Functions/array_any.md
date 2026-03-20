# array\_any

This function is used to check if any one element in the given array matches a condition. You check that by passing a [Predicate Function](Array_Functions.md#h) that runs on each element of the given array, and returns true or false.

This function returns true if the predicate function returns true for at least one of the elements in the given array range.

 
 

 
#### Returns:

[Boolean](../../../../GameMaker_Language/GML_Overview/Data_Types.md) (**true** if there is any element in the array for which the predicate returns **true**, **false** if there isn't any)

 

#### Example:

var \_array \=  

 \[  

     "apple",  

     "banana",  

     "coconut",  

     "dragonfruit"  

 ]  

  

 var \_contains\_apple \= array\_any(\_array, function(\_val, \_ind)  

 {  

     return \_val \=\= "apple"  

 });  

  

 show\_debug\_message(\_contains\_apple); // prints 1 (true)
 

This creates an array containing strings of fruit names. We want to check if the array contains "apple" anywhere.

The predicate function \_contains\_apple checks if \_val \=\= "apple" and returns the result. When this is true for any one of the array's elements, [array\_any](array_any.md) returns true.
