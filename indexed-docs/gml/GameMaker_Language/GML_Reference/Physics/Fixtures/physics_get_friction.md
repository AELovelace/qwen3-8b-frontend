# physics\_get\_friction

This function gets the friction value of the given bound fixture (*not* the "base" fixture).

 

#### Syntax:

physics\_get\_friction(fixture)

| Argument | Type | Description |
| --- | --- | --- |
| fixture | [Physics Bound Fixture ID](physics_fixture_bind.md) | The ID of the bound fixture |

 

#### Returns:

[Real](../../../GML_Overview/Data_Types.md)

 

#### Example:

var \_fric \= physics\_get\_friction(fix\_id);  

 physics\_set\_friction(fix\_id, \_fric \+ 0\.1\);

The code above gets the current friction value for the bound physics properties of the instance and then sets it to a different value.
