# asset\_add\_tags

This function adds one or more tag strings to any asset from [The Asset Browser](../../../../Introduction/The_Asset_Browser.md).

You supply either the asset name (as a string) or its asset handle, as well as either a single tag string or an array where each item is a single tag string.

If you supply an asset index number (legacy), then you will need to supply the optional asset type argument (a constant), as assets of different types can have the same index, even though they cannot have the same name. The available asset types are listed in the table below:

 
If the function succeeds in adding the tag(s) it will return true otherwise it will return false.

 

#### Syntax:

asset\_add\_tags(name\_or\_index, tags, \[asset\_type])

| Argument | Type | Description |
| --- | --- | --- |
| name\_or\_index | [String](../../../GML_Overview/Data_Types.md) or [Asset](../../../../The_Asset_Editors/The_Asset_Editors.md) | The name of the asset (a string) or its handle. |
| tags | [String](../../../GML_Overview/Data_Types.md) or [Array](../../../GML_Overview/Arrays.md) of Strings | A single asset tag string or an array with various asset tags. |
| \[asset\_type] | [Asset Type Constant](asset_get_type.md) |  |

 

#### Returns:

[Boolean](../../../GML_Overview/Data_Types.md)

 

#### Example:

var \_a \= array\_create(3\);  

 \_a\[0] \= "enemy";  

 \_a\[1] \= "all\_levels";  

 \_a\[2] \= "boss";  

asset\_add\_tags(obj\_Enemy\_Boss\_Parent, \_a, asset\_object);
 

The above code will create an array of tags and then add them to the given object.
