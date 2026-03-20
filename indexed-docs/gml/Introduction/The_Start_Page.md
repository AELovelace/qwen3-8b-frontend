# The Start Page

When you open GameMaker, the main [IDE](#) will open on the Start Page: 

When you start GameMaker for the first time, you will be able to see a description for each start screen element by hovering over it.

Here, you can click on the **"SKIP to Setup Wizard"** button to start creating your first project with the help of the Setup Wizard, which will take you through the steps necessary for creating your first game in GameMaker.

You can also click on "Close" to close the wizard and continue using GameMaker manually, and optionally enable the "Don't show me again" checkbox if you do not wish to see the wizard when you start GameMaker again.

  A warning message will be shown if GameMaker detects that your "My Projects" directory is set to a cloud storage location, as saving projects to cloud storage may cause problems when saving and building projects. You'll be asked to change it in the [Path Preferences](../Setting_Up_And_Version_Information/IDE_Preferences/General/Paths.md):

## Start Page Elements

The Start Page contains the following elements:

- **Menu Bar**: This shows you the menus that you can use throughout the IDE; more information is given in a section below.
- **Project Options**: The Projects section is where you can create, open or import projects. This is explained in more detail further down this page.
- **Recent Projects**: Here you can see a list of previous projects that you can open. You can also see the full project name and path, and clicking the left mouse button  will open the project. You can also switch the view of this section between tile mode and list mode by pressing the buttons in the top\-right corner.
- **Version \& Log In**: This section provides details on the current IDE version being used, as well as the current [Runtime](#) version. You will also get notified of any changes available to either the IDE or the Runtime in this section. Here you are also able to log in and access your account. See: [Version \& Account Details](../IDE_Navigation/Menus/Version_&_Account_Details.md).
- **Useful Resources**: This shows you various tiles that you can click on to access official tutorial resources for GameMaker.

## IDE Menus

At the top you can find the general IDE menus which are explained in the following sections of the manual:

- [The File Menu](../IDE_Navigation/Menus/The_File_Menu.md)
- [The Edit Menu](../IDE_Navigation/Menus/The_Edit_Menu.md)
- [The Build Menu](../IDE_Navigation/Menus/The_Build_Menu.md)
- [The Windows Menu](../IDE_Navigation/Menus/The_Windows_Menu.md)
- [The Tools Menu](../IDE_Navigation/Menus/The_Tools_Menu.md)
- [The Marketplace Menu](../IDE_Navigation/Menus/The_Marketplace_Menu.md)
- [The Layouts Menu](../IDE_Navigation/Menus/The_Layouts_Menu.md)
- [The Help Menu](../IDE_Navigation/Menus/The_Help_Menu.md)
- [Version \& Account Details](../IDE_Navigation/Menus/Version_&_Account_Details.md)

Note that there will also appear  **context specific** menu options in the top menu bar, depending on the window that you have focused on currently. For example, if you have the Image Editor window in focus then you will have extra menu items here for "**Images**", "**View**" and "**Effects**". These extra menu items are explained in the relevant sections of the manual for the workspace or window that generated them.

 

# Starting A New Project

You can click the **New** button to create a new project, the **Open** button to open an existing project or the **Import** button to open a compressed  YYZ GameMaker project file or a legacy [GameMaker: Studio 1\.4](#)  GMX project file. Both Open and Import will open the file explorer for you to browse to the project file you require.

  GameMaker is not completely backwards compatible with GameMaker: Studio 1\.4 projects but imported 1\.4 projects should still run, as obsolete functionality has been recreated for you automatically using **compatibility scripts**. For full details of the possible issues and the changes made to GML, please see the Help Center article [Porting A GMS 1\.4 Project To GameMaker](https://gamemaker.io/en/help/articles/porting-a-gms-1-4-game-to-gamemaker), as well as the section of the manual on [Obsolete Functions](../Additional_Information/Obsolete_Functions.md).

To create a new project simply click the button labelled **New**, which will open the Project Type and Template menu:

First select a project type, which should be **Game** unless you are making a [Live Wallpaper](https://gamemaker.io/en/help/articles/how-to-make-live-wallpapers-with-gamemaker) or [Game Strip](https://gamemaker.io/en/help/articles/how-to-create-game-strips-with-gamemaker) for GX.games.

After choosing your project type, choose a template. For games, there are two types of blank project templates provided:

- **Blank Game**: Creates a blank project with "**Interpolate colours between pixels**" turned **on** in all platforms' [Game Options](../Settings/Game_Options.md) (see: [Graphics](../Settings/Game_Options/Windows.md#graphics)). This smooths hard edges in the final render of the game.
- **Blank Pixel Game**: Creates a blank project with "**Interpolate colours between pixels**" turned **off**. Choose this option for projects that use pixel art, as pixels in the final render are not smoothed and everything appears crisp.

The rest of the templates are game samples that provide a starting point for different game genres and also double as a learning resource. If you selected a non\-blank template, you may need to choose between [GML Code](../GameMaker_Language.md) and [GML Visual](../GameMaker_Language.md) versions.

Then choose a name and save location for your project.

Finally, click on **Let's Go!** to create and open your new project.

 
  You can create your own template by opening a project, and [exporting as a template](../IDE_Navigation/Menus/The_File_Menu.md#exportproject).

  For information on project loading issues, see: [Project Format](../Additional_Information/Project_Format.md)
