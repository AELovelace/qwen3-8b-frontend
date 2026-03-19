# physics\_particle\_delete\_region\_circle

With this function you can delete (remove) all the particles that fall within the bounds of the defined circular area from the physics simulation in the current room. The function takes the x and y position for the center of the area to delete as well
 as the radius (in pixels) which defines the circular area.

 

#### Syntax:

physics\_particle\_delete\_region\_circle(x, y, radius)

| Argument | Type | Description |
| --- | --- | --- |
| x |  | The x position of the center of the area to delete. |
| y |  | The y position of the center of the area to delete. |
| radius |  | The radius (in pixels) of the circular area to delete. |

 

#### Returns:

 

#### Example:

physics\_particle\_delete\_region\_circle(mouse\_x, mouse\_y, 32\);

The above code will delete all particles found in a circular area around the mouse position.
