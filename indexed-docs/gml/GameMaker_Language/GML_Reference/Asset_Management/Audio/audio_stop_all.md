# audio\_stop\_all

This function stops *all* sounds that are currently playing. This includes all sounds that have been paused using [audio\_pause\_sound](audio_pause_sound.md) or [audio\_pause\_all](audio_pause_all.md).

This will also remove any queued buffers on [audio buffer queues](Audio_Buffers/Audio_Buffers.md) and run the [Audio Playback](../../../../The_Asset_Editors/Object_Properties/Async_Events/Audio_Playback.md) event for each buffer removed, with the key "queue\_shutdown" set to 1\.

 
 

#### Syntax:

audio\_stop\_all()

 

#### Returns:

N/A

 

#### Example:

if (!global.SFX)   

 {  

     audio\_stop\_all();  

 }

The above code checks the global variable SFX and if it returns false, it will stop all sounds that are currently playing.
