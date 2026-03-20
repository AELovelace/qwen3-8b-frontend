# Audio Properties Overview

This page gives a detailed overview of the audio properties that GameMaker supports and the different "levels" at which you can set/change them.

The table below lists all applicable levels for the basic audio properties, and lists the functions you can use to set and get each property at each level.

| Level | Gain | Pitch | Offset | Listener Mask |
| --- | --- | --- | --- | --- |
| Asset | [audio\_sound\_gain](audio_sound_gain.md) [audio\_sound\_get\_gain](audio_sound_get_gain.md) | [audio\_sound\_pitch](audio_sound_pitch.md) [audio\_sound\_get\_pitch](audio_sound_get_pitch.md) | [audio\_sound\_set\_track\_position](audio_sound_set_track_position.md) [audio\_sound\_get\_track\_position](audio_sound_get_track_position.md) | *N/A* |
| Group | [audio\_group\_set\_gain](Audio_Groups/audio_group_set_gain.md) [audio\_group\_get\_gain](Audio_Groups/audio_group_get_gain.md) | *N/A* | *N/A* | *N/A* |
| Emitter | [audio\_emitter\_gain](Audio_Emitters/audio_emitter_gain.md) [audio\_emitter\_get\_gain](Audio_Emitters/audio_emitter_get_gain.md) | [audio\_emitter\_pitch](Audio_Emitters/audio_emitter_pitch.md) [audio\_emitter\_get\_pitch](Audio_Emitters/audio_emitter_get_pitch.md) | *N/A* | [audio\_emitter\_set\_listener\_mask](Audio_Emitters/audio_emitter_set_listener_mask.md) [audio\_emitter\_get\_listener\_mask](Audio_Emitters/audio_emitter_get_listener_mask.md) |
| Instance/Voice | [audio\_sound\_gain](audio_sound_gain.md) [audio\_sound\_get\_gain](audio_sound_get_gain.md) [audio\_play\_sound](audio_play_sound.md), etc. | [audio\_sound\_pitch](audio_sound_pitch.md) [audio\_sound\_get\_pitch](audio_sound_get_pitch.md) [audio\_play\_sound](audio_play_sound.md), etc. | [audio\_sound\_set\_track\_position](audio_sound_set_track_position.md) [audio\_sound\_get\_track\_position](audio_sound_get_track_position.md) [audio\_play\_sound](audio_play_sound.md), etc. | [audio\_play\_sound](audio_play_sound.md), etc. |
| Global/Listener | [audio\_master\_gain](audio_master_gain.md) [audio\_set\_master\_gain](audio_set_master_gain.md) [audio\_get\_master\_gain](audio_get_master_gain.md) | *N/A* | *N/A* | [audio\_set\_listener\_mask](Audio_Listeners/audio_set_listener_mask.md) [audio\_get\_listener\_mask](Audio_Listeners/audio_get_listener_mask.md) |
| Result | Gasset \* Ggroup \* Gemitter \* Ginstance | Passet \* Pemitter \* Pinstance (might be clipped, see [Pitch](Audio_Properties.md#pitch)) | Asset\-level offset unless instance\-level offset is passed to the audio\_play\_sound\_\* functions | Memitter \& Minstance (bitwise AND, see [Bitwise Operators](../../../../Additional_Information/Bitwise_Operators.md)) |

 
## Notes

### Gain

 
This can still be changed in\-game later by calling [audio\_sound\_gain](audio_sound_gain.md) with the sound *asset* ID as the argument: 

audio\_sound\_gain(snd\_Explode, 0, 0\);  // Set the asset\-level gain to 0 (new and existing instances of this sound are muted)

### Pitch

The resulting *source* pitch has a lower limit of 1/256 (\-8 octaves) for all sounds. It has an upper limit dependent on the compression type of the sound \- uncompressed sounds have an upper limit of 256 (\+8 octaves), but compressed sounds have a limit of 4 (\+2 octaves).

If the source pitch is clipped, a warning message will be printed to the console. If the source pitch is clipped on the upper bound for a compressed sound, a note will also be printed to the console pointing out that they have a lower upper limit than uncompressed sounds.

  On HTML5, uncompressed sounds and compressed sounds have the same range of 1/256 to 256. Because of this, there is no specific warning for clipping a compressed sound on the upper bound.
