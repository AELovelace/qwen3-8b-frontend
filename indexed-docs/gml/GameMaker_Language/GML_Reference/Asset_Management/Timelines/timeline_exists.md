# timeline\_exists

With this function you can check and see whether a time line exists (returns true) or not (returns false). This is particularly useful when creating Timelines dynamically using the [timeline\_add()](timeline_add.md) function, but you should note that if you search for an uninitialised variable (that would otherwise be assigned to a time line's index) an error will be thrown.

 

#### Syntax:

timeline\_exists(ind)

| Argument | Type | Description |
| --- | --- | --- |
| ind |  | The index of the time line to check for. |

 

#### Returns:

 

#### Example:

if (timeline\_exists(global.tl))   

 {  

     timeline\_delete(global.tl);  

 }

The above code checks to see if a time line exists and is indexed in the global variable "tl" and if so it then deletes that time line.
