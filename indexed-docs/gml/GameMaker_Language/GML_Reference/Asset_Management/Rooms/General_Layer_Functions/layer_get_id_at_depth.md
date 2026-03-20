# layer\_get\_id\_at\_depth

You can use this function to get all layers assigned a specific depth.

You give the depth to check and the function will return an [Array](../../../../GML_Overview/Arrays.md) with 1 or more entries depending on whether there are any layers at the given depth or not. If there are no layers at the given depth then the array will have a single entry at the \[0] position holding an invalid layer handle (\-1\), but, if there are layers at the depth, then an entry will be made in the array for each layer found \- the entry value will be the handle for a layer.

 

#### Syntax:

layer\_get\_id\_at\_depth(depth)

| Argument | Type | Description |
| --- | --- | --- |
| depth | [Real](../../../../GML_Overview/Data_Types.md) | The depth to check and retrieve the layer IDs from |

 

#### Returns:

[Array](../../../../GML_Overview/Arrays.md)

 

#### Example:

var a \= layer\_get\_id\_at\_depth(0\);  

 if (a\[0] !\= \-1\)  

 {  

     for (var i \= 0; i \< array\_length(a); i\+\+)  

     {  

         layer\_destroy(a\[i]);  

     }  

 }

The above code retrieves data about the layers with a depth of 0\. A check is done to see if any layers exist at that depth, and if there are then the returned array is parsed and each of the found layers is destroyed.
