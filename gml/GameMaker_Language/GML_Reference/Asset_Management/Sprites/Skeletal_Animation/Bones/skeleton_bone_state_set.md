# skeleton\_bone\_state\_set

This function sets data related to the transform of a named bone of the instance's skeletal animation sprite.

Your skeletal animation is made up of a number of "bones", which you will have defined and given names to in your animation program, and this function can be used to set certain data for a named bone at any time. Note that this data will set the **current** pose for the skeleton, depending on the animation set used, and the function requires a previously created [DS Map](../../../../Data_Structures/DS_Maps/ds_map_create.md), which should have the following keys and their required values:

- **"x":** The local x position of the bone relative to the parent bone.
- **"y":** The local y position of the bone relative to the parent bone.
- **"angle":** The local rotation of the bone relative to the parent bone.
- **"xscale":** The local horizontal scale of the bone.
- **"yscale":** The local vertical scale of the bone.
- **"parent":** The name (a string) of the parent bone.

This function is provided so that you can "intercept" animation data and modify it before it is drawn on the screen, and as such you would want to use it in the [Other \- Animation Update](../../../../../../The_Asset_Editors/Object_Properties/Other_Events.md) event, since this event is triggered just before the Draw Events.

Note that you can use the same map you filled out using the [skeleton\_bone\_state\_get](skeleton_bone_state_get.md) function, even though it contains the additional "World" keys and values. Since these refer to *read\-only* values, setting them with this function will have no affect.

 

#### Syntax:

skeleton\_bone\_state\_set(bone, map)

| Argument | Type | Description |
| --- | --- | --- |
| bone | [String](../../../../../GML_Overview/Data_Types.md) | The name (as a string) of the bone. |
| map | [DS Map](../../../../Data_Structures/DS_Maps/ds_map_create.md) | The (previously created) DS map that stores the bone data. |

 

#### Returns:

N/A

 

#### Example:

var \_map \= ds\_map\_create();  

 skeleton\_bone\_state\_get("head", \_map);  

 var \_xx \= ds\_map\_find\_value(\_map, "worldX");  

 var \_yy \= ds\_map\_find\_value(\_map, "worldY");  

 var \_deltax \= mouse\_x \- (x \+ \_xx);  

 var \_deltay \= mouse\_y \- (y \+ \_yy);  

 var \_angle \= \-darctan2(\_deltay, \_deltax);  

 ds\_map\_replace(\_map, "angle", \_angle);  

 skeleton\_bone\_state\_set("head", \_map);  

 ds\_map\_destroy(\_map);

The above code creates a DS map and then populates it with the data from the bone named "head". It then extracts the world position for the bone, and uses that data to set the "angle" of the bone to track the mouse position in the game.
