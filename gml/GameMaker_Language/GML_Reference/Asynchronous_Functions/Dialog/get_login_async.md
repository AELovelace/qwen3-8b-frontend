# get\_login\_async

This function opens a window that asks the user to input a username and password. These arguments can be set as an empty string or you can store previously entered values to use if you wish.

This is an asynchronous function, and as such GameMaker does *not* block the device it is being run on while waiting for an answer, but rather keeps on running events as normal. Once the user has input the details and pressed the **Okay** button, an asynchronous [Dialog](../../../../The_Asset_Editors/Object_Properties/Async_Events/Dialog.md) event is triggered which, for the duration of that event *only*, will have a [DS Map](../../Data_Structures/DS_Maps/ds_map_create.md) stored in the variable [async\_load](../../../GML_Overview/Variables/Builtin_Global_Variables/async_load.md).

This map will contain the keys "id", "status", "username" and "password", with the user input stored in "username" and "password".

This function will return an index number for the async event that was triggered, which can then be checked in the corresponding event so that you can "target" specific data in case you're expecting more than one async event to be triggered (perhaps from some other function).

  This function is not supported on the GX.games target.

 
  The password is returned unencrypted. You should make sure to encrypt it before doing anything with it, e.g. saving it to disk, sending it over a network, ...

 

#### Syntax:

get\_login\_async(name, password)

| Argument | Type | Description |
| --- | --- | --- |
| username | [String](../../../GML_Overview/Data_Types.md) | The default username |
| password | [String](../../../GML_Overview/Data_Types.md) | The default password |

 

#### Returns:

[Async Request ID](../Asynchronous_Functions.md)

 

#### Example:

The **Create Event** (for example) of the object that is controlling the login of our user would have the following code:

Create Event

ini\_open("Profile.ini");  

 u \= ini\_read\_string("User", "0", "");  

 p \= ini\_read\_string("User", "1", "");  

 ini\_close();  

 login \= get\_login\_async(u, p);

The above code opens an INI file (or creates one if it doesn't exist) and gets the name and password stored in that file. If they do not exist, then the default of an empty string ("") is returned. These values are then used in get\_login\_async to ask the user for their username and password details, with the request index being stored in the variable login. Note that while waiting for the user to give the necessary information the game and its events will continue to run as normal.

Now that the asynchronous code has been fired off, we need to check for the return value in the [asynchronous event for Dialogs](../../../../The_Asset_Editors/Object_Properties/Async_Events/Dialog.md) in the following way:

Async Dialog Event

if (ds\_map\_find\_value(async\_load, "id") \=\= login)  

 {  

     u \= ds\_map\_find\_value(async\_load, "username");  

     p \= ds\_map\_find\_value(async\_load, "password");  

 }

The above code checks the "id" key of the [async\_load](../../../GML_Overview/Variables/Builtin_Global_Variables/async_load.md) DS map and if it holds the same value as that stored in the login variable, the map details are then read into the corresponding variables which you can then store, use to check against database values, etc.
