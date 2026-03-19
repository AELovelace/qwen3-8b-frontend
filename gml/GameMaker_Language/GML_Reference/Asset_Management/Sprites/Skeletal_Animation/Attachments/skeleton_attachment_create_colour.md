# skeleton\_attachment\_create\_colour

This function creates an attachment for the instance's skeletal animation sprite at runtime using a sprite asset from your game, blended with the given colour and alpha value.

When you create your skeletal animation sprite, you can assign *attachment slots* and *attachments* to go in them. These are simply images (sprites) that are separate from the animation but when attached will move along with the bone they are attached to. Normally you would assign these attachments in your animation program (Spine), but with this function you can create your own at runtime using a sprite asset from your game. The function requires that you give the attachment a name (as a string) and then set the [sprite\_index](../../Sprite_Instance_Variables/sprite_index.md) and [image\_index](../../Sprite_Instance_Variables/image_index.md) to use, as well as the x and y origin (which can be different from that defined by the sprite in the sprite properties), and you can also set any transforms that you wish to be applied to the image when attached as well as the colour to be blended with the image and its alpha (transparency) value. The function will return 1 if the attachment was successfully created, or \-1 if it wasn't (you supplied an invalid sprite index, or the base sprite is not a Spine sprite).

It is worth noting that the instance's sprite can have a blend colour and alpha setting ([image\_blend](../../Sprite_Instance_Variables/image_blend.md) and [image\_alpha](../../Sprite_Instance_Variables/image_alpha.md)), as can the attachment slot (see the function [skeleton\_slot\_colour\_set](../Slots/skeleton_slot_colour_set.md)), and so the final colour and alpha that the assigned attachment sprite for the slot will have will be a composite of all these values.

 
#### Syntax:

skeleton\_attachment\_create\_colour(name, sprite, ind, xorigin, yorigin, xscale, yscale, rot, colour, alpha)

| Argument | Type | Description |
| --- | --- | --- |
| name | [String](../../../../../GML_Overview/Data_Types.md) | The name (as a string) of the attachment to create. |
| sprite | [Sprite Asset](../../../../../../The_Asset_Editors/Sprites.md) | The sprite\_index to get the attachment image from. |
| ind | [Real](../../../../../GML_Overview/Data_Types.md) | The image\_index to get the attachment image from. |
| xorigin | [Real](../../../../../GML_Overview/Data_Types.md) | The x origin for the image being used. |
| yorigin | [Real](../../../../../GML_Overview/Data_Types.md) | The y origin for the image being used. |
| xscale | [Real](../../../../../GML_Overview/Data_Types.md) | The horizontal scaling of the image, as a multiplier: 1 \= normal scaling, 0\.5 is half, etc. |
| yscale | [Real](../../../../../GML_Overview/Data_Types.md) | The vertical scaling of the image, as a multiplier: 1 \= normal scaling, 0\.5 is half, etc. |
| rot | [Real](../../../../../GML_Overview/Data_Types.md) | The rotation of the image: 0 \= normal, 90 \= turned 90° counter\-clockwise, etc. |
| colour | [Colour](../../../../Drawing/Colour_And_Alpha/Colour_And_Alpha.md) | The colour value to use (A constant, integer or hex value). |
| alpha | [Real](../../../../../GML_Overview/Data_Types.md) | The alpha value to use (from 0 to 1\). |

 

#### Returns:

[Real](../../../../../GML_Overview/Data_Types.md) (1 if successful, \-1 if not)

 

#### Example:

skeleton\_attachment\_create\_colour("sword", spr\_Weapons, 0, 0, 80, 1, 1, 90, c\_red, 1\);  

skeleton\_attachment\_create\_colour("knife", spr\_Weapons, 1, 0, 45, 1, 1, 90, c\_yellow, 1\);  

skeleton\_attachment\_create\_colour("crossbow", spr\_Weapons, 0, 10, 30, 1, 1, 0, c\_white, 0\.5\);  

 skeleton\_attachment\_set("slot\_leftHand", choose("sword", "knife", "crossbow"));
 

The above code would check the currently assigned attachment name for the slot named "slot\_leftHand" and if an empty string is returned, a new sprite is attached.
