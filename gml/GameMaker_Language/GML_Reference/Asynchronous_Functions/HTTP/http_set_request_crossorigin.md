# http\_set\_request\_crossorigin

With this function you can set the cross origin type to use when loading images from a file (using [sprite\_add()](../../Asset_Management/Sprites/Sprite_Manipulation/sprite_add.md)), or sending custom HTTP requests to servers (e.g. using [http\_post\_string()](http_post_string.md)). The function is exclusively for the HTML5 platform.

When set to "use\-credentials" you no longer need to give an absolute path to the sprite being loaded, but instead would give a *relative* path (as shown in the example below).

By default the cross origin type is set to "anonymous".

 

#### Syntax:

http\_set\_request\_crossorigin(origin\_type)

| Argument | Type | Description |
| --- | --- | --- |
| origin\_type | [String](../../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The cross origin type to use (a string) |

 

#### Returns:

N/A

 

#### Example:

if (string\_lower(http\_get\_request\_crossorigin()) !\= "use\-credentials")   

 {  

     http\_set\_request\_crossorigin("use\-credentials");  

 }  

 sprite\_add("sprites/player\_outfit\_1\.png", 0, false, false, 0, 0\);

The above code will first check the currently set cross origin type and if it is not "use\-credentials" then it is set to "use\-credentials" and then a sprite is added from a file.
