# array\_copy\_while

This function creates a **new** array and adds elements of the input array to it *while* (or *as long as*) the predicate function returns true.

The function stops execution as soon as the predicate function returns false. The first element for which the predicate function returns false and any elements that come after it are **not** added to the new array.

  This function is identical to [array\_filter](array_filter.md) with the difference that this function stops execution after the first time the predicate function returns false. array\_filter on the other hand continues to check elements, even after encountering an element for which the predicate function returns false.

 
 

#### Returns:

[Array](../../../../GameMaker_Language/GML_Overview/Arrays.md)

 

#### Example:

array \= \["1", "2", "3", "STOP", "4", "5", "6", "STOP", "7", "8", "9"];  

 array\_up\_to\_stop \= array\_copy\_while(array, function(element, index)  

 {  

     return (element !\= "STOP");  

 }, \-1, \-infinity);

The above code first creates an array array that stores strings containing the first 9 digits, with the string "STOP" in between.

Then the function array\_copy\_while is called on this array, with a predicate function that returns true if the element is **not equal** to the string "STOP".

The offset parameter is set to \-1 and the length to \-[infinity](../../GML_Overview/Data_Types.md). This will start iterating over the values backwards starting at the last array index.

Finally the result is stored in the variable array\_up\_to\_stop, which should only contain "9", "8" and "7", in that order, as the array was traversed in reverse.
