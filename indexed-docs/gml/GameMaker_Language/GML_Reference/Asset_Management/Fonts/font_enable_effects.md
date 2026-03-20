# font\_enable\_effects

This function is used to enable various effects on an SDF font. The font must have been enabled to use SDF in [The Font Editor](../../../../The_Asset_Editors/Fonts.md) or at runtime using [font\_enable\_sdf](font_enable_sdf.md).

These effects will appear when you use your font at runtime with [draw\_set\_font](../../Drawing/Text/draw_set_font.md), or use it in a [text track in a Sequence](../../../../The_Asset_Editors/Sequence_Properties/Text_in_Sequences.md).

The enable argument takes true/false for enabling/disabling effects. The actual properties for your effects are supplied in the optional params struct.

## Effects

This function supports the following effects:

- Outline
- Glow
- Drop Shadow

Fig. 1

Each effect has its own set of properties, described below. These properties are supplied in a struct.

A single font can have any of these effects applied to it at the same time.

  The [SDF spread value](font_sdf_spread.md) limits how far an effect can spread from a glyph's edge.

[General](#)

There are a few "general" properties:

- **thickness**: Add or remove thickness from the font. **Minimum**: \-32, **Maximum**: 32\.
- **coreColour**: The colour of the core part of the font (excluding any outlines, glows, etc.).
- **coreAlpha**: The alpha of the core part of the font.

[Outline](#)

The following properties are provided for Outline:

- **outlineEnable**: Enable or disable the Outline effect. **Disabled** by default.
- **outlineDistance**: The thickness of the outline from the edge of each glyph. **Minimum**: 0, **Maximum**: 64\.
- **outlineColour**: The colour of the outline.
- **outlineAlpha**: The alpha of the outline.

[Glow](#)

The following properties are provided for Glow:

- **glowEnable**: Enable or disable the Glow effect. **Disabled** by default.
- **glowStart**: The distance from the glyph edge where the glow starts fading out. **Minimum**: 0, **Maximum**: 64\.
- **glowEnd**: The distance from the glyph edge where the glow has fully faded. **Minimum**: 0, **Maximum**: 64\.
- **glowColour**: The colour of the glow.
- **glowAlpha**: The alpha of the glow.

[Drop Shadow](#)

The following properties are provided for Drop Shadow:

- **dropShadowEnable**: Enable or disable the Drop Shadow effect. **Disabled** by default.
- **dropShadowSoftness**: Softness or blur level of the shadow. **Minimum**: 0, **Maximum**: 64\.
- **dropShadowOffsetX**: How much the shadow is moved on the X axis, 0 is the same as the text. E.g. a value of 4 moves it right by 4 pixels.
- **dropShadowOffsetY**: How much the shadow is moved on the Y axis, 0 is the same as the text. E.g. a value of 4 moves it down by 4 pixels.
- **dropShadowColour**: The colour of the shadow.
- **dropShadowAlpha**: The alpha of the shadow.

The offset of the drop shadow is affected by the scale at which the text is drawn, so a 10px offset will become 100px when drawn with a scale of 10\.

The colour of an effect will be multiplied with whatever [blend colour](../../Drawing/Colour_And_Alpha/draw_set_colour.md) is set when the text is drawn.

 

#### Syntax:

font\_enable\_effects(ind, enable, \[params])

| Argument | Type | Description |
| --- | --- | --- |
| ind | [Font Asset](../../../../The_Asset_Editors/Fonts.md) | The index of the font (must be [SDF\-enabled](font_enable_sdf.md)) |
| enable | [Boolean](../../../GML_Overview/Data_Types.md) | Enable (true) or disable (false) effects |
| params | [Struct](../../../GML_Overview/Structs.md) | A struct containing effect properties |

 

#### Returns:

N/A

 

#### Example 1:

Create Event

font\_enable\_effects(fnt\_outline, true, {  

     outlineEnable: true,  

     outlineDistance: 2,  

     outlineColour: c\_black  

 });  

  

 font\_enable\_effects(fnt\_glow, true, {  

     glowEnable: true,  

     glowEnd: 16,  

     glowColour: c\_red  

 });
 

This modifies two font assets that presumably have SDF enabled.

The first font fnt\_outline gets outline enabled with some properties set, and the second font fnt\_glow gets some glow properties.

You would draw text with these fonts by doing this in a Draw event:

Draw Event

draw\_set\_font(fnt\_outline);  

 draw\_text(x, y, "This font has an outline.");  

  

 draw\_set\_font(fnt\_glow);  

 draw\_text(x, y \+ 60, "This font has a glow.");
 

This switches to the outline font to draw text with an outline, and then switches to the glow font to draw glowing text.

The result of this font can be seen in **Fig. 1** at the top of this page.

 

#### Example 2:

font\_enable\_effects(fnt\_heading, true, {  

     dropShadowEnable: true,  

     dropShadowSoftness: 20,  

     dropShadowOffsetX: 4,  

     dropShadowOffsetY: 4,  

     dropShadowAlpha: 1,  

     outlineEnable: true,  

     outlineDistance: 2,  

     outlineColour: c\_black,  

     glowEnable: true,  

     glowEnd: 6,  

     glowColour: c\_red,  

     glowAlpha: 4  

 });

This example demonstrates that you can apply multiple effects to the same font at once:

Fig. 2
