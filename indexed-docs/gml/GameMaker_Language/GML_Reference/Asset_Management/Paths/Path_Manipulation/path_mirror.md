# path\_mirror

This function takes all the path points and mirrors them along the vertical axis, **changing the actual path asset**.

Since this function changes the actual path asset it will permanently affect how the path is used by all instances in the game from the moment the function is used until the end of the game. If this is not what you require, then you should use a function like [path\_duplicate](path_duplicate.md) to create a copy of the path first, then call this function on the duplicated asset (don't forget to call [path\_delete](path_delete.md) on the asset when it is no longer required).

#### Syntax:

path\_mirror(index)

| Argument | Type | Description |
| --- | --- | --- |
| index | [Path Asset](../../../../../The_Asset_Editors/Paths.md) | The index of the path to mirror. |

 

#### Returns:

N/A

 

#### Example:

path\_mirror(mypath);

This would mirror the path indexed in the variable mypath along the vertical axis.
