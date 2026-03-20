# surface\_get\_target\_depth

This function returns the surface whose depth buffer is currently used for drawing. A surface different than the current draw target can be set for depth when calling [surface\_set\_target](surface_set_target.md).

 
 

#### Syntax:

surface\_get\_target\_depth()

 

#### Returns:

[Real](../../../GML_Overview/Data_Types.md) (\-1 if no depth buffer is used)

 

#### Example:

var \_surf\_depth \= surface\_get\_target\_depth();

The code above gets the surface whose depth buffer is currently used for drawing and stores the result in a temporary variable \_surf\_depth.
