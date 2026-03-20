# get\_save\_filename

This function opens a dialogue and asks the player for a filename to save to with the given filter.

The filter has the form "name1\|mask1\|name2\|mask2\|...", where the mask may contain the different options with a semicolon between them and you can also use a \* to mean any string. For example: "bitmaps\|\*.bmp;\*.wmf", would ask the user to select the name of a bitmap file from the system, but only those that have the two specified extensions (bmp and png). This function does **not** save the file itself! It only returns a string with the full name and path of the file. If the user presses **Cancel** an empty string "" is returned.

An important thing to note when using this function is that it grants you certain permissions for that file, for the duration of your game. So, once you get the file path from the user, you can access it again and again without having to ask, and the permission applies to reading *and* writing equally.

  This function is only valid on the Windows and macOS targets.

 

#### Syntax:

get\_save\_filename(filter, fname)

| Argument | Type | Description |
| --- | --- | --- |
| filter | [String](../../../GML_Overview/Data_Types.md) | The file type filter and/or name |
| fname | [String](../../../GML_Overview/Data_Types.md) | The suggested filename to use |

 

#### Returns:

[String](../../../GML_Overview/Data_Types.md)

 

#### Example:

var \_file \= get\_save\_filename("screenshot\|\*.png", "");  

 if (\_file !\= "")  

 {  

     screen\_save(\_file);  

 }

The above code will ask the user to select an image file name file for saving then check the returned file name and path, and if it is not an empty string it takes a screenshot and saves it using the given name.
