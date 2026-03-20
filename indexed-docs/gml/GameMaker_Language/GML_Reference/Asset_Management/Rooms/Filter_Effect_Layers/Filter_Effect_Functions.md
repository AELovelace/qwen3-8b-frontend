# Filter and Effect Functions

## Overview

There are various GML functions that can be used to create, modify and remove filters/effects from layers within a room, allowing you to easily manage effects in real\-time to create realistic and dynamic filters/effects.

 
The latter method (of specifying the filter/effect in your code) only works with string [literal](#)s directly specified in the function argument, which means that if you use a variable or any logic to come up with the filter/effect name string, then the asset compiler will not detect that and the filter/effect will not be loaded.

Consider the following examples:

// This will work on its own  

 var \_fxshake \= fx\_create("\_filter\_screenshake");  

  

 // This will NOT work on its own  

 var \_myfilters \= { screenshake: "\_screenshake" }  

 var \_filter\_to\_use \= "\_filter" \+ \_myfilters.screenshake;  

 var \_fxshake \= fx\_create(\_filter\_to\_use);
 

To ensure that the latter method works, you can simply add the filter to at least one room in your project, or ensure that [fx\_create()](fx_create.md) is called anywhere in your project with the filter name as a string constant (and not a variable).

 
## Function List

The following functions are used to create and manage "FX Structs" containing effect data:

- [fx\_create](fx_create.md)
- [fx\_get\_parameter](fx_get_parameter.md)
- [fx\_get\_parameters](fx_get_parameters.md)
- [fx\_get\_name](fx_get_name.md)
- [fx\_get\_parameter\_names](fx_get_parameter_names.md)
- [fx\_get\_single\_layer](fx_get_single_layer.md)
- [fx\_set\_parameter](fx_set_parameter.md)
- [fx\_set\_parameters](fx_set_parameters.md)
- [fx\_set\_single\_layer](fx_set_single_layer.md)

The following functions are used for modifying layers that may contain Filters/Effects by making use of FX Structs:

- [layer\_set\_fx](layer_set_fx.md)
- [layer\_get\_fx](layer_get_fx.md)
- [layer\_clear\_fx](layer_clear_fx.md)
- [layer\_enable\_fx](layer_enable_fx.md)
- [layer\_fx\_is\_enabled](layer_fx_is_enabled.md)

## Modify FX At Runtime

You can modify filters/effects at runtime by doing the following:

- **Retrieve the FX struct** from the layer you want to modify by calling [layer\_get\_fx()](layer_get_fx.md)
	- *Or, create a new FX struct by calling [fx\_create()](fx_create.md) and apply it to a layer using [layer\_set\_fx()](layer_set_fx.md)*
- **Retrieve its parameter struct** by calling [fx\_get\_parameters()](fx_get_parameters.md)
- **Modify the parameters** as required by assigning values to the struct variables
	- *Get the parameter names from here: [FX Types \& Parameters](../../../../../The_Asset_Editors/Room_Properties/FX/All_Filter_Effect_Types.md)*
- **Apply the modified struct** back to the FX struct by calling [fx\_set\_parameters()](fx_set_parameters.md)
	- *You do not need to call [layer\_set\_fx()](layer_set_fx.md) here as modifying the FX struct directly affects the layer it is already assigned to*

Here is example code for the workflow mentioned above:

Create Event

// Store the FX struct, and its parameters struct, in variables  

 pixelate\_fx \= layer\_get\_fx("Effect\_1");  

 pixelate\_fx\_params \= fx\_get\_parameters(pixelate\_fx);

Step Event

// Change param as variable  

 pixelate\_fx\_params.g\_CellSize \= round((mouse\_x / room\_width) \* 64\);  

  

 // Or, change param as string  

 pixelate\_fx\_params\[$ "g\_CellSize"] \= round((mouse\_x / room\_width) \* 64\);  

  

 // Apply updated parameters struct to the FX struct  

 fx\_set\_parameters(pixelate\_fx, pixelate\_fx\_params);
 

## FX Runtime Parameters

The [FX Types \& Parameters](../../../../../The_Asset_Editors/Room_Properties/FX/All_Filter_Effect_Types.md) page lists all Filters/Effects along with their **Runtime Parameters**.

You can use the Runtime parameter names in the following three ways (using the parameter "g\_CellSize" as an example):

- Modify a parameter in an FX struct by calling [fx\_set\_parameter()](fx_set_parameter.md): fx\_set\_parameter(fx\_struct, **"g\_CellSize"**, 8\);
- Modify a variable in a parameter struct: params\_struct.**g\_CellSize** \= 8;
	- NOTE *Make sure to get the parameter struct first by calling [fx\_get\_parameters()](fx_get_parameters.md).*
- Modify a variable in a parameter struct using the $ accessor and a string: params\_struct\[$ **"g\_CellSize"**] \= 8;

## Single Layer Mode

By default, a filter/effect is applied to the layer that it is [assigned to](layer_set_fx.md) and all layers below that layer, however you can use [fx\_set\_single\_layer()](fx_set_single_layer.md) to enable **Single Layer** mode for a filter/effect to make sure that it's only applied to the layer that it is assigned to.

The following visual shows a filter being applied to multiple layers (which is the default behaviour for all FX layers), and then the same filter with Single Layer mode enabled and applied to a non\-FX layer:

Single Layer Mode OFF

Single Layer Mode ON

You can also make use of Single\-Layer effects in the Room Editor by using the [Inspector](../../../../../IDE_Tools/The_Inspector.md).
