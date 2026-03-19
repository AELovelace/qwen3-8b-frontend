# path\_duplicate

This function takes a path and copies it into a new path. The new path is created in the process, and its index is returned to be used in all further calls to use this new path.

 

#### Syntax:

path\_duplicate(index)

| Argument | Type | Description |
| --- | --- | --- |
| index |  | The index of the existing path to duplicate. |

 

#### Returns:

Path Asset

 

#### Example:

mypath \= path\_duplicate(choose(pth\_1, pth\_2, pth\_3, pth\_4\));

The above code chooses one of four path resources and duplicates it, storing the index of the new path in the variable "mypath".
