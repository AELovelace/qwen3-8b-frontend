# ref\_create

This function creates a reference to a [Variable](../../GML_Overview/Variables_And_Variable_Scope.md) in a struct or instance.

You provide the struct or instance that the variable belongs to, *or* a reference to it, and the name of the variable (**as a string**), *or* reference to a variable that stores the name or index.

For [Arrays](../../GML_Overview/Arrays.md), an index can be provided as the third argument that tells which index to create a reference to.

More complex references can be created. For the full list of possibilities, see the examples.

  The value can be changed through the reference in [The Debug Overlay](../Debugging/The_Debug_Overlay.md).

  You *cannot* create references to [Local Variables](../../GML_Overview/Variables/Local_Variables.md), since they exist only temporarily and cannot be referenced.

 

#### Syntax:

ref\_create(dbgrefOrStruct, dbgrefOrIndex\[, index])

| Argument | Type | Description |
| --- | --- | --- |
| dbgrefOrStruct | [Reference](ref_create.md) or [Struct](../../GML_Overview/Structs.md) | The [struct](../../GML_Overview/Structs.md#struct) or [instance](../Asset_Management/Instances/Instances.md) containing the variable to reference, or a reference to it. [self](../../GML_Overview/Instance_Keywords.md) / [other](../../GML_Overview/Instance_Keywords.md) / [global](../../GML_Overview/Variables/Global_Variables.md) are also accepted. |
| dbgrefOrIndex | [Reference](ref_create.md), [String](../../GML_Overview/Data_Types.md) or [Real](../../GML_Overview/Data_Types.md) | A reference to the variable, the variable [hash](variable_get_hash.md), or the name of the variable **as a string** |
| index | [Real](../../GML_Overview/Data_Types.md) | The index in the array, if what's referenced is an [array](../../GML_Overview/Arrays.md) |

 

#### Returns:

[Reference](ref_create.md)

 

#### Example 1: Basic Reference to an Instance Variable

text \= "This is some text";  

 ref\_to\_text \= ref\_create(self, "text");

The code above first creates an instance variable text in the Create event and then creates a reference to it using ref\_create, that's stored in the variable ref\_to\_text.

 

#### Example 2: Basic Reference to an Array Index

array \= \[1, 2, 3, 4, 5];  

 ref\_to\_index \= ref\_create(self, "array", 2\);

The code above first creates an array array with 5 elements in the instance executing the code. It then creates a reference to index 2 (the third element) using ref\_create. The reference is stored in a new instance variable ref\_to\_index.

 

#### Example 3: Complex Reference

the\_struct \= {a: "text", b: 485};  

 ref\_to\_struct \= ref\_create(self, "the\_struct");  

 ref\_to\_struct\_var \= ref\_create(ref\_to\_struct, "a");

The above code first creates a struct the\_struct in the instance executing the code that has two variables. It then creates a reference to that struct using ref\_create that is then passed as the dbgrefOrStruct parameter to the next call to ref\_create. This last call to ref\_create creates a reference to the struct's variable a and stores it in a variable ref\_to\_struct\_var. The struct itself is passed to the function *indirectly*, using the reference stored earlier in the variable ref\_to\_struct.

 

#### Example 4: Complex Array Reference

array \= \[3, 4, 1, 7, 8, 2];  

 index \= 4;  

 ref\_to\_array \= ref\_create(self, "array");  

 ref\_to\_index \= ref\_create(self, "index");  

 ref\_to\_array\_at\_index \= ref\_create(ref\_to\_array, ref\_to\_index);

The above code creates a reference to an array array where both the first parameter to ref\_create (the array to reference) and the second parameter (serving as the index into the array) are themselves references. This means that if you assign a different value to the variable index later on, the array element indexed by ref\_to\_array\_at\_index also changes to the new value set. If you assign an entirely new array to the instance variable array, ref\_to\_array\_at\_index will reference the element at the same index in that array.
