# title

This action can be used to set the built\-in sprite shape that a particle should use when drawing. You supply the unique ID value for the type to set the shape of (as returned when you created the type with the action [Create Particle Type](Create_Particle_Type.md)) and the shape to use. Particle shapes are simply white sprites that have been created for GameMaker to use specifically as particles and consist of the following forms:

  If you use this action then you should **not** use the action [Set Particle Sprite](Set_Particle_Sprite.md) as you can only have a sprite **or** a shape, but not both.

 

#### Action Syntax:

#### Arguments:

| Argument | Description |
| --- | --- |
| Type | The ID value for the type to set the shape of |
| Shape | The shape to use for the particle type |

 

#### Example:

The above action block code will create a new particle type and assign its unique ID value to a global variable. It then proceeds to set all the properties for the particle type.
