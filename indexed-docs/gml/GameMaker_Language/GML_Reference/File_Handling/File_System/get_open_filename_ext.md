# get\_open\_filename\_ext

This function opens a dialogue and asks the player for a filename to open with the given filter. The filter has the form "*name1\|mask1\|name2\|mask2\|...*", where the mask may contain the different options with a semicolon between them and you can also use a "\*" to mean any string. For example: "*bitmaps\|\*.bmp;\*.wmf*", would ask the user to select the name of a bitmap file from the system, but only those that have the two specified extensions (bmp and png). this function does **not** open the file itself! It only returns a string with the full name and path of the file. If the user presses "**Cancel**" an empty string "" is returned. You may also add in a directory to start the search from, and a caption to be shown at the top of the window instead of the default one.

An important thing to note when using this function is that it grants you certain permissions for that file, for the duration of your game. So, once you get the file path from the user, you can access it again and again without having to ask. However, since this function is for reading a file, the permissions granted are *only for reading* and saving will not be permitted by the OS. Should you need to read and write to the file, you can get permission using the function [get\_save\_filename()](get_save_filename.md).

**NOTE**: This function is only valid on the Windows and macOS targets.

 

#### Syntax:

get\_open\_filename\_ext(filter, fname, directory, caption)

| Argument | Type | Description |
| --- | --- | --- |
| filter |  | The file type filter and/or name. |
| fname |  | The suggested filename to use. |
| directory |  | The directory to start the search from. |
| caption |  | The caption for the window. |

 

#### Returns:

 

#### Example:

var file;  

 file \= get\_open\_filename\_ext("text file\|\*.txt", "", working\_directory, "Open a saved level");  

 if (file !\= "")   

 {  

     file\_text\_open\_read(file);  

 }

The above code will ask the user to select a text file for opening from the working\_directory and then check the returned file name and path, and if it exists will open the file for reading.
