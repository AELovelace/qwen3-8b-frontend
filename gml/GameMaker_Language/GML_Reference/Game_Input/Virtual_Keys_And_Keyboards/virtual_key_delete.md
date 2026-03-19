# virtual\_key\_delete

This function deletes a previously added virtual key.

If your game has different rooms or instances to control menus and gameplay and other things, then it is probable that you will need to change the position and key maps of your virtual keys at some point. For that you can use this function to delete the old ones before creating the new ones (if necessary). The function requires that you supply the ID of the virtual key to delete \- as returned by [virtual\_key\_add](virtual_key_add.md).

  Any virtual keys will be automatically removed from the room when the room is changed, so this function is *only* necessary when you wish to manually remove the keys before the room itself has finished.

 

#### Syntax

virtual\_key\_delete(index)

| Argument | Type | Description |
| --- | --- | --- |
| index | [Virtual Key ID](virtual_key_add.md) | The index of the virtual key to delete |

 

#### Returns:

N/A

 

#### Example:

virtual\_key\_delete(global.left);

The above code deletes the virtual key stored in the global variable global.left.
