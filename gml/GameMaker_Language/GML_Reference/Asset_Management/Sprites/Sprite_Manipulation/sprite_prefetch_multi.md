# sprite\_prefetch\_multi

This function can be used to prefetch (place into texture memory) a number of texture pages that contain the sprites given. You supply an array populated with the sprite indices (as defined when you created the sprite asset) and the texture pages that they are on will be loaded into memory. Note that the function will return \-1 if prefetch is not supported for the chosen resource or the target platform is HTML5, or it will return 0 if all worked correctly.

 
 
 

#### Syntax:

sprite\_prefetch\_multi(array)

| Argument | Type | Description |
| --- | --- | --- |
| array | [Array](../../../../GML_Overview/Arrays.md) of [Sprite Asset](../../../../../The_Asset_Editors/Sprites.md)s | Array with the sprite indices to fetch |

 

#### Returns:

[Real](../../../../GML_Overview/Data_Types.md) (\-1 or 0\)

 

#### Example:

spr\_a\[0] \= spr\_Player\_Aura1;  

 spr\_a\[1] \= spr\_Player\_Aura2;  

 spr\_a\[2] \= spr\_Player\_Aura3;  

 spr\_a\[3] \= spr\_Player\_Aura4;  

 sprite\_prefetch\_multi(spr\_a);

The above code creates an array where each element holds a sprite index. This array is then used to place those sprite textures into memory.
