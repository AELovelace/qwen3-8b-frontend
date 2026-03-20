# fx\_create

This function is used to create a new FX Struct for a given effect type, which can then be [applied to a layer](layer_set_fx.md).

The names of the Filters/Effects that you can pass into this function are listed on this page: [All Filter/Effect Types](../../../../../The_Asset_Editors/Room_Properties/FX/All_Filter_Effect_Types.md).

## Usage

You can read the parameters for the created effect by calling [fx\_get\_parameter](fx_get_parameter.md)/[s](fx_get_parameters.md) on the returned struct, and assign new values to them by calling [fx\_set\_parameter](fx_set_parameter.md)/[s](fx_set_parameters.md).

Note that the struct returned by this function will contain no visible members and can only be modified through one of the [Filter/Effect Functions](Filter_Effect_Functions.md).

## Function Failures

The function will return \-1 if the struct failed to create for any reason; this may happen if the specified FX name was wrong or the FX was not loaded into the game package.

To ensure that this function works properly, make sure the FX you need is loaded into your game package, as explained on the [Filter and Effect Functions](Filter_Effect_Functions.md) page:

 

If these conditions are not fulfilled, i.e. you are not passing in a string literal *and* the filter/effect is not present in any rooms, then the function will not be able to load that filter/effect and will return \-1\.

 

 

#### Syntax:

fx\_create(filter\_or\_effect\_name)

| Argument | Type | Description |
| --- | --- | --- |
| filter\_or\_effect\_name | [String](../../../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The name of the filter/effect to create (get them from [All Filter/Effect Types](../../../../../The_Asset_Editors/Room_Properties/FX/All_Filter_Effect_Types.md)). |

 

#### Returns:

[FX Struct](../../../../../../GameMaker_Language/GML_Reference/Asset_Management/Rooms/Filter_Effect_Layers/fx_create.md) or \-1 (on failure)

 

#### Example:

var \_fx\_tint \= fx\_create("\_filter\_tintfilter");  

 fx\_set\_parameter(\_fx\_tint, "g\_TintCol", \[1, 0, 0, 1]);  

 layer\_set\_fx("EffectLayer", \_fx\_tint);

The above code creates a new FX struct from the "\_filter\_tintfilter" effect, which is the "Colour Tint" filter found in the Room Editor. It assigns a value to its "g\_TintCol" parameter which is the colour of the tint, and as it's a vec4 internally, it takes an array containing four values (corresponding to its red, green, blue and alpha values). The FX struct for the tint is then applied to an FX layer.
