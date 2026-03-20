# title

This function is used to stop a GXC recording that was previously started with [gxc\_start\_movie\_recording()](gxc_start_movie_recording.md). It also submits the recording to the URL specified in the arguments, however the behaviour is different depending on the kind of string specified:

- If you specify a file name, the recording will be saved with that name in your Downloads folder
- If you specify a URL, the recording will be uploaded to that URL

The URL method should be used when the recording needs to be uploaded to GXC, and the file should be saved locally only for checking whether the recording was successful.

 

#### Syntax:

gxc\_stop\_movie\_recording(filename);

| Argument | Type | Description |
| --- | --- | --- |
| filename | [String](../../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The file name or URL where the recording is to be saved or uploaded |

 

#### Returns:

N/A

 

#### Example:

gxc\_submit\_challenge\_score(\_score, function(\_status, \_result) {  

 var \_uploadUrl \= \_result.data.gameplayVideoUploadUrl;  

 gxc\_stop\_movie\_recording(\_uploadUrl);  

 });

The above code uses the GXC API Library to upload a score to the currently active challenge, and when a response is received in its callback method, it retrieves the upload URL for the video and uploads the recording to it.
