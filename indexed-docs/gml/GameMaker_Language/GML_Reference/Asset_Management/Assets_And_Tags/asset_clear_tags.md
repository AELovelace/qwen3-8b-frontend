# asset\_clear\_tags

This function clears all tags present on the given asset from [The Asset Browser](../../../../Introduction/The_Asset_Browser.md) and returns whether any tags were removed.

If the function succeeds in clearing the tags it will return true otherwise it will return false.

You supply either the asset name (as a string) or its asset handle. If you supply an asset index number (legacy), then you will need to supply the optional asset type argument (a constant), as assets of different types can have the same index, even though they cannot have the same name. The available asset types are listed in the table below:

 
 

#### Syntax:

asset\_clear\_tags(name,\[asset\_type])

| Argument | Type | Description |
| --- | --- | --- |
| name\_or\_index | [String](../../../GML_Overview/Data_Types.md) or [Asset](../../../../The_Asset_Editors/The_Asset_Editors.md) | The name of the asset (a string) or its handle. |
| \[asset\_type] | [Asset Type Constant](asset_get_type.md) |  |

 

#### Returns:

[Boolean](../../../GML_Overview/Data_Types.md) (whether any tags were removed)

 

#### Example:

asset\_clear\_tags(obj\_Enemy\_Parent, asset\_object);

The above code will clear all tags from the given object asset.
