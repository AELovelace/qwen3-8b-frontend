# skeleton\_attachment\_replace

This function replaces an existing custom attachment on the current instance's skeletal animation sprite with another one.

The change to the attachment will be visible in all [Slots](../Slots/Slots.md) that have the attachment assigned.

 

#### Syntax:

skeleton\_attachment\_replace(name, sprite, ind, xorigin, yorigin, xscale, yscale, rot)

| Argument | Type | Description |
| --- | --- | --- |
| name | [String](../../../../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The name of the attachment to replace |
| sprite | [Sprite Asset](../../../../../../../The_Asset_Editors/Sprites.md) | The index of the sprite asset to use for the attachment |
| ind | [Real](../../../../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The image\_index of the sprite to use |
| xorigin | [Real](../../../../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The x origin to use for the image. The sprite's origin is ignored. |
| yorigin | [Real](../../../../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The y origin to use for the image. The sprite's origin is ignored. |
| xscale | [Real](../../../../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The horizontal scale factor of the image |
| yscale | [Real](../../../../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The vertical scale factor of the image |
| rot | [Real](../../../../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The rotation of the image. This is *added* to the bone's rotation. |

 

#### Returns:

[Real](../../../../../../../GameMaker_Language/GML_Overview/Data_Types.md) (1 if successful, \-1 if not)

 

#### Example:

if (skeleton\_attachment\_exists("weapon\_attachment"))   

 {  

     skeleton\_attachment\_replace("weapon\_attachment", spr\_baseball, 0, 0, 0, 1, 1, 0\);  

 }

The above code first checks if an attachment named "weapon\_attachment" exists. If it exists, the attachment is replaced with a new one that uses a sprite "spr\_baseball" and has no change in origin (offset), scale or rotation.
