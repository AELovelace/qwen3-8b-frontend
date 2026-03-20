# room\_get\_viewport

This function retrieves the details of a viewport in a room other than the current one.

You give the room and the index of the viewport to retrieve (from 0 to 7\) and the function will return an [Array](../../../GML_Overview/Arrays.md) of 5 indices, where:

- \[0] \= visible (boolean: true / false)
- \[1] \= x position (real)
- \[2] \= y position (real)
- \[3] \= width (real)
- \[4] \= height (real)

 

#### Syntax:

room\_get\_viewport(rm, vind)

| Argument | Type | Description |
| --- | --- | --- |
| rm | [Room Asset](../../../../The_Asset_Editors/Rooms.md) | The room to get viewport data from |
| vind | [Real](../../../GML_Overview/Data_Types.md) | The index of the viewport to get |

 

#### Returns:

[Array](../../../GML_Overview/Arrays.md) (5 elements: visible, x, y, width, height)

 

#### Example:

var \_view\_values \= room\_get\_viewport(rm\_game, 0\);  

 var \_visible\_text \= \_view\_values\[0] ? "visible" : "invisible";  

 show\_debug\_message($"Viewport 0 in rm\_game is {\_visible\_text} and drawn at the position: {\_view\_values\[1]}, {\_view\_values\[2]}. Its dimensions are {\_view\_values\[3]}x{\_view\_values\[4]}.");

The above code retrieves the viewport data for the given room then checks to see if it is flagged as visible. If it is not, the viewport data is set to make it visible.
