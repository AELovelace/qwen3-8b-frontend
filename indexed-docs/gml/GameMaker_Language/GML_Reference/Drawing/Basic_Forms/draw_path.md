# draw\_path

With this function you can get GameMaker to draw a path to the screen. The path will be drawn as a simple line, and can be either relative to the calling instance or at the absolute position it was created at in the path editor or through code. This function is extremely useful when debugging dynamic paths (for example, those created for instances with the [mp\_grid\_path()](../../Movement_And_Collisions/Motion_Planning/mp_grid_path.md) function).

 
 

#### Syntax:

draw\_path(path, x, y, absolute)

| Argument | Type | Description |
| --- | --- | --- |
| path | [Path Asset](The_Asset_Editors/Paths.md) | The path to draw |
| x | [Real](GameMaker_Language/GML_Overview/Data_Types.md) | The x coordinate of where the path is drawn |
| y | [Real](GameMaker_Language/GML_Overview/Data_Types.md) | The y coordinate of where the path is drawn |
| absolute | [Boolean](GameMaker_Language/GML_Overview/Data_Types.md) | Whether the path is drawn at the absolute position (true) or the relative position (false) |

 

#### Returns:

N/A

 

#### Example:

if (mp\_grid\_path(grid, path, x, y, obj\_Player.x, obj\_Player.y, 1\))   

 {  

     draw\_path(path, x, y, false);  

 }

The above code will use the mp\_grid\_path function to generate a path and store it in the variable "path". If the path is successfully created, it is then drawn on the screen at a position relative to the instance running the code.
