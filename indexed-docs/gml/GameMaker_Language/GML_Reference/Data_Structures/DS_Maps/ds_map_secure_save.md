# ds\_map\_secure\_save

This function will save the contents of the given DS map to a file that is linked to the device it was created on (meaning it can't be read if transferred to any other device).

The file itself can have almost any extension (for example, \*.dat, \*.json, \*.bin, ...) and will be obfuscated and stored to local storage on the target platform. You can then re\-load the DS map using the function [ds\_map\_secure\_load](ds_map_secure_load.md). Note that if the DS map being saved contains an array, this array will be converted into a DS list instead when saved.

  One of the features of a secure saved file is that it is locked to the device that it was created on, so you cannot load a file saved on one device into a project running on another device.

 

#### Syntax:

ds\_map\_secure\_save(map, filename)

| Argument | Type | Description |
| --- | --- | --- |
| map | [DS Map](ds_map_create.md) | The handle of the data structure to use |
| filename | [String](../../../GML_Overview/Data_Types.md) | The name of the file to save the map to |

 

#### Returns:

[Boolean](../../../GML_Overview/Data_Types.md)

 

#### Example:

ds\_map\_secure\_save(purchase\_map, "p\_data.dat");

The above code will save the DS map indexed in the variable purchase\_map to the given file for later retrieval.
