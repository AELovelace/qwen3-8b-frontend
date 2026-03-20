# Sequences

Sequences are usually created in the IDE using [The Sequence Editor](../../../../The_Asset_Editors/Sequences.md), but they can also be created and edited using code.

## Sequences Basics

Before looking at the functions available, it's important to understand the way that sequences are defined in GameMaker and the different terms that will be used.

To start with, at the top level, you have a **sequence element**. This is what you place on a layer in a room, either through [The Room Editor](../../../../The_Asset_Editors/Rooms.md) or in code using the appropriate [layer functions](../Rooms/Sequence_Layers/Sequence_Layers.md). The layer element has no real properties other than an element ID value, but this ID is required to use the above mentioned layer functions to change the sequence playback or to access the sequence data.

Next, you have **sequence objects** and **sequence instances** much like you have general objects and instances. A sequence *object* is the base asset as you created it in [The Asset Browser](../../../../Introduction/The_Asset_Browser.md) or using the function [sequence\_create](sequence_create.md), and the sequence *instance* is the "copy" of that sequence object that has been placed in a room as an element on a layer. Think of sequence objects as blueprints and sequence instances as the creation from those blueprints. Sequence objects and instances are [structs](../../../GML_Overview/Structs.md) and \- unlike regular objects \- a sequence object struct can be edited at run time, which will affect all further instances of that sequence when you create them as elements (and any editing done to a sequence object will **not** be reset by restarting the game or the room using the [room\_restart](../Rooms/room_restart.md) or [game\_restart](../../General_Game_Control/game_restart.md) functions). The sequence instance struct contains a few parameters to control playback and things (this is explained in more detail below) as well as the **sequence data** struct.

Finally, as mentioned above, you have the **sequence data**, which is another struct. This struct contains *all* the data about the sequence. The tracks it contains, the properties those tracks have, the playback speed and much more. The exact details of this structs contents are outlined below, but basically consists of **asset track** structs and **parameter track** structs which use **keyframe data** to actually perform actions while the sequence plays.

Sequence elements are dealt with using the room [layer functions](../Rooms/Sequence_Layers/Sequence_Layers.md), but for sequence objects, instances and data we have the functions that you can find in the [function reference](Sequences.md#func_ref).

There is also a **built\-in variable** associated with instances that can be used to determine if the instance has been used in a sequence or not:

- [in\_sequence](in_sequence.md)

 
If an instance is controlled by a sequence, that sequence will be stored in the instance's **built\-in variable**:

- [sequence\_instance](sequence_instance.md)

Another **built\-in variable** associated with instances can be used to determine if the instance draws itself or if it is drawn by a sequence instead:

- [drawn\_by\_sequence](drawn_by_sequence.md)

## Creating a Sequence in Code

Before using these functions to create or edit sequences, we recommend that you read the detailed descriptions given below for the struct properties. A general overview of how to create a new sequence would be:

- Create the new sequence object using the function [sequence\_create](sequence_create.md) and store the sequence object index in a variable. This index gives you access to the sequence object struct.

myseq \= sequence\_create();

- Set the sequence object top\-level values like length, play mode, play speed, etc. For example:

myseq.length \= 120;  

 myseq.loopmode \= seqplay\_pingpong;

- Before you can add tracks to the sequence object, you need to create them, so you'd now create *asset* tracks with the function [sequence\_track\_new](sequence_track_new.md) and add them to the sequence object's tracks. Note that in code, there is really no difference between asset tracks and parameter tracks \- they are all simply tracks and how they behave will depend on the type of track you create and whether they are assigned as sub\-tracks to a top\-level track or not. So, you would create a track for an asset, and then assign sub\-tracks for the different parameters to it and these sub\-tracks would act as the *parameter* tracks for the asset. The example below creates a single graphic asset track, gives it a name and assigns it as the sequence's first track:

var \_graphic\_track \= sequence\_track\_new(seqtracktype\_graphic);  

 \_graphic\_track.name \= "TestGraphicTrack";  

  

 myseq.tracks\[0] \= \_graphic\_track;
 

- Each asset track needs to have some data to tell the sequence how it will look, what its position is, etc. This is added in the form of *keyframes*. At the top level for an asset track, you can set keyframes for various things (listed in the section on the Track Struct, below), but note that as these are asset track keyframes, they won't be interpolated and will simply change the value they refer to when the given frame is reached. Each keyframe is a struct that is assigned to the next element of the asset track struct's keyframes member. To create the keyframe struct we would call the function [sequence\_keyframe\_new](sequence_keyframe_new.md) and to populate the keyframe with the required data, we would use the function [sequence\_keyframedata\_new](sequence_keyframedata_new.md):

// Create a new keyframe struct for a graphics asset track  

 var \_graphic\_keys \= sequence\_keyframe\_new(seqtracktype\_graphic);  

  

 // Set the graphics keyframe top\-level data for the keyframe position, length, etc.  

 \_graphic\_keys.frame \= 0;  

 \_graphic\_keys.length \= 1;  

 \_graphic\_keys.stretch \= true;  

 \_graphic\_keys.disabled \= false;  

  

 // Create the channel data that will go into this keyframe (note that each key can have multiple channels of keyframe data)  

 \_graphic\_keys.channels\[0] \= sequence\_keyframedata\_new(seqtracktype\_graphic);  

 \_graphic\_keys.channels\[0].spriteIndex \= spr\_platform;  

 \_graphic\_keys.channels\[0].channel \= 0;  

  

 // Assign the keyframe struct as the first keyframe of the graphic track  

 \_graphic\_track.keyframes\[0] \= \_graphic\_keys;
 

- We now need to create a parameter track which we'll assign as a sub\-track to the graphics track we just created. This will be done in a similar way as shown above, only now we need to give the track a name that shows its purpose, in this case "position" as we'll be using this track to move the graphics track over the course of the sequence animation frames:

// Create a new parameter track struct for the position of the graphic and assign it as a track  

 var \_param\_track \= sequence\_track\_new(seqtracktype\_real);  

 \_param\_track.name \= "position";  

 \_param\_track.interpolation \= seqinterpolation\_lerp;  

  

 \_graphic\_track.tracks\[0] \= \_param\_track;  

  

 // Create the keyframe and keyframe data structs to hold the parameter channel data and assign them  

 var \_keyframe;  

  

 // Keyframe 1  

 \_keyframe \= sequence\_keyframe\_new(seqtracktype\_real);  

 \_keyframe.frame \= 0;  

  

 \_keyframe.channels\[0] \= sequence\_keyframedata\_new(seqtracktype\_real);  

 \_keyframe.channels\[0].channel \= 0;  // Channel 0 for a position track is the X position  

 \_keyframe.channels\[0].value \= 0;  

 \_keyframe.channels\[1] \= sequence\_keyframedata\_new(seqtracktype\_real);  

 \_keyframe.channels\[1].channel \= 1;  // Channel 1 for a position track is the Y position  

 \_keyframe.channels\[1].value \= 0;  

  

 \_param\_track.keyframes\[0] \= \_keyframe;  

  

 // Keyframe 2  

 \_keyframe \= sequence\_keyframe\_new(seqtracktype\_real);  

 \_keyframe.frame \= 120;  

  

 \_keyframe.channels\[0] \= sequence\_keyframedata\_new(seqtracktype\_real);  

 \_keyframe.channels\[0].channel \= 0;  

 \_keyframe.channels\[0].value \= room\_width;  

 \_keyframe.channels\[1] \= sequence\_keyframedata\_new(seqtracktype\_real);  

 \_keyframe.channels\[1].channel \= 1;  

 \_keyframe.channels\[1].value \= room\_height;  

  

 \_param\_track.keyframes\[1] \= \_keyframe;
 

- With that done, we can now create an instance of our newly created sequence in the room:

layer\_sequence\_create("Assets\_1", 0, 0, myseq);

The above instructions create a very simple sequence object that draws a sprite at the (0, 0\) position *of the sequence* and then moves it to the bottom\-right corner and back in a loop.

 
## Sequence Structs

There are a number of places where you need to access different structs to give or get data about the sequence, and the sections below list all the different properties that these structs contain:

- [The Sequence Object Struct](Sequence_Structs/The_Sequence_Object_Struct.md)
- [The Sequence Instance Struct](Sequence_Structs/The_Sequence_Instance_Struct.md)
- [The Track Struct](Sequence_Structs/The_Track_Struct.md)
- [The Keyframe Struct](Sequence_Structs/The_Keyframe_Struct.md)
- [The Keyframe Data Struct](Sequence_Structs/The_Keyframe_Data_Struct.md)

## Events, Moments and Broadcast Messages

Finally, it is possible to add code to sequences that can be triggered as either an **event**, as a **moment** or as a **broadcast message**. This is explained fully on the following page:

- [Events, Moments and Broadcast Messages](Sequence_Events_Moments_Broadcast.md)

## Function Reference

### Functions

- [sequence\_exists](sequence_exists.md)
- [sequence\_create](sequence_create.md)
- [sequence\_destroy](sequence_destroy.md)
- [sequence\_get](sequence_get.md)
- [sequence\_track\_new](sequence_track_new.md)
- [sequence\_keyframe\_new](sequence_keyframe_new.md)
- [sequence\_keyframedata\_new](sequence_keyframedata_new.md)
- [sequence\_get\_objects](sequence_get_objects.md)
- [sequence\_instance\_override\_object](sequence_instance_override_object.md)

### Variables

- [in\_sequence](in_sequence.md)
- [drawn\_by\_sequence](drawn_by_sequence.md)
- [sequence\_instance](sequence_instance.md)
