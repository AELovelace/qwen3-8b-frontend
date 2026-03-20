# Plugin Preferences

The **Plugin Preferences** are used to control any extra plugins that have been added to the GameMaker IDE. By default this has one section dedicated to the **Source Control** plugin for integrating GameMaker projects with [Git](https://git-scm.com/).

[Project Tool](#)

This section contains the preferences related to [Project Tool](../../IDE_Tools/Project_Tool.md):

- **Path to Project Tool**: Here you can specify an alternative path to Project Tool. This field is empty by default, which indicates that either the version bundled with this release of the IDE or the latest version installed in the [Package Manager](../../IDE_Tools/Package_Manager.md) is used. You should normally not need to change this. See [Project Tool Versions](../../IDE_Tools/Project_Tool.md#project_tool_versions).
- **Show Project Tool Output**: When this option is checked, the [Project Tool Output](../../IDE_Tools/Project_Tool.md#project_tool_output) window will be shown when you convert projects with Project Tool. This is enabled by default.

[Source Control (Git)](#)

This section deals with the preferences that are required to get the [Git SCM](../../IDE_Tools/Source_Control.md) plugin to work with GameMaker.

- **Git executable path**: This is the location of the Git executable which GameMaker uses for all Source Control commands. This will be located in the cmd folder of your Git installation by default, as shown in the image above.

Below this you can set up the *Merge Tool* and the *Diff Tool* for Source Control with these settings (**optional**):

- **Merge (Tool location)**: Here you specify the full file path to the Git merge tool.
- ****Merge (Tool options)****: In this field you can add any extra commands to be run whenever you use the merge Tool.
- ****Diff (Tool location)****: Here you specify the full file path to the Git diff tool.
- ******Diff (Tool options)******: In this field you can add any extra commands to be run whenever you use the diff Tool.

Finally there are two more options that affect how Git is set up in new projects: 

- **Add skeleton .git defaults to new projects**: When this setting is enabled, GameMaker will add [.gitignore and .gitattributes Files](../../Additional_Information/Project_Format.md#gitignore_and_gitattributes_files) to new projects that you create. It is enabled by default.
- **Add skeleton .git defaults to imported projects**: When this setting is enabled, GameMaker will add [.gitignore and .gitattributes Files](../../Additional_Information/Project_Format.md#gitignore_and_gitattributes_files) to projects that you import from a .yyz file. It is enabled by default.
