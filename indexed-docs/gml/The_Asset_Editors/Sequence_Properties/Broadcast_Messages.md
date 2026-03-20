# Broadcast Messages \& Moments

## Broadcast Messages

Both [Sequences](../Sequences.md) and [Sprites](../../GameMaker_Language/GML_Reference/Asset_Management/Sprites/Sprites.md) can generate what are called **broadcast messages** at any point along their length. These messages are simple strings that are added to specific frames along the animation timeline, and when that point in the timeline is reached, then the string will be broadcast out to all instances that listen for it. Any instance that has a [Broadcast Message Event](../Object_Properties/Other_Events.md) (found in the "**Other**" event category) will receive the message string when it is reached in the timeline, at which point it's up to you to have some code that will parse it and react accordingly. Note too that sequences can also listen for broadcast messages, but this requires you to first set up the listener method using code (see the GML section on [Sequence Events And Moments](../../GameMaker_Language/GML_Reference/Asset_Management/Sequences/Sequence_Events_Moments_Broadcast.md) for more information).

  Setting the [image\_index](../../GameMaker_Language/GML_Reference/Asset_Management/Sprites/Sprite_Instance_Variables/image_index.md) of an instance directly to a frame will *not* trigger any Broadcast Messages that may be present on that frame of the object's sprite.

To add a Broadcast Message to the sequence or sprite timeline you simply click the  button. This will open a dialog where you can add the message to be broadcast:

Once added, the message will be shown in the Dope Sheet (or in the sprite frame view). To edit it, you must click the right mouse button  on the message icon to open a list of all the messages that overlap the frame (there can only be one message on a frame, but placing multiple messages on consecutive frames will cause them to overlap visually, making it harder to select the one you want and you can have a message and a [moment](../../GameMaker_Language/GML_Reference/Asset_Management/Sequences/Sequence_Events_Moments_Broadcast.md) on the same frame too), and then selecting one from this list will open the message dialog where you can edit it or remove it.

When a Broadcast Message event is triggered, there will be a special [DS Map](../../GameMaker_Language/GML_Reference/Data_Structures/DS_Maps/ds_map_create.md) created and stored in the built\-in variable [event\_data](../../GameMaker_Language/GML_Reference/Game_Input/Gesture_Input/event_data.md). This is a built\-in *global* scope variable, but will only contain DS map data in the event that triggered it \- in this case the Broadcast Message event \- and will hold an invalid DS map handle (\-1\) at all other times. The keys that the event will have are as follows:

| [Message Event Struct](Broadcast_Messages.md) | | |
| --- | --- | --- |
| Variable | Type | Description |
| event\_type | [String](../../GameMaker_Language/GML_Overview/Data_Types.md) | This will be the string "sequence event" for a message sent from a Sequence and "sprite event" for a message sent from a Sprite. |
| message | [String](../../GameMaker_Language/GML_Overview/Data_Types.md) | This contains the message string that has been received. |
| element\_id | [Layer Element ID](../../GameMaker_Language/GML_Reference/Asset_Management/Rooms/General_Layer_Functions/layer_get_all_elements.md) | This contains the ID of the layer element (sequence/sprite/instance) that fired the message. You can then use this ID value to find out what kind of element generated the message using the function [layer\_get\_element\_type](../../GameMaker_Language/GML_Reference/Asset_Management/Rooms/General_Layer_Functions/layer_get_element_type.md) and to use the other relevant functions to target it, or perform an action like play a sound, as required. |

Note that the broadcast message event of an instance will receive multiple strings for each of the times a broadcast message is sent. You do not need to act on all of them, and can have different instances listening for different broadcast strings. However, you may have an instance that is listening for messages that may be received at the same time. When this happens, the event will be triggered multiple times \- *once for each message string*.

Below is a brief example of how this event can be checked:

if (event\_data\[? "event\_type"] \=\= "sequence event") // or you can check "sprite event"  

 {  

     switch (event\_data\[? "message"])  

     {  

         case "hit":  

             audio\_play\_sound(snd\_hit, 0, false);  

         break;  

  

         case "destroy":  

             sequence\_destroy(event\_data\[? "element\_id"]);  

         break;  

     }  

 }
 

## Moments

A sequence **moment** is a position on the timeline where the sequence can call a **function**. This is a [scripted function](../../GameMaker_Language/GML_Overview/Script_Functions.md) that must have no parameters and when the moment (frame) on the timeline is reached, this function will be called. To set a moment, you simply move the playhead to the required position and then click the **Add Moment** button, and in the dialog that opens you give the name of the function to call.

When adding a moment function, you can click the  button to go to the script with the specified function, or you can click the  button to create a new script asset with an empty function ready for editing. You can also remove the moment and the function call it contains by clicking the  button.
