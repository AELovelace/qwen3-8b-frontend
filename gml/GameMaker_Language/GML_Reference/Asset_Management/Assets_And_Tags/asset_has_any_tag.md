# asset\_has\_any\_tag

This function checks if one or more tag strings is assigned to any asset from [The Asset Browser](../../../../Introduction/The_Asset_Browser.md).

You supply either the asset name (as a string) or its asset handle, as well as either a single tag string or an array where each item is a single tag string.

If you supply an asset index number (legacy), then you will need to supply the optional asset type argument (a constant), as assets of different types can have the same index, even though they cannot have the same name. The available asset types are listed in the table below:

 
If the function succeeds and one or more of the tag(s) is present for the asset then it will return true otherwise it will return false. If you need to check for a precise match to any given tag or set of tags, then use the function [asset\_has\_tags()](asset_has_tags.md).

 

#### Syntax:

asset\_has\_any\_tag(name\_or\_index, tags, \[asset\_type])

| Argument | Type | Description |
| --- | --- | --- |
| name\_or\_index | [String](../../../GML_Overview/Data_Types.md) or [Asset](../../../../The_Asset_Editors/The_Asset_Editors.md) | The name of the asset (a string) or its handle. |
| tags | [String](../../../GML_Overview/Data_Types.md) or [Array](../../../GML_Overview/Arrays.md) of Strings | A single asset tag string or an array with various asset tags. |
| \[asset\_type] | [Asset Type Constant](asset_get_type.md) |  |

 

#### Returns:

[Boolean](../../../GML_Overview/Data_Types.md)

 

#### Example:

var \_a \= array\_create(3\);  

 \_a\[0] \= "boss";  

 \_a\[1] \= "main\_boss";  

 \_a\[2] \= "final\_boss";  

  

 if asset\_has\_any\_tag(object\_index, \_a, asset\_object)  

 {  

     instance\_create\_layer(0, 0, "Overlay", obj\_Boss\_Text);  

 }
 

The above code will create an array of tags and then check to see if any of them are applied to the given object, and if they are it will create an instance of another object.
