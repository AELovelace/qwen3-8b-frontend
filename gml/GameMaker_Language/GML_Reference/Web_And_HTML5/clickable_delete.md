# clickable\_delete

This function must be used to remove a clickable icon previously created with [clickable\_add()](clickable_add.md) from the game window.

 

#### Syntax:

clickable\_delete(index)

| Argument | Type | Description |
| --- | --- | --- |
| index | Clickable ID | Index of the clickable icon to remove. |

 

#### Returns:

N/A

 

#### Example:

if (clickable\_exists(global.Help\_Icon))   

 {  

     clickable\_delete(global.Help\_Icon);  

 }

The above code removes the clickable icon indexed in the global variable "Help\_Icon" from the game window, if it exists.
