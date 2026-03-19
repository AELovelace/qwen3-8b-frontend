# timeline\_position

This variable holds the current position (moment) a time line is currently at. You can change this value to skip parts of the time line, or to repeat parts or to start the time line again from the beginning.

 

#### Syntax:

timeline\_position

 

#### Returns:

 (single precision floating point value)

 

#### Example:

if (!timeline\_running)   

 {  

     timeline\_position \= 0;  

     timeline\_running \= true;  

 }

The above code will check to see if the instance is running a time line, and if it is not then it resets the assigned time line to start at the first moment and then starts it.
