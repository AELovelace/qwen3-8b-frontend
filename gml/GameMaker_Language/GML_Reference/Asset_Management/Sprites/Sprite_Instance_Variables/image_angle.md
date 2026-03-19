# image\_angle

This value sets the angle (rotation) of the sprite and is measured in degrees, with the right being 0º, up being 90º, left being 180º and down being 270º. Set this variable to 0 to reset the sprite to be drawn as was defined in the sprite editor. Please note that for changes in this variable to be visible, the instance should have either *no* draw event (and so GameMaker will default draw the sprite) or be drawn using one of the extended drawing functions like [draw\_self()](../../../Drawing/Sprites_And_Tiles/draw_self.md) or [draw\_sprite\_ext()](../../../Drawing/Sprites_And_Tiles/draw_sprite_ext.md).

 

#### Syntax:

image\_angle

 

#### Returns:

[Real](../../../../GML_Overview/Data_Types.md)

 

#### Example:

image\_angle \= point\_direction(x, y, mouse\_x, mouse\_y);

The above code will rotate the sprite of the instance to always point at the mouse position.
