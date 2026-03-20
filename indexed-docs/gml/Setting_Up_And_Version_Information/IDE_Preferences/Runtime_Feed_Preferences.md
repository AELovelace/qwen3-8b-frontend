# Runtime Feeds Preferences

The **Runtime Feeds Preferences** are used to display and change the currently installed [Runtimes](#) as well as the runtime in current use.

GameMaker can have several different runtime versions installed at the same time and you can set which one to use from this menu.

Ideally you want to be using the most up\-to\-date runtimes, but sometimes it may have an issue, or you may be required to use an older one for compatibility, etc. and so you can change the runtime tools that GameMaker uses to build your game here.

## Remember last selection of modules

This option changes if and how the [Runtime Modules Dialog](../Installation_Guide.md#h) is shown.

The following options can be set here: 

| Option | Description |
| --- | --- |
| OK | This option remembers your choice of modules and will not show the [Runtime Modules Dialog](../Installation_Guide.md#h) each time you install any runtime. Instead, it will just automatically install those same runtime modules. It corresponds to the "Remember Selection" checkbox ticked in the Runtime Modules Dialog. |
| Show Message | This option always show the dialog when installing a different runtime. It corresponds to the "Remember Selection" checkbox unticked in the [Runtime Modules Dialog](../Installation_Guide.md#h). |

## Modify Current Runtime Modules

You can click this button to bring up the [Runtime Modules Dialog](../Installation_Guide.md#h) again at any time. Opening the dialog via this button allows you to change the modules that are installed for the *current* runtime.

  The current runtime version can be found in the Version Details displayed in the top\-right corner of the IDE (see [Start Page Elements](../../Introduction/The_Start_Page.md#h)).

The dialog shows the modules that you have already installed for the current runtime and allows you to install additional ones.

## Use Alternative DNS

GameMaker allows you to use an alternative [DNS](#) server if you want to or in case you experience delays getting the updated RSS feeds.

To use this, check the "Use Alternative DNS" checkbox and enter the IP address of the alternative DNS server to use: 

  If you leave the text field empty GameMaker will continue to use your system DNS settings.

Click "Apply" to save the changes. GameMaker will test to see if it can get a valid DNS result from the given IP address. If not an error message will be shown: 

A couple of alternative IP addresses that you can use are 1\.1\.1\.1 and 9\.9\.9\.9\.

## Runtime RSS Feeds

This section of the Runtime Feeds Preferences is related to where you pull the runtime tools from and requires you to input a [URL](#) to an [RSS](#) feed. This feed will then be scanned for updates to the runtime tools which can then be downloaded and installed.

This section will show the Master runtime feed URL by default, but you can click the *Add* button to create a new Runtime Feed where you give the name and the URL for the RSS feed, and then click Apply to tell GameMaker to access it. You will need to close and re\-open the Preferences window for the new feed to be shown.

## Runtime Feeds

Once a Runtime Feed has been created it will be listed in this section as a sub\-category, and you should always have at least one feed listed (by default this would be the *Master* feed). Regardless of the runtime being used, they will all have the same features, outlined below using the Master feed as an example:

Here you can select, install and uninstall the different runtimes. At the top is the runtime currently in use, the date it was created, and its location on the hard drive.

You then have a checkbox to enable GameMaker to automatically clean old runtime installations and a "Clean Runtimes Now" button to do that immediately. It then shows the expected runtime version for the installed IDE and the name of the current runtime feed.

Below that is a list of all the available runtimes. You can choose any one from this list (double\-click) to set it as the "running" runtime used for compiling your projects and you can update this list from the given RSS feed by clicking the refresh button   .

  Your IDE may not display older runtime versions that are not compatible with that IDE. If you already have such runtimes installed, double\-clicking them will do nothing, however you can click on  to delete them. Such older runtimes can be used alongside their matching IDE versions.

For each runtime you can find the version number, the date it was released, and (if it's installed) the path to where it's been installed to. The right hand side also shows the different status icons: 

|  | This marks the current runtime that has been selected for use when building your projects. |
| --- | --- |
|  | Clicking this will initiate the download and installation of the selected runtime (a status bar will be shown in the top right of the [IDE](#)). If [Remember last selection of modules](#h) is set to "No" or "Show Message" you will first be shown the [Runtime Modules Dialog](../Installation_Guide.md#h) where you can select the modules that should be included. |
|  | Clicking this will remove the selected runtime from your hard drive. |

To select a different runtime to use, find it in the list and then double click  its version number in the left\-hand column. If the runtime has not been downloaded and installed, then you will be prompted to do so. Depending on the setting of [Remember last selection of modules](Runtime_Feed_Preferences.md#h) the [Runtime Modules Dialog](../Installation_Guide.md#h) may or may not be shown before download and installation starts: 

Once the new runtime has been installed you will be asked to close and restart the IDE so that the runtime can be initialised.
