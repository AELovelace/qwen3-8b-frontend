# Files Action Library

The **File Actions** deal with two different file types \- Buffer files and Ini files \- and also have certain generic file actions to rename or copy existing files.

**Buffer files** are created by saving out the data from a buffer that you have previously created and this data can then be loaded into a buffer again at any time in the future. You can find out more information about buffers here: [Buffer Actions](../Buffers/Buffer_Actions.md).

**Ini files** are small, lightweight files which are compatible with most platforms. They are ideal for storing small pieces of information, like interface preferences, local high scores, level data etc... and are very easy to use. Ini files don't have to have been created previously to use these actions, and you can read from a non\-existent Ini file and you'll simply get a default return value (which you specify), however we recommend that you create at least a "base" ini file for opening and modifying before using the actions. This base ini file can be created by simply calling the [Open Ini File](Open_Ini_File.md) action followed by the [Close Ini File](Close_Ini_File.md), since closing the file will write it to the disk, or you can include one in the [Included Files](../../../Settings/Included_Files.md) of the Asset Browser. If you are using a file included in the Asset Browser as your base Ini, you should also read the section of the manual about [how the File System works](../../../Additional_Information/The_File_System.md).

The following actions exist for working with files:

|  | [Load Buffer](Load_Buffer.md) |
| --- | --- |
|  | [Save Buffer](Save_Buffer.md) |
|  | [Rename File](Rename_File.md) |
|  | [Copy File](Copy_File.md) |
|  | [Delete File](Delete_File.md) |
|  | [Open Ini File](Open_Ini_File.md) |
|  | [Close Ini File](Close_Ini_File.md) |
|  | [Write To Ini File](Write_To_Ini_File.md) |
|  | [Read Ini File](Read_Ini_File.md) |
|  | [If File Exists](If_File_Exists.md) |
