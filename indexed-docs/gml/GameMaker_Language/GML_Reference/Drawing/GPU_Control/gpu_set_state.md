# gpu\_set\_state

This function will set the current GPU state using the passed\-in [DS Map](../../Data_Structures/DS_Maps/ds_map_create.md).

The supplied map can be created using the function [gpu\_get\_state](gpu_get_state.md). It contains the following keys: 

GPU State DS Map

| Key | Type | Description |
| --- | --- | --- |
| Colour \& Alpha | | |
| colorwriteenable | [Real](../../../GML_Overview/Data_Types.md) | A bitmask consisting of 4 bits, ordered ABGR, where each bit indicates whether the channel is written to or not. Corresponds to [gpu\_set\_colourwriteenable](gpu_set_colourwriteenable.md). |
| blendenable | [Boolean](../../../GML_Overview/Data_Types.md) | Whether colour blending is enabled. As set with [gpu\_set\_blendenable](gpu_set_blendenable.md). |
| sepalphaenable | [Boolean](../../../GML_Overview/Data_Types.md) | A **read\-only** value that indicates whether separate blend mode factors for the RGB and alpha channels are enabled. It will be true if you've set the blend mode using [gpu\_set\_blendmode\_ext\_sepalpha](gpu_set_blendmode_ext_sepalpha.md), false in all other cases. |
| srcblend | [Blend Mode Factor Constant](gpu_get_blendmode_ext.md) | The source blend mode factor. |
| srcblendalpha | [Blend Mode Factor Constant](gpu_get_blendmode_ext.md) | The source blend mode factor of the alpha channel. |
| destblend | [Blend Mode Factor Constant](gpu_get_blendmode_ext.md) | The destination blend mode factor. |
| destblendalpha | [Blend Mode Factor Constant](gpu_get_blendmode_ext.md) | The destination blend mode factor of the alpha channel. |
| alphatestenable | [Boolean](../../../GML_Overview/Data_Types.md) | Whether to enable alpha testing. As set with [gpu\_set\_alphatestenable](gpu_set_alphatestenable.md). |
| alphatestfunc | [Comparison Function Constant](gpu_get_zfunc.md) | A **read\-only** value that indicates the comparison function used by GameMaker for the alpha test. Always set to cmpfunc\_greater. |
| alphatestref | [Real](../../../GML_Overview/Data_Types.md) | The reference value to use for the alpha test, as a value from 0 to 255\. As set with [gpu\_set\_alphatestref](gpu_set_alphatestref.md). |
| Depth and Stencil Buffer | | |
| zwriteenable | [Boolean](../../../GML_Overview/Data_Types.md) | Whether z\-writing is enabled. As set with [gpu\_set\_zwriteenable](gpu_set_zwriteenable.md). |
| ztestenable | [Boolean](../../../GML_Overview/Data_Types.md) | Whether z\-testing is enabled. As set with [gpu\_set\_ztestenable](gpu_set_ztestenable.md). |
| zfunc | [Comparison Function Constant](gpu_get_zfunc.md) | The comparison function to use for z\-testing. As set with [gpu\_set\_zfunc](gpu_set_zfunc.md). |
| stencilenable | [Boolean](../../../GML_Overview/Data_Types.md) | Whether to enable the stencil test. As set with [gpu\_set\_stencil\_enable](gpu_set_stencil_enable.md). |
| stencilfunc | [Comparison Function Constant](gpu_get_zfunc.md) | The comparison function to use for the stencil test. As set with [gpu\_set\_stencil\_func](gpu_set_stencil_func.md). |
| stencilref | [Real](../../../GML_Overview/Data_Types.md) | The reference value used for the stencil test. As set with [gpu\_set\_stencil\_ref](gpu_set_stencil_ref.md). |
| stencilpass | [Stencil Op Constant](../Depth_And_Stencil_Buffer/The_Depth_And_Stencil_Buffer.md) | The stencil operation to perform when the stencil test passes. As set with [gpu\_set\_stencil\_pass](gpu_set_stencil_pass.md). |
| stencilfail | [Stencil Op Constant](../Depth_And_Stencil_Buffer/The_Depth_And_Stencil_Buffer.md) | The stencil operation to perform when the stencil test fails. As set with [gpu\_set\_stencil\_fail](gpu_set_stencil_fail.md). |
| stencilzfail | [Stencil Op Constant](../Depth_And_Stencil_Buffer/The_Depth_And_Stencil_Buffer.md) | The stencil operation to perform when the stencil test passes but the depth test fails. As set with [gpu\_set\_stencil\_depth\_fail](gpu_set_stencil_depth_fail.md). |
| stencilwritemask | [Real](../../../GML_Overview/Data_Types.md) | An 8 bit bitmask that determines which bits in the stencil buffer can be written to. As set with [gpu\_set\_stencil\_write\_mask](gpu_set_stencil_write_mask.md). |
| stencilreadmask | [Real](../../../GML_Overview/Data_Types.md) | An 8 bit bitmask that determines the bits to compare in the stencil test. As set with [gpu\_set\_stencil\_read\_mask](gpu_set_stencil_read_mask.md). |
| Backface Culling | | |
| cullmode | [Culling Mode Constant](gpu_get_cullmode.md) | The backface culling mode. As set with [gpu\_set\_cullmode](gpu_set_cullmode.md). |
| Fog | | |
| fogenable | [Boolean](../../../GML_Overview/Data_Types.md) | Whether fog is set to enabled. The first element in the array passed to [gpu\_set\_fog](gpu_set_fog.md). |
| fogcolor | [Colour](../Colour_And_Alpha/Colour_And_Alpha.md) | The fog colour to use, if enabled. The second element in the array passed to [gpu\_set\_fog](gpu_set_fog.md). |
| fogstart | [Real](../../../GML_Overview/Data_Types.md) | The distance at which the fog starts. The third element in the array passed to [gpu\_set\_fog](gpu_set_fog.md). |
| fogend | [Real](../../../GML_Overview/Data_Types.md) | The distance at which the fog ends. The fourth element in the array passed to [gpu\_set\_fog](gpu_set_fog.md). |
| Textures | | |
| minfilter | [Mipmapping Filter Constant](../Mipmapping/gpu_set_tex_mip_filter.md) | The filtering mode used when textures are drawn minified. Determined by [gpu\_set\_texfilter](gpu_set_texfilter.md). |
| magfilter | [Mipmapping Filter Constant](../Mipmapping/gpu_set_tex_mip_filter.md) | The filtering mode used when textures are drawn magnified. Determined by [gpu\_set\_texfilter](gpu_set_texfilter.md). |
| addressu | [Real](../../../GML_Overview/Data_Types.md) | The texture wrapping/clamping mode in the horizontal direction. As set with [gpu\_set\_texrepeat](gpu_set_texrepeat.md). |
| addressv | [Real](../../../GML_Overview/Data_Types.md) | The texture wrapping/clamping mode in the vertical direction. As set with [gpu\_set\_texrepeat](gpu_set_texrepeat.md). |
| Mipmapping | | |
| mipenable | [Mipmapping Constant](../Mipmapping/gpu_get_tex_mip_enable.md) | Whether to enable mipmapping. As set with [gpu\_set\_tex\_mip\_enable](../Mipmapping/gpu_set_tex_mip_enable.md). |
| mipmip | [Real](../../../GML_Overview/Data_Types.md) | The minimum mipmap level to use. As set with [gpu\_set\_tex\_min\_mip](../Mipmapping/gpu_set_tex_min_mip.md). |
| maxmip | [Real](../../../GML_Overview/Data_Types.md) | The maximum mipmap level to use. As set with [gpu\_set\_tex\_max\_mip](../Mipmapping/gpu_set_tex_max_mip.md). |
| mipfilter | [Mipmapping Filter Constant](../Mipmapping/gpu_set_tex_mip_filter.md) | The mip filter to use with mipmapping. As set with [gpu\_set\_tex\_mip\_filter](../Mipmapping/gpu_set_tex_mip_filter.md). |
| mipbias | [Real](../../../GML_Overview/Data_Types.md) | The bias value to use for mipmapping. As set with [gpu\_set\_tex\_mip\_bias](../Mipmapping/gpu_set_tex_mip_bias.md). |
| maxaniso | [Real](../../../GML_Overview/Data_Types.md) | The maximum level of anisotropy to use with the tf\_anisotropic filter. As set with [gpu\_set\_tex\_max\_aniso](../Mipmapping/gpu_set_tex_max_aniso.md). |

 

#### Syntax:

gpu\_set\_state(ds\_map)

| Argument | Type | Description |
| --- | --- | --- |
| ds\_map | [DS Map](../../Data_Structures/DS_Maps/ds_map_create.md) | The GPU state to set as a DS Map. |

 

#### Returns:

N/A

 

#### Example:

gpu\_set\_state(gpu\_map);

The above code sets the GPU state using the map supplied in the variable gpu\_map.
