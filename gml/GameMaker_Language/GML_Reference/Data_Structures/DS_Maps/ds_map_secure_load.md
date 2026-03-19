# ds\_map\_secure\_load

This function will load a DS map, saved previously using [ds\_map\_secure\_save](ds_map_secure_save.md), from the given file.

When loaded, the function will return the handle of the DS map that has been created from the loaded data. This DS map handle should be stored in a variable and used for all further function calls to this map. Note that if the DS map being loaded was saved with an array as one of the key values, this array will have been converted into a DS list on load.

  One of the features of a secure saved file is that it is locked to the device that it was created on, so you cannot load a file saved on one device into a project running on another device.

 

#### Syntax:

ds\_map\_secure\_load(filename)

| Argument | Type | Description |
| --- | --- | --- |
| filename | [String](../../../GML_Overview/Data_Types.md) | The name of the file to load the map data from |

 

#### Returns:

[DS Map](ds_map_create.md)

 

#### Example:

p\_map \= ds\_map\_secure\_load("p\_data.dat");

The above code will load a securely saved DS map and store its index value in a variable for future use.
