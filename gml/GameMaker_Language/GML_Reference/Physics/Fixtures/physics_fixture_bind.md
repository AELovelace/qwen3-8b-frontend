# physics\_fixture\_bind

This function binds the given fixture to the given target object or instance and returns the ID of the bound fixture.

Once we have defined our fixture it has to be bound to an instance. This means that its *properties* are transferred to the selected instance, **not the actual fixture itself**, so that one fixture can be bound to multiple instances if all are to have the same properties. You can specify an object index for the target and all instances of that object present in the room at the time will receive that fixture's properties (but not any new instances of the object created later), or you can use the special keywords [other](../../../GML_Overview/Instance Keywords/other.md) and [all](../../../GML_Overview/Instance Keywords/all.md). You can even specify a parent object and all instances that are instances of children of that parent object will also receive the fixture. Once the fixture has been bound to all the instances that you need, it can be deleted if no longer necessary and the instances with that fixture's properties will not be affected and maintain those properties.

The fixture will be bound to the instance with the centre of mass being positioned at the origin of the instance, and polygon fixtures are bound based on the position of the points *relative* to the origin. If you require your fixture to be bound to a point other than the origin then you should be using [physics\_fixture\_bind\_ext](physics_fixture_bind_ext.md).

The function will also return a unique "id" value for the *bound* fixture (**not the fixture itself**) which can then be used to remove ("un\-bind") the physics properties from the instance using the function [physics\_remove\_fixture](physics_remove_fixture.md). This permits you to add and remove physical properties from an instance without destroying and re\-creating instances.

  Fixtures should be deleted when no longer needed as failure to do so may cause a memory leak which will slow down and eventually crash your game.

 

#### Syntax:

physics\_fixture\_bind(fixture, target)

| Argument | Type | Description |
| --- | --- | --- |
| fixture | [Physics Fixture ID](physics_fixture_create.md) | The fixture that is to be bound |
| target | [Object Instance](../../Asset_Management/Instances/Instance_Variables/id.md) or [Object Asset](../../../../The_Asset_Editors/Objects.md) | The target instance that is to receive the fixture (can be an instance, an object, [other](../../../GML_Overview/Instance Keywords/other.md) or [all](../../../GML_Overview/Instance Keywords/all.md)) |

 

#### Returns:

[Physics Bound Fixture ID](physics_fixture_bind.md)

 

#### Example:

Create Event

var \_fix \= physics\_fixture\_create();  

 physics\_fixture\_set\_circle\_shape(\_fix, 16\);  

 physics\_fixture\_set\_density(\_fix, 1\.0\);  

 my\_bound\_fix \= physics\_fixture\_bind(\_fix, id);  

 physics\_fixture\_delete(\_fix);

Clean Up Event

physics\_remove\_fixture(id, my\_bound\_fix);

The code above shows how to bind a physics fixture to the instance executing the code and remove it afterwards.

In the Create event, a fixture is created and its index is assigned to a temporary variable \_fix. The shape and density of the fixture are then defined and the fixture is bound to the calling instance with the index for the **bound** fixture stored in the instance variable my\_bound\_fix. Finally, the fixture is deleted to prevent memory leaks as it is no longer needed.

In the Clean Up event, the bound fixture is removed.
