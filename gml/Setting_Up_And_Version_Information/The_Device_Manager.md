# The Device Manager

The **Device Manager** is accessed by clicking  on the pencil button  within the [Target List](../Introduction/Compiling.md):

Clicking this button will open the **Device Manager** where you can configure different devices for the target platforms that you wish to compile and test on (note that the platforms available will depend on the [Licence](GMS2_Version_Information.md) that you have and not all of them may be visible). Below you can find details on configuring devices for each of the target platforms:

[Android](#)

Here you can click on the *Add New Device* button to add a new Android device to the list manually, or you can click the *Detect Device* button to have GameMaker automatically detect any devices connected through a wired connection. You can also set up an **Android Virtual Device** by clicking the button marked *Run AVD*. This will open up the Android Virtual Device manager where you can create a new AVD (see [here](https://developer.android.com/studio/run/managing-avds.html) for more information). Once you have one created, you need to launch it from the AVD manager and then in GameMaker click on the *Detect Device* button and it should be added automatically to the device list:

Once you have a device (physical or virtual) added, you can then check the connection using the *Test Connection* button or remove it from the list again by clicking the  *Remove Device* button.

 

[HTML5](#)

The HTML5 device manager is for adding different browsers to the device list for targeting when running. To start with, you should click the *Detect Browsers* button, which should create devices for each of the installed browsers on your machine. If your browser is not listed, you can also click the *Add New Browser* button and then give the device a name and point GameMaker to the path for the browser executable.

The additional available fields can be set up to help control how the browser runs your projects, with the following options available:

- **Browser Command Line Arguments**: Here you can add in any command line arguments to be appended to the browser path. You can find a list of these from the following links to the main popular browsers:
	- [Chromium (Chrome)](https://peter.sh/experiments/chromium-command-line-switches/)
	- [Firefox](https://developer.mozilla.org/en-US/docs/Mozilla/Command_Line_Options)
	- [Internet Explorer](https://docs.microsoft.com/en-us/previous-versions/windows/internet-explorer/ie-developer/general-info/hh826025(v=vs.85))
- **Web Server Address**: The address of the web [server](#) to target (default is 127\.0\.0\.1\). You may need to change this depending on the specifications of different APIs, for example, Facebook would require this to be set to http://localhost (and then have that whitelisted on their app console).
- **Web Server Port**: Set the [port number](#) for the web server (default is 51264\).
- **Allowed Web Server IPs / CIDR IP Ranges**: Set the allowed web server, hostnames and CIDR IP ranges as required.

 

[iOS](#)

Before you can set up your iOS devices, you must have set up your Mac device and tested its connection (see below for details). Once that is done you can select the Mac that you want to target from the drop down menu at the top of the window and then click the *Detect Device* button to have GameMaker automatically find any connected iOS devices, including simulators. Once connected, the device details will be shown in the list in this window, and you can edit the device name to make it more user friendly (this change only affects how the device is presented in the Target Manager and nothing else).

 

[tvOS](#)

Before you can set up your tvOS devices, you must have set up your Mac device and tested its connection (see below for details). Once that is done you can select the Mac that you want to target from the drop down menu at the top of the window and then click the *Detect Device* button to have GameMaker automatically find any connected tvOS devices, including simulators. Once connected, the device details will be shown in the list in this window, and you can edit the device name to make it more user friendly (this change only affects how the device is presented in the Target Manager and nothing else).

 

[macOS](#)

To add a Mac device to the manager, you must first click on the button labelled *Add New device* which will add the device and create some blank fields which you will need to fill in to enable the connection.

First you need to **name** the device so that you can identify it in the target list and then give the **host name** (or IP) of the Mac. You must then give the **username** of the user that you wish to link to, and the **password** that they used. If you wish, you can also change the **Install Folder** on the Mac to wherever you would prefer GameMaker to store the build files for your projects.

When that is all done, you can click on the *Test Connection* button to make sure that GameMaker can communicate with the Mac.

**NOTE**: If you are developing for iOS then you must have done this first and have established a working connection to the Mac you wish to use for development.

**NOTE**: You **must** have enabled **Remote Login** on the target mac. This can be done by going to **Preferences** \-\> **Sharing** and **Enable Remote Login** for the user you want to be able to login.

 

[Ubuntu (Linux)](#)

To add an Ubuntu (Linux) device to the manager, you must first click on the button labelled *Add New Device* which will add the device and create some blank fields which you will need to fill in to enable the connection.

First you need to **name** the device so that you can identify it in the target list and then give the **host name** (or IP) of the Ubuntu machine (or VM). You must then give the **username** of the user that you wish to link to, and the **password** that they used. You are also required to give an **install folder** on the Ubuntu machine that you want to use for installing your projects. When that is all done, you can click on the *Test Connection* button to make sure that GameMaker can communicate with the Ubuntu machine.

Note that the final executable created by GameMaker **will depend on the architecture of the device being targetted**, which can be either **x64** or **ARM**. For example, if you connect a Raspberry Pi 3 or 4, the executable created will be a 32bit ARM executable, and if you connect a Linux PC it will be 64bit x64 executable.

 

 

All the different device windows have an option at the bottom to **Clear Devices** which, when clicked, will remove all the connected devices from the list.

Once you have set up your devices, you can then connect to any one of them from the Target options at the top of the GameMaker IDE and testing/building your game will push the project to that device:
