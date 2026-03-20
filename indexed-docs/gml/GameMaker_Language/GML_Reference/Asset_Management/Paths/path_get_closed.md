# path\_get\_closed

This function can be used to return whether the path is flagged as closed (true) or open (false), i.e. whether the path loops or if it has a definitive beginning and end.

The default for a newly created path is closed (true).

 

#### Syntax:

path\_get\_closed(index)

| Argument | Type | Description |
| --- | --- | --- |
| index | [Path Asset](../../../../The_Asset_Editors/Paths.md) | The index of the path to check. |

 

#### Returns:

[Boolean](../../../GML_Overview/Data_Types.md)

 

#### Example:

state \= path\_get\_closed(pth\_Patrol);

This will set "state" to either true or false depending on the closed state of the path indexed in "pth\_Patrol".
