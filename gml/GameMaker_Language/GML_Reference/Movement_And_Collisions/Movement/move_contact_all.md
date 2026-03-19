# move\_contact\_all

This function will move the instance running the code a set number of pixels in the specified direction until it meets *any* other instance with a valid mask. You can use \-1 or 0 for the maxdist being a default 1000px, ie: GameMaker will move the instance continually up 1000 pixels until it is out of collision.

 

#### Syntax:

move\_contact\_all(dir, maxdist)

| Argument | Type | Description |
| --- | --- | --- |
| dir |  | The direction to move in. |
| maxdist |  | The maximum distance the object can travel (\-1 or 0 a default value of 1000 pixels). |

 

#### Returns:

 

#### Example:

if (!place\_meeting(x, y \+ 1, all))   

 {  

     move\_contact\_all(270, \-1\);  

 }

The above code will check beneath the instance for a collision, and if there is none, then it will move it down until there is or until 1000pixels have been covered.
