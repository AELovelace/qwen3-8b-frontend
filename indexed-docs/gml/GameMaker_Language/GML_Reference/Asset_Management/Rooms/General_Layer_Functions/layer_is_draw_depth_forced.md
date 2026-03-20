# layer\_is\_draw\_depth\_forced

This function can be used to check and see whether forced Z depth is enabled for rendering the layers in the project. See [layer\_force\_draw\_depth()](layer_force_draw_depth.md) for more information.

 

#### Syntax:

layer\_is\_draw\_depth\_forced()

 

#### Returns:

 

#### Example:

if (!layer\_is\_draw\_depth\_forced())   

 {  

     layer\_force\_draw\_depth(true, 0\);  

 }

The above code checks to see if the layer Z depth is forced or not and if it is not, it sets the Z depth to 0 and enables it.
