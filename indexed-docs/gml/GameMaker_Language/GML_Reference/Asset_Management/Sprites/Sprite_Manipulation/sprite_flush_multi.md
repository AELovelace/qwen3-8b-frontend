# sprite\_flush\_multi

This function removes any number of texture pages for the given sprites from texture memory (VRAM).

You supply the sprites as an array and the texture pages they are assigned to will be removed from texture memory. The function will return \-1 if flush is not supported for the chosen assets, or it will return 0 if all worked correctly.

  If one of the texture pages is used elsewhere in the room (by another instance sprite, background, etc.) you may get a minor performance hit as the page is immediately reloaded back into memory again, so care should be taken when using this function.

 
 

#### Syntax:

sprite\_flush\_multi(array)

| Argument | Type | Description |
| --- | --- | --- |
| array | [Array](../../../../GML_Overview/Arrays.md) | Array with the sprites to flush |

 

#### Returns:

[Real](../../../../GML_Overview/Data_Types.md) (\-1 or 0\)

 

#### Example:

spr\_a\[0] \= spr\_Player\_Aura1;  

 spr\_a\[1] \= spr\_Player\_Aura2;  

 spr\_a\[2] \= spr\_Player\_Aura3;  

 spr\_a\[3] \= spr\_Player\_Aura4;  

sprite\_flush\_multi(spr\_a);
 

The above code creates an array where each element holds a sprite index. This array is then used to clear those sprites' textures from memory.
