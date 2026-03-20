# gpu\_set\_alphatestenable

This function will enable or disable alpha testing for your game (by default this is disabled). By switching alpha testing on you can then use the companion function [gpu\_set\_alphatestref()](gpu_set_alphatestref.md) to set the "cut\-off" value at which all alpha values will be set to 0\. The image below shows the difference that can be seen when alpha testing is switched on or off:

**NOTE**: This function may negatively affect performance on iOS and Android devices.

 

#### Syntax:

gpu\_set\_alphatestenable(enable)

| Argument | Type | Description |
| --- | --- | --- |
| enable |  | Enable or disable alpha testing (true / false) |

 

#### Returns:

 

#### Example:

if (!gpu\_get\_alphatestenable())   

 {  

     gpu\_set\_alphatestenable(true);  

     gpu\_set\_alphatestref(128\);  

 }

The above code will check to see if alpha testing is enabled and if not it will switch on alpha testing and set the test threshold to 128 (only pixels with an alpha over 0\.5 will be drawn).
