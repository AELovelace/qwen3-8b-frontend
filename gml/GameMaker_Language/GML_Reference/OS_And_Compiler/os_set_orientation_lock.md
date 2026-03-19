# os\_set\_orientation\_lock

This function changes the orientations that are allowed for the game. You can enable or disable landscape and portrait orientations separately.

Calling this function will disable the flipped versions of both orientations, which are found in the [Android](../../../Settings/Game_Options/Android.md) / [iOS](../../../Settings/Game_Options/iOS.md) Game Options.

 

#### Syntax:

os\_set\_orientation\_lock(landscape\_enable, portrait\_enable)

| Argument | Type | Description |
| --- | --- | --- |
| landscape\_enable | [Boolean](../../../../GameMaker_Language/GML_Overview/Data_Types.md) | Set to true or false to enable or disable landscape orientations. |
| portrait\_enable | [Boolean](../../../../GameMaker_Language/GML_Overview/Data_Types.md) | Set to true or false to enable or disable portrait orientations. |

 

#### Returns:

N/A

 

#### Example:

os\_set\_orientation\_lock(true, true);

This enables both landscape and portrait orientations.
