# buffer\_set\_surface\_depth

This function copies data from a [Buffer](buffer_create.md) into a surface's depth buffer.

Depth values in the buffer must be of type buffer\_f32 and range from 0 (representing the near plane) to 1 (representing the far plane).

The copying process stops once either the buffer's boundaries or the surface's boundaries are reached.

  This function may not be supported on all platforms. To see if the copy was successful you can check the returned boolean value.

 

#### Syntax:

buffer\_set\_surface\_depth(buffer, surface, offset)

| Argument | Type | Description |
| --- | --- | --- |
| buffer | [Buffer](buffer_create.md) | The buffer from which the data will be copied |
| surface | [Surface](../Drawing/Surfaces/surface_create.md) | The surface that has the depth buffer to write to |
| offset | [Real](../../GML_Overview/Data_Types.md) | The offset, in bytes, in the buffer to start copying data. This is automatically clamped to the buffer's boundaries. |

 

#### Returns:

[Boolean](../../GML_Overview/Data_Types.md) (whether the copy was successful)

 

#### Example:
