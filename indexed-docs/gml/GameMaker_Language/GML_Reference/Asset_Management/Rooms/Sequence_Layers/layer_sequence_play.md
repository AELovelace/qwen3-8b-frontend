# layer\_sequence\_play

With this function you can start the playback of the given sequence. You supply the sequence element ID as returned by [layer\_sequence\_create](layer_sequence_create.md) or by one of the [layer element functions](../General_Layer_Functions/General_Layer_Functions.md) and the function will play the sequence, which you can then pause if required using the function [layer\_sequence\_pause](layer_sequence_pause.md).

 
 

#### Syntax:

layer\_sequence\_play(sequence\_element\_id)

| Argument | Type | Description |
| --- | --- | --- |
| sequence\_element\_id | [Sequence Element ID](layer_sequence_create.md) | The unique ID value of the sequence element to target |

 

#### Returns:

N/A

 

#### Example:

if (keyboard\_check\_pressed(ord("P")))  

 {  

     global.Pause \= !global.Pause;  

     var a \= layer\_get\_all\_elements(layer);  

     for (var i \= 0; i \< array\_length(a); i\+\+)  

     {  

         if (layer\_get\_element\_type(a\[i]) \=\= layerelementtype\_sequence)  

         {  

             if (global.Pause)  

             {  

                 layer\_sequence\_pause(a\[i]);  

             }  

             else  

             {  

                 layer\_sequence\_play(a\[i]);  

             }  

         }  

     }  

 }

The above code checks to see if the game has been paused or not when a key is pressed. If the game is paused, then it loops through all sequence elements on the current layer (the layer of the calling instance) and pauses their playback, and if the game is not paused, then the loop will start their playback again.
