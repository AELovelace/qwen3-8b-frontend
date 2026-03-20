# Building \& Testing via Command Line

  Building executables via command line requires you to have [logged in to the IDE](../Setting_Up_And_Version_Information/Licencing_Information.md).

In addition to building your project through the IDE, GameMaker allows you to build your projects through a command\-line interface using the many options and commands described below. You can use this to build your project, test it and deploy it to multiple platforms by running one batch file, and to set up continuous integration through an automation server such as [Jenkins](https://www.jenkins.io/ "Jenkins") or [GitHub Actions](https://github.com/features/actions).

This is done by running the Igor.exe executable present within your runtime folder and passing in the options and commands listed on this page.

By default, Igor can be found in:

- Windows: C:\\ProgramData\\GameMakerStudio2\\Cache\\runtimes\\runtime\-\[version]\\bin\\igor\\\\\\\\
- macOS: /Users/Shared/GameMakerStudio2/Cache/runtimes/runtime\-\[version]/bin/igor/osx/\/

  You must have logged into the IDE with your account at least once before attempting command line building.

### Index

This page covers the following:

- [Igor CI Building](#s1)
- [Igor Runtime](#s2)
- [Igor Testing](#s3)

Also see: [Compiler Batch Files / Scripts](Runner_Details/Compiler_Batch_Files.md)

 

# Igor CI Building

## Setting Up

To set up CI building on a machine, you will need to do the following:

- Install GameMaker and the runtimes needed
- Build the projects through the IDE for the targets required, to make sure that they work fine
- Test building from the command line (see examples below)
- Create a batch file that will do the build that you require within the task (test this from the command line)
- Set up a CI environment (this depends on how you are going to build your games), like [Jenkins](https://www.jenkins.io/ "Jenkins") or [GitHub Actions](https://github.com/features/actions).
- Set up your CI task and ensure that all the prerequisites are set up (i.e. source control sync to your project)
- Hook the batch file into the CI task and test it (e.g. within the Jenkins/GitHub environment)

## Notes

- Some platforms may have issues with the length of your file paths, in which case you will need to [subst](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/subst "subst documentation") virtual drives on your PC before passing them into your commands
- Some platforms (notably Android) will automatically subst a drive while building, so you may need to manually clean this up in the event of an error

## Options

Here are the options that you can use while running the **Igor** executable:

| Option | Description |
| --- | --- |
| /lf\=\[licence\_plist\_file] | The full path to the licence file, either from the IDE or from the [Access Key](#access_key) service   To retrieve the licence from the IDE, the paths are as follows:  Windows: %appdata%\\GameMakerStudio2\\username\_number\\licence.plist macOS: \~/Library/Application Support/GameMakerStudio2/username\_number/licence.plist |
| /uf\=\[user\_folder] | The user folder used for retrieving licence information, alternative to /lf   On Windows, this will be: %appdata%\\GameMakerStudio2\\username\_number\\  On macOS, this will be: \~/Library/Application Support/GameMakerStudio2/username\_number/ |
| /rp\=\[runtime\_root] | The root folder of the runtime |
| /project\=\[project\_YYP\_file] | The full path to the project's .yyp file |
| /cache\=\[cache\_dir\_path] | The cache directory to use (defaults to \\cache in the current directory) |
| /temp\=\[temp\_dir\_path] | The temporary directory to use (defaults to c:\\temp) |
| /of\=\[output\_filename] | The filename of the output executable without the extension, e.g. C:/output/game, which would output the executable at C:/output/game.zip (or a different file format depending on the platform)   If this is not specified, a directory named output will be created in the same directory as the .bat file (or where the command is running from), containing the extracted build files |
| /tf\=\[target\_file] | The actual file name of the ZIP file or NSIS installer that is created |
| /config\=\[configName] | The name of the configuration to use (defaults to Default) |
| /runtime\=YYC\|VM | The output type (either YYC or VM), defaults to VM |
| /j\=\[NumCPUs] | The number of CPUs to use during the build process |
| /df\=\[devices\_json\_file] | The path to your devices.json file, required when building to other devices.   On Windows, this will be: %appdata%\\GameMakerStudio2\\username\_number\\devices.json  On macOS, this will be: \~/Library/Application Support/GameMakerStudio2/username\_number/devices.json |
| /device\=\[device\_name\_from\_IDE] | The name of the target device to build to, as set up in the IDE |
| /launch | Launch the executable on the target device after building; same as the ["Create Executable and Launch" option](../IDE_Navigation/Menus/The_Build_Menu.md) in the IDE |
| /packagetype | For the GX.games target, select the type of package to build, from: "OperaGXPackage\_Zip", "OperaGXPackage\_Gamestrip", or "OperaGXPackage\_Wallpaper" |
| /prefabs | Directory containing any [Prefab](../IDE_Tools/Prefab_Library.md) Collections used in the project, which can be found in the GameMakerStudio2 folder described at the top of this page (under Igor path). You can use the original directory or copy the required Prefab Collections elsewhere and link this option to the directory containing them.    The /projecttool option is required when using this. |
| /projecttool | The [Project Tool](../IDE_Tools/Project_Tool.md) executable file to use, required if using the /prefabs option. This can be found in the [package install directory](../Setting_Up_And_Version_Information/IDE_Preferences/Package_Manager_Preferences.md) under GMTools. |

## Access Key

The /lf option requires a path to your licence.plist file, which can be retrieved from your GameMaker installation after you've logged into the IDE, as described in the table above.

However, if you don't have access to an IDE installation, you can request an access key from the GameMaker website, and generate a licence.plist file from it.

- Go to [gamemaker.io/account/access\_keys](https://gamemaker.io/account/access-keys), and log in with an account that has the appropriate licence
- Generate a key and copy it to your clipboard
- Open a command prompt and navigate to the Igor directory (the path is given at the top of this page)
	- cd \
- Generate a licence file using Igor
	- igor runtime FetchLicense \-ak\=\ \-of\=\
- The licence.plist file generated to the \-of path can now be used in the /lf option

## Hello World

Here is a step\-by\-step example for running a game on Windows:

- Open a command prompt window
	- Win\+R, write cmd, press Enter
- Navigate to the Igor directory given at the top of this page
	- cd \
- Write igor and hit Enter to confirm you are in the correct place. Doing this should give you a list of Igor's commands. If you get a different result, ensure you are in the correct directory.
- Run a game by supplying the project file, runtime directory, licence file, platform and build type. Enclose each directory in double quotes (" ") to ensure spaces are handled properly.
	- igor /project\="\\\projectname.yyp" /rp\="\" /lf\="\\\licence.plist" Windows Run
- Your game should now run!

## Platform Examples

Below you can find examples of build commands for all platforms:

[GX.games](#)

Cleaning GX.games project:

Igor.exe /uf\=\[user\_folder] /rp\=\[runtime\_path] /project\=\[project\_YYP\_file] /cache\=\[cache\_dir\_path] /temp\=\[temp\_dir\_path] \-\- OperaGX Clean

Running GX.games:

Igor.exe /uf\=\[user\_folder] /rp\=\[runtime\_path] /project\=\[project\_YYP\_file] /cache\=\[cache\_dir\_path] /temp\=\[temp\_dir\_path] \-\- OperaGX Run

Building GX.games as a ZIP:

Igor.exe /uf\=\[user\_folder] /rp\=\[runtime\_path] /project\=\[project\_YYP\_file] /cache\=\[cache\_dir\_path] /temp\=\[temp\_dir\_path] /packagetype\="OperaGXPackage\_Zip" \-\- OperaGX Package

[Windows](#)

Cleaning Windows project:

Igor.exe /uf\=\[user\_folder] /rp\=\[runtime\_path] /project\=\[project\_YYP\_file] /cache\=\[cache\_dir\_path] /temp\=\[temp\_dir\_path] \-\- Windows Clean

Cleaning when using a remote device for Mac/Linux on Windows (simply mention a /device and use Mac or Linux instead of Windows):

Igor.exe /uf\=\[user\_folder] /rp\=\[runtime\_path] /project\=\[project\_YYP\_file] /cache\=\[cache\_dir\_path] /temp\=\[temp\_dir\_path] /device\=\[device\_name] \-\- Mac/Linux Clean

Building VM for Windows \-\- Run, PackageZip and PackageNsis:

Igor.exe /uf\=\[user\_folder] /rp\=\[runtime\_path] /project\=\[project\_YYP\_file] /cache\=\[cache\_dir\_path] /temp\=\[temp\_dir\_path] \-\- Windows Run

Igor.exe /uf\=\[user\_folder] /rp\=\[runtime\_path] /project\=\[project\_YYP\_file] /cache\=\[cache\_dir\_path] /temp\=\[temp\_dir\_path] /of\=\[output\_filename] /tf\=\[target\_file] \-\- Windows PackageZip

Igor.exe /uf\=\[user\_folder] /rp\=\[runtime\_path] /project\=\[project\_YYP\_file] /cache\=\[cache\_dir\_path] /temp\=\[temp\_dir\_path] /of\=\[output\_filename] /tf\=\[target\_file] \-\- Windows PackageNsis

Building YYC for Windows\-\- Run, PackageZip and PackageNsis:

Igor.exe /uf\=\[user\_folder] /rp\=\[runtime\_path] /project\=\[project\_YYP\_file] /cache\=\[cache\_dir\_path] /temp\=\[temp\_dir\_path] /runtime\=YYC \-\- Windows Run

Igor.exe /uf\=\[user\_folder] /rp\=\[runtime\_path] /project\=\[project\_YYP\_file] /cache\=\[cache\_dir\_path] /temp\=\[temp\_dir\_path] /of\=\[output\_filename] /tf\=\[target\_file] /runtime\=YYC \-\- Windows PackageZip

Igor.exe /uf\=\[user\_folder] /rp\=\[runtime\_path] /project\=\[project\_YYP\_file] /cache\=\[cache\_dir\_path] /temp\=\[temp\_dir\_path] /of\=\[output\_filename] /tf\=\[target\_file] /runtime\=YYC \-\- Windows PackageNsis

[macOS](#)

  On Mac you will need to use **mono** to run Igor, so you will need to write **mono** before all your commands, e.g.: mono Igor.exe \[options]

Cleaning macOS project:

Igor.exe /uf\=\[user\_folder] /rp\=\[runtime\_path] /project\=\[project\_YYP\_file] /cache\=\[cache\_dir\_path] /temp\=\[temp\_dir\_path] \-\- Mac Clean

Building VM for macOS while on a Mac:

  Use **PackageZip** to build a ZIP file, and **PackageDMG** to build a DMG. These examples use **PackageZip**.

Igor.exe /uf\=\[user\_folder] /rp\=\[runtime\_path] /project\=\[project\_YYP\_file] /cache\=\[cache\_dir\_path] /temp\=\[temp\_dir\_path] /of\=\[output\_filename] /tf\=\[target\_file] \-\- Mac PackageZip

Building VM for macOS while on a PC:

Igor.exe /uf\=\[user\_folder] /rp\=\[runtime\_path] /project\=\[project\_YYP\_file] /cache\=\[cache\_dir\_path] /temp\=\[temp\_dir\_path] /of\=\[output\_filename] /tf\=\[target\_file] /device\=\[device\_IDE\_Name] \-\- Mac PackageZip

Building YYC for macOS while on a Mac:

Igor.exe /uf\=\[user\_folder] /rp\=\[runtime\_path] /project\=\[project\_YYP\_file] /cache\=\[cache\_dir\_path] /temp\=\[temp\_dir\_path] /of\=\[output\_filename] /tf\=\[target\_file] /runtime\=YYC \-\- Mac PackageZip

Building YYC for macOS while on a PC:

Igor.exe /uf\=\[user\_folder] /rp\=\[runtime\_path] /project\=\[project\_YYP\_file] /cache\=\[cache\_dir\_path] /temp\=\[temp\_dir\_path] /of\=\[output\_filename] /tf\=\[target\_file] /runtime\=YYC /device\=\[device\_IDE\_Name] \-\- Mac PackageZip

[Linux / Ubuntu](#)

Cleaning Linux project:

Igor.exe /uf\=\[user\_folder] /rp\=\[runtime\_path] /project\=\[project\_YYP\_file] /cache\=\[cache\_dir\_path] /temp\=\[temp\_dir\_path] \-\- Linux Clean

Building VM for Linux while on a PC:

Igor.exe /uf\=\[user\_folder] /rp\=\[runtime\_path] /project\=\[project\_YYP\_file] /cache\=\[cache\_dir\_path] /temp\=\[temp\_dir\_path] /of\=\[output\_filename] /tf\=\[target\_file] /device\=\[device\_IDE\_Name] \-\- Linux Package

Building YYC for Linux while on a PC:

Igor.exe /uf\=\[user\_folder] /rp\=\[runtime\_path] /project\=\[project\_YYP\_file] /cache\=\[cache\_dir\_path] /temp\=\[temp\_dir\_path] /of\=\[output\_filename] /tf\=\[target\_file] /runtime\=YYC /device\=\[device\_IDE\_Name] \-\- Linux Package

[HTML5](#)

Cleaning HTML5 project:

Igor.exe /uf\=\[user\_folder] /rp\=\[runtime\_path] /project\=\[project\_YYP\_file] /cache\=\[cache\_dir\_path] /temp\=\[temp\_dir\_path] \-\- HTML5 Clean

Building HTML5 folder (make sure to specify a target folder with /tf):

Igor.exe /uf\=\[user\_folder] /rp\=\[runtime\_path] /project\=\[project\_YYP\_file] /cache\=\[cache\_dir\_path] /temp\=\[temp\_dir\_path] /of\=\[output\_filename] /tf\=\[target\_folder] \-\- HTML5 folder

[iOS](#)

Building VM for iOS while on a Mac:

Igor.exe /uf\=\[user\_folder] /rp\=\[runtime\_path] /project\=\[project\_YYP\_file] /cache\=\[cache\_dir\_path] /temp\=\[temp\_dir\_path] /of\=\[output\_filename] /tf\=\[target\_file] \-\- ios Package

Building VM for iOS while on a PC:

Igor.exe /uf\=\[user\_folder] /rp\=\[runtime\_path] /project\=\[project\_YYP\_file] /cache\=\[cache\_dir\_path] /temp\=\[temp\_dir\_path] /of\=\[output\_filename] /tf\=\[target\_file] /device\=\[device\_IDE\_Name] \-\- ios Package

Building YYC for iOS while on a Mac:

Igor.exe /uf\=\[user\_folder] /rp\=\[runtime\_path] /project\=\[project\_YYP\_file] /cache\=\[cache\_dir\_path] /temp\=\[temp\_dir\_path] /of\=\[output\_filename] /tf\=\[target\_file] /runtime\=YYC \-\- ios Package

Building YYC for iOS while on a PC:

Igor.exe /uf\=\[user\_folder] /rp\=\[runtime\_path] /project\=\[project\_YYP\_file] /cache\=\[cache\_dir\_path] /temp\=\[temp\_dir\_path] /of\=\[output\_filename] /tf\=\[target\_file] /runtime\=YYC /device\=\[device\_IDE\_Name] \-\- ios Package

[Android](#)

Cleaning Android project:

Igor.exe /uf\=\[user\_folder] /rp\=\[runtime\_path] /project\=\[project\_YYP\_file] /cache\=\[cache\_dir\_path] /temp\=\[temp\_dir\_path] \-\- Windows Clean

Building an Android APK using VM:

Igor.exe /uf\=\[user\_folder] /rp\=\[runtime\_path] /project\=\[project\_YYP\_file] /cache\=\[cache\_dir\_path] /temp\=\[temp\_dir\_path] /of\=\[output\_filename] /tf\=\[target\_file] \-\- Android Package

Building an Android APK using YYC:

Igor.exe /uf\=\[user\_folder] /rp\=\[runtime\_path] /project\=\[project\_YYP\_file] /cache\=\[cache\_dir\_path] /temp\=\[temp\_dir\_path] /of\=\[output\_filename] /tf\=\[target\_file] /runtime\=YYC \-\- Android Package

[tvOS](#)

Cleaning tvOS project:

Igor.exe /uf\=\[user\_folder] /rp\=\[runtime\_path] /project\=\[project\_YYP\_file] /cache\=\[cache\_dir\_path] /temp\=\[temp\_dir\_path] \-\- tvos Clean

Building VM for tvOS while on a Mac:

Igor.exe /uf\=\[user\_folder] /rp\=\[runtime\_path] /project\=\[project\_YYP\_file] /cache\=\[cache\_dir\_path] /temp\=\[temp\_dir\_path] /of\=\[output\_filename] /tf\=\[target\_file] \-\- tvos Package

Building VM for tvOS while on a PC:

Igor.exe /uf\=\[user\_folder] /rp\=\[runtime\_path] /project\=\[project\_YYP\_file] /cache\=\[cache\_dir\_path] /temp\=\[temp\_dir\_path] /of\=\[output\_filename] /tf\=\[target\_file] /device\=\[device\_IDE\_Name] \-\- tvos Package

Building YYC for tvOS while on a Mac:

Igor.exe /uf\=\[user\_folder] /rp\=\[runtime\_path] /project\=\[project\_YYP\_file] /cache\=\[cache\_dir\_path] /temp\=\[temp\_dir\_path] /of\=\[output\_filename] /tf\=\[target\_file] /runtime\=YYC \-\- tvos Package

Building YYC for tvOS while on a PC:

Igor.exe /uf\=\[user\_folder] /rp\=\[runtime\_path] /project\=\[project\_YYP\_file] /cache\=\[cache\_dir\_path] /temp\=\[temp\_dir\_path] /of\=\[output\_filename] /tf\=\[target\_file] /runtime\=YYC /device\=\[device\_IDE\_Name] \-\- tvos Package

[PS4](#)

Cleaning PS4 project:

Igor.exe /uf\=\[user\_folder] /rp\=\[runtime\_path] /project\=\[project\_YYP\_file] /cache\=\[cache\_dir\_path] /temp\=\[temp\_dir\_path] \-\- ps4 Clean

Building VM for PS4 while on a PC:

Igor.exe /uf\=\[user\_folder] /rp\=\[runtime\_path] /project\=\[project\_YYP\_file] /cache\=\[cache\_dir\_path] /temp\=\[temp\_dir\_path] /of\=\[output\_filename] /tf\=\[target\_file] /device\=\[device\_IDE\_Name] \-\- ps4 Package

Building YYC for PS4 while on a PC:

Igor.exe /uf\=\[user\_folder] /rp\=\[runtime\_path] /project\=\[project\_YYP\_file] /cache\=\[cache\_dir\_path] /temp\=\[temp\_dir\_path] /of\=\[output\_filename] /tf\=\[target\_file] /runtime\=YYC /device\=\[device\_IDE\_Name] \-\- ps4 Package

[PS5](#)

Cleaning PS5 project:

Igor.exe /uf\=\[user\_folder] /rp\=\[runtime\_path] /project\=\[project\_YYP\_file] /cache\=\[cache\_dir\_path] /temp\=\[temp\_dir\_path] \-\- ps5 Clean

Building VM for PS5 while on a PC:

Igor.exe /uf\=\[user\_folder] /rp\=\[runtime\_path] /project\=\[project\_YYP\_file] /cache\=\[cache\_dir\_path] /temp\=\[temp\_dir\_path] /of\=\[output\_filename] /tf\=\[target\_file] /device\=\[device\_IDE\_Name] \-\- ps5 Package

Building YYC for PS5 while on a PC:

Igor.exe /uf\=\[user\_folder] /rp\=\[runtime\_path] /project\=\[project\_YYP\_file] /cache\=\[cache\_dir\_path] /temp\=\[temp\_dir\_path] /of\=\[output\_filename] /tf\=\[target\_file] /runtime\=YYC /device\=\[device\_IDE\_Name] \-\- ps5 Package

[Xbox One](#)

Cleaning Xbox One project:

Igor.exe /uf\=\[user\_folder] /rp\=\[runtime\_path] /project\=\[project\_YYP\_file] /cache\=\[cache\_dir\_path] /temp\=\[temp\_dir\_path] \-\- XBoxOne Clean

Building VM for Xbox One while on a PC:

Igor.exe /uf\=\[user\_folder] /rp\=\[runtime\_path] /project\=\[project\_YYP\_file] /cache\=\[cache\_dir\_path] /temp\=\[temp\_dir\_path] /of\=\[output\_filename] /tf\=\[target\_file] /device\=\[device\_IDE\_Name] \-\- XBoxOne Package

Building YYC for Xbox One while on a PC:

Igor.exe /uf\=\[user\_folder] /rp\=\[runtime\_path] /project\=\[project\_YYP\_file] /cache\=\[cache\_dir\_path] /temp\=\[temp\_dir\_path] /of\=\[output\_filename] /tf\=\[target\_file] /runtime\=YYC /device\=\[device\_IDE\_Name] \-\- XBoxOne Package

[Xbox Series X/S](#)

Cleaning Xbox Series X/S project:

Igor.exe /uf\=\[user\_folder] /rp\=\[runtime\_path] /project\=\[project\_YYP\_file] /cache\=\[cache\_dir\_path] /temp\=\[temp\_dir\_path] \-\- XBoxOneSeriesXS Clean

Building VM for Xbox Series X/S:

Igor.exe /uf\=\[user\_folder] /rp\=\[runtime\_path] /project\=\[project\_YYP\_file] /cache\=\[cache\_dir\_path] /temp\=\[temp\_dir\_path] /of\=\[output\_filename] /tf\=\[target\_file] /device\=\[device\_IDE\_Name] \-\- XBoxOneSeriesXS Package

Building YYC for Xbox Series X/S:

Igor.exe /uf\=\[user\_folder] /rp\=\[runtime\_path] /project\=\[project\_YYP\_file] /cache\=\[cache\_dir\_path] /temp\=\[temp\_dir\_path] /of\=\[output\_filename] /tf\=\[target\_file] /runtime\=YYC /device\=\[device\_IDE\_Name] \-\- XBoxOneSeriesXS Package

[Switch](#)

Cleaning Switch project:

Igor.exe /uf\=\[user\_folder] /rp\=\[runtime\_path] /project\=\[project\_YYP\_file] /cache\=\[cache\_dir\_path] /temp\=\[temp\_dir\_path] \-\- Switch Clean

Building VM for Switch while on a PC:

Igor.exe /uf\=\[user\_folder] /rp\=\[runtime\_path] /project\=\[project\_YYP\_file] /cache\=\[cache\_dir\_path] /temp\=\[temp\_dir\_path] /of\=\[output\_filename] /tf\=\[target\_file] /device\=\[device\_IDE\_Name] \-\- Switch Package

Building VM for YYC while on a PC:

Igor.exe /uf\=\[user\_folder] /rp\=\[runtime\_path] /project\=\[project\_YYP\_file] /cache\=\[cache\_dir\_path] /temp\=\[temp\_dir\_path] /of\=\[output\_filename] /tf\=\[target\_file] /runtime\=YYC /device\=\[device\_IDE\_Name] \-\- Switch Package

 

# Igor Runtime

Here are the options that can be used with the Igor runtime:

| Option | Description |
| --- | --- |
| /uf\=\[user\_folder] | Set the user folder used for retrieving licence information so GameMaker knows which modules can be installed |
| /lf\=\[license\_file] | Set the direct path to a licence file, can be used as an alternative to setting a user folder (/uf) |
| /ru\=\[runtime\_url] | Set the URL to fetch runtime information from (defaults to the stable release) |
| /rp\=\[runtime\_root] | Set the local runtime install folder to list the installed runtimes or install new runtimes |

Here are the commands that can be used with the Igor runtime:

#### Syntax:

Igor.exe \[command]

| Command | Description |
| --- | --- |
| Runtime List | Lists the runtimes available on a feed (version number, date/time of build) |
| Runtime ListInstalled \[\-directory] | Lists the runtimes available in the current folder (directory\=full path to the folder)   You can specify a directory to look in, but if it's not specified it will default to the current directory   This also checks whether there is a receipt.json file and a manifest folder inside the directory (making sure that it's actually a runtime) |
| Runtime Info \[\-version] | Prints out information about the most recent runtime on the given feed; also needs a licence file to show information regarding the modules available for the user  version can either by a string used to search through the feed titles (e.g.: "739" would show information for all builds containing 739 in their version numbers), or it can be all to show information for all feeds   It will list the modules with the .zip file names for each module |
| Runtime Install \[\-version] | Installs the latest runtime from the given feed using the given version as a search filter; if that is not specified, it defaults to the latest version. It will get all the modules that the user has on their licence. |
| Runtime Verify \[\-folder\=.] | Calculates the checksums for all the installed files and compares them to the checksums written into the manifest folder. You can specify a folder to check, however if that is not specified it will default to the current directory.   This will flag any files where the checksums don't match, files that are missing and files that should not be there.   Do note that the manifest files themselves are not verified and a user can alter the manifest files to match the installed ones. |
| Runtime FetchLicences \[\-ak] \[\-of] | Generates a licence.plist file (\-of) from an access key (\-ak), see [Access Key](#access_key) |

 

# Igor Testing

Here are the options that can be used for testing your builds with Igor:

| Option | Description |
| --- | --- |
| /uf\=\[user\_folder] | Set the user folder used for retrieving licence information so GameMaker knows which modules can be installed |
| /lf\=\[license\_file] | Set a direct path to a licence file, can be used as an alternative to setting a user folder (/uf) |
| /df\=\[device\_file] | Set a direct path to a devices.json file, can be used as an alternative to setting a user folder (/uf) |
| /timeout\=\[number\_of\_seconds\_to\_wait] | The timeout to use for the test in seconds, defaults to 120 seconds; the test will be stopped after this timeout is over and will be marked as failed |
| /waittime\=\[number\_of\_seconds\_to\_wait] | Number of seconds to wait in the main loop before declaring the test as passed, defaults to 30 seconds |
| /device\=\[device\_name] | Used to look up the device name in the user folder's devices.json file |
| /target\=\[list\_of\_targets] | Comma\-separated list of targets in the PLATFORM\|DEVICE format, e.g.: /target\="Windows\|Local,HTML\|Firefox"   If you specify **all**, the tests will attempt to run for every device in the devices.json file |

  If you are facing bugs in your test set\-up, please [submit a bug report](../Setting_Up_And_Version_Information/Error_Reporting.md) and attach your test files which we can review and test on our end.

There is one command that you can use to run tests with Igor:

Igor.exe Tests RunTests \[test\_directory/test\_filename]

You must specify either a test directory or a test file name.

- If it's a directory, Igor will look for a file called tests.json in the directory
	- If the file **is not found**, Igor will recursively search for .yyz and .yyp files in the directory
		- Each project found will be built and run on Windows
		- It will wait till the runner reaches the main loop
			- The test passes if the runner is still running after the wait time
			- The test fails if the project does not compile within the timeout period, or crashes before the wait time is over
	- If a tests.json file **is found**, Igor will run the tests described in the file (see example below)
- Alternatively, you can supply a direct path to a tests.json file instead of a directory

 

# Tests.json File

## Format

The tests.json file must have the following format:

- The JSON file should contain an array of objects
- Each object should describe one test
	- The test object must contain these keys:
		- name: A name used to report whether the test has passed or failed
		- path: A path to a .yyp, .yyz, .gml, .js file or folder for the test
		- command: The Igor command for the test (Run, CreatePackage, etc. as described above)
	- The test object may also contain these keys:
		- platform: Passed directly through to Igor to do the test
		- device: The device name from the devices.json file
		- target: The target in a "PLATFORM\|TARGET" format, e.g.: "Windows\|Local"
		- timeout: A timeout for the total test including compile and run; if exceeded the test will be stopped and marked as failed
		- waittime: The length of time to wait after entering the main loop before deciding whether the test has passed
		- owner: the e\-mail address of the user who will be e\-mailed if this test fails

## Example

Here is an example of a tests.json file:

\[  

  {  

   "name" : "Game Idea Windows",  

   "path" : "C:/scratch/GameIdea.yyz",  

   "platform" : "Windows",  

   "command" : "Run",  

   "timeout" : "500",  

   "waittime" : "30"  

  },  

  {  

   "name" : "Platformer Game Windows",  

   "path" : "C:/Users/\/Documents/GameMakerStudio2/Platformer Game/PlatformerGame.yyp",  

   "target" : "Windows\|Local,HTML5\|selenium:firefox,PS4\|Default",  

   "command" : "Run"  

  },  

  {  

   "name" : "Puzzle Game Windows",  

   "path" : "C:/Users/\/Documents/GameMakerStudio2/Puzzle Game/PuzzleGame.yyp",  

   "platform" : "HTML5",  

   "command" : "Run",  

   "device" : "selenium:chrome"  

  }  

 ]
