# draw\_enable\_skeleton\_blend\_override

This function sets whether the default blend mode is automatically overridden if a skeletal animation sprite atlas uses premultiplied alpha.

Skeletal animation sprites that use premultiplied alpha require different blend factors than those used by the default blend mode bm\_normal to be drawn correctly. With this setting enabled, GameMaker will automatically set the appropriate blend mode for drawing skeletal animation sprites.

  This is only applied if the blend mode is set to the default, i.e. bm\_normal.

 

#### Syntax:

draw\_enable\_skeleton\_blend\_override(enable)

| Argument | Type | Description |
| --- | --- | --- |
| enable | [Boolean](../../../../../GML_Overview/Data_Types.md) | Whether to enable the blend mode override |

 

#### Returns:

N/A

 

#### Example:

gpu\_set\_blendmode(bm\_normal);  

 draw\_enable\_skeleton\_blend\_override(true);

The code above sets the blend mode to the default bm\_normal and then enables automatically setting the blend mode for skeletal animation sprites using draw\_enable\_skeleton\_blend\_override.
