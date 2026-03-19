# gpu\_get\_colourwriteenable

This function can be used to retrieve the current colour write\-enable values.

The function returns a 4 element 1D array with the following elements in it which will be either true (enabled) or false (disabled). By default all colour writing is set to true:

- \[0] \= Red channel enabled/disabled
- \[1] \= Green channel enabled/disabled
- \[2] \= Blue channel enabled/disabled
- \[3] \= Alpha channel enabled/disabled

 

#### Syntax:

gpu\_get\_colourwriteenable()

 

#### Returns:

[Array](../../../GML_Overview/Arrays.md) (4 elements only; see above for details)

 

#### Example:

var \_cw \= gpu\_get\_colourwriteenable();  

 \_cw\[3] \= false;  

 gpu\_set\_colourwriteenable(\_cw);

The above code gets the current colour write values and then sets the alpha component to false.
