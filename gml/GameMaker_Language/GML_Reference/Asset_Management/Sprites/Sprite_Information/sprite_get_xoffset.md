# sprite\_get\_xoffset

This function returns the x offset of the origin of the given sprite.

When you define a sprite in [The Sprite Editor](../../../../../The_Asset_Editors/Sprites.md), you need to set the *origin* for that sprite. This is the point at which the sprite will be "attached" or "drawn" when used with an instance. This function returns the relative offset for the x\-axis of the origin based on the upper left corner being the (0, 0\) position, with a \+x being right and a \-x being left of this. The following image illustrates this:

 

#### Syntax:

sprite\_get\_xoffset(index)

| Argument | Type | Description |
| --- | --- | --- |
| index | [Sprite Asset](../../../../../The_Asset_Editors/Sprites.md) | The index of the sprite to find the xoffset of |

 

#### Returns

[Real](../../../../GML_Overview/Data_Types.md)

 

#### Example:

var \_xoffset \= sprite\_get\_xoffset(sprite\_index);  

 if (x \- \_xoffset \< 0\)  

 {  

     x \= \_xoffset;  

 }

The above code will ensure that an instance is maintained within the room based on the sprite (so the sprite is always visible).
