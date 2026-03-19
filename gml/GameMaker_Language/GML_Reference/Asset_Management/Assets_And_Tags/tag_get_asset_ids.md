# tag\_get\_asset\_ids

This function gets all the assets of a given type that have the given tags assigned to them.

You supply either a single tag (as a string) or an array, where each item in the array is a tag (as a string), as well as the type of asset to check. The type of asset should be one of the following constants:

 
The function will return an array, where each item in the array will be a single asset handle. If there are no assets of the type that have the given tag(s), an empty array will be returned.

  When "**Automatically remove unused assets when compiling**" is enabled (which it is by default), the returned array will not contain any assets that are not directly referenced in your project or marked with a used tag with [gml\_pragma](../../OS_And_Compiler/gml_pragma.md)("MarkTagAsUsed", \). The removed assets may be represented by an invalid reference with a value of \-1.

 

#### Syntax:

tag\_get\_asset\_ids(tags, asset\_type)

| Argument | Type | Description |
| --- | --- | --- |
| tags | [String](../../../GML_Overview/Data_Types.md) or [Array](../../../GML_Overview/Arrays.md) of Strings | A single asset tag string or an array with various asset tags. |
| asset\_type | [Asset Type Constant](asset_get_type.md) | An asset type constant (listed above) |

 

#### Returns:

[Array](../../../GML_Overview/Arrays.md)

 

#### Example:

var \_paths \= tag\_get\_asset\_ids("enemy", asset\_path);  

 var \_num \= irandom(array\_length(\_paths) \- 1\);  

 path\_start(\_paths\[\_num], 1, path\_action\_reverse, false);

The above code uses the tag "enemy" to find all the path assets with that tag, before choosing one at random and assigning it to the instance running the code.
