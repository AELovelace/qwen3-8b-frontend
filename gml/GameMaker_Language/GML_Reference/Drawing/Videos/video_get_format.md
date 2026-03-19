# video\_get\_format

This function returns the colour format of the currently loaded video. This can be any one of the following constants:

| Video Format Constant | |
| --- | --- |
| Constant | Description |
| video\_format\_rgba | The video surface uses the RGBA color model |
| video\_format\_yuv | The video surface uses the YUV color model |

 

As the drawing methods for RGBA and YUV videos are different, the return value from this function may be used to run different code based on the format of the playing video. See [Draw Video](YUV_Videos.md#h) for an example.

 

#### Syntax:

video\_get\_format()

 

#### Returns:

Video Format Constant
