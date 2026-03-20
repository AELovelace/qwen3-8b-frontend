# physics\_remove\_fixture

This function removes (or "un\-binds") a bound fixture from an instance or instances.

It requires the unique "ID" of the bound fixture (as returned by the function [physics\_fixture\_bind](physics_fixture_bind.md)) and it will remove all the currently defined physics properties for the instance, permitting you to redefine a new fixture and bind that to the instance. In this way you can change the instance's physical properties without having to destroy and re\-create it.

 

#### Syntax:

physics\_remove\_fixture(id, fixture)

| Argument | Type | Description |
| --- | --- | --- |
| id | [Object Instance](../../Asset_Management/Instances/Instance_Variables/id.md) or [Object Asset](../../../../The_Asset_Editors/Objects.md) | The ID of the instance, or an object ID to remove the fixture from all instances of that object |
| fixture | [Physics Bound Fixture ID](physics_fixture_bind.md) | The ID of the bound fixture that is to be removed |

 

#### Returns:

N/A

 

#### Example:

physics\_remove\_fixture(id, my\_bound\_fix);

The code above will remove the fixture with the ID stored in the variable my\_bound\_fix from the instance.
