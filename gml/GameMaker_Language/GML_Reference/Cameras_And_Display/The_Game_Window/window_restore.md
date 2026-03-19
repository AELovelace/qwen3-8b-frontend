# window\_restore

This function restores the game window which may have been minimised by the user or using the function [window\_minimise](window_minimise.md).

  This is only supported on Windows and Linux. On macOS the game will not restore as execution is paused in minimised state.

 

#### Syntax:

window\_restore()

 

#### Returns:

N/A

 

#### Example:

Key Press \- Space event:

window\_minimise();  

  

 alarm\_set(0, 300\);
 

Alarm 0 event:

window\_restore();

On pressing space, this will minimise the game window and set Alarm 0 to 300 steps. When the alarm is called, the game window will be automatically restored.
