# physics\_fixture\_set\_density

This function sets the density of the given physics fixture.

The density of something is defined as its mass per unit volume, which basically means *how much mass is crammed into the space it takes up in the world*. So, a balloon would have a low density as it has little mass that occupies a large space, while a lead bar would have a high density as it has a great mass, yet occupies little space.

In the GameMaker 2D physics world, mass is calculated automatically for you from the values you input for the **density** and by the **surface area** of the shape you define for the fixture. This will have a direct impact on how much inertia a fixture has as well as how it reacts to collisions and forces, so if you make a small shape with a high density it will have a very large mass (like a bar of lead), but if you define a large shape with a low density it will have a much smaller mass (like a balloon).

  If you wish the instance that is going to receive the fixture to be **static** (i.e.: immobile in the game world) then the density should be set to 0, essentially giving it an infinite density.

  A static fixture can be made **kinematic** (i.e.: it can move but without the effects of force or gravity) by making it have a density of 0 and then setting the [phy\_speed\_x](../Physics_Variables/phy_speed_x.md), [phy\_speed\_y](../Physics_Variables/phy_speed_y.md), or [phy\_angular\_velocity](../Physics_Variables/phy_angular_velocity.md) variables.

 

#### Syntax:

physics\_fixture\_set\_density(fixture, density)

| Argument | Type | Description |
| --- | --- | --- |
| fixture | [Physics Fixture ID](physics_fixture_create.md) | the index of the fixture |
| density | [Real](../../../GML_Overview/Data_Types.md) | the density of the fixture calculated as kg/m² |

 

#### Returns:

N/A

 

#### Example:

physics\_fixture\_set\_density(fix\_balloon, 0\.1\);

The code above will set the density of the fixture indexed in fix\_balloon to 0\.1\.
