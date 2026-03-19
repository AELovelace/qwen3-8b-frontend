# array\_map

This function returns a **new** array that is a modified version of the given array (or a range of it), based on a callback function.

You provide an array, and a [Callback Method](Array_Functions.md#h2), which is called for each element in the given array. The callback function can return any value, which is applied to that index in a new copy of the array.

After the callback is executed for all elements, the modified array (or the affected range of it) is returned as a new array. The original array is **not changed**; for that, see [array\_map\_ext](array_map_ext.md).

[Callback Function](../../../assets/snippets/Syntax_predicate_general.hts#)

The callback function you pass into this function should take the following arguments:

#### Syntax:

array\_map(element, index)

| Argument | Type | Description |
| --- | --- | --- |
| element | [Any](../../../../GameMaker_Language/GML_Overview/Data_Types.md#variable) | The current array element |
| index | [Real](../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The current array index |

This callback function should return a value of [Any](../../../../GameMaker_Language/GML_Overview/Data_Types.md#variable) type that will be applied back to the array element.

 

 
 

#### Returns:

[Array](../../../../GameMaker_Language/GML_Overview/Arrays.md)

 

 
#### Example:

var \_numbers \= \[1, 2, 3, 4, 5];  

  

 var \_double \= function (\_element, \_index)  

 {  

     return \_element \* 2;  

 }  

  

 var \_numbers\_doubled \= array\_map(\_numbers, \_double);
 

The above code creates an array \_numbers with numbers from 1 to 5\.

It creates a function \_double that takes the array element and index, and returns the element multiplied by 2\.

This function is then used in an array\_map call, which returns a modified version of the array with all numbers doubled: \[2, 4, 6, 8, 10].
