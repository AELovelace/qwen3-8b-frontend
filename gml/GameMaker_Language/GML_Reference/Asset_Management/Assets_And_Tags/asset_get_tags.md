# asset\_get\_tags

This function retrieves all tags assigned to an asset from [The Asset Browser](../../../../Introduction/The_Asset_Browser.md).

You supply either the asset name (as a string) or its asset handle, and the function will return an [array](../../../GML_Overview/Arrays.md) of tags for that asset. If no tags are found or there is an error (i.e.: the name string given doesn't exist) then the returned array will be empty.

If you supply an asset index number (legacy), then you will need to supply the optional asset type argument (a constant), as assets of different types can have the same index, even though they cannot have the same name or handle. The available asset types are listed in the table below:

 
 

#### Syntax:

asset\_get\_tags(name\_or\_index, \[asset\_type])

| Argument | Type | Description |
| --- | --- | --- |
| name\_or\_index | [String](../../../GML_Overview/Data_Types.md) or [Asset](../../../../The_Asset_Editors/The_Asset_Editors.md) | The name of the asset (a string) or its handle. |
| \[asset\_type] | [Asset Type Constant](asset_get_type.md) |  |

 

#### Returns:

[Array](../../../GML_Overview/Arrays.md)

 

#### Example:

my\_tags \= asset\_get\_tags(object\_get\_name(object\_index));

The above code will retrieve all the tags assigned to the object that the instance running the code has been created from.
