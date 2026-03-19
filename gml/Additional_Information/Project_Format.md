# Project Format

This page contains details on the project format used by GameMaker. Issues with project compatibility may be resolved with the [Project Tool](../IDE_Tools/Project_Tool.md).

## Project Load Failure

Project loading may sometimes fail if certain resources cannot be found. This may occur with regular resources (assets etc.) or with [Prefabs](../IDE_Tools/Prefab_Library.md).

For errors that don't cause the project to fail loading, see the **Project Health** window at the bottom of [The Windows Menu](../IDE_Navigation/Menus/The_Windows_Menu.md).

For errors that cause the project to fail loading, GameMaker will try to salvage what it can by prompting you to unlink resources:

This is **not a replacement** for proper source control and only attempts to load the project in a way that doesn't make the IDE unstable, hence it is not a solution for a broken project.

In case the missing resources are from a [package](../IDE_Tools/Package_Manager.md), you will have the option to reinstall the linked packages:

## Format Basics

### The YYP Project File

At the root is the main project file, with a \*.yyp extension. It describes the resources in the project and other metadata specific to it.

### The .resource\_order File

Next to it is another file with a \*.resource\_order extension. This file stores the order of groups and assets in [The Asset Browser](../Introduction/The_Asset_Browser.md) used when the filter is set to **Custom Order**.

  GameMaker will add this file to .gitignore by default if **Add skeleton .git defaults to new/imported projects** is enabled under **Source Control (Git)** in the [Plugin Preferences](../Setting_Up_And_Version_Information/IDE_Preferences/Plugin_Preferences.md).

### YY Files

These are resource files; they store information on individual assets in a GameMaker project. They describe the data for the resource and any other files belonging to the resource (e.g. scripts, shaders, images and audio files). These data are stored in a JSON\-like format.

Any YY resource files with missing associated files (e.g. a missing PNG for a sprite resource) are reported in the [Project Health](../IDE_Navigation/Menus/The_Windows_Menu.md) window when the project is opened.

### .gitignore and .gitattributes Files

These two files affect how a GameMaker project is treated by Git. They are automatically added to new and/or imported projects when **Add skeleton .git defaults to new/imported projects** under **Source Control (Git)** in the [Plugin Preferences](../Setting_Up_And_Version_Information/IDE_Preferences/Plugin_Preferences.md) is enabled. They're also added to new projects that you create from local asset packages. Alternatively, you can disable the settings and add and modify these files yourself instead.

  These files are only used with source control, which you can enable in the [Game Options](../Settings/Game_Options.md).

The .gitignore file is used to make Git ignore certain patterns of files. The default .gitignore file added by GameMaker ignores a few files and file extensions:

- Files added to directories by Windows and macOS that can be ignored (e.g. thumbnails).
- The .resource\_order file used by GameMaker itself, used as more of a user\-specific way of ordering the asset tree. This file doesn't have to be included in source control unless explicitly wanted.

The .gitattributes file controls how Git handles certain files. The default .gitattributes file added by GameMaker introduces the following changes: 

- GameMaker's .yy files as marked as *linguist\-generated*, which prevents GitHub from identifying these as the wrong language.
- Line endings are forced to be LF (*line feed*) for metadata files to make merging easier across different platforms, as Windows, macOS and Linux all use different conventions to represent a line ending.

## YYZ Files

This type of file stores a compressed project export, created via the **Export Project** \> **YYZ** option in [The File Menu](../IDE_Navigation/Menus/The_File_Menu.md). Depending on the version of GameMaker, the compression method used may vary.

## Local Asset Packages

These are created and imported from (part of) a project's contents using **Create Local Package** and **Import Local Package** respectively in [The Tools Menu](../IDE_Navigation/Menus/The_Tools_Menu.md).

The following is an overview of the file formats used by different GameMaker versions: 

- YYMPS \- Compressed Marketplace Asset 2\.3\+; a file containing a marketplace asset stored in a compressed manner.
- YYMP \- Compressed Marketplace Asset \< 2\.3; older formatted marketplace asset stored in a compressed manner. These will be upgraded on import.
- GMEZ \- Compressed Marketplace Asset 1\.x; older again formatted marketplace asset. These will be upgraded on import.
- GMX \- Resource File 1\.x; older formatted resource file. project.gmx are project files and will be upgraded on import. Importing GMX resources as standalone is not supported.
