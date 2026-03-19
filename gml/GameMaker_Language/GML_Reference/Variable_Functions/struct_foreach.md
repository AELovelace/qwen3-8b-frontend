# struct\_foreach

This function calls the provided callback function on each member of the struct.

  The member name and value are available in the callback function, but cannot be modified through it.

 

[Callback Function](#)

The callback function to pass into this function should take the following arguments: 

#### Syntax:

function(member\_name, value)

| Variable Name | Data Type | Description |
| --- | --- | --- |
| member\_name | [String](../../GML_Overview/Data_Types.md) | The name of the struct member |
| value | [Any](../../GML_Overview/Data_Types.md#variable) | The value assigned to the struct member |

This callback function should not return a value. It simply executes the function on all elements in the given range.

 

#### Syntax:

struct\_foreach(struct, func)

| Argument | Type | Description |
| --- | --- | --- |
| struct | [Struct](../../GML_Overview/Structs.md) | The struct to use |
| func | [Function](../../GML_Overview/Script_Functions.md) or [Method](../../GML_Overview/Method_Variables.md) | The function to execute on each member of the struct |

 

#### Returns:

N/A

 

#### Example:

var \_inventory \= {apples: 17, bananas: 261, oranges: 2, lemons: 5};  

struct\_foreach(\_inventory, function(\_name, \_value)  

 {  

     show\_debug\_message($"{\_name}: {\_value}");  

 });
 

The above code first creates a temporary variable \_inventory that contains a mapping of an inventory item to the number of that item held in the inventory. struct\_foreach is then called to display all the amounts using a debug message.
