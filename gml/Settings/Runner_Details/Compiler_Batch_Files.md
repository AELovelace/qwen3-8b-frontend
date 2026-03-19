# Compiler Batch Files / Scripts

The GameMaker compiler allows you to place Batch files (Windows) or Shell scripts (on macOS and Linux) in your project directory, and in the directory for each extension in your project. These are run when you build your game or clean cache.

## Placement

A script file may be placed at the root of your project directory, alongside the project's .yyp file.

A script file may also be placed in the directory of an extension, which may look like this: \/extensions/\/.

The extension versions of a script file will be executed first, and its root version will be executed last. The order in which extensions are executed cannot be controlled, so an extension developer must ensure that one extension's scripts do not rely on another extension's scripts.

## Execution

Script files with specific names, placed in any of the directories described above, are executed at various points during the asset compiler process.

The scripts listed in the table below are run first for all the processes that make use of compiler scripts (whether it's building, running or cleaning cache):

| Windows Batch File Name | macOS/Linux Shell Script Name | Description |
| --- | --- | --- |
| **pre\_project\_step.bat** | **pre\_project\_step.sh** | This is executed before the asset compiler starts loading the project files    If placed in an extension, that extension's "Copies To" setting will be ignored for pre\_project\_step and it will run even if the extension does not export to the target/configuration being compiled. This happens because the project has not been loaded yet and the extension's settings cannot be determined. |
| **post\_project\_step.bat** | **post\_project\_step.sh** | This is executed after the asset compiler has finished loading the project files    The note for pre\_project\_step above applies to this as well: extension export settings will be ignored for consistency with the previous step. |

The scripts listed below are run when running or building your project:

  The steps in these tables are listed in the order that they are run, and work on every platform, except for those under "**Platform\-Specific Steps**".

| Windows Batch File Name | macOS/Linux Shell Script Name | Description |
| --- | --- | --- |
| **pre\_run\_step.bat** | **pre\_run\_step.sh** | *Only runs when testing the game ("Run" command or F5 in the IDE), not run when building a package*   This is executed before the game deployment is about to start |
| **pre\_build\_step.bat** | **pre\_build\_step.sh** | This is executed before the asset compiler is asked to build the game |
| **post\_textures.bat** | **post\_textures.sh** | This is executed after the textures for your game have been generated. You can use this step to optimise your game textures manually.   This script receives an environment variable called TexturesDir, which stores the path to the generated textures. |
| **post\_build\_step.bat** | **post\_build\_step.sh** | This is executed after the asset compiler has been started for building the game |
| **remote\_build\_step.bat** | **remote\_build\_step.sh** | This is executed on the remote machine, when you are on a Windows machine and compiling remotely for macOS/iOS/tvOS or Ubuntu. |
| **pre\_package\_step.bat** | **pre\_package\_step.sh** | This is executed before the final packaging step, which is when all files are ready but the final ZIP file or store package is about to be created |
| **post\_package\_step.bat** | **post\_package\_step.sh** | *Only runs when building a package/executable*   This is executed after the final packaging step has completed and the final ZIP file or store package has been prepared. It will run locally on the machine where the package command was executed even when compiling for a different device (e.g. Windows to macOS). |
| **post\_run\_step.bat** | **post\_run\_step.sh** | *Only runs when testing the game ("Run" command or F5 in the IDE), not run when building a package*   This is executed when the game is prepared and ready to run. After the script's execution, the game is started (unless you exit the script with 1). It will run locally on the machine where the run command was executed even when compiling for a different device (e.g. Windows to macOS). |
| Platform\-Specific Steps | | |
| **pre\_gradle\_step.bat** | **pre\_gradle\_step.sh** | Android This is executed when the files necessary for the Android tools have been created, but before Gradle is called. You can use this step to access and modify the Android files yourself, before the Android tools compile it into a final executable. |

The scripts listed below are run when cleaning the cache:

| Windows Batch File Name | macOS/Linux Shell Script Name | Description |
| --- | --- | --- |
| **pre\_clean\_step.bat** | **pre\_clean\_step.sh** | This is executed before the cache directory is cleaned during a Clean operation |
| **post\_clean\_step.bat** | **post\_clean\_step.sh** | This is executed after the cache directory is cleaned during a Clean operation |

## Environment Variables

You can retrieve the extension version and any of the extension options in the Batch files/Shell scripts: 

- Extension option: YYEXTOPT\_\\_\
- Version number: GMEXT\_\\_version

Replace \ here with the name of the extension you're using.

The GameMaker compiler also sets other variables. To get the full list you can use the set command in a script on Windows and the env command on Mac and Linux.

## Disabling Scripts for an Extension

If you use multiple extensions that run scripts, for example, Steamworks and GDK, then you'll want to disable Steamworks when exporting to GDK, and vice versa.

For that, see: [How to Disable An Extension For A Target?](../../The_Asset_Editors/Extension_Creation/Disabling_Extensions.md)
