# os\_type

This **read\-only** variable holds one of the various constants GameMaker has to tell you which operating system the game has been created for. Note that this is *not* necessarily the same as the OS of the device running it, since \- for example \- your game could be running on an Amazon Fire OS, but will have been built for the Android platform (in which case os\_type will be os\_android).

The following constants can be returned:

| [OS Type Constant](os_type.md) | |
| --- | --- |
| Constant | Description |
| os\_windows | Windows OS |
| os\_gxgames | GX.games |
| os\_linux | Linux |
| os\_macosx | macOS X |
| os\_ios | iOS (iPhone, iPad, iPod Touch) |
| os\_tvos | Apple tvOS |
| os\_android | Android |
| os\_ps4 | Sony PlayStation 4 |
| os\_ps5 | Sony PlayStation 5 |
| os\_gdk / os\_xboxseriesxs | Microsoft GDK (Xbox One and Xbox Series X/S) |
| os\_switch | Nintendo Switch |
| os\_unknown | Unknown OS |

 

#### Syntax:

os\_type

 

#### Returns:

[OS Type Constant](os_type.md)

 

#### Example:

switch (os\_type)  

 {  

     case os\_windows: global.config \= 0; break;  

     case os\_linux: global.config \= 1; break;  

     case os\_macosx: global.config \= 2; break;  

 }

The above code checks the OS running the game and sets a global variable accordingly.
