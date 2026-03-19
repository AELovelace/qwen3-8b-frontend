# zip\_add\_file

This function is used to add a file into a ZIP file created with [zip\_create](zip_create.md).

If the call is successful, the function will return 0, otherwise it will throw a fatal error.

The src file is only loaded when [zip\_save](zip_save.md) is called later, so an invalid file will not throw an error during this call.

 
 

#### Syntax:

zip\_add\_file(zip\_object, dest, src)

| Argument | Type | Description |
| --- | --- | --- |
| zip\_object | [ZIP File](../../../../../GameMaker_Language/GML_Reference/File_Handling/Encoding_And_Hashing/zip_create.md) | A ZIP file created with [zip\_create](zip_create.md) |
| dest | [String](../../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The destination file name to be created in the ZIP. Can include directories. |
| src | [String](../../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The source file to be placed into the ZIP |

 

#### Returns:

[Real](../../../../../GameMaker_Language/GML_Overview/Data_Types.md)

 

#### Example:

var \_zip \= zip\_create();  

  

 zip\_add\_file(\_zip, "new.txt", "new.txt");  

 zip\_add\_file(\_zip, "sounds/snd\_attack\_arc\_01\.wav", "snd\_attack\_arc\_01\.wav");  

  

 zip\_save(\_zip, "upload.zip");
 

This creates a new ZIP file, adds two files to it (with the second file in a subdirectory called sounds/) and then saves the ZIP to disk as upload.zip.
