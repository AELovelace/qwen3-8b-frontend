# display\_set\_timing\_method

This function sets the timing method to be used for rendering your game.

The method can be one of the following constants:

 
By default on all platforms *except* PS4, Ubuntu and HTML5, GameMaker will use the vsync timing method, while on the unsupported platforms, *only* sleep margin timing can be used.

Setting the mode to sleep margin will try to ensure that each frame lasts for the correct amount of time (say 1/30th or 1/60th of a second) by waiting or sleeping, while the vsync timing method uses the target platform's support for vertical synchronisation to provide an anchor for the game's render timing calculations. In general the default vsync timing will give the smoothest results, but note that when using the vsync method, the [sleep margin](display_set_sleep_margin.md) values are still relevant, although it will have a reduced impact and we recommend keeping it at its default value when using this method.

On Windows, you can use tm\_countvsyncs\_winalt which is an alternate vsync timing method that you can experiment with if you are facing performance issues.

Using "system timing" allows the frame rate to be as high as supported by the machine. This method removes all of GameMaker's sleeps and game speed control and allows the game speed to be set by the system. Certain Android devices make use of specific frame rates, where you may want to use the system timing method. Note that on most platforms this may not always result in the highest frame rate, as depending on the display driver, its configuration and window focus, the frame rate may be restrained.

If you wish to set the sleep margin you can do so using the function [display\_set\_sleep\_margin](display_set_sleep_margin.md) and you can find which timing method is currently being used with the function [display\_get\_timing\_method](display_get_timing_method.md).

 

#### Syntax:

display\_set\_timing\_method(method)

| Argument | Type | Description |
| --- | --- | --- |
| method | [Display Timing Method Constant](display_get_timing_method.md) | The timing method to use (see the list of constants, above) |

 

#### Returns:

N/A

 

#### Example:

if (display\_get\_timing\_method() !\= tm\_sleep)  

 {  

     display\_set\_timing\_method(tm\_sleep);  

     if (display\_get\_sleep\_margin() !\= 20\)  

     {  

         display\_set\_sleep\_margin(20\);  

     }  

 }

The above code will check the timing method and if it's not set to tm\_sleep it will be set to that and the sleep margin set to 20\.
