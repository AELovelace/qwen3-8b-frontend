# gpu\_get\_fog

This function can be used to retrieve the fog settings. The function returns a 4 element 1D array with the following information:

- \[0] \= enabled toggle (a Boolean, either true or false), default false
- \[1] \= Colour Constant, default c\_black
- \[2] \= start distance (Real), default 0
- \[3] \= end distance (Real), default 1

Note that you can change these values and pass the full array to the [gpu\_set\_fog()](gpu_set_fog.md) function as a single argument.

 

#### Syntax:

gpu\_get\_fog()

 

#### Returns:

Array (4 elements only; see above for details)

 

#### Example:

var fog\_a \= gpu\_get\_fog();  

 fog\_a\[1] \= c\_red;  

 gpu\_set\_fog(fog\_a);

The above code gets the current fog settings and then sets the colour element of the array to c\_red before setting the fog again using the changed array.
