# array\_create

With this function you can create an array of the given size.

You tell the function the length of the array to create, and it will return the "handle" for the array which you can then assign to a variable.

Arrays created in this way will have each entry initialised to 0 unless you specify an (optional) initialisation value. If you do supply the extra value for initialising the array, then all indices within the new array will be set to that instead of 0, but note that the function will have a greater performance overhead in this case.

  If the initialisation value is a reference (e.g. a struct or an array), every array element will hold this same reference and therefore reference the same thing in memory due to the way GameMaker handles [Values and References](../../GML_Overview/Values_And_References.md). To initialise each entry with a unique copy of this value instead of a reference, you can use a function with [array\_create\_ext](array_create_ext.md).

#### Syntax:

array\_create(size, \[value])

| Argument | Type | Description |
| --- | --- | --- |
| size | [Real](../../GML_Overview/Data_Types.md) | The size of the array to create. |
| value | [Any](../../GML_Overview/Data_Types.md#variable) | The value to use to initialise all array indices. |

 

#### Returns:

[Array](../../GML_Overview/Arrays.md)

 

#### Example 1: Basic Use

instance\_array \= array\_create(100, noone);

The above code will create a new array of 100 entries, each one set to the keyword [noone](../../GML_Overview/Instance Keywords/noone.md), and then assign it to a variable instance\_array.

 

#### Example 2: Creating a 2D Array With all Elements Initialised to a Simple Value

the\_array \= array\_create(100\);  

  

 var i \= 0;  

 repeat(100\)  

 {  

     the\_array\[i\+\+] \= array\_create(100, "the\_value");  

 }
 

The above code creates a 2D array and initialises all elements to a simple value different from 0\.

First, a 1D array of 100 elements is created with a first call to array\_create. This array is assigned to a variable the\_array. Next, in a [repeat](../../GML_Overview/Language_Features/repeat.md) loop every array element is assigned a value that is a new array, also created with array\_create. After the code has executed the variable the\_array holds a 100x100 2D array in which every element is set to the string "the\_value".

Note that the following line of code:

the\_array \= array\_create(100, array\_create(100, "the\_value"));

does *not* create a proper 100x100 2D array with 10000 unique elements. Instead, this code creates an array of 100 elements, where each of the elements [references](../../GML_Overview/Values_And_References.md "Values and References") the array passed as the initialisation value. Because of this, assigning a different value to, e.g., the\_array\[2]\[25] also changes the\_array\[0]\[25], the\_array\[1]\[25], the\_array\[3]\[25] and so on.
