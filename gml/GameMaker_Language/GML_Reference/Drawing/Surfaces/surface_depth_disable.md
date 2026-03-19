# surface\_depth\_disable

This function disables (true) or re\-enables (false) automatic depth and stencil buffer creation for *all* surfaces.

By default, *the depth and stencil buffer are enabled*, i.e. a depth *and* stencil buffer are automatically created for surfaces. This applies to surfaces that you create manually using [surface\_create](surface_create.md) as well as to the [application\_surface](application_surface.md).

To use this function you call it *before* creating a surface, and then you can enable it again later (if required). All surfaces created when this setting is disabled will not be created with a depth buffer and so cannot use it when drawn to. This results in the things being drawn to the surface having parity of depth. The images below illustrate this in practice:

In the above image, we draw a rectangle and a triangle using a vertex buffer in 3D. The coordinates for the red triangle place it behind the green rectangle, but the code to draw the triangle is called *after* the code that draws the rectangle. With the depth buffer enabled, the triangle is still drawn behind the rectangle as the 3D depth is being respected. However, when we disable the depth buffer for the surface, only the code order is respected and so the triangle is drawn over the rectangle.

  Allocating depth buffers essentially doubles the amount of memory required for surfaces. This could be an excessive and unnecessary overhead, especially if your game is very memory intensive.

To properly preserve depth in 3D when drawing to a surface, not only should you have the depth buffer enabled, you should also have z\-writing and z\-testing enabled. See the functions [gpu\_set\_zwriteenable](../GPU_Control/gpu_set_zwriteenable.md) and [gpu\_set\_ztestenable](../GPU_Control/gpu_set_ztestenable.md) more information.

If your game is 100% 2D or you know that you don't need a surface depth buffer, then it should be fine to simply call this function once at the start of the game to disable the buffer.

 
See: [The Depth And Stencil Buffer](../Depth_And_Stencil_Buffer/The_Depth_And_Stencil_Buffer.md)

 

#### Syntax:

surface\_depth\_disable(disable)

| Argument | Type | Description |
| --- | --- | --- |
| disable | [Boolean](../../../GML_Overview/Data_Types.md) | If set to true the depth buffer will be disabled for newly created surfaces. |

 

#### Returns:

N/A

 

#### Example:

var \_depth\_setting \= surface\_get\_depth\_disable();  

 surface\_depth\_disable(false);  

 surface\_with\_depth\_and\_stencil \= surface\_create(room\_width, room\_height);  

 surface\_depth\_disable(true);  

 surface\_without\_depth\_and\_stencil \= surface\_create(room\_width, room\_height);  

 surface\_depth\_disable(\_depth\_setting);

The above code stores the current depth buffer setting in a variable and then creates two surfaces, one with depth buffering enabled and one without, before restoring the original setting again.
