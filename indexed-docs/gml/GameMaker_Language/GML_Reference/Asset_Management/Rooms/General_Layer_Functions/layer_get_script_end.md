# layer\_get\_script\_end

This function returns the function assigned to run at the end of rendering the given layer, or it will return an invalid handle (\-1\) if no function is assigned.

You supply the layer handle (which you get when you create the layer using [layer\_create](layer_create.md)) or the layer name (as a string \- this will have a performance impact) and this function will return the function assigned to run at the end of rendering for that layer, or it will return an invalid handle (\-1\) if no function is assigned.

You can assign script functions to a layer with [layer\_script\_begin](layer_script_begin.md) and [layer\_script\_end](layer_script_end.md).

 

#### Syntax:

layer\_get\_script\_end(layer\_id)

| Argument | Type | Description |
| --- | --- | --- |
| layer\_id | [String](../../../../GML_Overview/Data_Types.md) or [Layer](layer_get_id.md) | The layer to target (or the layer name as a string) |

 

#### Returns:

 

 

#### Example:

if (layer\_get\_script\_end(layer) \=\= \-1\)  

 {  

     layer\_script\_end(layer, scr\_ResetShaderValues);  

 }

The above code will check to see if the layer that the instance running the code has a script function assigned to it and if it doesn't one is assigned.
