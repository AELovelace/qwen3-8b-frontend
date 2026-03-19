# physics\_get\_restitution

This function returns the restitution of the given bound fixture.

When you bind a fixture to an instance using [physics\_fixture\_bind](physics_fixture_bind.md) this returns an "ID" for the bound fixture. You can use this ID to get the restitution (the "bounciness" property) value of the bound fixture, *not* the "base" fixture, at any time using this function.

 

#### Syntax:

physics\_get\_restitution(fixture)

| Argument | Type | Description |
| --- | --- | --- |
| fixture | [Physics Bound Fixture ID](physics_fixture_bind.md) | The ID of the bound fixture |

 

#### Returns:

[Real](../../../GML_Overview/Data_Types.md)

 

#### Example:

var \_rest \= physics\_get\_restitution(fix\_id);  

 physics\_set\_restitution(fix\_id, \_rest \* 2\);

The code above gets the current restitution value for the bound physics properties of the instance and then sets it to a different value.
