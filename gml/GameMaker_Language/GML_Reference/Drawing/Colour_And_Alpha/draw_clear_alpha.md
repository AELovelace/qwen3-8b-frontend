# draw\_clear\_alpha

This function can be used to clear the entire screen with a given colour and the alpha component of the destination is set to the value you have set \- this function does *not* do any blending as it works but any subsequent blend operations can be set up to use the destination alpha that you have set. This is only for use in [Draw Events](../../../../The_Asset_Editors/Object_Properties/Draw_Events.md) of an instance (it will not show if used in any other event), and it can also be very useful for clearing [surfaces](../Surfaces/Surfaces.md) when they are newly created.

It is worth noting that when using the HTML5 module, you can use this function to make the canvas background transparent, which will then permit any images being used in the host HTML to be seen with the game running over them. To achieve this effect you must first go into the room editor and remove any **Background Layers** from the [Room Editor](../../../../The_Asset_Editors/Rooms.md), then untick the option **Clear View Background** found on the [View Properties](../../../../The_Asset_Editors/Room_Properties/Room_Properties.md). Finally, you will need to make a new object, place it in the first room of the game, and assign it a very high depth (for example, 10000\). Then in the **Pre Draw** event use this function to set the canvas alpha to the colour and transparency that you wish it to have.

 

#### Syntax:

draw\_clear\_alpha(col, alpha)

| Argument | Type | Description |
| --- | --- | --- |
| col | [Colour](Colour_And_Alpha.md) | The colour with which the screen will be cleared |
| alpha | [Real](../../../GML_Overview/Data_Types.md) | The transparency of the colour with which the screen will be cleared |

 

#### Returns:

N/A

 

#### Example:

draw\_clear\_alpha(c\_red, 0\.5\);

This will clear the screen with 50% (0\.5\) transparency with the colour red.
