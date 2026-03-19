# sprite\_save

This function can be used to save any sub\-image of a sprite to disc, giving it the specified filename. The sprite must have been [added](sprite_add.md) at runtime (you cannot save sprites added through the IDE) and the file must be saved with a \*.png extension.

 
 

#### Syntax:

sprite\_save(ind, subimg, fname)

| Argument | Type | Description |
| --- | --- | --- |
| ind | [Sprite Asset](The_Asset_Editors/Sprites.md) | The index of the sprite to save. |
| subimg | [Real](GameMaker_Language/GML_Overview/Data_Types.md) | The sub\-image of the sprite to save. |
| fname | [String](GameMaker_Language/GML_Overview/Data_Types.md) | The filename for the saved sprite. |

 

#### Returns

N/A

 

#### Example:

var surf, spr\_custom;  

 surf \= surface\_create(32, 32\);  

 surface\_set\_target(surf);  

 draw\_clear\_alpha(c\_black, 0\);  

 draw\_sprite(spr\_Body, 0, 0, 0\);  

 draw\_sprite(spr\_Clothes, 0, 0, 0\);  

 draw\_sprite(spr\_Hair, 0, 0, 0\);  

 spr\_custom \= sprite\_create\_from\_surface(surf, 0, 0, 32, 32, true, true, 16, 16\);  

 surface\_reset\_target();  

 surface\_free(surf);  

 sprite\_save(spr\_custom, 0, "Player\_Custom\_Sprite.png");  

 sprite\_delete(spr\_Custom);

The above code creates a surface and stores its index in the local variable "surf". It then targets that surface, clears it and draws several sprites on top of each other. It creates a new sprite from the composite image drawn on the surface and assigns its index to the local variable "spr\_Custom" before freeing up the memory used by the surface. Finally, the resulting sprite is saved to a file and then removed from memory too.
