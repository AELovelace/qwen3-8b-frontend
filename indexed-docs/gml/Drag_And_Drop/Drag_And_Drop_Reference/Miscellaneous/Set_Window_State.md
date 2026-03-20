# title

With this action you can set the state of the game window to either fullscreen or windowed. There are three options here:

- **Toggle** \- When this option is selected, each time you call the action it will toggle the window between fullscreen and windowed states
- **Fullscreen** \- This will make the window go fullscreen from a windowed state
- **Windowed** \- This will make the window return to a windowed state if in fullscreen

Note that how the game looks while in a fullscreen state will depend on the [Game Options \- Graphics](../../../Settings/Game_Options/Windows.md) settings for you target platforms, since if the game does not have some mechanism for adjusting
 to different aspect ratios and resolutions you can get stretching (if the game option is set to **Full Scale**), or you can get black bars added (if the game option is set to **Keep Aspect Ratio**). In general if you have nothing in place to
 deal with different resolutions, you should be using **Keep Aspect Ratio** for the target platforms you want to compile to.

 

#### Action Syntax:

#### Arguments:

| Argument | Description |
| --- | --- |
| State | The window state to set (see above for options) |

 

#### Example:

The above action block code will toggle the window state between fullscreen and windowed
 every time the F4 key is pressed.
