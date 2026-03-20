# physics\_set\_restitution

This function sets the restitution value of the given bound fixture.

When you bind a fixture to an instance using [physics\_fixture\_bind](physics_fixture_bind.md) this returns an "ID" for the bound fixture. You can use this ID to set the restitution value of the bound fixture, *not* the "base" fixture, at any time using this function. Restitution is usually set as a value between 0 and 1, but you can use higher values if required, although the results may be unpredictable.

 
 

#### Syntax:

physics\_set\_restitution(fixture, restitution)

| Argument | Type | Description |
| --- | --- | --- |
| fixture | [Physics Bound Fixture ID](physics_fixture_bind.md) | The ID of the bound fixture |
| restitution | [Real](../../../GML_Overview/Data_Types.md) | The new restitution value to apply |

 

#### Returns:

N/A

 

#### Example:

var \_rest \= physics\_get\_restitution(fix\_id);  

 physics\_set\_restitution(fix\_id, \_rest \* 2\);

The code above gets the current restitution value for the bound physics properties of the instance and then sets it to a different value.
