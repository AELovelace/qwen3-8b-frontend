# virtual\_key\_show

This function draws a coloured rectangle to represent the given virtual key on the screen.

Once you have created a virtual key for your devices, you may need to debug and test that it is correctly positioned and working properly. For that you can use this function, using the index of the virtual key that you want to see (previously created and stored using [virtual\_key\_add](virtual_key_add.md)) which will draw a coloured rectangle to represent the key on the screen. Once you are happy with things it is recommended that you create and place your own graphic in its area.

  The rectangle being drawn will be affected by the blending, colour and alpha options set by the corresponding [draw functions](../../Drawing/Colour_And_Alpha/Colour_And_Alpha.md).

 

#### Syntax

virtual\_key\_show(index)

| Argument | Type | Description |
| --- | --- | --- |
| index | [Virtual Key ID](virtual_key_add.md) | The index of the virtual key to show |

 

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
