# tileset\_get\_name

This function will return the name *as a string* of the specified tile set asset. This name is the one that has been specified for the tile set in the Asset Browser of the main GameMaker window.

  This is *only* a string and cannot be used to reference the tile set directly \- for that you would need the *tile set index*. You can, however, use this string to get the *tile set index* using the returned string along with the function [asset\_get\_index](../Assets_And_Tags/asset_get_index.md).

 

#### Syntax:

tileset\_get\_name(index)

| Argument | Type | Description |
| --- | --- | --- |
| index | [Tile Set Asset](../../../../../The_Asset_Editors/Tile_Sets.md) | The index of the tile set to get the name of. |

 

#### Returns

[String](../../../../../GameMaker_Language/GML_Overview/Data_Types.md)

 

#### **Example:**

var \_l \= layer\_get\_id("tilemap\_trees");  

 var \_m \= layer\_tilemap\_get\_id(\_l);  

 var \_t \= tilemap\_get\_tileset(\_m);  

 tileset\_name \= tileset\_get\_name(\_t);

The above code will get the name of the tile set index for the given layer, storing the return string in the variable tileset\_name.
