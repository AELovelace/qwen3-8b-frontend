# physics\_fixture\_set\_friction

This function sets the friction of the given physics fixture.

Friction is the force that resists the relative motion of material elements sliding against each other, which in the GameMaker physics world, translates as the loss of momentum caused by the collision of two instances with fixtures bound to them. So, when two instances collide, their motion is affected by this value, with a high friction causing a larger loss of momentum than a lower value. Note that the friction is usually set to a value between 0 and 1, but you can use any non\-negative value if required.

 

#### Syntax:

physics\_fixture\_set\_friction(fixture, friction)

| Argument | Type | Description |
| --- | --- | --- |
| fixture | [Physics Fixture ID](physics_fixture_create.md) | the index of the fixture |
| friction | [Real](../../../GML_Overview/Data_Types.md) | the friction of the fixture |

 

#### Returns:

N/A

 

#### Example:

physics\_fixture\_set\_friction(fix\_brick, 0\.1\);

The code above will set the friction of the fixture indexed in fix\_brick to 0\.1\.
