# array\_sort

With this function you can sort an array in ascending order or descending order or using a custom function to define the sort order. The function requires you to provide the array to sort, and then either of the following:

- The constant true or false to indicate an ascending (true) or descending (false) sort order, or
- A custom function to define the sort order

This function will modify the contents of the original array that was supplied. To create a sorted copy, use [array\_copy](array_copy.md) to duplicate the array first, and then pass that into this function.

### Using a custom function

If you use a custom function for sorting, it must take 2 arguments which will receive the values of the current element and the next element respectively. The function should return any of the following values to affect the sort order (where current is the current element and next is the next element):

- 0: if current and next are equal
- \<\= \-1 (negative integer): if current goes before next
- \>\= 1 (positive integer): if current goes after next

  The value returned by your custom function must be an integer. Floating point values less than 1 will be read as 0, so you must use [sign()](../Maths_And_Numbers/Number_Functions/sign.md) or [round()](../Maths_And_Numbers/Number_Functions/round.md) if your function works with floating point values.

  When your custom function returns 0 for a pair of elements (or the pair is equal when using ascending/descending order), the order of that pair may not be preserved as the sorting algorithm used (qsort) is not stable.

If the array contains a set of strings, then the strings will be sorted alphabetically based on the English alphabet when using the default ascending/descending sort type. All other data types will be sorted based on their numerical value, the exact values of which will depend on the data type itself (for example, an array of buffers would be sorted based on the numerical value of their indices).

 

#### Syntax:

array\_sort(variable, sorttype\_or\_function)

| Argument | Type | Description |
| --- | --- | --- |
| variable | [Array](../../GML_Overview/Arrays.md) | The variable that holds the array. |
| sorttype\_or\_function | [Boolean](../../GML_Overview/Data_Types.md) or [Script Function](../../GML_Overview/Script_Functions.md)/[Method](../../GML_Overview/Method_Variables.md) | The sort type (true for ascending or false for descending) or a function reference to use for sorting. |

 

#### Returns:

N/A

 

#### Example:

var \_a \= \[10, 9, 8, 7, 6, 5];  

  

 array\_sort(\_a, function(current, next)  

 {  

     return current \- next;  

 });
 

The above code uses a custom sorting function to sort the array in an ascending order. The sorting function takes the two array elements as current and next and performs a subtraction on them. If current is greater than next, the subtraction results in a positive number which pushes current to be after next, hence putting them in an ascending order.

Here is an extended example:

var \_xx, \_yy, \_a;  

  

 for (var i \= 0; i \< 10; i\+\+)  

 {  

     \_xx \= irandom(room\_width);  

     \_yy \= irandom(room\_height);  

     \_a\[i] \= instance\_create\_layer(\_xx, \_yy, layer, obj\_Bullet);  

 }  

  

 show\_debug\_message(\_a);  

  

 var \_f \= function(inst1, inst2\)  

 {  

     return inst1\.x \- inst2\.x;  

 }  

  

 array\_sort(\_a, \_f);  

 show\_debug\_message(\_a);
 

The above code will create an array of 10 instances placed at random positions within the room. The first debug message will show something like the following:

\[ ref instance 100002,ref instance 100003,ref instance 100004,ref instance 100005,ref instance 100006,ref instance 100007,ref instance 100008,ref instance 100009,ref instance 100010,ref instance 100011 ]

The code then creates a method to be used in the array\_sort function that returns the difference between each of the X positions of the instances in the room. Then the array\_sort function is run using that method, sorting the instances by X from lowest to highest. The output for the array would then look something like this:

\[ ref instance 100009,ref instance 100011,ref instance 100007,ref instance 100002,ref instance 100006,ref instance 100004,ref instance 100008,ref instance 100010,ref instance 100003,ref instance 100005 ]
