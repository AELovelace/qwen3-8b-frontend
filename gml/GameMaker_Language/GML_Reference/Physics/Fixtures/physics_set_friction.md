# physics\_set\_friction

This function sets the friction value of the given bound fixture.

When you bind a fixture to an instance using [physics\_set\_friction](physics_set_friction.md) this returns an "ID" for the bound fixture. You can use this ID to set the friction value of the bound fixture, *not* the "base" fixture, at any time using this function. Note that the friction is usually set to a value between 0 and 1, but you can use any non\-negative value if required.

 
 

#### Syntax:

physics\_set\_friction(fixture, friction)

| Argument | Type | Description |
| --- | --- | --- |
| fixture | [Physics Bound Fixture ID](physics_fixture_bind.md) | The ID of the bound fixture |
| friction | [Real](../../../GML_Overview/Data_Types.md) | The new friction value to apply |

 

#### Returns:

N/A

 

#### Example:

var \_fric \= physics\_get\_friction(fix\_id);  

 physics\_set\_friction(fix\_id, \_fric \+ 0\.1\);

The code above gets the current friction value for the bound physics properties of the instance and then sets it to a different value.
