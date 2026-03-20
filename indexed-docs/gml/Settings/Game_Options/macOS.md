# macOS Game Options

This section outlines the different options available to you that control how your macOS game projects will be compiled. The different sections are:

## General

Here you also need to give the **Team Identifier** that you wish to use for signing the final application that GameMaker creates for you. Setting it here will override the Team ID that you have supplied in the [macOS Preferences](../../Setting_Up_And_Version_Information/Platform_Preferences/macOS.md). After the Team Identifier you also have the option to supply the **Signing Identifier**, which is required by Apple for all non\-appstore applications (like Steam games, for example).

Then you have the option to **Disable file system sandbox**. Checking this will disable the GameMaker sandboxing for saving and loading files, permitting your games to access files from anywhere on the system running the game. This option is unchecked by default, as we recommend that you maintain the GameMaker sandbox for files on all systems and when checked, some save/load areas may still not be available depending on the OS\-level permissions. For more information on the sandbox, please see the pages on the GameMaker [File System](../../Additional_Information/The_File_System.md).

You can select the architectures that your final YYC build will support. "**Min Version**" is the minimum version of macOS that the game can be played on.

## Graphics

The graphics options are those that you should configure to determine how your game will use the graphics card of your target Mac. The following options are included for you to modify:

- **Allow Menu And Dock In Fullscreen**: When checked, this option will show the OS menu and dock if the game is in fullscreen mode. This is off by default.
- **Display Cursor**: When this is checked the regular macOS cursor will be shown, and un\-checking it will mean that no cursor is shown unless you have created one in your game code. This is off by default.
- **Start Fullscreen**:
- **Allow Fullscreen Switching**: With this ticked the user can switch from fullscreen to windowed and back again using the standard macOS shortcuts. This is off by default.
- **Interpolate colours between pixels**:
- **Use synchronization to avoid tearing**: This toggles [v\-sync](#) on or off. Note, that if you have a game with a room speed of 120 and the player has a monitor with a refresh rate of 60, turning this option on will lock your game speed to 60 too. This is on by default.
- **Allow window resize**: Checking this permits the user to change the size of the game window. This option is off by default.
- **Enable Retina**: Checking this will set the back buffer to be at the higher (actual) resolution when the game is run on a retina enabled monitor, while un\-checking it will set the back buffer to be at the apparent (lower) resolution. What this means is that the initial game window will be set to twice the width and height that the room/viewport that the first room is set to. However, this does NOT scale the application surface to suit, and so if you want your game to make the most of the retina display you should also set the application surface to be the same as the window size (note that this will double the pixels along the width and height, so only enable this and scale the application surface if your game will benefit from the increased resolution).  

  

 This option is off by default, and enabling it will not show any difference when you run or debug the game using VM, as the runner is pre\-built in that case. It will only work if you build an executable through VM, or use YYC for testing or building the game, as that will rebuild the runner with your customised Game Options.
- **Scaling**: Here you can choose to maintain aspect ratio (so a 4:3 room will be "letter boxed" on a 16:9\) or to scale fully (stretching the image to fit the full screen).  

  

*Switching off the application surface will disable all the scaling options set in the macOS Game Options until it has been switched back on again. See The Application Surface for further details.*

Finally there is the option to set the size of the [texture page](#). The default (and most compatible) size is 2048x2048, but you can choose from anywhere between 256x256 up to 8192x8192\. There is also a button marked ****Preview****which will generate the texture pages for this platform and then open a window so that you can see how they look. This can be very useful if you wish to see how the texture pages are structured and to prevent having texture pages larger (or smaller) than necessary. For more information on texture pages, please see [here](../Texture_Information/Texture_Pages.md).

  Be aware that the larger the size of the texture page, the less compatible your game will be on PC's with lower specifications.

## Images

The images section is where you supply the images that your game requires. For Mac, you need to supply an **Icon** file (that must be in .png format and 1024x1024px) and a **Splash Screen** (which can be .png, .bmp, .jpg or .gif format). The splash screen will be shown while the game loads.

For DMG packages, you can supply an **Installer Background** image which will appear as the background of the DMG installer.

It is worth noting that GameMaker has a [Project Image Generator](../../IDE_Tools/Project_Image_Generator.md) tool which can be used to automatically create all the images required for all the different target platforms your game is being compiled to. If you use this tool, you should revise the images created to ensure that they are what you require.

## Packaging

If you wish the finished game to be App Store Ready then you need to check the **Build for Mac App Store** option, but be aware that this will only function if you are a registered Developer and have the necessary certificates. Under that are the app **Permissions** which you should only check if they are true as Apple can reject your app if they are checked when they are not needed or vice versa. These options simply permit your game to use the http\_ and url\_ functions. It is worth noting that if you wish to support GamePads in your game then the option to create an App Store ready package should be *off*.

Finally, you need to select its **App Category** (for more information, see [here](https://developer.apple.com/library/content/documentation/General/Reference/InfoPlistKeyReference/Articles/LaunchServicesKeys.html)).

## Social

This option is for using the **Apple Sign In Extension** on Mac. You can get this extension from the [GameMaker Marketplace](https://marketplace.gamemaker.io/publishers/23/yoyo-games), and the extension itself contains full instructions for use. If you are not using this extension then you should not tick this option.
