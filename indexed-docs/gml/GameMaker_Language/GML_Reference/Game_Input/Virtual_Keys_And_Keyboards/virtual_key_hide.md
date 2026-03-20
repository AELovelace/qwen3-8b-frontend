# virtual\_key\_hide

This function hides the coloured rectangle that's drawn to represent the given virtual key on the screen.

Once you have created your virtual key for your devices, you may need to debug and test that it is correctly positioned and working properly and for that you would call the function [virtual\_key\_show](virtual_key_show.md). However, you may need to toggle this view on and off, so you can also hide the virtual key with this function, using the index of the virtual key that you want to hide (previously created and stored using [virtual\_key\_add](virtual_key_add.md)). Once you are happy with things it is recommended that you create and place your own graphic in its area.

 

#### Syntax

virtual\_key\_hide(index)

| Argument | Type | Description |
| --- | --- | --- |
| index | [Virtual Key ID](virtual_key_add.md) | The index of the virtual key to hide |

 

#### Returns:

N/A

 

#### Example:

if (global.debug)  

 {  

     virtual\_key\_show(global.left);  

 }  

 else  

 {  

     virtual\_key\_hide(global.left);  

 }

The above code checks the global variable global.debug and if it tests true then the virtual key indexed in the variable global.left will be drawn on the screen, and if it is false then the key will be hidden.
