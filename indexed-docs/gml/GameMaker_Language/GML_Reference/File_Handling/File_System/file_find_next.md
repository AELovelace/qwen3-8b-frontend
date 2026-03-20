# file\_find\_next

This function returns the name of the next file that satisfies the previously given mask and the attributes (defined by [file\_find\_first](file_find_first.md)), or an empty string "" if no such file exists.

 
 
 

#### Syntax:

file\_find\_next()

 

#### Returns:

[String](../../../GML_Overview/Data_Types.md)

 

#### Example:

if (directory\_exists("/User Content"))  

 {  

     fileA \= file\_find\_first("/User Content/\*.doc", fa\_readonly);  

     fileB \= file\_find\_next();  

     fileC \= file\_find\_next();  

     file\_find\_close();  

 }

This code checks if the specified directory exists and if it does, goes there and returns the first "read\-only" .doc file found. It then looks for two more files and closes the file finder.

You can look for any number of files using a [while](../../../GML_Overview/Language_Features/while.md) loop:

var \_files \= \[];  

 var \_file\_name \= file\_find\_first("/User Content/\*.doc", fa\_readonly);  

  

 while (\_file\_name !\= "")  

 {  

     array\_push(\_files, \_file\_name);  

  

     \_file\_name \= file\_find\_next();  

 }  

  

 file\_find\_close();
 

The above code creates an empty array to store all the file names that were found, and starts looking for read\-only .doc files. If that file name is not an empty string, it pushes it into the \_files array, and then attempts to find the next file. The loop will keep repeating until an empty string is found (meaning there are no more matching files), which is when it ends the loop and closes the file finder at the end.
