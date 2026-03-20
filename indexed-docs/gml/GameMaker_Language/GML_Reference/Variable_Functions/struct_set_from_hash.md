# struct\_set\_from\_hash

This function sets the value of the struct member referred to by the given hash, returned by an earlier call to [variable\_get\_hash](variable_get_hash.md).

 
 

#### Syntax:

struct\_set\_from\_hash(struct, hash, val)

| Argument | Type | Description |
| --- | --- | --- |
| struct | [Struct](../../GML_Overview/Structs.md) | The struct reference to set |
| hash | [Real](../../GML_Overview/Data_Types.md) | The hash of the variable to set (as returned by [variable\_get\_hash](variable_get_hash.md)) |
| val | [Any](../../GML_Overview/Data_Types.md#variable) | The value to assign to the struct variable |

 

#### Returns:

N/A

 

#### Example:

point \= {x: 200, y: 100};  

 hash\_x \= variable\_get\_hash("x");  

 repeat(1000\)  

 {  

     struct\_set\_from\_hash(data, hash\_x, random(room\_width));  

 }

The above code first creates a struct point with an x and y variable in it. Next, the hash for the variable name "x" is then retrieved using [variable\_get\_hash](variable_get_hash.md). After that, a repeat loop is executed a total of 1000 times. Every iteration of the repeat loop assigns a new random value to the point's x coordinate. This is done using struct\_set\_from\_hash to optimise this operation.
