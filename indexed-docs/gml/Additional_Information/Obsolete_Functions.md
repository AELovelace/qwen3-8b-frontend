# Obsolete Functions

Here you can find a list of all the functions that have been made obsolete when you compare GameMaker to legacy versions of the product. The functions listed here will be converted into [Compatibility Scripts](Compatibility_Scripts.md) when you import a \*.yyz made with a legacy version, and you can continue to work on the project as before. However, we recommend that you revise all the compatibility scripts created in a project, and ensure that future projects use the new functions/methods of working rather than depend on these scripts.

[Backgrounds](#)

In legacy GameMaker you had a separate **background** resource, where you could add images to be used as backgrounds. In GameMaker all images are considered sprites, and the use you put them too will depend on the layer they are assigned to in the room. This means that there is no longer a "background" resource, and it also means that the following functions are obsolete:

| draw\_background | draw\_background\_ext | draw\_background\_  stretched | draw\_background\_  stretched\_ext |
| --- | --- | --- | --- |
| draw\_background\_  part | draw\_background\_  part\_ext | draw\_background\_  general | draw\_background\_  tiled |
| draw\_background\_  tiled\_ext | background\_name | background\_exists | background\_get\_  name |
| draw\_background | draw\_background\_ext | draw\_background\_  stretched | draw\_background\_  stretched\_ext |
| background\_get\_  width | background\_get\_  height | background\_get\_  transparent | background\_get\_  smooth |
| background\_get\_  preload | background\_get\_uvs | background\_get\_  texture | background\_set\_alpha\_  from\_background |
| background\_create\_  from\_surface | background\_create\_  color | background\_create\_  colour | background\_create\_  gradient |
| background\_add | background\_replace | background\_add\_  alpha | background\_replace\_  alpha |
| background\_delete | background\_duplicate | background\_assign | background\_save |
| background\_prefetch | background\_  prefetch\_multi | background\_flush | background\_flush\_  multi |
| room\_set\_background | room\_set\_  background\_colour |  |

Legacy GameMaker lso had a number of different background variables that accessed the global background array. These are no longer required in GameMaker:

|
|  |
| background\_  index\[0\..7] | background\_  visible\[0\..7] | background\_  alpha\[0\..7] | background\_  blend\[0\..7] |
| background\_x\[0\..7] | background\_y\[0\..7] | background\_  colour | background\_  showcolour |
| background\_  foreground\[0\..7] | background\_  hspeed\[0\..7] | background\_  vspeed\[0\..7] | background\_  htiled\[0\..7] |
| background\_  vtiled\[0\..7] | background\_  width\[0\..7] | background\_  height\[0\..7] | background\_  xscale\[0\..7] |
| background\_  yscale\[0\..7] |

You can find out more about **Background Layers** from the section on [The Room Editor](../The_Asset_Editors/Rooms.md), and for more information on the functions that control background layers using code see [Background Layers](../GameMaker_Language/GML_Reference/Asset_Management/Rooms/Background_Layers/Background_Layers.md).

 

[Tiles](#)

As with backgrounds (explained above) the **tile** resource from legacy GameMaker no longer exists, and instead we have **Tile Sets** in GameMaker. In legacy GameMaker, tiles used a background resource and were placed at different depths in the room editor or through code, however the method used was not terribly flexible and was also not that efficient. To address these issues, in GameMaker tilesets are now created from a sprite resource, and can have various different properties (like animation or auto\-tiling). They are then placed on a tilemap layer within the room editor or through code. Due to these changes the following functions are now obsolete:

| tile\_get\_x | tile\_get\_y | tile\_get\_left | tile\_get\_top |
| --- | --- | --- | --- |
| tile\_get\_width | tile\_get\_height | tile\_get\_depth | tile\_get\_visible |
| tile\_get\_xscale | tile\_get\_yscale | tile\_get\_alpha | tile\_get\_background |
| tile\_set\_visible | tile\_set\_background | tile\_set\_region | tile\_set\_position |
| tile\_set\_depth | tile\_set\_scale | tile\_set\_blend | tile\_set\_alpha |
| tile\_get\_count | tile\_get\_id | tile\_get\_ids | tile\_get\_ids\_at\_depth |
| tile\_add | tile\_exists | tile\_delete | tile\_layer\_hide |
| tile\_layer\_show | tile\_layer\_delete | tile\_layer\_shift | tile\_layer\_find |
| tile\_layer\_delete\_at | tile\_layer\_depth | room\_tile\_add | room\_tile\_add\_ext |
| room\_tile\_clear |

You can find out more about Tile Sets from the manual section on the [Tile Set Editor](../The_Asset_Editors/Tile_Sets.md) and about how to use them in the room editor from the section on [Tile Layers](../The_Asset_Editors/Room_Properties/Layer_Properties.md). For more information on the functions that control background layers using code see [Tilemap Layers](../GameMaker_Language/GML_Reference/Asset_Management/Rooms/Tile_Map_Layers/Tile_Map_Layers.md). It is also worth noting that the GameMaker Language has some specific funtions related to using legacy tiles in imported projects, and you can find information on those [here](Compatibility_Functions.md).

 

[Objects](#)

The way objects are treated in GameMaker has changed slightly due to the introduction of layers in the Room Editor. There still exists the "depth" variable, but it is now only really used for compatibility and you can no longer get or set the depth for objects, only instances. This makes the following functions obsolete:

| object\_get\_depth |
| --- |
| object\_set\_depth |

You can find out more about object resources from the manual section on [The Object Editor](../The_Asset_Editors/Objects.md) and on the functions that control objects using code from the section [Objects](../GameMaker_Language/GML_Reference/Asset_Management/Objects/Objects.md).

 

[Sounds](#)

Legacy GameMaker had two different sound API's, one which used the deprecated sound\_ functions (that was only really valid for the HTML5 target platform), and the other which used the audio\_ functions. The audio API has been improved and expanded in GameMaker, making the legacy functions listed below obsolete:

| sound\_name | sound\_exists | sound\_get\_name | sound\_get\_kind |
| --- | --- | --- | --- |
| sound\_get\_preload | sound\_exists | sound\_restore | sound\_delete |
| sound\_play | sound\_loop | sound\_stop | sound\_stop\_all |
| sound\_isplaying | sound\_volume | sound\_fade | sound\_global\_volume |
| audio\_music\_gain | audio\_music\_is\_playing | audio\_new\_system | audio\_old\_system |
| audio\_pause\_music | audio\_play\_music | audio\_resume\_music | audio\_stop\_music |
| audio\_system |

You can find out more about audio resources from the manual section on [The Sound Editor](../The_Asset_Editors/Sounds.md) and on the functions that control audio using code from the section on [Audio](../GameMaker_Language/GML_Reference/Asset_Management/Audio/Audio.md). 

 

[D3D](#)

When using 3D models or primitives in legacy GameMaker, you had to use the d3d\_ functions. These used an obsolete API for drawing and in many cases were not related strictly to Direct 3D API, or even to using 3D itself. With the advent of vertex buffers, matrices and cameras in GameMaker, the following functions have been made obsolete:

|
|  |
| d3d\_start | d3d\_end | d3d\_set\_perspective | d3d\_set\_hidden |
| d3d\_set\_depth | d3d\_set\_lighting | d3d\_set\_shading | d3d\_set\_fog |
| d3d\_set\_culling | d3d\_set\_zwriteenable | d3d\_set\_projection | d3d\_set\_projection\_ext |
| d3d\_set\_projection\_  ortho | d3d\_set\_projection\_  perspective | d3d\_transform\_set\_  identity | d3d\_transform\_  set\_translation |
| d3d\_transform\_set\_  scaling | d3d\_transform\_  set\_rotation\_x | d3d\_transform\_set\_  rotation\_y | d3d\_transform\_  set\_rotation\_z |
| d3d\_transform\_set\_  rotation\_axis | d3d\_transform\_  add\_translation | d3d\_transform\_add\_  scaling | d3d\_transform\_  add\_rotation\_x |
| d3d\_transform\_add\_  rotation\_y | d3d\_transform\_  add\_rotation\_z | d3d\_transform\_add\_  rotation\_axis | d3d\_transform\_  stack\_clear |
| d3d\_transform\_stack\_  empty | d3d\_transform\_  stack\_push | d3d\_transform\_stack\_  pop | d3d\_transform\_  stack\_top |
| d3d\_transform\_stack\_  discard | d3d\_transform\_vertex | d3d\_light\_define\_  ambient | d3d\_light\_define\_  direction |
| d3d\_light\_define\_point | d3d\_light\_enable | d3d\_primitive\_begin | d3d\_primitive\_  begin\_texture |
| d3d\_primitive\_end | d3d\_vertex | d3d\_vertex\_color | d3d\_vertex\_colour |
| d3d\_vertex\_texture | d3d\_vertex\_texture\_  color | d3d\_vertex\_texture\_  colour | d3d\_vertex\_normal |
| d3d\_vertex\_normal\_  color | d3d\_vertex\_normal\_  colour | d3d\_vertex\_normal\_  texture | d3d\_vertex\_normal\_  texture\_color |
| d3d\_vertex\_normal\_  texture\_colour | d3d\_draw\_block | d3d\_draw\_cylinder | d3d\_draw\_cone |
| d3d\_draw\_ellipsoid | d3d\_draw\_wall | d3d\_draw\_floor | d3d\_model\_create |
| d3d\_model\_destroy | d3d\_model\_clear | d3d\_model\_load | d3d\_model\_save |
| d3d\_model\_draw | d3d\_model\_primitive\_  begin | d3d\_model\_  primitive\_end | d3d\_model\_vertex |
| d3d\_model\_vertex\_  color | d3d\_model\_vertex\_  colour | d3d\_model\_  vertex\_texture | d3d\_model\_vertex\_  texture\_color |
| d3d\_model\_vertex\_  texture\_colour | d3d\_model\_vertex\_  normal | d3d\_model\_  vertex\_normal\_color | d3d\_model\_vertex\_  normal\_colour |
| d3d\_model\_vertex\_  normal\_texture | d3d\_model\_vertex\_  normal\_texture\_color | d3d\_model\_vertex\_  normal\_texture\_colour | d3d\_model\_block |
| d3d\_model\_cylinder | d3d\_model\_cone | d3d\_model\_ellipsoid | d3d\_model\_wall |
| d3d\_model\_floor |

You can find out more about vertex buffers [here](../GameMaker_Language/GML_Reference/Drawing/Primitives/Primitives_And_Vertex_Formats.md), more about matrices [here](../GameMaker_Language/GML_Reference/Maths_And_Numbers/Matrix_Functions/Matrix_Functions.md), more about cameras [here](../GameMaker_Language/GML_Reference/Cameras_And_Display/Cameras_And_Viewports/Cameras_And_View_Ports.md), and more about the GPU functions [here](../GameMaker_Language/GML_Reference/Drawing/GPU_Control/GPU_Control.md).

 

[View Variables And Window Functions](#)

With the advent of the camera functions in GameMaker, it means that a number of view variables are no longer required, specifically those referring to the view into the room rather than the view\_port (which is still used). There are also a few functions for controlling how things are displayed that were available in legacy versions of GameMaker Studio which are also no longer appropriate. These variables and functions are listed below:

| view\_object | view\_angle | view\_xview | view\_yview |
| --- | --- | --- | --- |
| view\_hview | view\_wview | view\_hborder | view\_vborder |
| view\_hspeed | view\_vspeed | display\_set\_windows\_  vertex\_buffer\_method | display\_get\_windows\_  vertex\_buffer\_method |
| display\_set\_windows\_  alternate\_sync | display\_get\_windows\_  alternate\_sync | room\_set\_view |

You can find out more about cameras from the manual section on [Cameras And The Display](../GameMaker_Language/GML_Reference/Cameras_And_Display/Cameras_And_Display.md).

 

[3rd Party Support](#)

GameMaker moves a lot of built\-in functionality from previous versions into [extensions](../The_Asset_Editors/Extensions.md), meaning that the following 3rd party support functions are considered obsolete:

| ads\_enable | ads\_disable | ads\_move | ads\_get\_display\_  width |
| --- | --- | --- | --- |
| ads\_get\_display\_  height | ads\_interstitial\_  available | ads\_interstitial\_  display | ads\_setup |
| ads\_engagement\_  available | ads\_engagement\_  launch | ads\_engagement\_  active | ads\_event |
| ads\_event\_preload | ads\_set\_reward\_  callback | playhaven\_add\_  notification\_badge | playhaven\_hide\_  notification\_badge |
| playhaven\_position\_  notification\_badge | playhaven\_update\_  notification\_badge | pocketchange\_display\_  reward | pocketchange\_display\_  shop |
| analytics\_event | analytics\_event\_ext | facebook\_init | facebook\_login |
| facebook\_request\_  publish\_permissions | facebook\_request\_  read\_permissions | facebook\_check\_  permission | facebook\_status |
| facebook\_accesstoken | facebook\_user\_id | facebook\_graph\_  request | facebook\_dialog |
| facebook\_send\_invite | facebook\_post\_  message | facebook\_logout | facebook\_launch\_  offerwall |
| iap\_event\_queue | iap\_files\_purchased | iap\_is\_downloaded | iap\_product\_files |
| iap\_product\_status | iap\_store\_status | iap\_data | iap\_activate |
| iap\_status | iap\_enumerate\_products | iap\_restore\_all | iap\_acquire |
| iap\_consume | iap\_product\_details | iap\_purchase\_details |  |
| immersion\_play\_effect | immersion\_stop |
| achievement\_\* | win8\_\* | uwp\_appbar\_\* |

You can get our official extensions for advertising and other APIs from the [Marketplace Page](https://marketplace.gamemaker.io/publishers/23/yoyo-games).

 

[GML Visual Actions](#)

Both legacy GameMaker and GameMaker have a visual scripting **GML Visual** interface for creating your games, however the way it is handled in GameMaker is quite different to the previous methods used. Previously, all GML Visual actions had their own corresponding function which worked "behind the scenes" to get the desired results, however this was not very transparent and added in extra overheads to the function calls, resulting in poorer performance. In GameMaker this has been changed, and now all actions compile to pure code (and can be shown as such if required), meaning that the following action functions are obsolete:

| action\_path\_old | action\_set\_sprite | action\_draw\_font | action\_draw\_font\_old |
| --- | --- | --- | --- |
| action\_fill\_color | action\_fill\_colour | action\_line\_color | action\_line\_colour |
| action\_highscore | action\_set\_relative | action\_move | action\_set\_motion |
| action\_set\_hspeed | action\_set\_vspeed | action\_set\_gravity | action\_set\_friction |
| action\_move\_point | action\_move\_to | action\_move\_start | action\_move\_random |
| action\_snap | action\_wrap | action\_reverse\_xdir | action\_reverse\_ydir |
| action\_move\_contact | action\_bounce | action\_path | action\_path\_end |
| action\_path\_position | action\_path\_speed | action\_linear\_step | action\_potential\_step |
| action\_kill\_object | action\_create\_object | action\_create\_object\_motion | action\_create\_object\_random |
| action\_change\_object | action\_kill\_position | action\_sprite\_set | action\_sprite\_transform |
| action\_sprite\_color | action\_sprite\_colour | action\_sound | action\_end\_sound |
| action\_if\_sound | action\_another\_room | action\_current\_room | action\_previous\_room |
| action\_next\_room | action\_if\_previous\_room | action\_if\_next\_room | action\_set\_alarm |
| action\_sleep | action\_set\_timeline | action\_timeline\_set | action\_timeline\_start |
| action\_timeline\_stop | action\_timeline\_pause | action\_set\_timeline\_position | action\_set\_timeline\_speed |
| action\_message | action\_show\_info | action\_show\_video | action\_end\_game |
| action\_restart\_game | action\_save\_game | action\_load\_game | action\_replace\_sprite |
| action\_replace\_sound | action\_replace\_  background | action\_if\_empty | action\_if\_collision |
| action\_if | action\_if\_number | action\_if\_object | action\_if\_question |
| action\_if\_dice | action\_if\_mouse | action\_if\_aligned | action\_execute\_script |
| action\_inherited | action\_if\_variable | action\_draw\_variable | action\_set\_score |
| action\_if\_score | action\_draw\_score | action\_highscore\_show | action\_highscore\_clear |
| action\_set\_life | action\_if\_life | action\_draw\_life | action\_draw\_life\_images |
| action\_set\_health | action\_if\_health | action\_draw\_health | action\_set\_caption |
| action\_partsyst\_create | action\_partsyst\_destroy | action\_partsyst\_clear | action\_parttype\_create\_old |
| action\_parttype\_create | action\_parttype\_color | action\_parttype\_colour | action\_parttype\_life |
| action\_parttype\_speed | action\_parttype\_gravity | action\_parttype\_secondary | action\_partemit\_create |
| action\_partemit\_destroy | action\_partemit\_burst | action\_partemit\_stream | action\_cd\_play |
| action\_cd\_stop | action\_cd\_pause | action\_cd\_resume | action\_cd\_present |
| action\_cd\_playing | action\_set\_cursor | action\_webpage | action\_splash\_web |
| action\_draw\_sprite | action\_draw\_background | action\_draw\_text | action\_draw\_text\_transformed |
| action\_draw\_rectangle | action\_draw\_gradient\_hor | action\_draw\_gradient\_vert | action\_draw\_ellipse |
| action\_draw\_  ellipse\_gradient | action\_draw\_line | action\_draw\_arrow | action\_color |
| action\_colour | action\_font | action\_fullscreen | action\_snapshot |
| action\_effect |

You can find out more about the new GML Visual from the manual section on [GML Visual](../Drag_And_Drop/Drag_And_Drop_Index.md).

 

[Vectors and Matrices](#)

The data type used to store vectors and matrices in GameMaker are [Arrays](../GameMaker_Language/GML_Overview/Arrays.md). Therefore, the following functions relating to working with vectors and matrices were removed: 

| is\_vec3 | is\_vec4 | is\_matrix |
| --- | --- | --- |

These functions appeared to check for a specific type, while the underlying type is always an array or a range of an array (of respectively length 3, 4 and 16\). E.g. the functions [matrix\_build](../GameMaker_Language/GML_Reference/Maths_And_Numbers/Matrix_Functions/matrix_build.md) and [matrix\_build\_identity](../GameMaker_Language/GML_Reference/Maths_And_Numbers/Matrix_Functions/matrix_build_identity.md) return a *matrix*, of which the 16 elements are stored in an *array* datatype. To check the datatype you should use [is\_array](../GameMaker_Language/GML_Reference/Variable_Functions/is_array.md) instead and combine this with the length of the array given by [array\_length](../GameMaker_Language/GML_Reference/Variable_Functions/array_length.md) to work out the datatype.

  Checking for an array datatype and its length doesn't mean the actual contents represent a valid vector or matrix.

Alternatively, to store vectors and matrices you can use other data structures provided by GameMaker, such as [Buffers](../GameMaker_Language/GML_Reference/Buffers/Buffers.md), [DS Grids](../GameMaker_Language/GML_Reference/Data_Structures/DS_Grids/DS_Grids.md) a [struct](../GameMaker_Language/GML_Overview/Structs.md#struct) or even a [surface](../GameMaker_Language/GML_Reference/Drawing/Surfaces/Surfaces.md) to store the same information, instead of a dedicated data type.

 

The following built\-in global variables are also obsolete, although they are still considered reserved variables in GML so that the IDE can recognise them and flag them for updating/removing when a legacy project that uses them is imported (as are the variables listed under the Views and the Backgrounds sections, above):

| gamemaker\_registered | gamemaker\_progamemaker\_  version | secure\_mode |
| --- | --- | --- |
| show\_health | show\_score | show\_lives |
| caption\_score | caption\_lives | caption\_health |
| argument\_relative | room\_caption | room\_speed |
| transition\_steps | transition\_kind | game\_guid |
| error\_last | error\_occurred | buffer\_surface\_copy |
