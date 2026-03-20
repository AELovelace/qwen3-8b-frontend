# sprite\_get\_bbox\_right

This function returns the relative position of the right of the sprite bounding box.

This value is given as a relative value based on the upper left corner of the base sprite asset being (0, 0\). it is the same value as can be found in the Sprite Editor for the [collision mask properties](../../../../../The_Asset_Editors/Sprites.md). The image below shows how it is calculated:

#### Syntax:

sprite\_get\_bbox\_right(ind)

| Argument | Type | Description |
| --- | --- | --- |
| ind | [Sprite Asset](../../../../../The_Asset_Editors/Sprites.md) | The index of the sprite to check. |

 

#### Returns

[Real](../../../../GML_Overview/Data_Types.md)

 

#### Example:

var \_ww, \_hh;  

 \_ww \= sprite\_get\_bbox\_right(sprite\_index) \- sprite\_get\_bbox\_left(sprite\_index);  

 \_hh \= sprite\_get\_bbox\_bottom(sprite\_index) \- sprite\_get\_bbox\_top(sprite\_index);

The above code calculates the width and height of the collision mask based on the relative bounding box side positions.
