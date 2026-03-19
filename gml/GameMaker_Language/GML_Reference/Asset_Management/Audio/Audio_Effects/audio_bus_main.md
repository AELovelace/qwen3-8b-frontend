# audio\_bus\_main

This built\-in struct represents the main audio bus used by GameMaker.

The main bus represents the main mix in GameMaker's audio, which is the combination of all currently active sound sources after they have been processed (to apply effects, positioning, doppler effect etc.) and all emitters. All of GM's audio ends up on this bus.

Any audio effect that you apply to the main bus will be heard on all sounds, as all buses are routed to this one.

 

#### Syntax:

audio\_bus\_main

 

#### Returns:

[AudioBus Struct](AudioBus.md)

 

#### Example:

var \_ef\_reverb \= audio\_effect\_create(AudioEffectType.Reverb1\);  

 audio\_bus\_main.effects\[0] \= \_ef\_reverb;

The above code first creates a new audio effect and stores it in a temporary variable \_ef\_reverb. It then assigns this new effect as the first effect on the main audio bus's effects array.
