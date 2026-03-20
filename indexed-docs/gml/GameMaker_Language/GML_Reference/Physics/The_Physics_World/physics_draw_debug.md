# physics\_draw\_debug

This function debug\-draws a visual representation of the current physics\-enabled instance.

When creating a physics system in GameMaker, it is often important to have a visual representation of what is actually happening with an instance. This can be achieved by using physics\_draw\_debug, which draws a schematic outline of the physical properties associated with the instance running the code. Here is an image of how it looks:

It should be noted that for this to work it *must* be in the Draw event of the instance, and it will be drawn using the currently defined draw colour.

 

#### Syntax:

physics\_draw\_debug()

 

#### Returns:

N/A

 

#### Example:

draw\_set\_colour(c\_red);  

 physics\_draw\_debug();

The code above will draw a representation of the physical properties associated with that instance using the colour red.
