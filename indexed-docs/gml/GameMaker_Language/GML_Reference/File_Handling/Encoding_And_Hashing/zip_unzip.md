# zip\_unzip

This function will open a stored zip file and extract its contents to the given directory.

If you do not supply a full path to the ZIP directory, then the current drive *root* will be used, and if you want to place it in a relative path to the game bundle working directory, then you should use the [working\_directory](../File_Directories/working_directory.md) variable as part of the path (relative paths using "." or ".." will not work so should be avoided). Note too that the zip must be either part of the game bundle (i.e.: an [Included File](../../../../Settings/Included_Files.md)) or have been downloaded to the storage area using [http\_get\_file()](../../Asynchronous_Functions/HTTP/http_get_file.md).

The function will return a value indicating the number of files extracted, or it will return 0 or less if the extraction has failed.

This function is synchronous and may cause your game to freeze while it extracts the ZIP. Use [zip\_unzip\_async](zip_unzip_async.md) for extracting asynchronously.

 

#### Syntax:

zip\_unzip(zip\_file, target\_directory)

| Argument | Type | Description |
| --- | --- | --- |
| zip\_file | [String](../../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The zip file to open |
| target\_directory | [String](../../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The target directory to extract the files to |

 

#### Returns:

[Real](../../../../../GameMaker_Language/GML_Overview/Data_Types.md)

 

#### Example:

var num \= zip\_unzip("/downloads/level\_data.zip", working\_directory \+ "extracted/");  

 if (num \<\= 0\)   

 {  

     show\_debug\_message("Extraction Failed!");  

 }

The above code will open the zip file stored in the directory "downloads" and extract its contents to the directory "extracted" (creating that directory if it doesn't already exist) and then check to see that the extraction has been correct, showing a debug message should it fail.
