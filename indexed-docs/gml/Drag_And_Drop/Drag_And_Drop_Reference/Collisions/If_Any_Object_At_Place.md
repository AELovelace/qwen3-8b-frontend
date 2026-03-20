# If Any Object At Place

This action is used to check and see if there is an instance of *any* object placed at a position based on the collision mask of the calling instance. You give the position, which can be an absolute position or a position relative to the instance, and the action will return true if there is a collision or false if there is not. You can also check the "Not" flag to check if there is *not* a collision at the given position, and the action will then return true if no collisions are found and false otherwise. Collisions are calculated based on the collision mask of the calling instance overlapping the collision mask of any instance at the position (as if it was being "placed" at the position).

  Collisions will only register for those instances that have a valid collision mask, ie: they have a sprite assigned to the sprite\_index, or a sprite assigned to the mask\_index. If **either** of the instances in the collision have no collision mask then the collision will not be detected, regardless of what the instance is drawing at the time.

Note that to add actions into an "if" block, they should be dropped to the *side* of the action, as shown in the image below:

 

#### Action Syntax:

#### Arguments:

| Argument | Description |
| --- | --- |
| x | The x position to check |
| y | The y position to check |

 

#### Example:

The above action block code checks for a collision at the position where the instance is placed and if one is found it blends the instance with red, otherwise it leaves the blending as normal (white).
