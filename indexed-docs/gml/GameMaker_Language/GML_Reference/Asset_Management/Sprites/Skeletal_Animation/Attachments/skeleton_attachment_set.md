# skeleton\_attachment\_set

With this function you can set an attachment to a given slot, where you are required to give the names (as strings) of the slot and the attachment.

A skeletal animation sprite may have other images added as attachments, with these images being added to a named slot (the name is given when you create the attachment slot in your animation program) and they will be drawn along with the animation of the current sprite. With this function you can set an attachment to a given slot, where you are required to give the names (as strings) of the slot and the attachment. These names are defined by the animation program used, or, in the case of the attachment, when you call [skeleton\_attachment\_create](skeleton_attachment_create.md).

Note that you can also pass in a sprite index as the attachment, and that sprite will be used, or you can use \-1 to remove the attachment from the slot. When you pass in a sprite index as an argument, it will create an attachment slot using the name of the sprite as the string to name the slot (so using spr\_sword, for example, will create an attachment slot "spr\_sword"), and the slot will use the first image index (0\) of the the sprite, as well as its x and y origin offset, with a scale of (1, 1\) and a rotation of 0\.

 

#### Syntax:

skeleton\_attachment\_set(slot, attachment)

| Argument | Type | Description |
| --- | --- | --- |
| slot | [String](../../../../../GML_Overview/Data_Types.md) | The slot name (a string) to get the attachment of |
| attachment | [String](../../../../../GML_Overview/Data_Types.md) or [Sprite Asset](../../../../../../The_Asset_Editors/Sprites.md) | The name (as a string or a sprite\_index) of the attachment image |

 

#### Returns:

[String](../../../../../GML_Overview/Data_Types.md)

 

#### Example:

if (skeleton\_attachment\_get("slot\_leftHand") \=\= "")  

 {  

     skeleton\_attachment\_set("slot\_leftHand", choose("sword", "spear", "knife"));  

 }

The above code would check the currently assigned attachment name for the slot named "slot\_leftHand" and, if an empty string "" is returned, a new sprite is attached.
