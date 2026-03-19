# audio\_channel\_num

With this function you can set how many audio channels are available for playing audio in GameMaker.

This basically means the number of sounds (or *sound instances* or *voices*) that can be played *simultaneously*. Or, put differently, the number of calls to any of the audio\_play\_sound\* (and [audio\_play\_in\_sync\_group](Audio_Synchronisation/audio_play_in_sync_group.md)) functions that you can make before sounds may be lost. If the number exceeds this value, those sounds with a lower *priority* are stopped to free up a channel for the sounds with a higher *priority*.

You can pass 0 to disable audio playback.

  You can use this function to optimise your game for devices as the lower the number of channels for audio the better the performance, but bear in mind that this may also cause noticeable cutoff of certain sounds if many are played at once.

  This function is a configuration function of the audio engine and stops all playing sounds when called (i.e. [audio\_stop\_all](audio_stop_all.md)). Ideally it should not be called when sounds are already playing, unless you are e.g. using this as an adjustable setting in your game.

 

#### Syntax:

audio\_channel\_num(num)

| Argument | Type | Description |
| --- | --- | --- |
| num | [Real](../../../GML_Overview/Data_Types.md) | Number of available audio channels (default is 128) |

 

#### Returns:

N/A

 

#### Example:

switch (os\_browser)  

 {  

     case browser\_not\_a\_browser:  

         switch (os\_type)  

         {  

             case os\_windows:  

             case os\_macosx:  

                 audio\_channel\_num(200\);  

             break;  

  

             default:  

                 audio\_channel\_num(64\);  

             break;  

         }  

     break;  

  

     default:  

         audio\_channel\_num(16\);  

     break;  

 }
 

The above code checks the platform that the game is running on and changes the number of available sound channels to increase performance.
