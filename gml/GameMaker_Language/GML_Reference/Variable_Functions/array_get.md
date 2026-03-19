# array\_get

With this function you can retrieve the value from an index in an array. The function requires you to provide a variable that holds the array and the index to get the value from within that array. Note that if the array index given is out of bounds then the game will crash with an error. This function can also be used for multi\-dimensional arrays, as long as you specify which dimension you want to get when you supply the array index, following this pattern:

// 1D array  

 array\_get(my\_array, 0\);  

 // 2D array  

 array\_get(my\_array\[0], 0\);  

 // 3D array  

 array\_get(my\_array\[0]\[0], 0\);  

 // etc...

 

#### Syntax:

array\_get(variable, index)

| Argument | Type | Description |
| --- | --- | --- |
| variable | [Array](../../GML_Overview/Arrays.md) | The variable that holds the array. |
| index | [Real](../../GML_Overview/Data_Types.md) | The index of the array element to get the value from. |

 

#### Returns:

[Any](../../GML_Overview/Data_Types.md#variable) (Any valid data type that an array can hold)

 

#### Example:

for (var i \= 0; i \< 10; \+\+i)  

 {  

     show\_debug\_message(array\_get(my\_array, i));  

 }

The above code will output the first 10 items of the given to the console.
