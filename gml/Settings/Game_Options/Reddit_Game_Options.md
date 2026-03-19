# Reddit Game Options

The Reddit Game Options allow you to modify the properties for your Reddit game. The following sections are provided:

## Game

This section has the following properties:

- **Game Name**: This is your game's name (title) on Reddit.
- **Devvit Project Id**: The project ID as registered on Devvit.
- **Devvit Project Path:** Path to the local Devvit project.

## Graphics

Here you can change the following details related to how your game will be displayed:

- **Display cursor**: Controls whether the mouse cursor is visible when your game starts. Useful for games that don't require mouse input or use a [custom mouse sprite](../../GameMaker_Language/GML_Reference/General_Game_Control/cursor_sprite.md).
- **Interpolate colours between pixels**:
- **Transparent Background**: Allows the game canvas to be transparent in areas where nothing is drawn.
- **Scaling**: Your game can be configured to scale the draw canvas automatically to **maintain the aspect ratio** within the browser, or you can select to have it run **full scale**. The full scale option will not full screen the game in the browser, but rather stretch what is drawn to fit the canvas size, as defined by the first room of the game. This is set to keep aspect ratio by default.

Finally there is the option to set the size of the [texture page](macOS.md#). The default (and most compatible) size is 2048x2048, but you can choose from anywhere between 256x256 up to 8192x8192\. There is also a button marked ****Preview****which will generate the texture pages for this platform and then open a window so that you can see how they look. This can be very useful if you wish to see how the texture pages are structured and to prevent having texture pages larger (or smaller) than necessary. For more information on texture pages, please see [here](../Texture_Information/Texture_Pages.md).
