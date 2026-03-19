# timeline\_get\_name

This function can be used to get the name of a time line as a string. if the time line has been created dynamically using the [timeline\_add()](timeline_add.md) function, the name returned will have the
 format "\_\_newtimeline*N*" where "*N*" is the number of the time line (starting from 0\). Please note that this is *only* a string and cannot be used to reference the timeline directly \- for
 that you would need the *timeline index*. You can, however, use this string to get the *timeline index* using the returned string along with the function [asset\_get\_index()](../Assets_And_Tags/asset_get_index.md).

 

#### Syntax:

timeline\_get\_name(ind)

| Argument | Type | Description |
| --- | --- | --- |
| ind |  | The index of the time line to check the name of. |

 

#### Returns:

 

#### Example:

var \_str \= timeline\_get\_name(timeline\_index);  
 show\_debug\_message("Current timeline \= " \+ \_str);

The above code get the name of the currently assigned timeline and output it to the console.
