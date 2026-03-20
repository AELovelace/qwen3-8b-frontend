# YoYo Compiler

The YoYo Compiler (YYC) is a special compiler for creating executable packages that use [machine code](#) instead of interpreted code and a runner (which is what the GameMaker VM compile uses). Compiled code is faster to run, but takes more time to compile the executable.

## Setting Up The SDK

In order for the YoYo Compiler to be able to compile for the target platform, you will need to have the correct [SDK](#)s installed.

The following page contains links to the SDK set\-up guides for each platform:  

## Building a project with YYC

Once you have the [SDK](#)s set up correctly you can change the Output option for the selected platform to YYC: 

In case the current runtime doesn't include the YYC module for the platform you want to build for you will be asked to install it first: 

After that you can create the executable from [The Build Menu](../IDE_Navigation/Menus/The_Build_Menu.md) as with the VM output.

If the path to the [SDK](#) wasn't configured correctly you may get an error like the following (the image shows the message on the Windows platform): 

GameMaker needs to know the location of the files needed to build an executable on the selected platform. In case this hasn't been set up correctly, a compile error is shown.

To verify that the paths have been set correctly for the selected platform, you can check the [Platform Preferences](../Setting_Up_And_Version_Information/Platform_Preferences.md).

To save minidump files from YYC executables on fatal errors, see [Command Line Parameters](Command_Line_Parameters.md).
