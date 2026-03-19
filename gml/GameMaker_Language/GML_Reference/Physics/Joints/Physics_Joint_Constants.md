# Physics Joint Constants

There are a great number of constants included within the GameMaker GML that are specific to *joints* between fixtures in the physics world. These can be used in conjunction with many of the different joint functions to set or get information from them in real time while the physics simulation is running. You should be aware, however, that complex calculations are done when you call these, so they should be used with care and only when necessary and note that *many are unique to a specific type of joint*. Also note that while you can get all these values with the appropriate function, you can only set those that are marked as not being read\-only.

In general these constants would be used in conjunction with the following functions:

- [physics\_joint\_get\_value](physics_joint_get_value.md)
- [physics\_joint\_set\_value](physics_joint_set_value.md)

## General

The following constants can be applied to any of the available joint types:

| [Physics Joint Constant](Physics_Joint_Constants.md) | | |
| --- | --- | --- |
| Constant | Description | Read Only |
| phy\_joint\_anchor\_1\_x | The x coordinate of the first anchor point of the joint *in the room* | Yes |
| phy\_joint\_anchor\_1\_y | The y coordinate of the first anchor point of the joint *in the room* | Yes |
| phy\_joint\_anchor\_2\_x | The x coordinate of the second anchor point of the joint *in the room* | Yes |
| phy\_joint\_anchor\_2\_y | The y coordinate of the second anchor point of the joint *in the room* | Yes |
| phy\_joint\_reaction\_force\_x | This is the reaction force being applied to the second instance in a joint at the x anchor position | Yes |
| phy\_joint\_reaction\_force\_y | This is the reaction force being applied to the second instance in a joint at the y anchor position | Yes |
| phy\_joint\_reaction\_torque | This is the torque being applied to the second instance in a joint at the anchor position | Yes |

## Motors

These constants are for those joints that have a *motor* attached to them (revolute, prismatic, wheel):

| [Physics Joint Constant](Physics_Joint_Constants.md) | | |
| --- | --- | --- |
| Constant | Description | Read Only |
| phy\_joint\_max\_motor\_force | The value specified when the joint was created for the maximum motor force | No |
| phy\_joint\_max\_motor\_torque | The value specified when the joint was created for the maximum motor torque | No |
| phy\_joint\_motor\_force | The current motor force | Yes |
| phy\_joint\_motor\_speed | The current motor speed | No |
| phy\_joint\_motor\_torque | The current motor torque | Yes |

## Revolute Joints

For a revolute joint you can use the following constant (as well as the *motor* constants if one has been added):

| [Physics Joint Constant](Physics_Joint_Constants.md) | | |
| --- | --- | --- |
| Constant | Description | Read Only |
| phy\_joint\_angle | The angle that a line between the two anchor points of the joint makes. This is calculated using the *physics world* coordinates  (**not** the GameMaker room coordinates) in radians. | Yes |
| phy\_joint\_angle\_limits | Enable or disable angle limiting for the joint. Set the value to true to enable or false to disable. | No |
| phy\_joint\_upper\_angle\_limit | The upper angle limit for the joint in degrees. | No |
| phy\_joint\_lower\_angle\_limit | The lower angle limit for the joint in degrees. | No |

## Prismatic Joints

For a prismatic joint you can use the following constant:

| [Physics Joint Constant](Physics_Joint_Constants.md) | | |
| --- | --- | --- |
| Constant | Description | Read Only |
| phy\_joint\_translation | The distance between the anchor x/y coordinates and the local x/y coordinates. | Yes |
| phy\_joint\_speed | The current joint movement speed. | Yes |

## Distance Joints, Weld Joints and Wheel Joints

For a distance, weld, and wheel joints you can use the following constants (as well as those for pulley joints):

| [Physics Joint Constant](Physics_Joint_Constants.md) | | |
| --- | --- | --- |
| Constant | Description | Read Only |
| phy\_joint\_damping\_ratio | The damping ratio is non\-dimensional and defines the "springiness" of the joint. The value for this constant is typically between 0 and 1, but can be larger, and at 1, the damping is critical meaning that all oscillations should vanish. | No |
| phy\_joint\_frequency | This will return (or set) the oscillation frequency for the joint, in hertz, and typically the frequency should be less than a half the frequency of the time step, as set by the function [physics\_world\_update\_speed](../The_Physics_World/physics_world_update_speed.md). | No |
| phy\_joint\_length\_1 | This will return the length of the joint from the first local x/y coordinates to the first anchor x/y coordinates (Distance joints only, can only be read from) | Yes |
| phy\_joint\_length\_2 | This will return the length of the joint from the second local x/y coordinates to the second anchor x/y coordinates (Distance joints only, can only be written to) | No |

## Friction Joints

For a friction joint you can use the following constants:

| [Physics Joint Constant](Physics_Joint_Constants.md) | | |
| --- | --- | --- |
| Constant | Description | Read Only |
| phy\_joint\_max\_torque | The maximum torque value for the joint. | No |
| phy\_joint\_max\_force | The maximum force value for the joint. | No |

## Rope Joints

For a rope joint you can use the following constant:

| [Physics Joint Constant](Physics_Joint_Constants.md) | | |
| --- | --- | --- |
| Constant | Description | Read Only |
| phy\_joint\_max\_length | The maximum extension for the connection between the two anchor points. | No |
