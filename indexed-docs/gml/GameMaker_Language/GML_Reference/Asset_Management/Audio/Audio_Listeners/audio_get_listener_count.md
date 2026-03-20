# audio\_get\_listener\_count

Certain target platforms permit more than one listener, so it is important that you know how many the target has before changing or using different listeners. This function will return the number of listeners available.

 

#### Syntax:

audio\_get\_listener\_count()

 

#### Returns:

 

#### Example:

global.listener\_num \= audio\_get\_listener\_count();

The above code gets the number of available listeners and stores the return value in a global variable.
