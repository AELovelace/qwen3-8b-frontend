# physics\_get\_density

This function returns the density of the given bound fixture.

When you bind a fixture to an instance using [physics\_fixture\_bind](physics_fixture_bind.md) this returns an "ID" for the bound fixture. You can use this ID to get the density value of the bound fixture (*not* the "base" fixture) at any time using this function.

 

#### Syntax:

physics\_get\_density(fixture)

| Argument | Type | Description |
| --- | --- | --- |
| fixture | [Physics Bound Fixture ID](physics_fixture_bind.md) | The ID of the bound fixture |

 

#### Returns:

[Real](../../../GML_Overview/Data_Types.md)

 

#### Example:

var \_density \= physics\_get\_density(fix\_id);  

 physics\_set\_density(fix\_id, \_density \- 0\.1\);

The code above gets the current density value for the bound physics properties of the instance and then sets it to a different value.
