# skeleton\_bone\_state\_get

This function sets data related to the transform of a named bone of the instance's skeletal animation sprite.

Your skeletal animation is made up of a number of "bones", which you will have defined and given names to in your animation program, and this function can be used to get certain data for the named bone at any time. Note that this data refers to the **current** pose for the skeleton, depending on the animation set used, and the function requires a previously created [DS Map](../../../../Data_Structures/DS_Maps/ds_map_create.md), which will then have the following keys and their equivalent values after calling the function:

- **"x":** The local x position of the bone relative to the parent bone.
- **"y":** The local y position of the bone relative to the parent bone.
- **"angle":** The local rotation of the bone relative to the parent bone.
- **"xscale":** The local horizontal scale of the bone, in reference to the parent bone.
- **"yscale":** The local vertical scale of the bone, in reference to the parent bone.
- **"worldScaleX":** The magnitude (always positive) of the world scale X (this is a *read\-only* value).
- **"worldScaleY":** The magnitude (always positive) of the world scale Y (this is a *read\-only* value).
- **"worldAngleX":** The world rotation for the X axis (this is a *read\-only* value).
- **"worldAngleY":** The world rotation for the Y axis (this is a *read\-only* value).
- **"worldX":** The world X position (this is a *read\-only* value).
- **"worldY":** The world Y position (this is a *read\-only* value).
- **"appliedAngle":** This is the local rotation used to pose the skeleton bones.
- **"parent":** The name (a string) of the parent bone.

The map data returned is similar to that returned for the default pose when you use [skeleton\_bone\_data\_get](skeleton_bone_data_get.md), only now you have the extra "world" keys. These refer to the position of the bone relative to the *root* (origin) of the skeletal animation sprite, and the returned values do not take into consideration any scaling or rotation that has been done by setting the built\-in sprite variables like [image\_xscale](../../Sprite_Instance_Variables/image_xscale.md) or [image\_angle](../../Sprite_Instance_Variables/image_angle.md). The world values are *read\-only* and cannot be set.

 

 

#### Syntax:

skeleton\_bone\_state\_get(bone, map)

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
