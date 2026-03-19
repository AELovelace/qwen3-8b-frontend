# file\_text\_eof

This function returns true when the end of a given opened text file has been reached or false if not.

 

#### Syntax:

file\_text\_eof(fileid)

| Argument | Type | Description |
| --- | --- | --- |
| fileid |  | The id of the file to check. |

 

#### Returns:

 

#### Example:

var num \= 0;  

 var file \= file\_text\_open\_read(working\_directory \+ "Game\_Data.txt");  

 while (!file\_text\_eof(file))  

 {  

     str\[num\+\+] \= file\_text\_readln(file);  

 }  

 file\_text\_close(file);

The above code opens a file for writing then loops through the lines of text already written to the file until it reaches the end, storing each line in the array "str".
