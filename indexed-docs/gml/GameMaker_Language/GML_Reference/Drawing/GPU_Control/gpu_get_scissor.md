# gpu\_get\_scissor

This function returns the current scissor region as a struct with the following members:

| Variable Name | Data Type | Description |
| --- | --- | --- |
| **x** | [Real](../../../GML_Overview/Data_Types.md) | The X position of the scissor region |
| **y** | [Real](../../../GML_Overview/Data_Types.md) | The Y position of the scissor region |
| **w** | [Real](../../../GML_Overview/Data_Types.md) | The width of the scissor region |
| **h** | [Real](../../../GML_Overview/Data_Types.md) | The height of the scissor region |

 
 

#### Syntax:

gpu\_get\_scissor()

 

#### Returns:

[Struct](../../../GML_Overview/Structs.md)

 

#### Example:

var \_scissor \= gpu\_get\_scissor();  

 gpu\_set\_scissor(200, 200, 600, 600\);  

  

 draw\_self();  

  

 gpu\_set\_scissor(\_scissor);
 

This gets the current scissor region and stores it in a local variable. It then changes the scissor region, draws something, and resets the scissor region to what it was before the gpu\_set\_scissor() call.
