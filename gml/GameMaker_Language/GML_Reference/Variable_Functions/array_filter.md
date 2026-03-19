# array\_filter

This function returns a **new** array that is the *filtered* version of the given array (or a range of it).

You supply a [Predicate Function](Array_Functions.md#h) which runs for all elements in the array. It should return either true or false based on a condition.

Elements for which the predicate function returns true are included in the returned array, and ones that get false are ignored.

By default the function checks the whole array. You can optionally supply [Offset And Length](Array_Functions.md#offset_and_length) arguments to check a part of the array, traversing the array forward or backward.

 
  See [array\_copy\_while](array_copy_while.md) which is similar, but stops execution after the first false return of the predicate function.

 
#### Returns:

[Array](../../../../GameMaker_Language/GML_Overview/Arrays.md)

 

#### Example:

function passed\_the\_test(element, index)  

 {  

     return element \>\= 50;  

 }  

  

 scores \= \[0, 15, 4, 78, 96, 65, 49];  

 passed \= array\_filter(scores, passed\_the\_test);
 

The above code first defines a function passed\_the\_test that takes in element and index parameters, which is usual for array predicate functions.

The function returns true if the value of element is greater than or equal to 50, otherwise it returns false.

It then creates an array scores with various values between 0 and 100\. Finally it calls array\_filter on this array and stores the new array in a variable passed.

The passed array would only contain values from the scores array that were greater than or equal to 50, satisfying the condition set in the predicate function.
