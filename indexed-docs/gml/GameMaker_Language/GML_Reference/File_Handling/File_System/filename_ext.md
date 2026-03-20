# filename\_ext

This function returns the extension part of the indicated file name, including the leading dot.

 

#### Syntax:

filename\_ext(fname)

| Argument | Type | Description |
| --- | --- | --- |
| fname |  | The file to use. |

 

#### Returns:

 

#### Example:

ext \= filename\_ext(file\_find\_first("\*.\*", 0\));

The above code gets the extension (as a string) of the specified file.
