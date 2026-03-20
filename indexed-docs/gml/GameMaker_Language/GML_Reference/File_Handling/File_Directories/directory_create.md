# directory\_create

This function creates a directory with the given name in the save area.

This function will not work on HTML5 or GX.games as you cannot create or remove directories in the browser local storage.

 
 

#### Syntax:

directory\_create(dname)

| Argument | Type | Description |
| --- | --- | --- |
| dname | [String](../../../GML_Overview/Data_Types.md) | The name of the directory to create. |

 

#### Returns:

N/A

 

#### Example:

if (!directory\_exists("Games"))  

 {  

     directory\_create("Games");  

 }

This will check to see if the specified directory exists in the local data folder and, if it does not, it creates it for you.
