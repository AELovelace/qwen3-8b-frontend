# Drawing Action Library

The **Drawing** action library is where you can find the actions required to draw sprites, text or shapes as well as set certain draw properties. Most of these actions are **only for use in the various [Draw Events](../../../The_Asset_Editors/Object_Properties/Draw_Events.md)** of an object, and may not work if used outside of the Draw Event. The exceptions to this are the *Set* actions, which can be added to any event and will affect all drawing for all instances afterwards.

It is important to note that if you add any actions into the main **Draw Event** of an object, then it will *not* draw the sprite that has been assigned to the instance unless you explicitly tell GameMaker to draw it, using an action like [Draw Self](Draw_Self.md). Basically, GameMaker will default draw any sprite assigned to an instance, only if there is *nothing* else in the Draw Event.

The Draw actions available are as follows:

|  | [Draw Self](Draw_Self.md) |
| --- | --- |
|  | [Draw Value](Draw_Value.md) |
|  | [Draw Transformed Value](Draw_Transformed_Value.md) |
|  | [Draw Sprite](Draw_Sprite.md) |
|  | [Draw Sprite Transformed](Draw_Sprite_Transformed.md) |
|  | [Draw Stacked Sprites](Draw_Stacked_Sprites.md) |
|  | [Draw Rectangle](Draw_Rectangle.md) |
|  | [Draw Gradient Rectangle](Draw_Gradient_Rectangle.md) |
|  | [Draw Ellipse](Draw_Ellipse.md) |
|  | [Draw Gradient Ellipse](Draw_Gradient_Ellipse.md) |
|  | [Draw Line](Draw_Line.md) |
|  | [Draw Healthbar](Draw_Healthbar.md) |
|  | [Draw Instance Score](Draw_Instance_Score.md) |
|  | [Draw Instance Health](Draw_Instance_Health.md) |
|  | [Draw Instance Lives](Draw_Instance_Lives.md) |
|  | [Set Draw Colour](Set_Draw_Colour.md) |
|  | [Get Draw Colour](Get_Draw_Colour.md) |
|  | [Set Draw Alpha](Set_Draw_Alpha.md) |
|  | [Get Draw Alpha](Get_Draw_Alpha.md) |
|  | [Set Font](Set_Font.md) |
|  | [Get Draw Font](Get_Draw_Font.md) |
|  | [Set Text Alignment](Set_Text_Alignment.md) |
|  | [Get Text Alignment](Get_Text_Alignment.md) |
