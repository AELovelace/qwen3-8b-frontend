# get\_string\_async

This function opens a window and displays a message as well as a space for the user to input a string (which will contain the supplied default string to start with).

This is an asynchronous function, and as such GameMaker does *not* block the device it is being run on while waiting for an answer, but rather keeps on running events as normal. Once the user has typed out their string and pressed the **Okay** button, an [asynchronous Dialog event](../../../../The_Asset_Editors/Object_Properties/Async_Events/Dialog.md) is triggered which, for the duration of that event *only*, will have a [DS Map](../../Data_Structures/DS_Maps/ds_map_create.md) stored in the variable [async\_load](../../../GML_Overview/Variables/Builtin_Global_Variables/async_load.md).

This map will contain the following three keys:

- "id" is the value that was returned by the function when called.
- "status" will be either true for the **Okay** button being pressed, or false if the message was cancelled (where applicable as not all target platforms permit the message to be cancelled).
- "result" will hold the string that contains the user input (or an empty string "" if none was supplied).

 
 
 

#### Syntax:

get\_string\_async(string, default)

| Argument | Type | Description |
| --- | --- | --- |
| string | [String](../../../GML_Overview/Data_Types.md) | The message to show in the dialog |
| default | [String](../../../GML_Overview/Data_Types.md) | The default string |

 

#### Returns:

[Async Request ID](../Asynchronous_Functions.md)

 

#### Example:

The **Mouse Left Pressed Event** (for example) of the object that is showing the message would have the following code:

Mouse Left Pressed Event

msg \= get\_string\_async("What's your name?", "Anon");

The above will show a message requesting that the user input a string and press **Okay**. The async ID is stored in the variable msg and will be used in the asynchronous [Dialog](../../../../The_Asset_Editors/Object_Properties/Async_Events/Dialog.md) event as shown below:

Async Dialog Event

var \_id \= ds\_map\_find\_value(async\_load, "id");  

 if (\_id \=\= msg)  

 {  

     if (ds\_map\_find\_value(async\_load, "status"))  

     {  

         if (ds\_map\_find\_value(async\_load, "result") !\= "")  

         {  

             global.name \= ds\_map\_find\_value(async\_load, "result");  

         }  

     }  

 }

The above code checks the "id" key of the returned [DS Map](../../Data_Structures/DS_Maps/ds_map_create.md) against the value stored in the variable msg. If they are the same, it then checks to see if **Okay** was pressed (rather than the window being closed/cancelled) and if it returns true it then checks the "result" of a string to make sure that no empty strings were returned before setting a global variable.
