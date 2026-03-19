# time\_bpm\_to\_seconds

This function takes a beats\-per\-minute value, and returns the length of each beat in seconds.

This can be used when [creating a Time Source](time_source_create.md) to use a BPM value for the Time Source. It's important that such a Time Source uses **seconds** as its [unit](Time_Source_Units.md).

 

#### Syntax:

time\_bpm\_to\_seconds(bpm)

| Argument | Type | Description |
| --- | --- | --- |
| bpm | [Real](../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The beats\-per\-minute value to convert into seconds\-per\-beat |

 

#### Returns:

[Real](../../../../GameMaker_Language/GML_Overview/Data_Types.md)

 

#### Example:

var \_bpm \= 90;  

 var \_seconds \= time\_bpm\_to\_seconds(\_bpm);  

  

 time\_source \= time\_source\_create(time\_source\_game, \_seconds, time\_source\_units\_seconds, function()  

 {  

     show\_debug\_message("BEAT!");  

 }, \[], \-1\);
 

This code converts a value of 90 BPM into seconds, and uses that to create a Time Source that runs indefinitely.

On each beat, it prints the message "BEAT!" to the output log.
