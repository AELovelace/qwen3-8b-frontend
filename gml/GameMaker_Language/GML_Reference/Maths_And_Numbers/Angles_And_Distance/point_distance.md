# point\_distance

This function returns the length of a vector formed by the specified components (x1, y1\) and (x2, y2\).

For example, in the image below if we want to get the distance between the player ship position and the enemy position so that we can calculate if the enemy is close enough to shoot at then we would use this function (the exact code is in the example below the image):

 

#### **Syntax:**

point\_distance(x1, y1, x2, y2\)

| Argument | Type | Description |
| --- | --- | --- |
| x1 | [Real](../../../GML_Overview/Data_Types.md) | The x coordinate of the first component of the vector |
| y1 | [Real](../../../GML_Overview/Data_Types.md) | The y coordinate of the first component of the vector |
| x2 | [Real](../../../GML_Overview/Data_Types.md) | The x coordinate of the second component of the vector |
| y2 | [Real](../../../GML_Overview/Data_Types.md) | The y coordinate of the second component of the vector |

 

#### Returns:

[Real](../../../GML_Overview/Data_Types.md)

 

#### Example:

var \_nearest\= instance\_nearest(x, y, obj\_enemy);  

if (\_nearest !\= noone)  

{  

    if (point\_distance(x, y, \_nearest.x, \_nearest.y) \< 200\)  

    {  

        instance\_create\_layer(x, y, "Bullets", obj\_missile);  

    }  

}

The above code finds the nearest enemy using [instance\_nearest](../../Asset_Management/Instances/instance_nearest.md) and, if the return value isn't [noone](../../../GML_Overview/Instance Keywords/noone.md) (i.e. such an instance exists), checks the distance (length of the vector) between this instance and the player instance. If the value is less than 200, the player instance will create an instance of obj\_missile.
