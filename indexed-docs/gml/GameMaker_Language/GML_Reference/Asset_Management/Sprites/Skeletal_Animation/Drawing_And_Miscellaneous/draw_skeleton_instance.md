# draw\_skeleton\_instance

This function draws the skeletal animation sprite assigned to a particular instance.

This function is *only* for use with instances which have sprites assigned to them created using the skeletal animation program Spine. While you can draw these sprites using the normal draw functions (like [draw\_self](../../../../Drawing/Sprites_And_Tiles/draw_self.md)), there are times when you may want to draw a single frame or show a change of skin texture without actually changing the sprite properties for an instance. In these cases you can draw the sprite that has been assigned to the instance with this function, where you give the unique Instance ID and then the name of the animation to get the frame from (a string, as set within the program used to make the sprite). Next you give the name of the skin to use (again, as set when the sprite was made), and a frame value. The frame value is for telling GameMaker what part of the animation to show and is a value between 0 and the [image\_number](../../Sprite_Instance_Variables/image_number.md). The rest of the arguments are the same as those used for normal sprite drawing and will change the scale, angle, blend colour and alpha of the final animation frame being drawn.

Because of the way skeletal animations are interpolated between various "key" frames, there is an additional overhead associated with this call and therefore it is recommended that you avoid drawing skeleton based sprites using this method unless absolutely necessary.

 

#### Syntax:

draw\_skeleton\_instance(instance, animname, skinname, frame, x, y, xscale, yscale, rot, colour, alpha)

| Argument | Type | Description |
| --- | --- | --- |
| instance | [Object Instance](../../../Instances/Instance_Variables/id.md) | The index of the instance to draw the sprite from. |
| animname | [String](../../../../../GML_Overview/Data_Types.md) | The name of the animation to get the frame from (a string). |
| skinname | [String](../../../../../GML_Overview/Data_Types.md) | The name of the skin to use (a string). |
| frame | [Real](../../../../../GML_Overview/Data_Types.md) | The animation frame to draw (from 0 to image\_number \- 1\). |
| x | [Real](../../../../../GML_Overview/Data_Types.md) | The x coordinate of where to draw the sprite. |
| y | [Real](../../../../../GML_Overview/Data_Types.md) | The y coordinate of where to draw the sprite. |
| xscale | [Real](../../../../../GML_Overview/Data_Types.md) | The horizontal scaling of the sprite, as a multiplier: 1 \= normal scaling, 0\.5 is half etc... |
| yscale | [Real](../../../../../GML_Overview/Data_Types.md) | The vertical scaling of the sprite, as a multiplier: 1 \= normal scaling, 0\.5 is half etc... |
| rot | [Real](../../../../../GML_Overview/Data_Types.md) | The rotation of the sprite. 0\=normal, 90\=turned 90 degrees counter\-clockwise etc. |
| colour | [Colour](../../../../Drawing/Colour_And_Alpha/Colour_And_Alpha.md) | The colour with which to blend the sprite. |
| alpha | [Real](../../../../../GML_Overview/Data_Types.md) | The alpha of the sprite (from 0 to 1 where 0 is transparent and 1 opaque). |

 

#### Returns:

N/A

 

#### Example:

draw\_skeleton\_instance(obj\_Player, "jump", "skin1", 0, x, y, 1, 1, 0, c\_white, 1\);

The above code will draw the first frame of the skeletal animation sprite assigned to the instance given, using the "jump" animation set and the skin defined as "skin1".
