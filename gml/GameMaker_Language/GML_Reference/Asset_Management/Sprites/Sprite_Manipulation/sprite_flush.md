# sprite\_flush

This function removes the texture page for the given sprite from texture memory (VRAM). The texture will stay in RAM after being flushed.

You supply the sprite (as defined when creating the sprite) and the texture page it is assigned to will be removed from texture memory. The function will return \-1 if flush is not supported for the chosen asset, or it will return 0 if all worked correctly.

  If the texture page is used elsewhere in the room (by another instance sprite, a background, etc.) you may get a minor performance hit as the page is immediately reloaded, so care should be taken when using this function.

 
 

#### Syntax:

sprite\_flush(ind)

| Argument | Type | Description |
| --- | --- | --- |
| ind | [Sprite Asset](../../../../../The_Asset_Editors/Sprites.md) | The sprite asset to flush |

 

#### Returns:

[Real](../../../../GML_Overview/Data_Types.md) (\-1 or 0\)

 

#### Example:

sprite\_flush(spr\_Player\_Aura);

The above code flushes the sprite spr\_Player\_Aura from memory.
