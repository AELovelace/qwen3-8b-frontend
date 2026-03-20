# buffer\_get\_surface\_depth

This function copies the data from a surface's depth buffer into a [Buffer](buffer_create.md).

Depth values are written to the buffer as 32\-bit floating point values (buffer\_f32), with values ranging from 0 (representing the near plane) to 1 (representing the far plane).

The copying process stops once either the buffer's boundaries or the surface's boundaries are reached.

  This function may not be supported on all platforms. To see if the copy was successful you can check the returned boolean value.

 

#### Syntax:

buffer\_get\_surface\_depth(buffer, surface, offset)

| Argument | Type | Description |
| --- | --- | --- |
| buffer | [Buffer](buffer_create.md) | The buffer into which the depth buffer data will be copied |
| surface | [Surface](../Drawing/Surfaces/surface_create.md) | The surface from which the depth data will be copied |
| offset | [Real](../../GML_Overview/Data_Types.md) | The offset, in bytes, in the buffer to start writing the depth data |

 

#### Returns:

[Boolean](../../GML_Overview/Data_Types.md) (whether the copy was successful)

 

#### Example:
