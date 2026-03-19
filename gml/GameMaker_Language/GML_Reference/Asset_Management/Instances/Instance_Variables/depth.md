# depth

This **built\-in variable** stores the depth of the instance.

You would normally not need to use this variable as you should be setting instances to be added to discreet [layers](layer.md), which in turn are set to a specific depth, but it may be that you want to change the depth of an instance using this value, in which case a "temporary layer" will be created specifically for the instance at the given depth. Note that when no instances are on the same depth then this temporary layer will be removed from memory (unlike regular layers which will remain even if they have nothing on them).

In GameMaker the lower the depth value for an instance, the "closer to the camera" that instance will be drawn, while a higher depth value means that the instance will be drawn "further away from the camera", i.e.: \-1000 is drawn on top of \-100, which is drawn on top of 0, and so on.

Note that instances that have the **same** depth may be drawn **above *or* below one another** regardless of how they appear in [The Room Editor](../../../../../The_Asset_Editors/Rooms.md). This is not guaranteed to be consistent between target platforms as it will depend on the graphics device in use. If you want to guarantee that something is drawn over or under everything else, you should always set the depth (or layer) explicitly.

 
### Usage Notes

- You **cannot** set the depth of an instance in its Draw event (all other events are fine). You can, however, set the depth at which to draw things in [Draw Events](../../../../../The_Asset_Editors/Object_Properties/Draw_Events.md) using [gpu\_set\_depth](../../../Drawing/GPU_Control/gpu_set_depth.md).
- There is a minimum (\-16000) and maximum (16000) depth value outside of which instances will not be drawn, although they will still exist and process events.
- You can assign a floating point value as the depth, though the decimals will have no effect as GameMaker truncates the value (i.e. removes the decimal part). Depth is treated as an as integer number internally.
- When you modify the depth
variable and GameMaker manages the layers, the built\-in [layer](layer.md) variable will hold an invalid layer handle (\-1) instead of a valid one, since managed layers cannot be manipulated through code.
- Modifying the depth of an instance may change which [Filters \& Effects](../../../../../The_Asset_Editors/Room_Properties/Filters_and_Effects.md) are applied on it, as changing the depth to be lower than an FX layer's depth will no longer apply its effect on the instance.

 

#### Syntax:

depth

 

#### Returns:

[Real](../../../../GML_Overview/Data_Types.md) (single precision floating point value)

 

#### Example:

if (y !\= yprevious)  

 {  

     depth \= \-y;  

 }

The above code will check to see if the y position has changed and if it has then the depth will also be set to correspond to it.
