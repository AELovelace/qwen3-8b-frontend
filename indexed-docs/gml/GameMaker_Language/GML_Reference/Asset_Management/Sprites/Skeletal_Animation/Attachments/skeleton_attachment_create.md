# skeleton\_attachment\_create

This function creates an attachment for the instance's skeletal animation sprite at runtime using a sprite asset from your game.

When you create your skeletal animation sprite, you can assign *attachment slots* and *attachments* to go in them. These are simply images (sprites) that are separate from the animation but when attached will move along with the bone they're attached to. Normally you would assign these attachments in your animation program (Spine), but with this function you can create your own at runtime using a sprite asset from your game. The function requires that you give the attachment a name (as a string) and then set the sprite\_index and image\_index to use, as well as the x and y origin (which can be different from that defined by the sprite in the sprite properties), and you can also set any transforms that you wish to be applied to the image when attached. The function will return 1 if the attachment was successfully created, or \-1 if it wasn't (you supplied an invalid sprite index, or the base sprite is not a Spine sprite).

 
#### Syntax:

skeleton\_attachment\_create(name, sprite, ind, xorigin, yorigin, xscale, yscale, rot)

| Argument | Type | Description |
| --- | --- | --- |
| name | [String](../../../../../GML_Overview/Data_Types.md) | The name (as a string) of the attachment to create. |
| sprite | [Sprite Asset](../../../../../../The_Asset_Editors/Sprites.md) | The sprite\_index to get the attachment image from. |
| ind | [Real](../../../../../GML_Overview/Data_Types.md) | The image\_index to get the attachment image from. |
| xorigin | [Real](../../../../../GML_Overview/Data_Types.md) | The x origin for the image being used. |
| yorigin | [Real](../../../../../GML_Overview/Data_Types.md) | The y origin for the image being used. |
| xscale | [Real](../../../../../GML_Overview/Data_Types.md) | The horizontal scaling of the image, as a multiplier: 1 \= normal scaling, 0\.5 is half, etc. |
| yscale | [Real](../../../../../GML_Overview/Data_Types.md) | The vertical scaling of the image, as a multiplier: 1 \= normal scaling, 0\.5 is half, etc. |
| rot | [Real](../../../../../GML_Overview/Data_Types.md) | The rotation of the image. 0\=normal, 90\=turned 90 degrees counter\-clockwise etc. |

 

#### Returns:

[Real](../../../../../GML_Overview/Data_Types.md) (1 if successful, \-1 if not)

 

#### Example:

skeleton\_attachment\_create("sword", spr\_Weapons, 0, 0, 80, 1, 1, 90\);  

skeleton\_attachment\_create("knife", spr\_Weapons, 1, 0, 45, 1, 1, 90\);  

skeleton\_attachment\_create("crossbow", spr\_Weapons, 0, 10, 30, 1, 1, 0\);  

 skeleton\_attachment\_set("slot\_leftHand", choose("sword", "knife", "crossbow"));
 

The above code would check the currently assigned attachment name for the slot named "slot\_leftHand" and if an empty string is returned, a new sprite is attached.
