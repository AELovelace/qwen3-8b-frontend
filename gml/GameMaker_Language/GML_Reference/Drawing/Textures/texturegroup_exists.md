# texturegroup\_exists

This function returns whether a texture group with the given name exists.

  This function will return false for texture groups defined in the [Texture Group Manager](../../../../Settings/Texture_Groups.md) which contain graphics that aren't referenced in your game. See **Automatically remove unused assets when compiling** in the [Game Options](../../../../Settings/Game_Options.md).

 

#### Syntax:

texturegroup\_exists(groupname)

| Argument | Type | Description |
| --- | --- | --- |
| groupname | [String](../../../GML_Overview/Data_Types.md) | The name to check |

 

#### Returns:

[Boolean](../../../GML_Overview/Data_Types.md)

 

#### Example:

var \_group\_name \= "MyTextureGroup";  

  

 if (texturegroup\_exists(\_group\_name))  

 {  

     var \_arr\_sprites \= texturegroup\_get\_sprites(\_group\_name);  

     var \_num\_sprites \= array\_length(\_arr\_sprites);  

     show\_debug\_message($"The texture group named \\"{\_group\_name}\\" exists and contains {\_num\_sprites} sprites.");  

 }  

 else  

 {  

     show\_debug\_message($"The texture group named \\"{\_group\_name}\\" does not exist.");  

 }
 

The above code first checks in an if statement if a texture group with the name "MyTextureGroup" exists. If it does, the sprites on the texture group are retrieved using [texturegroup\_get\_sprites](texturegroup_get_sprites.md) and stored in a temporary array. The number of sprites is then obtained by getting the number of items in the array with a call to [array\_length](../../Variable_Functions/array_length.md) and this number is output in a debug message. If the texture group doesn't exist, a different debug message is output.
