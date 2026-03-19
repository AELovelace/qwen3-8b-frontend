# texture\_prefetch

This function can be used to "prefetch" a texture page or a group of texture pages, i.e.: load them into VRAM when required.

You supply the unique **texture page ID** (as found in the array from [texturegroup\_get\_textures](texturegroup_get_textures.md)) to prefetch a single page, or you can supply a **texture group name** (as defined in the [Texture Group Editor](../../../../Settings/Texture_Groups.md)) to prefetch all the texture pages in the group.

 
 
 

#### Syntax:

texture\_prefetch(tex\_id)

| Argument | Type | Description |
| --- | --- | --- |
| tex\_id | [Texture](../../Asset_Management/Sprites/Sprite_Information/sprite_get_texture.md) or [String](../../../GML_Overview/Data_Types.md) | The texture page pointer *or* a texture group name (a string) |

 

#### Returns:

N/A

 

#### Example:

var \_tex\_array \= texturegroup\_get\_textures( "MainMenu");  

 for (var i \= 0; i \< array\_length(\_tex\_array); \+\+i)  

 {  

     texture\_prefetch(\_tex\_array\[i]);  

 }

The above code will prefetch all the texture pages under the texture group "MainMenu".
