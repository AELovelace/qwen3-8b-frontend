# Image Loaded

This event is triggered when you load an image into GameMaker *asynchronously*. This can occur in a few situations:

- When you add a sprite with [sprite\_add](../../../GameMaker_Language/GML_Reference/Asset_Management/Sprites/Sprite_Manipulation/sprite_add.md) on HTML5\.
- When you pass a [URL](#) to [sprite\_add](../../../GameMaker_Language/GML_Reference/Asset_Management/Sprites/Sprite_Manipulation/sprite_add.md).
- When you add a sprite with [sprite\_add\_ext](../../../GameMaker_Language/GML_Reference/Asset_Management/Sprites/Sprite_Manipulation/sprite_add_ext.md).

For example, say you want to load a sprite image, and only change the current sprite for the instance to the new one after it has loaded. You would have something like this in the Create event (or any other event):

Create Event

var \_url \= "http://www.angusgames.com/game/background1\.png";  

 spr \= sprite\_add(\_url, 0, false, false, 0, 0\);

This will now start to load the image into the device or the browser, but it will not block GameMaker while it waits for the file to be loaded. Instead, GameMaker will keep running as normal until the image is loaded and the [callback](#) triggers the **Image Loaded Event**, where a [DS Map](../../../GameMaker_Language/GML_Reference/Data_Structures/DS_Maps/ds_map_create.md) is created and stored in the special variable [async\_load](../../../GameMaker_Language/GML_Overview/Variables/Builtin_Global_Variables/async_load.md). The map contains the following information:

- "filename": The complete path to the file you requested.
- "id": The ID of the resource that you have loaded. This will be the same as the variable that you have assigned the resource to.
- "status": Returns a value of less than 0 for an error.

You would then assign the newly loaded image to a sprite in this event. The following code example demonstrates how the returned information would be used:

Async \- Image Loaded Event

if (async\_load\[? "id"] \=\= spr)  

 {  

     if (async\_load\[? "status"] \>\= 0\)  

     {  

         sprite\_index \= spr;  

     }  

 }

The above code will first check the "id" of the DS map that has been created, then check the "status" of the callback. If the value is greater than or equal to 0 (signalling success), the result from the callback will be used to set the sprite index to the newly loaded image.

  While the sprite is loading, GameMaker uses a temporary 1x1 placeholder sprite. When the async Image Loaded event is executed, the sprite has been downloaded and the placeholder is removed. [Information](../../../GameMaker_Language/GML_Reference/Asset_Management/Sprites/Sprite_Information/Sprite_Information.md "Sprite Information") that you request from this sprite will only be correct in this event and afterwards (for example, [sprite\_get\_width](../../../GameMaker_Language/GML_Reference/Asset_Management/Sprites/Sprite_Information/sprite_get_width.md) and [sprite\_get\_height](../../../GameMaker_Language/GML_Reference/Asset_Management/Sprites/Sprite_Information/sprite_get_height.md) will return a value of 1 before that).
