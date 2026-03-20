# audio\_bus\_create

This function creates a new audio bus and returns an [AudioBus Struct](AudioBus.md) through which you can access and modify it.

  A user\-created audio bus will be garbage collected when it's unreferenced and any linked emitters are destroyed, and as such there is no "destroy" or "free" function for audio buses.

 

#### Syntax:

audio\_bus\_create()

 

#### Returns:

[AudioBus Struct](AudioBus.md)

 

#### Example:

emitter1 \= audio\_emitter\_create();  

 emitter1\_bus \= audio\_bus\_create();  

 audio\_emitter\_bus(emitter1, emitter1\_bus);  

 audio\_play\_sound\_on(emitter1, snd\_Ambience, true, 100\);

The above code first creates a new audio emitter and a new audio bus. It then assigns the emitter to the bus, and plays a sound on the emitter.

The sound will have any effects from emitter1\_bus applied first and then the ones from[audio\_bus\_main](audio_bus_main.md).
