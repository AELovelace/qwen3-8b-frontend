# ds\_map\_find\_value

With this function you can get the value from a specified key. The input values of the function are the (previously created) DS map to use and the key to check for.

  If no such key exists then the function will return undefined. You should always check this using the [is\_undefined()](../../Variable_Functions/is_undefined.md) function.

 

#### Syntax:

ds\_map\_find\_value(id, key)

| Argument | Type | Description |
| --- | --- | --- |
| id | [DS Map ID](GameMaker_Language/GML_Reference/Data_Structures/DS_Maps/ds_map_create.md) | The handle of the map to use. |
| key | [String](GameMaker_Language/GML_Overview/Data_Types.md) | The key to find. |

 

#### Returns:

[Any](GameMaker_Language/GML_Overview/Data_Types.md#variable) or [undefined](GameMaker_Language/GML_Overview/Data_Types.md)

 

#### Example:

amount \= ds\_map\_find\_value(inventory, "food");

Or, using the map [accessor](../../../GML_Overview/Accessors.md) "?":

amount \= inventory\[? "food"];

The above code will get the value of the key "food" and store it in the variable "amount".
