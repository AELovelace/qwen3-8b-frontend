# title

With this action you can delete a file that has been created previously. You supply the file name (as a string) of the file to be deleted. Note that you *cannot* delete any files that are included in the game bundle, only those that have been created
 using the [Close Ini](Close_Ini_File.md) or [Save Buffer](Save_Buffer.md) actions (see the section on [The File System](../../../Additional_Information/The_File_System.md) for more information).

 

#### Action Syntax:

#### Arguments:

| Argument | Description |
| --- | --- |
| Filename | The name (as a string) of the file to delete |

 

#### Example:

The above action block code will check to see if the file "checkpoint.sav" exists, and if
 it does it then checks to see if the file "checkpoint\_OLD.sav" exists. If that file exists as well, then it is deleted, and then the original "checkpoint.sav" file is renamed to "checkpoint\_OLD.sav". Finally a buffer
 is saved as "checkpoint.sav" (essentially we are backing up a saved buffer file each time we save it, so that there is always a "current" save and an "old" save file).
