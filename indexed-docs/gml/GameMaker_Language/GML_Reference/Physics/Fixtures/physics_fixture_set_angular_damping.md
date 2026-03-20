# physics\_fixture\_set\_angular\_damping

This function sets the angular damping of the given fixture.

If you think about any rotating object in the "real world", unless it has a motor or is in space, it slows down over time due to the influence of external forces (like friction with the air around it). We can use the function physics\_fixture\_set\_angular\_damping in GameMaker to simulate this effect and reduce the velocity of rotation of instances in the physics world, as, without it, any rotating instance would continue to rotate infinitely. Damping parameters should be between 0 and infinity, with 0 meaning no damping, and infinity meaning full damping. Normally you will use a damping value between 0 and 1, but you can use any non\-negative value if required.

 

#### Syntax:

physics\_fixture\_set\_angular\_damping(fixture, damping)

| Argument | Type | Description |
| --- | --- | --- |
| fixture | [Physics Fixture ID](physics_fixture_create.md) | the index of the fixture |
| damping | [Real](../../../GML_Overview/Data_Types.md) | the angular damping of the fixture, usually between 0 and 1 |

 

#### Returns:

N/A

 

#### Example:

physics\_fixture\_set\_angular\_damping(fix\_ball, 0\.1\);

The code above will set the angular damping of the fixture indexed in fix\_ball to 0\.1\.
