# layer\_get\_element\_type

You can use this function to get the *element type* for the given element. You supply the unique element ID value (for example, as returned the function that created the element or from [The Room Editor](../../../../../The_Asset_Editors/Rooms.md)) and the function will return one of the following constants: 

| [Layer Element Type Constant](layer_get_element_type.md) | |
| --- | --- |
| Constant | Description |
| layerelementtype\_background | The element is a background. |
| layerelementtype\_instance | The element is an instance. |
| layerelementtype\_sprite | The element is a sprite asset. |
| layerelementtype\_tilemap | The element is a tilemap. |
| layerelementtype\_oldtilemap | The element is an old type tilemap. |
| layerelementtype\_particlesystem | The element is a particle system. |
| layerelementtype\_tile | The element is a legacy background tile (this is only valid for projects that have been imported from previous versions of GameMaker). |
| layerelementtype\_sequence | The element is a sequence. |
| layerelementtype\_undefined | The element does not exist or the ID value is erroneous. |

  This function is most useful when you have multiple different element types assigned to the one layer, and that you can get a list of all the elements on any given layer using the function [layer\_get\_all\_elements](layer_get_all_elements.md).

 

#### Syntax:

layer\_get\_element\_type(element\_id)

| Argument | Type | Description |
| --- | --- | --- |
| element\_id | [Layer Element ID](layer_get_all_elements.md) | The unique ID value of the element to get the type of |

 

#### Returns:

[Layer Element Type Constant](layer_get_element_type.md) (layerelementtype\_undefined if element does not exist or is invalid)

 

#### Example:

var a \= layer\_get\_all\_elements(layer);  

 for (var i \= 0; i \< array\_length(a); i\+\+)  

 {  

     if (layer\_get\_element\_type(a\[i]) \=\= layerelementtype\_sprite)  

     {  

         layer\_sprite\_destroy(a\[i]);  

     }  

 }

The above code gets the IDs for all the instance elements assigned to the layer of the instance running the code. The code then checks to see if any of the returned elements are sprite assets and if they are, they're destroyed.
