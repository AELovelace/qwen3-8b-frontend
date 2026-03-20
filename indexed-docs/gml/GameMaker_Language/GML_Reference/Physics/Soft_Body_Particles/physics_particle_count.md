# physics\_particle\_count

This function will return the number of particles that are active in a physics enabled room.

 

#### Syntax:

physics\_particle\_count()

 

#### Returns:

 

#### Example:

if (physics\_particle\_count() \< physics\_particle\_get\_max\_count())  

 {  

     physics\_particle\_create(0, x, y, 0, 0, c\_white, 1, 1\)  

 }

The above code will check to see if there are less than the maximum number of permitted particles in the room, and if so create one more.
