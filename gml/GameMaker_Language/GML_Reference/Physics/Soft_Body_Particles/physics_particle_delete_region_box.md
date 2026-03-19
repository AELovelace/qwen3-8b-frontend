# physics\_particle\_delete\_region\_box

With this function you can delete (remove) all the particles that fall within the bounds of the defined rectangular area from the physics simulation in the current room. The function takes the x and y position for the center of the area to delete as
 well as the half width and height of the rectangle (in pixels) which defines the area.

 

#### Syntax:

physics\_particle\_delete\_region\_box(x, y, halfWidth, halfHeight)

| Argument | Type | Description |
| --- | --- | --- |
| x |  | The x position of the center of the area to delete. |
| y |  | The y position of the center of the area to delete. |
| halfWidth |  | The *half* width of the rectangle. |
| halfHeight |  | The *half* height of the rectangle. |

 

#### Returns:

 

#### Example:

physics\_particle\_delete\_region\_box(mouse\_x, mouse\_y, 32, 32\);

The above code will delete all particles found in a rectangular area around the mouse position.
