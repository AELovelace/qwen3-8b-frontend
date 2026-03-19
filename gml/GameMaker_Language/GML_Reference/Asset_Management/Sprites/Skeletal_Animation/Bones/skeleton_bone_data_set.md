# skeleton\_bone\_data\_set

This function sets transform data for a named bone of the instance's skeletal animation sprite.

Your skeletal animation is made up of a number of "bones", which you will have defined and given names to in your animation program. Tthis function can be used to set certain data for the named bone at any time. The data must be set from a previously created [DS Map](../../../../Data_Structures/DS_Maps/ds_map_create.md), which should have the following keys and their equivalent values:

- **"x":** The local x position of the bone relative to the parent bone.
- **"y":** The local y position of the bone relative to the parent bone.
- **"angle":** The local rotation of the bone relative to the parent bone.
- **"xscale":** The local horizontal scale of the bone.
- **"yscale":** The local vertical scale of the bone.
- **"parent":** The name (a string) of the parent bone.

  This data refers to the **default** pose for the skeleton, and not the current pose that is being drawn (for that use the function [skeleton\_bone\_state\_set](skeleton_bone_state_set.md)).

 

#### Syntax:

skeleton\_bone\_data\_set(bone, map)

| Argument | Type | Description |
| --- | --- | --- |
| bone | [String](../../../../../GML_Overview/Data_Types.md) | The name (as a string) of the bone. |
| map | [DS Map](../../../../Data_Structures/DS_Maps/ds_map_create.md) | The (previously created) DS map that stores the bone data. |

 

#### Returns:

N/A

 

#### Example:

var \_bone\_map \= ds\_map\_create();  

 skeleton\_bone\_data\_get("head", \_bone\_map);  

 ds\_map\_replace(\_bone\_map, "parent", "body");  

 skeleton\_bone\_data\_set("head", \_bone\_map);  

 ds\_map\_destroy(\_bone\_map);

The above code creates a DS map and then populates it with the data from the bone named "head". It then replaces the "parent" bone key in the map with a new value and sets the "head" bone again with the new set of data.
