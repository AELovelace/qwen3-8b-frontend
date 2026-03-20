# object\_get\_physics

This function will tell you whether the object you are checking has been flagged as "physics enabled"  \- in which case it'll return true, \- or not \- in which case it will return false.

 

#### Syntax:

object\_get\_physics(obj)

| Argument | Type | Description |
| --- | --- | --- |
| obj |  | The index of the object to check. |

 

#### Returns:

 

#### Example:

if (object\_get\_physics(object\_index))   

 {  

     phy\_active \= true;  

 }

The above code will check the instance running it to see if the object it is created from is physics enabled, and if it is it activates the physics simulation for the instance.
