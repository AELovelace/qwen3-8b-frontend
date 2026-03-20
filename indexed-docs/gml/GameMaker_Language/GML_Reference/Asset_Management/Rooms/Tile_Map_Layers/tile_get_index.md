# tile\_get\_index

This function can be used to get the tile index (the position of the tile within the tile set image) from a set of tile\-data.

You specify the tile\-data, which can be retrieved using the function [tilemap\_get()](tilemap_get.md), and the function will return an integer value for the index.

  When using this function, ensure that the given tile data is valid, otherwise the returned index value will not be valid either which may result in unexpected behaviour.

 

#### Syntax:

tile\_get\_index(tiledata)

| Argument | Type | Description |
| --- | --- | --- |
| tiledata | [Tile Data](tilemap_get.md) | the tile\-data to check |

 

#### Returns:

[Real](../../../../GML_Overview/Data_Types.md)

 

#### Example:

var lay\_id \= layer\_get\_id("Tiles\_sky");  

 var map\_id \= layer\_tilemap\_get\_id(lay\_id);  

 var mx \= tilemap\_get\_cell\_x\_at\_pixel(map\_id, mouse\_x, mouse\_y);  

 var my \= tilemap\_get\_cell\_y\_at\_pixel(map\_id, mouse\_x, mouse\_y);  

 var data \= tilemap\_get(map\_id, mx, my);  

 var ind \= tile\_get\_index(data);  

 data \= tile\_set\_index(data, irandom(23\));  

 tilemap\_set(map\_id, data, mx, my);

The above code gets the tile map ID from the given layer and then uses that to get the tile\-data for the cell under the mouse position. This data is then used to set the tile index to a random number.
