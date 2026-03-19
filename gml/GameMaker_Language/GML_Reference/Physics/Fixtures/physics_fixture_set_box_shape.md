# physics\_fixture\_set\_box\_shape

This function defines a box shape for the given fixture. It takes the *half* width and height as the physics world uses this value far more than whole width/height values to determine things like collisions.

 

#### Syntax:

physics\_fixture\_set\_box\_shape(fixture, half\_width, half\_height)

| Argument | Type | Description |
| --- | --- | --- |
| fixture | [Physics Fixture ID](physics_fixture_create.md) | the index of the fixture |
| half\_width | [Real](../../../GML_Overview/Data_Types.md) | the *half* width of the box |
| half\_height | [Real](../../../GML_Overview/Data_Types.md) | the *half* height of the box |

 

#### Returns:

N/A

 

#### Example:

physics\_fixture\_set\_box\_shape(fix\_border, room\_width/2, 10\);

The code above will apply a box shape to the fixture indexed in the variable fix\_border with a width of the room and a height of 20 pixels.
