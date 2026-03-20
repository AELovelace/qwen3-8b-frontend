# show\_question\_async

This function opens a window and displays the question you define in the function to the user.

This is an asynchronous function, and as such GameMaker does *not* block the device it is being run on while waiting for an answer, but rather keeps on running events as normal. The function has two buttons that show **Yes** and **No**, and once the user has pressed one, an asynchronous [Dialog](../../../../The_Asset_Editors/Object_Properties/Async_Events/Dialog.md) event is triggered which, for the duration of that event *only*, will have a [DS Map](../../Data_Structures/DS_Maps/ds_map_create.md) stored in the variable [async\_load](../../../GML_Overview/Variables/Builtin_Global_Variables/async_load.md).

This map will contain the two keys: "id" and "status". "id" is the value that was returned by the function when called, while the "status" will be either true or false for **Yes** and **No** respectively.

 
 
 

#### Syntax:

show\_question\_async(string)

| Argument | Type | Description |
| --- | --- | --- |
| string | [String](../../../GML_Overview/Data_Types.md) | The question to ask the user |

 

#### Returns:

[Async Request ID](../Asynchronous_Functions.md)

 

#### Example:

The **Mouse Left Pressed Event** (for example) of the object that is showing the message would have the following code:

Mouse Left Pressed Event

msg \= show\_question\_async("Do you want to buy some armour for " \+ string(armour\[0, 5]) \+ "coins?");

The above will show a question with the given string, requesting that the user press either **Yes** or **No**. The async ID is stored in the variable msg and will be used in the [Asynchronous Dialog event](../../../../The_Asset_Editors/Object_Properties/Async_Events/Dialog.md) as shown below:

Async \- Dialog Event

var \_id, \_stat;  

 \_id \= ds\_map\_find\_value(async\_load, "id");  

 if (\_id \=\= msg)  

 {  

     if (ds\_map\_find\_value(async\_load, "status"))  

     {  

         coins \-\= armour\[0, 5];  

         global.protection \+\= armour\[0, 0];  

     }  

 }

The above code checks the "id" key of the returned [DS Map](../../Data_Structures/DS_Maps/ds_map_create.md) against the value stored in the variable "msg". If they are the same, it then checks to see if one of the two buttons were pressed and if it returns true it will then deduct a value from a variable and add a value to a global variable too.
