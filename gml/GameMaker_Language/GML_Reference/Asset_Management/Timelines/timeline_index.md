# timeline\_index

This variable holds the index of the timeline currently associated with the instance.

You can set this to a particular timeline to use that one, or set it to \-1 to stop using a timeline for the instance (if no timeline is defined for the instance, an invalid handle (holding \-1) is returned too). Note that this does *not* start the timeline \- for that use the variable [timeline\_running](timeline_running.md).

 

#### Syntax:

timeline\_index

 

#### Returns:

[Timeline Asset](../../../../The_Asset_Editors/Timelines.md)

 

#### Example:

if (timeline\_exists(global.tl))  

 {  

     timeline\_index \= global.tl;  

 }

The above code will assign the instance running the code a time line indexed in the variable global.tl if that timeline exists.
