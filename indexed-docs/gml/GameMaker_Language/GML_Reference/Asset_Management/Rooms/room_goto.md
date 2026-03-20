# room\_goto

This function permits you to go to any room in your game project, whether created using code or in the Asset Browser. You supply the room index (stored in the variable for the room name, or as a variable returned from the function [room\_add()](room_add.md)). Note that the room will not change until the end of the event where the function was called, so any code after this has been called will still run if in the same event. This function will also trigger the **Room End** event.

 
NOTE Room IDs are not based on their order in the Asset Browser or the Room Manager, and so you should avoid supplying a number value directly. Instead, use the room [constant](#) for the asset you want to reference (which is simply its name) or retrieve it through a function.

#### Syntax:

room\_goto(index)

| Argument | Type | Description |
| --- | --- | --- |
| index | [Room Asset](../../../../The_Asset_Editors/Rooms.md) | The index of the room to go to. |

 

#### Returns:

N/A

 

#### Example:

switch (global.level)  

 {  

     case 0: room\_goto(rm\_level1\); break;  

     case 1: room\_goto(rm\_level2\); break;  

     case 2: room\_goto(rm\_level3\); break;  

 }

The above code will check a global variable and change room based on the value that it holds.
