# layer\_get\_forced\_depth

This function can be used to retrieve the Z depth set for rendering layers within the room. See [layer\_force\_draw\_depth()](layer_force_draw_depth.md) for more information.

 

#### Syntax:

layer\_get\_forced\_depth()

 

#### Returns:

[Real](../../../../../../GameMaker_Language/GML_Overview/Data_Types.md)

 

#### Example:

if (layer\_get\_forced\_depth() !\= 0\)   

 {  

     layer\_force\_draw\_depth(true, 0\);  

 }

The above code checks to see if the layer Z depth is forced to a value of 0 or not and if it is not, it sets the layer Z depth to 0\.
