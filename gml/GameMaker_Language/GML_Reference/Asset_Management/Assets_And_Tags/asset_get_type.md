# asset\_get\_type

This function gets the type of asset being referenced from its name or handle.

One of the **constants** listed below will be returned.

  On HTML5, passing an asset reference into this function will always return \-1 as HTML5 asset references do not contain the asset type information.

 

#### Syntax:

asset\_get\_type(name\_or\_ref)

| Argument | Type | Description |
| --- | --- | --- |
| name\_or\_ref | [Asset](../../../../The_Asset_Editors/The_Asset_Editors.md) or [String](../../../GML_Overview/Data_Types.md) | The name of or a reference to the game asset to get the type of. |

 

#### Returns:

[Asset Type Constant](asset_get_type.md)

> 

 
 

#### Example:

if (asset\_get\_type("pth\_Path\_" \+ string(global.Game)) \=\= asset\_unknown)  

 {  

     show\_debug\_message("Path doesn't exist!!!");  

 }  

 else  

 {  

     path\_index \= asset\_get\_index("pth\_Path\_" \+ string(global.Game));  

 }

The above code checks a dynamically created asset name to see if the asset is of the correct type. If it is not, then a debug message will be shown, otherwise the asset name is used to assign the asset to the instance.
