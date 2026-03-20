# path\_get\_kind

This function can be used to find out whether the given path is smooth (true) or not (false).

Paths can be either *smooth* or *straight* (a smooth path calculates a curved path around the defining points, whereas a straight path just goes straight from one point to another).

 

#### Syntax:

path\_get\_kind(index)

| Argument | Type | Description |
| --- | --- | --- |
| index | [Path Asset](../../../../The_Asset_Editors/Paths.md) | The index of the path to check. |

 

#### Returns:

[Boolean](../../../GML_Overview/Data_Types.md)

 

#### Example:

path\_kind \= path\_get\_kind(pth\_Patrol);

This will set the "path\_kind" variable to true or false depending on the kind of path the given path index is.
