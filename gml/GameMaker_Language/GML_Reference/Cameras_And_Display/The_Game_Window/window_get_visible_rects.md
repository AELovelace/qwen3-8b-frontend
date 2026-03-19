# window\_get\_visible\_rects

With this function you can find the overlapping region of the rectangle defined by (x1,y1\) to (x2,y2\) on each of the attached displays.

The function will return an array with 8 values per display (i.e.: if you have two displays, the array will have a length of 16 indices), where the values \[0 ... 3] correspond to the overlapx1, overlapy1, overlapx2, overlapy2 \- defining the region of overlap on this display and will be set to 0, 0, 0, 0 if no overlap \- and the values \[4 ... 7] corresponds to the monitorx1, monitory1, monitorx2, monitory2 \- the coordinates of the display in the virtual display space. This can be used to test whether a saved window position is going to be visible or not (the user may have disconnected an external monitor or moved the window off screen which left the window position that was saved as not being valid), for example.

 

#### Syntax:

window\_get\_visible\_rects(x1, y1, x2, y2\)

| Argument | Type | Description |
| --- | --- | --- |
| x1 | [Real](../../../GML_Overview/Data_Types.md) | The left edge of the rectangle to check |
| y1 | [Real](../../../GML_Overview/Data_Types.md) | The top edge of the rectangle to check. |
| x2 | [Real](../../../GML_Overview/Data_Types.md) | The right edge of the rectangle to check |
| y2 | [Real](../../../GML_Overview/Data_Types.md) | The bottom edge of the rectangle to check. |

 

#### Returns:

[Array](../../../GML_Overview/Arrays.md)

 

#### Example:

var \_wx \= window\_get\_x();  

 var \_wy \= window\_get\_y();  

 var \_ww \= window\_get\_width();  

 var \_wh \= window\_get\_height();  

 display\_data \= window\_get\_visible\_rects(\_wx, \_wy, \_wx \+ \_ww, \_wy \+ \_wh);  

 display\_num \= array\_length(display\_data) / 8;

The above code will generate a 1D array held in the variable display\_data containing the information about the displays, as well as create the variable display\_num to hold the number of active displays found.
