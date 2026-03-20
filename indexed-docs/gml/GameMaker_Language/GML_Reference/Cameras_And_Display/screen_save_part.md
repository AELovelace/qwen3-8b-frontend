# screen\_save\_part

With this function you can save a screenshot of a part of the game as it currently appears in the game display.

The selection coordinates are based on the *absolute* size of the display (or window if not fullscreen), so (0, 0\) is always the top left hand corner of the screen (or window). Below is an image that shows how this function works:

The file will be saved to the [working directory](../File_Handling/File_Directories/working_directory.md) of the game. It is important to note that the function is designed to be called in the **Draw GUI End Event**, which should give consistent results across all platforms. Using it in any other event may not work as expected, and may give different results across different targets and even devices.

  This function does not work on the HTML5 target.

 

#### Syntax:

screen\_save\_part(fname, x, y, w, h)

| Argument | Type | Description |
| --- | --- | --- |
| fname | [String](../../GML_Overview/Data_Types.md) | The filename for the screenshot to save |
| x | [Real](../../GML_Overview/Data_Types.md) | The x coordinate of the top left corner of the area of the screen to capture |
| y | [Real](../../GML_Overview/Data_Types.md) | The y coordinate of the top left corner of the area of the screen to capture |
| w | [Real](../../GML_Overview/Data_Types.md) | The width of the area of the screen to capture |
| h | [Real](../../GML_Overview/Data_Types.md) | The height of the area of the screen to capture |

 

#### Returns:

N/A

 

#### Example:

if (keyboard\_check\_pressed(ord("S")))  

 {  

     screen\_save\_part("Screens\\Screen\_" \+ string(num\+\+) \+ ".png", 0, 0, 100, 100\);  

 }

The above code takes a screenshot of a part of the game screen that is 100 pixels square when the user presses the "S" key. This screenshot is saved to a specific folder and numbered using a variable which is then incremented.
