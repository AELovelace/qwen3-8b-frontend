# Live Wallpapers

This page lists functions for use with the Live Wallpaper functionality.

For information on how to set these up, see the [helpdesk article on GX Live Wallpapers](https://gamemaker.io/en/help/articles/how-to-make-live-wallpapers-with-gamemaker).

## Functions

The following functions are given for Live Wallpapers:

- [wallpaper\_set\_config](wallpaper_set_config.md)
- [wallpaper\_set\_subscriptions](wallpaper_set_subscriptions.md)

Also see: [Wallpaper Events](../../../The_Asset_Editors/Object_Properties/Wallpaper_Config_Event.md)

## Restrictions

The following restrictions apply to a Live Wallpaper, after being installed through the store:

- **Mouse Input**: Disabled by default, enabled with [wallpaper\_set\_subscriptions](wallpaper_set_subscriptions.md)
- **File Access**: The standard [file sandbox](../../../Additional_Information/The_File_System.md) applies; [disabling sandbox](../../../Settings/Game_Options/Windows.md) does nothing
- **Networking**: Completely disabled (including TCP, UDP, HTTP, etc.)
- **Microphone**: Disabled
- **Extensions**: Calls to DLL functions included in [extensions](../../../The_Asset_Editors/Extensions.md) are disabled (including [external\_call](../OS_And_Compiler/external_call.md), [external\_define](../OS_And_Compiler/external_define.md), etc.)
- **Functions**: None of the url\_open\*() functions will work. game\_change() is also disabled.
