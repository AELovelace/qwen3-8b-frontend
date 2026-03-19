# Draw Self

When you add any type of action or code to the Draw Event of an object, you are telling GameMaker that you are taking over and that *you* will tell it what to draw from now on (by default an instance will draw the sprite assigned to it in the object editor when there are no actions in the main Draw Event). This means that any assigned sprite will no longer be drawn unless you explicitly say so, which is when you would use this action. This simply draws the assigned sprite for the object with any transforms that may have been set in previous events (like scaling, blending or changes in alpha) at the current sub\-image.

 
 

#### Action Syntax:

#### Example:

The above action block code draws a "shadow" sprite at the same relative position as the instance, then draws the instance sprite over the top.
