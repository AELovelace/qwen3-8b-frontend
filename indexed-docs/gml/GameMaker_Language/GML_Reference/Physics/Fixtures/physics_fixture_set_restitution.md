# physics\_fixture\_set\_restitution

This function sets the restitution of the given physics fixture.

In physics, restitution is defined as "the return of an object or system to its original state after elastic deformation", but as the fixtures in the GameMaker are really rigid bodies and cannot be deformed, restitution is really a way of saying how "bouncy" the fixture is. This setting will affect how much an object "bounces" when it collides with other objects and is co\-dependent on other forces that act on the instance like gravity and friction, and is usually a value between 0 and 1 (higher values can be used but may give unpredictable results). Here is an illustration of how it works:

#### Syntax:

physics\_fixture\_set\_restitution(fixture, restitution)

| Argument | Type | Description |
| --- | --- | --- |
| fixture | [Physics Fixture ID](physics_fixture_create.md) | The index of the fixture |
| restitution | [Real](../../../GML_Overview/Data_Types.md) | The restitution of the fixture (usually between 0 and 1\) |

 

#### Returns:

N/A

 

#### Example:

physics\_fixture\_set\_restitution(fix\_ball, 0\.9\);

The code above will set the restitution of the fixture indexed in fix\_ball to 0\.9\.
