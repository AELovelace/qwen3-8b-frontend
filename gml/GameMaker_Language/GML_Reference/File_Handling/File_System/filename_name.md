# filename\_name

Using this function returns the name part of the indicated file, *with* the extension but *without* the path.

 

#### Syntax:

filename\_name(fname)

| Argument | Type | Description |
| --- | --- | --- |
| fname |  | The file to use. |

 

#### Returns:

String

 

#### Example:

name \= filename\_name(file\_find\_first("C:/Games/\*.doc", 0\));

The above code gets the name (as a string) of the first "doc" type file found in the specified directory.
