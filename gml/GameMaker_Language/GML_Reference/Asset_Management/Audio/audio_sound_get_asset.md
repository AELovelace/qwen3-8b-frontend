# audio\_sound\_get\_asset

This function returns the [Sound Asset](../../../../The_Asset_Editors/Sounds.md) that was used to play the given [Sound Instance ID](audio_play_sound.md). The sound must be active (i.e. [currently playing](audio_is_playing.md)) for this function to return the correct value, otherwise it will throw a fatal error.

 

#### Syntax:

audio\_sound\_get\_asset(index)

| Argument | Type | Description |
| --- | --- | --- |
| index | [Sound Instance ID](audio_play_sound.md) | A sound instance returned from a function like [audio\_play\_sound](audio_play_sound.md). |

 

#### Returns:

[Sound Asset](../../../../The_Asset_Editors/Sounds.md) or [undefined](../../../GML_Overview/Data_Types.md)

 

#### Example:

Create Event

sound \= audio\_play\_sound(Sound1, 1, 0\);

Key Press \- Space Event

var \_asset \= audio\_sound\_get\_asset(sound);  

  

 if (audio\_exists(\_asset))  

 {  

     audio\_play\_sound(\_asset, 1, 0\);  

 }
 

In the **Create** event, this plays a sound, storing its sound instance into a variable.

In the **Key Press \- Space** event, it gets the asset used for playing the previously stored sound instance. If it returned a valid sound asset, another sound is playing using that same sound asset.

This way, the asset that this function returns for a sound can be reused to play that same sound again.
