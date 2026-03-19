# skeleton\_attachment\_get

Using this function you can get the name (as a string) of the attachment for the given slot of the currently assigned skeletal animation sprite.

A skeletal animation sprite may have other sprites added as attachments, with these sprites being added to a named slot (the name is given when you create the attachment slot in your animation program) and they will be drawn along with the animation of the current sprite. With this function you can get the name (as a string) of the attachment for the given slot of the currently assigned sprite. Note that attached sprites are referenced through their *name string* as assigned in Spine, or when you called [skeleton\_attachment\_create](skeleton_attachment_create.md).

 

#### Syntax:

skeleton\_attachment\_get(slot)

| Argument | Type | Description |
| --- | --- | --- |
| slot | [String](../../../../../GML_Overview/Data_Types.md) | The slot name (a string) to get the attachment of |

 

#### Returns:

[String](../../../../../GML_Overview/Data_Types.md)

 

#### Example:

if (skeleton\_attachment\_get("slot\_leftHand") \=\= "")  

 {  

     skeleton\_attachment\_set("slot\_leftHand", choose("sword", "spear", "knife"));  

 }

The above code would check the currently assigned attachment name for the slot named "slot\_leftHand" and if an empty string "" is returned, a new sprite is attached.
