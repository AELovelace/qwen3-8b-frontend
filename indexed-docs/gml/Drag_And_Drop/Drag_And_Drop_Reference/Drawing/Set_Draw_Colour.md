# Set Draw Colour

With this action you can set the colour to use for any shapes (rectangle/ellipse/line) or for any text that is drawn subsequently. Note that this does not have to be called before every draw action, and can be set once only at the start of the game. For example, if all your text is going to be yellow, you can call this action in the Create Event of the first room of the game, and all text (and shapes) will then be drawn yellow from then onwards. However if you need to use multiple different colours, then you will need to call this before each text or shape that requires a different colour.

The action has a checkbox at the bottom for **Use alpha**. This enables the alpha component of the colour to be used to set the draw alpha too (much the same as using [Set Draw Alpha](Set_Draw_Alpha.md) does. If you do not want to include the alpha component and just have a solid colour, this can be disabled (it is enabled by default).

 

#### Action Syntax:

#### Example:

The above action block code sets the font, the draw colour, and the alignment for some text that is drawn.
