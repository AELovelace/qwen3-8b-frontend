# path\_append

With this function you can append one path onto another one, effectively joining them together.

For this to work, both paths must previously exist. In general you would want to use this function on paths created using [path\_add](path_add.md), since if you use it on a path asset, **it will permanently affect the path for instances in the game** from the moment the function is used until the end of the game.

  This will not remove the path being appended from the game. It is still there, only it now has no points in it and if you no longer wish to use it you should remove it with the function [path\_delete](path_delete.md).

 

#### Syntax:

path\_append(index, path)

| Argument | Type | Description |
| --- | --- | --- |
| index | [Path Asset](../../../../../The_Asset_Editors/Paths.md) | The new index of the path. |
| path | [Path Asset](../../../../../The_Asset_Editors/Paths.md) | The index of the path that will be appended to 'index'. |

 

#### Returns:

N/A

 

#### Example:

path\_append(mypath, mppath);  

 path\_delete(mppath);

The above code appends the path data indexed in the variable mppath to the path indexed in the variable mypath and then deletes the mppath from memory.
