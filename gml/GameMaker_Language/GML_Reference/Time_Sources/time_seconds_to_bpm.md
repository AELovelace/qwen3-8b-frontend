# time\_seconds\_to\_bpm

This function takes the length of a beat in seconds, and returns a beats\-per\-minute value.

 

#### Syntax:

time\_seconds\_to\_bpm(seconds)

| Argument | Type | Description |
| --- | --- | --- |
| seconds | [Real](../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The seconds\-per\-beat value to convert into beats\-per\-minute |

 

#### Returns:

[Real](../../../../GameMaker_Language/GML_Overview/Data_Types.md)

 

#### Example:

var \_period \= time\_source\_get\_period(time\_source);  

 var \_bpm \= time\_seconds\_to\_bpm(\_period);  

  

 show\_debug\_message(\_bpm);
 

This function gets the period of a Time Source, converts it to BPM and prints that value to the output log.

This code follows the example for [time\_bpm\_to\_seconds()](time_bpm_to_seconds.md).
