# time\_source\_pause

This function pauses the given Time Source. The Time Source must be active when this function is called.

To resume it, call [time\_source\_resume()](time_source_resume.md).

 

#### Syntax:

time\_source\_pause(id)

| Argument | Type | Description |
| --- | --- | --- |
| id | [Time Source ID](../../../../GameMaker_Language/GML_Reference/Time_Sources/time_source_create.md) | The Time Source to pause |

 

#### Returns:

N/A

 

#### Example:

if (keyboard\_check\_pressed(vk\_space))  

 {  

     var \_state \= time\_source\_get\_state(time\_source);  

  

     if (\_state \=\= time\_source\_state\_active)  

     {  

         time\_source\_pause(time\_source);  

     }  

     else if (\_state \=\= time\_source\_state\_paused)  

     {  

         time\_source\_resume(time\_source);  

     }  

 }
 

When the Space key is pressed, this code will get a Time Source's state.

When the state is active, it will pause the Time Source, and when it's paused, it will resume it.
