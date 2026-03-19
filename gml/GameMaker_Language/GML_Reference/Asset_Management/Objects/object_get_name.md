# object\_get\_name

This function will return the name *as a string* of the specified object. This name is the one that has been specified for the object in the Asset Browser of the main GameMaker window. Please note that this is *only* a string
 and cannot be used to reference the object directly \- for that you would need the *object index*. You can, however, use this string to get the *object index* using the returned string along with the function [asset\_get\_index()](../Assets_And_Tags/asset_get_index.md).

 

#### Syntax:

object\_get\_name(obj)

| Argument | Type | Description |
| --- | --- | --- |
| obj |  | The index of the object to check. |

 

#### Returns:

 

#### Example:

str \= object\_get\_name(object\_index);

The above code will get the name of the object index for the instance running the code and store the return value in the variable "str".
