# filename\_change\_ext

This function returns the indicated file name with the extension (including the dot) changed to the new extension. By using an empty string as the new extension you can remove the extension part all together.

 

#### Syntax:

filename\_change\_ext(fname, newext)

| Argument | Type | Description |
| --- | --- | --- |
| fname |  | The file to use. |
| newext |  | The new extension to use. |

 

#### Returns:

 

#### Example:

ext \= filename\_change\_ext(file\_find\_first(working\_directory \+ "\*.\*", 0\), "");

The above code gets the name of the file (as a string) with the extension part removed.
