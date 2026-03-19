# timeline\_running

This variable holds current state of the assigned time line and will return true if it is running and false if it is not. You can also set this variable to either true or false to start and stop the time line at any time. it should be noted that a stopped time line is *not* reset, and so starting it again at a later time will start it from the exact moment that it was stopped at.

 

#### Syntax:

timeline\_running

 

#### Returns:

 

#### Example:

if (!timeline\_running)   

 {  

     timeline\_position \= 0;  

     timeline\_running \= true;  

 }

The above code will check to see if the instance is running a time line, and if it is not then it resets the assigned time line to start at the first moment and then starts it.
