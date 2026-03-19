# display\_get\_timing\_method

This function returns the timing method to be used for rendering your game.

The method can be one of the constants listed below:

 
For more information on the different timing methods, please see [display\_set\_timing\_method](display_set_timing_method.md).

 

#### Syntax:

display\_get\_timing\_method()

 

#### Returns:

[Display Timing Method Constant](display_get_timing_method.md)

 

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
