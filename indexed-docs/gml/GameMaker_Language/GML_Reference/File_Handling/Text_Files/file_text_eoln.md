# file\_text\_eoln

With this function you can get GameMaker to check the currently opened file to see if the line being read has finished. The function returns true if the end of the line has been reached and false otherwise.

 

#### Syntax:

file\_text\_eoln(fileid)

| Argument | Type | Description |
| --- | --- | --- |
| fileid |  | The id of the file to check. |

 

#### Returns:

 

#### Example:

var file \= file\_text\_open\_read(working\_directory \+ "Game\_Data.txt");  

 var num \= 0; while (!file\_text\_eoln(file))  

 {  

     score\_array\[num] \= file\_text\_read\_real(file);  

     num\+\+;  

 }  

 file\_text\_close(file);

The above code opens a file for reading then reads the values from a single line into an array.
