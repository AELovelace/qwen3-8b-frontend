# skeleton\_bone\_data\_get

This function gets information on the transform of a named bone of the instance's skeletal animation sprite.

Your skeletal animation is made up of a number of "bones", which you will have defined and given names to in your animation program. This function can be used to get information on the named bone at any time and store the data in an empty [DS Map](../../../../Data_Structures/DS_Maps/ds_map_create.md), which you must have created previously.

When you call this function the map will be populated with the following keys:

- **"x":** The local x position of the bone relative to the parent bone.
- **"y":** The local y position of the bone relative to the parent bone.
- **"angle":** The local rotation of the bone relative to the parent bone.
- **"xscale":** The local horizontal scale of the bone, in reference to the parent bone.
- **"yscale":** The local vertical scale of the bone, in reference to the parent bone.
- **"parent":** The name (a string) of the parent bone.

  This data refers to the **default** pose for the skeleton, and not to the current pose that is being drawn. If you need the data from the **current** pose, use [skeleton\_bone\_state\_get](skeleton_bone_state_get.md).

 

#### Syntax:

skeleton\_bone\_data\_get(bone, map)

| Argument | Type | Description |
| --- | --- | --- |
| bone | [String](../../../../../GML_Overview/Data_Types.md) | The name (as a string) of the bone. |
| map | [DS Map](../../../../Data_Structures/DS_Maps/ds_map_create.md) | The (previously created) DS map that will receive the bone data. |

 

#### Returns:

N/A

 

#### Example:

bone\_map \= ds\_map\_create();  

 skeleton\_bone\_data\_get("leftarm", bone\_map);

The above code creates a DS map and then populates it with the data from the bone named "leftarm".
