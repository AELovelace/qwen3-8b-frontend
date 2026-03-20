# audio\_system\_is\_available

This function can be used to check and see if the audio system has been initialised and the audio context is initialised and running.

On all platforms, this function will return true immediately after Game Start when the audio engine is [initialised](audio_system_is_initialised.md), *except on the **HTML5** target*. On HTML5, the audio context status can change at any time depending on user input, the browser being used, and its version, so this function can be used to check and see if audio can be played or not. If the function returns false (i.e. the audio context status is not running), then only unstreamed sounds *may* play (but it's not guaranteed, and you should assume that no audio can be played), while if it returns true then all audio will play.

  To check if the audio system is *initialised* on HTML5, you should use [audio\_system\_is\_initialised](audio_system_is_initialised.md) instead. The audio system has to be initialised first before it can be available.

#### Syntax:

audio\_system\_is\_available()

 

#### Returns:

[Boolean](../../../../../GameMaker_Language/GML_Overview/Data_Types.md)

 

#### Example:

if audio\_system\_is\_available()  

 {  

     if audio\_is\_paused(global.Music)  

     {  

         audio\_resume\_sound(global.Music)  

     }  

     else  

     {  

         if !audio\_is\_playing(global.Music)  

         {  

             global.Music \= audio\_play\_sound(snd\_Music, 0, true);  

         }  

     }  

 }  

 else  

 {  

     if audio\_is\_playing(global.Music)  

     {  

         audio\_pause\_sound(global.Music);  

     }  

 }

The above code will pause/unpause an audio track depending on whether the audio system is initialised and available or not.
