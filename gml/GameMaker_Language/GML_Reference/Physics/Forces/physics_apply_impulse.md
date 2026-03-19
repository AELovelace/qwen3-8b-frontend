# physics\_apply\_impulse

This function applies an impulse to the current physics\-enabled instance.

Not only can you apply force and gravity to an object with the physics in GameMaker but you can also apply an impulse. This is slightly different to a force in that when it is applied it will *immediately* affect the speed, and, potentially the torque (or "spin") of the object, particularly if the point chosen to apply the impulse is not aligned with the center of mass (note: the center of mass is *not necessarily* the same as the origin!). Here is an illustration:

As you can see, the player has clicked on the ball and this has given it an impulse to move to the upper right, spinning as it goes. The exact impulse is defined by the vector we get from the components ximpulse/yimpulse in relation to the xpos/ypos coordinates \- which simply means that the impulse is calculated as the distance from xpos/ypos to ximpulse/yimpulse in newton, and the direction is the angle that we get from xpos/ypos to ximpulse/yimpulse.

 
 

#### Syntax:

physics\_apply\_impulse(xpos, ypos, ximpulse, yimpulse)

| Argument | Type | Description |
| --- | --- | --- |
| xpos | [Real](../../../GML_Overview/Data_Types.md) | The x coordinate *in the room* where the impulse will be applied |
| ypos | [Real](../../../GML_Overview/Data_Types.md) | The y coordinate *in the room* where the impulse will be applied |
| ximpulse | [Real](../../../GML_Overview/Data_Types.md) | The x component of the impulse vector |
| yimpulse | [Real](../../../GML_Overview/Data_Types.md) | The y component of the impulse vector |

 

#### Returns:

N/A

 

#### Example:

if (mouse\_check\_button\_pressed(mb\_left))  

 {  

     with (place\_meeting(mouse\_x, mouse\_y, all))  

     {  

         physics\_apply\_impulse(mouse\_x, mouse\_y, \-10 \+ irandom(20\), \-10 \+ irandom(20\));  

     }  

 }

The code above will apply an impulse with a random vector to an instance that is at the mouse position when the left button is pressed.
