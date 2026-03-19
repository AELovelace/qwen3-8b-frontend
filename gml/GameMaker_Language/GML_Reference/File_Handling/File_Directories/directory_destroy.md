# directory\_destroy

This function will remove a directory with the given name in the save area.

This function will not work on HTML5 or GX.games as you cannot create or remove directories in the browser local storage.

 
 

#### Syntax:

directory\_destroy(dname)

| Argument | Type | Description |
| --- | --- | --- |
| dname | [String](../../../GML_Overview/Data_Types.md) | The name of the directory to remove. |

 

#### Returns:

N/A

 

#### Example:

if (directory\_exists("DLC"))  

 {  

     directory\_destroy("DLC");  

 }

This will check to see if the specified directory exists in the local data folder and, if it does, it is removed.
