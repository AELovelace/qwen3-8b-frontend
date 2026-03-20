# window\_get\_borderless\_fullscreen

This function returns whether a [borderless window](window_enable_borderless_fullscreen.md) for fullscreen mode is enabled or not.

  This function only works on Windows and macOS.

 

#### Syntax:

window\_get\_borderless\_fullscreen()

 

#### Returns:

[Boolean](../../../GML_Overview/Data_Types.md)

 

#### Example:

var \_borderless \= window\_get\_borderless\_fullscreen();  

 show\_debug\_message($"Borderless Fullscreen Enabled: {\_borderless}");

The code above calls window\_get\_borderless\_fullscreen to find out if borderless fullscreen is currently enabled. It then shows a debug message.
