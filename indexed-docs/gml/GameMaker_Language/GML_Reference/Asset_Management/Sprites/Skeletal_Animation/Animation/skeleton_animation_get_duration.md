# skeleton\_animation\_get\_duration

This function will return the time required for the given animation set to run before looping back to the beginning. The return value is in seconds.

 

#### Syntax:

skeleton\_animation\_get\_duration(animname)

| Argument | Type | Description |
| --- | --- | --- |
| animname |  | The name (a string) of the animation set to use. |

 

#### Returns:

 

#### Example1:

time \+\= delta\_time / 1000000;  
 var duration \= skeleton\_animation\_get\_duration(skeleton\_animation\_get());  
 var frame \= floor((image\_number \* (mTime / duration)) \+ 0\.5\) % image\_number;  
 image\_index \= frame;  
 draw\_self();
 

The above code will set the image\_index to the correct value for the currently assigned skeletal animation sprite.

#### Example2:

time \+\= delta\_time / 1000000;  
 var d \= skeleton\_animation\_get\_duration("walk");  
 if time \> d time \-\= d;  
 draw\_skeleton\_time(sprite\_index, "walk", "skin1", time, x, y, image\_xscale, image\_yscale, image\_angle,
 c\_white);

The above code will draw the given skeletal animation sprite using delta\-time to set the frame being drawn.
