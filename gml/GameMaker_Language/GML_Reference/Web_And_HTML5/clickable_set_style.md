# clickable\_set\_style

This function lets you set the CSS style properties for the given button via the key/value pairs in the provided [DS Map](../Data_Structures/DS_Maps/DS_Maps.md). You need to have previously created the both the button element (using [clickable\_add()](clickable_add.md)) and the DS Map and supply the stored indices to each as arguments.

 

#### Syntax:

clickable\_set\_style(index, map)

| Argument | Type | Description |
| --- | --- | --- |
| index | Clickable ID | The index of the clickable icon to style. |
| map | DS Map ID | The index of the DS Map to set the style from. |

 

#### Returns:

N/A

 

#### Example:

var map \= ds\_map\_create();  

 ds\_map\_add(map, "opacity", "0\.5");  

 clickable\_set\_style(button, map);  

 ds\_map\_destroy();

The above code will change the style of the clickable button with the index stored in the variable "button".
