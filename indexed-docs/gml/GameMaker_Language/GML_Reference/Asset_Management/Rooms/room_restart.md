# room\_restart

This function will restart the current room, as if it had just been entered. Note that the room will not restart until the end of the event where the function was called, so any code after this has been called will still run if in the same event. This function will also trigger the **Room End** event.

 
 

#### Syntax:

room\_restart()

 

#### Returns:

N/A

 

#### Example:

if lives \< 1 room\_restart();

The above code checks to see if the variable "lives" is less than 1 and if it is it will restart the room.
