# gx\_share

This [asynchronous](../../Asynchronous_Functions/Asynchronous_Functions.md) function is used on GX.games to share an image (as a buffer) or a URL (as a string) through the browser's [share function](https://developer.mozilla.org/en-US/docs/Web/API/Navigator/share).

The function returns 0 on success or \-1 on error. When the request is complete, the [Async \- Social event](../../../../The_Asset_Editors/Object_Properties/Async_Events/Social.md) will be triggered with the following keys in its [async\_load](../../../GML_Overview/Variables/Builtin_Global_Variables/async_load.md) DS Map:

- "type": "share\_complete" ([String](../../../GML_Overview/Data_Types.md))
- "success": true or false
- "error": Only if "success" is false, contains the error message returned by the browser

See the example at the bottom of the page for sharing images.

 

#### Syntax:

gx\_share(content, \[title], \[text], \[filename]);

| Argument | Type | Description |
| --- | --- | --- |
| content | [Buffer](../../Buffers/buffer_create.md) or [String](../../../GML_Overview/Data_Types.md) | A buffer containing the image data (see example below) or a string containing the URL to share |
| title | [String](../../../GML_Overview/Data_Types.md) | The title for the share dialog |
| text | [String](../../../GML_Overview/Data_Types.md) | The text for the share diolog |
| filename | [String](../../../GML_Overview/Data_Types.md) | The filename in case of an image (should contain the extension) |

 

#### Returns:

N/A

 

#### Example:

var \_buff\_screenshot \= buffer\_create(1024, buffer\_grow, 1\);  

  

 surface\_save(application\_surface, \_buff\_screenshot);  

  

 var \_filename \= $"screenshot\_{string\_digits(date\_current\_datetime())}.png";  

 gx\_share(\_buff\_screenshot, "Share screenshot", "Screenshot taken of Game", \_filename);  

  

 buffer\_delete(\_buff\_screenshot);
 

The above code creates a [grow buffer](../../Buffers/buffer_create.md) and saves the [application\_surface](../../Drawing/Surfaces/application_surface.md) into the buffer. As the application surface contains the final render of the game (excluding GUI), this essentially captures a screenshot of the game in the buffer.

After setting up a local variable with the file name (containing digits from the current [Datetime](../../Maths_And_Numbers/Date_And_Time/date_current_datetime.md)), it calls the gx\_share function to share that buffer as an image with the optional share dialog title, text and filename passed.

At the end it deletes the buffer as it's no longer needed in memory.
