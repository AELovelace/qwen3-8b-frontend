# Package Manager

The Package Manager lets you install packages that GameMaker can use for the IDE and during your game's compilation. Currently you can use this to install and manage versions of various IDE features like localisation plugins, [Project Tool](Project_Tool.md) and the [Prefab Library](Prefab_Library.md). This is also used for packages that are required for [GMRT (GameMaker Runtime)](../Settings/Runner_Details/GMRT_(GameMaker_Runtime).md).

The list on the left will show you all packages from the selected source, and clicking on a package will show its information on the right, where you can choose a version for the package and install it.

Right\-clicking on a package brings up a menu with options:

You can enable or disable update notifications as well as automatic updates for the given package. Note that notifications are enabled by default for GMRT packages and disabled for all other packages.

  Some packages may have other packages installed as dependencies. On uninstalling a package, depending on the package, it may or may not uninstall its dependencies or it may prompt the user to choose whether dependencies should be deleted or kept.

  You cannot uninstall a package if another installed package uses it as a dependency or if it is a required package for the IDE (e.g. Filters and Effects).

In the top\-left corner you can search for a package, and in the top\-right corner you can change the source for the packages from a drop\-down menu.

### Package Sources

A package source is a URL to a remote registry where packages are stored. Selecting a source will change what packages you see listed in the Package Manager, depending not only on the URL of the registry but also on the scopes of that source, which acts as a filter, so only those packages matching the scopes are shown.

You can click on  next to the source drop\-down to edit the list, which will show the following menu:

This shows all the currently available package sources and you can click on a source to edit its details or remove it. You can click on the  button to add a new source.

For each source you can define its name in the list, its URL, its scopes, a username/password and the install subdirectory (under the [Package Manager path](../Setting_Up_And_Version_Information/IDE_Preferences/Package_Manager_Preferences.md)). You can also force all packages to be visible if the registry contains any hidden packages.
