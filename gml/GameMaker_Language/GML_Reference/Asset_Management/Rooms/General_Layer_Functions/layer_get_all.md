# layer\_get\_all

This function will return an [array](../../../../GML_Overview/Arrays.md) populated with the handles of each layer in the current room. This will also include [UI Layers](../../../../../The_Asset_Editors/Room_Properties/UI_Layers.md) as well as any layers created at runtime using [layer\_create](layer_create.md) in the current room, unless a [target room](layer_set_target_room.md) has been set, then it will only return the room layers created in the IDE for that particular room (even if it is set to the current room).

 

#### Syntax:

layer\_get\_all()

 

#### Returns:

[Array](../../../../GML_Overview/Arrays.md) (populated with Layer IDs) or \-1 on error

 

#### Example:

var a \= layer\_get\_all();  

 for (var i \= 0; i \< array\_length(a); i\+\+)  

 {  

     layer\_destroy(a\[i]);  

 }

The above code retrieves all the layers in the current room and adds their handles to an array. This array is then parsed to destroy the room layers.
