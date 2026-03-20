# draw\_clear

This function can be used to clear the entire screen (with no alpha blend) to the given colour, and is only for use in the [Draw Events](../../../../The_Asset_Editors/Object_Properties/Draw_Events.md) of an instance (it will not show if used in any other event). It can also be useful for clearing [surfaces](../Surfaces/Surfaces.md) when they are newly created.

 

#### Syntax:

draw\_clear(col)

| Argument | Type | Description |
| --- | --- | --- |
| col | [Colour](Colour_And_Alpha.md) | The colour with which the screen will be cleared |

 

#### Returns:

N/A

 

#### Example:

draw\_clear(c\_blue);

This will clear the screen with the colour blue.
