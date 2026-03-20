# path\_get\_name

This function will return the name of the path that is referenced as a string. The name is whatever has been used to define the path in the editor or (if the path has been created through a code function) it will return a string with the format "
 \_newpathXX" where "XX" is the number of the path generated, starting at 0 and incrementing by one every time a new path is created. Please note that this is *only* a
 string and cannot be used to reference the path directly \- for that you would need the *path index ID*. You can, however, use this string to get the *path index ID* using the returned string along
 with the function [asset\_get\_index()](../Assets_And_Tags/asset_get_index.md).

 

#### Syntax:

path\_get\_name(index)

| Argument | Type | Description |
| --- | --- | --- |
| index |  | The index of the path to check. |

 

#### Returns:

 

#### Example:

path\_name \= path\_get\_name(path\_array\[0]);

This will set "path\_name" to the name of the path indexed in the given array at position 0\.
