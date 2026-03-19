# title

This action will set the colour or colours to use when your sprite is created and over its lifetime. You first specify the particle type ID value (which should be the same as the value returned when you created the particle using the [Create Particle Type](Create_Particle_Type.md) action) and then you can set the colours to use.

You can pick three colours to use, and the sprite will blend between them over the lifetime of the particle. For example, if a particle has red, green and yellow colours, and a lifetime of 60 game frames, then when it is created (frame 0\) it will be tinted red, then it will fade towards green at half way through its life (frame 30\), before fading on into yellow at the end of its life (frame 60\). If you are using a custom sprite instead of a particle shape, any colour other than white will blend with the sprite used.

  The alpha component of the colour is **not** used, only the RGB components from the colour picker. To set the alpha use the [Set Particle Alpha](Set_Particle_Alpha.md) action.

 

#### Action Syntax:

#### Arguments:

| Argument | Description |
| --- | --- |
| Type | The unique ID value for the particle type to set the colour of |
| Start | The initial colour to use |
| Middle | The in between colour to use |
| End | The final colour to use |

 

#### Example:

The above action block code will create a new particle type and assign its unique ID value to a global variable. It then proceeds to set all the properties for the particle type.
