# filename\_drive

This function returns the drive information of the filename.

 

#### Syntax:

filename\_drive(fname)

| Argument | Type | Description |
| --- | --- | --- |
| fname |  | The file to use. |

 

#### Returns:

 

#### Example:

drive \= filename\_drive(file\_find\_first(working\_directory \+ "\*.doc", 0\));

The above code gets the drive information (as a string) of the specified file.
