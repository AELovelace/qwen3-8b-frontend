# array\_create\_ext

This function creates an array of the given size. For each element in the new array, it calls the given callback function, and applies the return value to that element.

Using this function you can initialise the array with values that change depending on the array index.

[Callback function](../../../assets/snippets/Syntax_predicate_general.hts#)

The callback function supplied in the second argument should take 1 argument, which is the index of the current array element. It can return any type of value, which is stored in the array at that index.

#### Syntax:

array\_create\_ext(index)

| Argument | Type | Description |
| --- | --- | --- |
| index | [Real](../../GML_Overview/Data_Types.md) | The current array index |

 

#### Syntax:

array\_create\_ext(size, function)

| Argument | Type | Description |
| --- | --- | --- |
| size | [Real](../../GML_Overview/Data_Types.md) | The size of the array |
| function | [Function](../../GML_Overview/Script_Functions.md) | The callback function used to initialise each entry |

#### Returns:

[Array](../../GML_Overview/Arrays.md)

 

#### Example 1: Basic Use

var \_f \= function(\_index)  

 {  

     return \_index \+ 1;  

 }  

 array \= array\_create\_ext(100, \_f);  

 show\_debug\_message(array);

The above code first creates a temporary function \_f that takes in an index as an argument, and returns that index with 1 added to it.

It then uses array\_create\_ext with the \_f function which creates an array filled with the integer numbers from 1 to 100\.

 

#### Example 2: Array of Structs

create\_point \= function()  

 {  

     return {x: 0, y: 0};  

 }  

 array \= array\_create\_ext(10, create\_point);

The above code first defines a function that returns a simple struct with an x and y variable, each set to 0\. It then creates an array with a call to array\_create\_ext. The previously created function is passed as the callback function and is called for every element, i.e. 10 times. This creates a new struct for every array element.
