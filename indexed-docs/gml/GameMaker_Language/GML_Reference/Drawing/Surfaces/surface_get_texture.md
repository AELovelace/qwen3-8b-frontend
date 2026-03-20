# surface\_get\_texture

This function returns the texture for the surface's texture page. This value can then be used in other draw functions, particularly in general 3D and some of the 2D primitive functions.

This function returns the ID of the texture used by the surface, rather than a pointer to it, as is the case for [sprite\_get\_texture](../../Asset_Management/Sprites/Sprite_Information/sprite_get_texture.md). GameMaker's drawing functions accept both in the same way.

 
 
 

#### Syntax:

surface\_get\_texture(surface\_id)

| Argument | Type | Description |
| --- | --- | --- |
| surface\_id | [Texture](../../Asset_Management/Sprites/Sprite_Information/sprite_get_texture.md) | The surface to get the texture of. |

 

#### Returns:

[Texture](../../Asset_Management/Sprites/Sprite_Information/sprite_get_texture.md) or \-1 if the surface doesn't exist

 

#### Example:

var \_tex \= surface\_get\_texture(surf);  

 draw\_primitive\_begin\_texture(pr\_trianglestrip, \_tex);  

 draw\_vertex\_texture(0, 0, 0, 0\);  

 draw\_vertex\_texture(640, 0, 1, 0\);  

 draw\_vertex\_texture(0, 480, 0, 1\);  

 draw\_vertex\_texture(640, 480, 1, 1\);  

 draw\_primitive\_end();

The above code will draw a 4 vertex triangle strip textured with the texture held in the \_tex variable, which is itself taken from a previously created surface surf.
