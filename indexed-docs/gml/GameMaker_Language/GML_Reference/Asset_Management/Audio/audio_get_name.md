# audio\_get\_name

This function will return the name of a given audio asset as a string.

The "index" value can be that of the asset itself (as seen in [The Asset Browser](../../../../Introduction/The_Asset_Browser.md)) or the [Sound Instance ID](audio_play_sound.md) that is given when you play the sound using, for example, [audio\_play\_sound](audio_play_sound.md).

To get the actual asset reference originally used to play a sound instance, use [audio\_sound\_get\_asset](audio_sound_get_asset.md).

  The string returned is *not* the same as the resource ID and cannot be used to access the resource itself, so should only be used for displaying or error checking.

 

#### Syntax:

audio\_get\_name(index)

| Argument | Type | Description |
| --- | --- | --- |
| index | [Sound Asset](../../../../The_Asset_Editors/Sounds.md) | The index of the sound to check. |

 

#### Returns:

[String](../../../GML_Overview/Data_Types.md)

 

#### Example:

var snd \= audio\_play\_sound(choose(snd\_One, snd\_Two, snd\_Three), 0, false);  

 var name \= audio\_get\_name(snd);  

 show\_debug\_message("Sound \= " \+ name);

The above code plays a random sound chosen from three different sound resources then shows a debug message with its name.
