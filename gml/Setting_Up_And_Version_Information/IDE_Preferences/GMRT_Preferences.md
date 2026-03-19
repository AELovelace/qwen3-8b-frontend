# GMRT Preferences

This section contains preferences for [GMRT (GameMaker Runtime)](../../Settings/Runner_Details/GMRT_(GameMaker_Runtime).md):

- **Path to GMRT**: This should be where the GMRT [packages](Package_Manager_Preferences.md) are installed.
- **Custom Build Graph Path**:
- **Max Jobs**:
- **Path to ...**: The rest of the path options are optional and provided in case you want to use your own tools for GMRT compilation. GMRT packages should already include all of this and you will not need to change these options unless you specifically want to.
	- **CMake generator**: Specifies which CMake generator should be used when building a project. By default this is set to Ninja, but can be changed to "Visual Studio 17" to build a VS 2022 project.
	- **Path to CMake generator**: Path to a custom CMake generator if a non\-default CMake Generator is needed.
- **Compile with verbose output**: This enables detailed logging for the compiler output which can help debug issues when submitting reports. This may slow down compilation.
- **Build CMake Project**:
- **Build Type**: The build of GMRT to use.

The GMRT section will also contain subsections for each [platform](../Platform_Preferences.md) that needs to have different settings for GMRT compared to the GMS2 runtime settings (found under [Platform Preferences](../Platform_Preferences.md)). Currently it contains a section for WASM ([GX.games](../Platform_Preferences/GX_Games_Preferences.md)).
