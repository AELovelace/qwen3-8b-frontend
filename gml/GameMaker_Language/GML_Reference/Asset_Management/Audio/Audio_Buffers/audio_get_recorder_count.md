# audio\_get\_recorder\_count

This function will return the number of audio recording sources (like microphones, etc...) currently available to your game. So, if you have a return value of, for example, four, then you will have audio input on the sources 0, 1, 2 and 3, with one of these values being that which you use to start recording from using the function [audio\_start\_recording()](audio_start_recording.md). This value can change at any time as people plug/unplug microphones or other input sources to the device. Note that you can use the function [audio\_get\_recorder\_info()](audio_get_recorder_info.md) to get information on each device connected.

IMPORTANT This function will always return 1 on the GX.games and iOS/tvOS targets.

 

#### Syntax:

audio\_get\_recorder\_count()

 

#### Returns:

[Real](../../../../GML_Overview/Data_Types.md)

 

#### Example:

if (audio\_get\_recorder\_count() \> 0 )  

 {  

 channel\_index \= audio\_start\_recording(0\);  

 }

The above code checks the audio recorders available and if there are 1 or more, it starts recording from the first one indexed (source 0\).
