# Prefab Library

The **Prefab Library** is used to import assets from a single **source project** into the currently open project. A source project containing Prefab assets is known as a **Collection**.

When you use an asset from the Prefab Library, that asset is *not copied* into your project but is simply referenced. The actual asset is only loaded from its Collection (source project) when your game is built. This means your game stays up\-to\-date with any changes in the Collection package without you needing to re\-import any assets.

This allows you to use the same assets in multiple projects and have them all be updated when the Collection is updated.

You can customise a Prefab asset to use custom properties while retaining its link to its Collection. You can also choose to duplicate an asset into your project, at which point the asset is unlinked from its Collection, meaning that it will no longer receive updates from its Collection however it will be fully modifiable within your project. See: [Modifying Prefabs](#modif)

  If any used Prefab Collections could not be located during compilation, GameMaker will attempt to download and install the required packages and start the build process again. However, in case the installation fails for any reason (e.g. no internet connection), you can double\-click on the relevant message that appears in the [Compiler Output](../Introduction/The_Output_Window.md) to attempt installation of the required package.

  For possible issues with project loading when Prefab resources cannot be found, see: [Project Format](../Additional_Information/Project_Format.md)

## Adding Prefab Packages

Currently you can use the official GameMaker Asset Bundles via the Prefab Library.

Open the Prefab Library via the [Windows menu](../IDE_Navigation/Menus/The_Windows_Menu.md) in the menu bar. When you open this for the first time, your Prefab Library will be empty.

  You may see Prefab Collections installed by default that are needed for IDE functionality (e.g. [Filters and Effects](../The_Asset_Editors/Room_Properties/Filters_and_Effects.md)).

Click on "**Package Manager**" to add Collection packages:

This opens the [Package Manager](Package_Manager.md) window with the "Package source" drop\-down set to "Prefabs". From here, you can install any of the official GameMaker Asset Bundles.

Once installed, they will show up in your Prefab Library, from where you can navigate to any individual assets within the Collections:

## Using Prefab Assets

Assets from the Prefab Library can be dragged into compatible [asset editors](../The_Asset_Editors/The_Asset_Editors.md) (or [The Inspector](The_Inspector.md)). Currently, you can use assets in the following ways:

- Use [Sprite](../The_Asset_Editors/Sprites.md) assets in [The Object Editor](../The_Asset_Editors/Objects.md), [The Sequence Editor](../The_Asset_Editors/Sequences.md), [The Room Editor](../The_Asset_Editors/Rooms.md), [The Tile Set Editor](../The_Asset_Editors/Tile_Sets.md), and [The Particle System Editor](../The_Asset_Editors/Particle_Systems.md)
- Use [Sound](../The_Asset_Editors/Sounds.md) assets in [The Sequence Editor](../The_Asset_Editors/Sequences.md)
- Use [Tile Set](../The_Asset_Editors/Tile_Sets.md) assets in [The Room Editor](../The_Asset_Editors/Rooms.md)

  You cannot use assets from different versions of the same Prefab Collection in one project. If you do so, you will be prompted to upgrade uses of the older version to the new one for consistency.

Assets from Prefab Collections will not be visible in the Asset Browser, however they will be shown in the Asset Explorers from asset editors (e.g. when selecting a Sprite for an Object). They can also be dragged from the Prefab Library or be used in code (only when the project has a reference to the Collection, see the section below).

When a Prefab Asset is used in any editor, it's shown with an orange highlight as shown below. When inspecting an asset such as an Object, the usual  "Edit Sprite" button is replaced with the  "Open Prefab" button which opens the Prefab Library with the used asset selected.

  If you use assets from a Collection in your project and then delete the package for that Collection, you will get a "**Resource load failure**" error window on opening the project in the IDE and potential errors at runtime.

### Referencing Prefab Assets In Code

For Prefab assets to be used in code, your project needs to have a reference to that Prefab Collection. This is done by either making use of one of its assets through the IDE, which adds a reference to the Prefab Collection in your project, or by manually adding a reference through the right\-click menu in the Prefab Library ("**Add Collection Reference**").

Once your project has a reference to a Prefab Collection, you can use any assets from that Collection in your project's code. However there may be cases where either your project or other referenced Collections have assets with the same name, in which case you can target an asset from a specific Collection using the following syntax:

::package\-version::asset

  You can get the package ID by clicking on a Collection in the Prefab Library window and copying it from the Inspector.

You can pick and choose the details to specify using this syntax, e.g. you may specify just the package without a version, specify only the major version, or specify everything.

For example, say you're trying to use spr\_ui\_heart from io.gamemaker.uiicons:

- spr\_ui\_heart: Simply writing the asset name will pull the asset from the Collection that the project has a reference to, assuming there are no name collisions with other assets in the project or other referenced Collections.
- ::uiicons::spr\_ui\_heart: This will pull the asset from any referenced Collection that has uiicons as the last part of its package ID (e.g. io.gamemaker.uiicons or io.community.uiicons).
- ::io.gamemaker.uiicons::spr\_ui\_heart: This will pull specifically from the io.gamemaker.uiicons package, useful in case there are multiple Collections that end with the same name.
- ::io.gamemaker.uiicons\-1::spr\_ui\_heart: This will pull from a version of the Collection that has 1 as its major version, so e.g. it may pull 1\.0\.0, 1\.0\.3 or 1\.2\.0 etc.
- ::io.gamemaker.uiicons\-1\.0\.3::spr\_ui\_heart: This specifies the full package ID and version to ensure there are no possible name collisions.

Note that your project **must** have a reference to the version of the Collection you are trying to pull from. If the specified asset is not found in the specified Collection, you will get a compile error.

### Referencing Code Symbols

Scripts included in Prefab Collections may export [Enums](../GameMaker_Language/GML_Overview/Variables/Constants.md), [Macros](../GameMaker_Language/GML_Overview/Variables/Constants.md) and [Script Functions](../GameMaker_Language/GML_Overview/Script_Functions.md) using the following syntax:

\#export symbol1,symbol2,symbol3,...

Any project that has a reference to such a Collection can use the exported symbols in code, e.g. to make use of an Enum/Macro or call a Script Function.

### Modifying Prefab Macros

Your project can modify the value of a macro exported by a Prefab Collection, using the following syntax:

\#macro ::\::\[\:]\ \

The \ part can use any kind of the Prefab referencing syntaxes listed in the previous section (e.g. just the last part of the ID, or the full ID, including or excluding a specific version number). The config part is displayed here in square brackets as it's optional.

For example, say a Prefab Collection exports the macro IS\_DEBUG as false by default, and you want to set it to true:

\#macro ::io.gamemaker.platformer::IS\_DEBUG true

You can optionally specify the version of the Prefab Collection and specify a configuration so the macro override only applies to that configuration (here, the configuration is Release):

\#macro ::io.gamemaker.platformer**\-1\.0\.0**::**Release:**IS\_DEBUG true

## Modifying Prefab Assets

Selecting a Prefab asset (e.g. a Sprite, Object, etc.) in the Prefab Library will display its properties in [The Inspector](The_Inspector.md). Here you can preview the properties of the asset.

For text assets (e.g. Shaders, Scripts, Notes), you can view its documents by double\-clicking on it (in read\-only mode and only when using [Code Editor 2 (Beta)](../The_Asset_Editors/The_Text_Editor.md)). For Objects you can double\-click on any of its events to view them.

Dragging an asset from the Prefab Library into the [Asset Browser](../Introduction/The_Asset_Browser.md) will give you the option to either customise the asset or duplicate it:

Both options can also be accessed through the right\-click menu on a Prefab asset and are explained below.

### Customising Prefab Assets

You can right\-click on a Prefab asset or a folder/collection (or a selection of both) and select "**Customise**". This displays the asset (or all assets under the chosen folder/collection) under a "**Prefabs**" folder in the Asset Browser, where you can select an asset and modify its properties (e.g. the Collision Mask of a Sprite, Attributes of a Sound, etc.) in [The Inspector](The_Inspector.md).

Asset customisation is maintained at a project level, so use of the same Prefab Asset in another project is not affected by its customisation in a different project. When the game is built, the asset itself is pulled from the Collection however its modified properties are used as per your modifications in the project. This means the asset still gets updates from its original Collection, if you choose to update it.

  Not every asset type can be customised e.g. Scripts, Shaders and Notes, as they have no customisable properties besides the code content itself. Rooms, Extensions, Tile Sets etc. can also not be customised due to the way their asset editing works.

### Duplicating Prefab Assets

Using the "**Duplicate into Project**" option on an asset (or multiple assets/folders) unlinks the asset(s) from their original Collection and copies them into the currently open project. This means the asset is no longer linked to its Collection and will not receive any updates, and has been copied into the project directory and will take up space in the project. You can fully modify such a duplicated asset similar to any other asset created in the project.

## Exporting a Project with Prefabs

When you [export your project](../IDE_Navigation/Menus/The_File_Menu.md#exportproject) as a **.yyz**, you'll be asked whether you want to include Prefabs Collections in the exported package:

- Choosing "**Yes**" copies the Prefab Collections used in the project into the package and reroutes all references to the copied Collection, detaching it from the installed Collections that the importer may or may not have.
- Choosing "**No**" keeps the Prefab references in the package but does not copy the used Collections, meaning that upon import, the user will need to have the required Collections installed (which they will be prompted to do if the Collections were not found)

## Prefab Library Features

The Prefab Library window is divided into the following sections:

The left section displays the Folder List that contains a tree view of your Prefab Collections. The right section displays the contents of the currently open folder (or your Prefab Collections if no folder is selected). The divider between these two sections can be dragged to resize the sections.

The Folder List section contains the following parts:

- **Search Bar**: This lets you search for any assets across all of the Prefab Collections that you have added from the [Package Manager](Package_Manager.md).
- **Sort/Filter**: This menu gives you the following options for sorting and filtering Prefabs:
	- **A\-Z**/**Z\-A**: Change the alphabetical sorting of Collections and Prefab assets
	- **Used Collections**: Only show the Collections that have been used
	- **Used Prefabs Only**: Only show the Prefab assets that have been used
	- **Customised Prefabs Only**: Only show the Prefab assets that have been customised
	- **Filters \& Effects**: Whether to only show filter and effect Prefabs or to not show them (disabled by default)
	- **Recent Prefabs**: Only show Prefab assets that have been used recently
	- **Favourites**: Only show the Prefab assets that have been favourited
	- **Authors**: Filter by author
	- **Asset Type**: Filter by asset type, so only the selected asset types are shown
	- **Tags**: Filter by tag
- **View Menu**: This lets you switch between the following views that affect how the Prefab Library is displayed:
	- **Horizontal View**: This is the default view. It displays the folder list on the left and the content view on the right.
	- **Vertical View**: This displays the folder list at the top and the content view at the bottom.
	- **Simple View**: This disables the folder list and only displays the content view.
	- **Tree View**: This disables the content view and only displays the folder list. The folder list will now also show the assets within folders so they can be dragged for use in other editors.
- **Package Manager**: This button opens the [Package Manager](Package_Manager.md) where you can install any new Prefab Collections or delete the ones that you have installed.
- **Folder List**: A list of folders from installed Prefab Collections. Selecting a folder here will show its contents in the Contents view if enabled. If you have multiple versions of the same Prefab Collection package installed, they will all be shown in this list and you can choose which version to use (however you can only use assets from one version in the same project).  

  

 You can use the UP and DOWN arrow keys to navigate the list and ENTER to expand/collapse a folder or view its contents in the Contents view if there are no child folders.  

  

 Use CTRL\+LMB or SHIFT\+LMB to select multiple assets/folders so you can run operations on them all at once (e.g. customise, duplicate). Selecting multiple folders in this list will display the contents of all selected folders in the Content View (to the right by default).

The Content View contains the following parts:

- **Path**: This displays a hierarchy of folders that you have opened. You can click on any folder to navigate back to it or click on \< to navigate back to the root. This will be hidden if multiple folders are selected in the Folder List.
- **View Toggle**: This button lets you toggle between grid and list mode for the contents.
- **Contents**: Displays the assets and folders in the selected folder. Double\-clicking on an asset will display its information (name, description and icon) and you can drag assets from this view into other editors in your project (such as the Object Editor, Room Editor, etc.).  

  

 Use CTRL\+LMB or SHIFT\+LMB to select multiple assets/folders so you can run operations on them all at once (e.g. customise, duplicate).

The bottom bar of the window displays the number of items in the selected folder or the number of Collections if no folder is selected.

### RMB Menu

Right\-clicking on any item or selection in the Prefab Library displays the following options:

  Not all of these options may appear at the same time as some depend on the type of item (folder, Collection or asset) and other settings.

- **Make Favourite**: Add the selected folder or asset to Favourites. Your Favourites can be viewed from the  **Sort/Filter** menu.
- **Add/Remove Collection Reference**: Add or remove a reference to this Collection in the current project. When the project has a reference to the Collection, assets from the Collection can be referenced in code.
- **Customise**: This adds the selected asset or all assets under the selected folder to the Asset Browser where you can customise its properties. See: [Customising Prefabs](#custom)
- **Reinstall Prefab Collection**: This reinstalls the package associated with the Prefab Collection. Use this in case you are facing any errors or unintended behaviour with the Prefab Collection.
- **Upgrade Prefab Collection**: If a newer package version of this Collection is installed, upgrade to that version.
- **Uninstall Prefab Collection**: This uninstalls the Prefab Collection and the package associated with it. This is useful in cases where the version of the Prefab Collection you have installed no longer exists in the Package Manager and you would be unable to uninstall it from there. (  You cannot use this option if the Prefab Collection is being used in the currently open project.)
- **Duplicate into Project**: This duplicates the selected asset (or all assets in the selected Collection/folder) into your project as a local asset, i.e. the asset becomes unlinked from its Collection and is fully editable as part of the current project. It will no longer be updated if there are changes to the source asset in the Collection.
	- When used on a Collection or a folder in a Collection, this process is recursive, i.e. it duplicates assets in all subfolders present within the selected folder and all subfolders within them, and so on.
- **Show In Inspector**: Show the selected asset in [The Inspector](The_Inspector.md).
 

---
- **Change Prefab Collection Versions**: Opens a window that allows you to change the version of each Prefab Collection used for the current project.
- **Show in Package Manager**: This opens the [Package Manager](Package_Manager.md) with the package for the Collection selected, so you can check for new versions or make any other changes to the source package.
 

---
- **Expand/Collapse Children**: This option is available in the Folder List. It expands or collapses all folders under the selected folder.
- **Expand/Collapse All:**This option is available in the Folder List. It expands or collapses all folders in the tree view.
