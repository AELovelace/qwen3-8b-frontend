# variable\_clone

This function clones the value you pass it and returns the new clone.

It clones nested structs and arrays up to a given depth (128 by default), which you can override by providing the optional depth parameter.

To create a shallow copy of an array or struct, pass 0 as the depth parameter. For example:

array \= \[0, 1, 2, \[3, 4, 5], {"a": "a", "b": "b", "c": "c"}];  

 array2 \= variable\_clone(array, 0\);

This creates a copy of the array without duplicating the nested array and struct. Instead, the values at indices 3 and 4 will hold a reference to the *same* array and struct, respectively.

See: [Values and References](../../GML_Overview/Values_And_References.md)

### Usage Notes

- When cloning a struct created using a constructor, the new struct will also be an instance of the original constructor.
- When cloning a struct that contains a method whose "self" exists in the struct being cloned, the clone of the method in the new struct will be rebound to the clone of the original "self" in the new struct, mirroring the relationships of the original.  

  

 If the method's "self" does *not* exist in the struct being cloned, the clone of the method is bound to the original "self".
- The built\-in [Data Structures](../Data_Structures/Data_Structures.md) and [Instances](../Asset_Management/Instances/Instances.md) are *not* cloned; for this type of variable the actual value (data structure reference or instance handle, respectively) is copied.
- Built\-in structs, such as the structs related to sequences and animation curves, cannot be cloned using this function.

 

#### Syntax:

variable\_clone(value, \[depth])

| Argument | Type | Description |
| --- | --- | --- |
| value | [Any](../../GML_Overview/Data_Types.md#variable) | The value to clone |
| depth | [Real](../../GML_Overview/Data_Types.md) | The maximum depth level to clone the variable, in case this is e.g. a nested struct. The default is 128, the maximum possible value. |

 

#### Returns:

[Any](../../GML_Overview/Data_Types.md#variable)

 

#### Example 1: Basic Use

var \_the\_original \= {a: "some text", b: \[1, 2, 3, 4, 5], c: 6};  

 var \_the\_clone \= variable\_clone(\_the\_original);

The above code first defines a temporary struct variable \_the\_original. A clone is then created from this variable using variable\_clone. The new variable is stored in another variable \_the\_clone.

 

#### Example 2: Cloning Methods

the\_struct \=   

 {  

     my\_value: 12,  

     my\_method: function() { show\_debug\_message($"My value is: {my\_value}"); }  

 }  

  

 the\_new\_struct \= variable\_clone(the\_struct);  

 the\_new\_struct.my\_value \= 24;  

  

 the\_struct.my\_method();  

 the\_new\_struct.my\_method();
 

The above code example shows an example where variable\_clone is used to copy a struct that contains a method.

First, a struct with two variables is defined: a variable my\_value that stores the value 12 and a variable my\_method that stores a method bound to this struct. The struct is stored in a variable the\_struct. Next, the struct is cloned, including the method it contains. Since the method is bound to the struct itself, its "self" exists in the struct being cloned and the "self" of its clone is rebound to the clone of the original "self" struct. The new struct's my\_value variable is then set to 24. Finally, the method of each struct is called. Calling the original struct's method outputs 12, calling the cloned struct's method outputs 24.

 

#### Example 3: Clone Depth

array \= \[\["a", "b", "c"], \["d", "e", "f"], {"g": "g", "h": "h", "i": "i"}];  

 copy0 \= variable\_clone(array, 0\);  

 copy1 \= variable\_clone(array, 1\);  

  

 array\[0]\[0] \= "g";  

 array\[0]\[1] \= "m";  

  

 array\[2]\[$"h"] \= "m";  

 array\[2]\[$"i"] \= "l";  

  

 show\_debug\_message(array);  

 show\_debug\_message(copy0\);  

 show\_debug\_message(copy1\);
 

This code shows how to use the optional clone depth parameter.

First, an array of 3 elements is created. The array holds two nested arrays, each holding 3 elements, and one nested struct holding 3 variables. variable\_clone is then called twice, a first time with a depth of 0 and a second time with a depth of 1\. The first call makes a copy of the array itself, though doesn't access the references to the arrays and struct to also make a copy of those (i.e. it stays at depth 0\). The value that is copied is the reference to the array or struct so that, for example, array\[0] and copy0\[0] hold a reference to the original array or struct. The second call to the function also makes a copy of the top\-level array and, since it is passed a depth of 1, it will go one level deeper to access elements that are references and make a copy of those too. So the arrays and struct in the cloned array copy1 will be references to a new array or struct in memory, holding the same values as their counterpart in the original array.

After the calls to the function, a few elements at various positions in the original array array are modified. These changes will show in copy0 since its elements reference the original array or struct. The changes will not show in copy1 as its elements are a copy of the original array.

Finally, the contents of the three arrays are output in an identical number of debug messages.
