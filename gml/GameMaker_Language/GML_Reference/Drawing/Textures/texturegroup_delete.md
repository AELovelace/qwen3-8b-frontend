# texturegroup\_delete

This function deletes a Texture Group that was previously created using [texturegroup\_add](texturegroup_add.md). The name to be specified in this function is the same name that was passed into [texturegroup\_add](texturegroup_add.md) for creating the Texture Group.

The function returns true if the Texture Group was successfully deleted, otherwise it returns false.

  This function is not supported on HTML5\.

 

#### Syntax:

texturegroup\_delete(groupname)

| Argument | Type | Description |
| --- | --- | --- |
| groupname | [String](../../../GML_Overview/Data_Types.md) | The name of the texture group to delete, must have been created with [texturegroup\_add](texturegroup_add.md) |

 

#### Returns:

[Boolean](../../../GML_Overview/Data_Types.md)

 

#### Example:

/// Create event  

 texturegroup\_add("MyTextureGroup", "image.png", \_sprite\_data);  

  

 /// Destroy event  

 texturegroup\_delete("MyTextureGroup");
 

After a Texture Group is created in the Create event (see the full example code on the [texturegroup\_add](texturegroup_add.md) page), this function is used to delete the same Texture Group in the Destroy event. The name that was specified when creating the Texture Group is used to delete it.
