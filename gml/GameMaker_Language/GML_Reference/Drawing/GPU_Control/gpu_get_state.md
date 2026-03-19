# gpu\_get\_state

This function gets the current GPU state and returns it as a [DS Map](../../Data_Structures/DS_Maps/DS_Maps.md).

This can then be manipulated or even saved, and you can return this map to the GPU using the function [gpu\_set\_state](gpu_set_state.md).

 

#### Syntax:

gpu\_get\_state()

 

#### Returns:

GPU State DS Map

 

#### Example:

gpu\_map \= gpu\_get\_state();

The above code stores the current GPU state in a variable.
