# lin\_to\_db

This function converts a linear gain to a gain expressed in decibels (dB). You get a linear gain value from functions such as [audio\_sound\_get\_gain](audio_sound_get_gain.md).

Changes in gain can be expressed in dB. This corresponds better to how we perceive changes in amplitude (human perception of sound is not linear).

The conversion from a gain expressed in dB to a linear gain is done using the formula: gain\_db \= 20 \* log10(gain\_linear);

 

#### Syntax:

lin\_to\_db(x)

| Argument | Type | Description |
| --- | --- | --- |
| x | [Real](../../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The value to convert |

 

#### Returns:

[Real](../../../../../GameMaker_Language/GML_Overview/Data_Types.md)

 

#### Example:

var \_db \= lin\_to\_db(1\.5\);

The above code calculates the gain in dB corresponding to a linear gain of 1\.5\. The result of the conversion is stored in a temporary variable \_db.
