# path\_get\_length

You can use this function to get the exact length of a path in pixels. this is *not* an approximate length from point to point, but rather an exact length along the shape of the path, even when the path is smooth with
 a high curved precision.

 

#### Syntax:

path\_get\_length(index)

| Argument | Type | Description |
| --- | --- | --- |
| index |  | The index of the path to measure. |

 

#### Returns:

 

#### Example:

path\_len \= path\_get\_length(pth\_AI);

This will set "path\_len" to the total length of the path indexed in "pth\_AI" in pixels.
