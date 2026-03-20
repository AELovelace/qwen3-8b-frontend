# sprite\_prefetch

This function can be used to prefetch (place into texture memory) a texture page with the given sprite. You supply the sprite index as defined when you created the sprite asset, and the texture page it is on will be loaded into memory. Note that the function will return \-1 if prefetch is not supported for the chosen resource or the target platform is HTML5, or it will return 0 if all worked correctly.

 
 
 

#### Syntax:

sprite\_prefetch(ind)

| Argument | Type | Description |
| --- | --- | --- |
| ind | [Sprite Asset](../../../../../The_Asset_Editors/Sprites.md) | The sprite index to fetch |

 

#### Returns:

[Real](../../../../GML_Overview/Data_Types.md) (\-1 or 0\)

 

#### Example:

sprite\_prefetch(spr\_Player\_Aura);

The above code will place the referenced sprite into texture memory ready for use.
