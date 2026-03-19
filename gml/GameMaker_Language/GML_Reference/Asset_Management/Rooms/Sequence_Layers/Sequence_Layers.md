# Sequence Elements

In this section we have the functions that are used for adding, removing and editing [Sequences](../../../../../The_Asset_Editors/Sequences.md) and for changing how they behave in a game room in relation to the *layer* they are on. It should be noted that sequences are similar to objects, in that when one is created on a layer in a room, it is considered an *instance* of the main sequence *object* from [The Asset Browser](../../../../../Introduction/The_Asset_Browser.md). So, when you add a sequence to a layer in a room, you are creating an *instance* of the base sequence object, and this sequence instance is added as an *element* on a room layer. The sequence instance is what controls things like playback speed and direction, and will itself contain another sequence data *struct* which is what contains the actual sequence track data. This is important, as the functions listed below will reference the sequence **element ID** (the ID of the sequence *on the layer*) as well as the sequence **instance ID** (the actual ID of the sequence that is being referenced by the element) and the sequence data [struct](../../../../GML_Overview/Structs.md) (which contains all the sequence data).

The functions given below for modifying Sequence Elements can also be used on Sequence Elements contained within UI layers, accessible through the [Flex Panel Struct](../../../Flex_Panels/Flex_Panels_Styling.md).

There are also additional functions available for dealing with the contents of sequences and for defining your own. You can find a complete list of these functions on the [Sequences](../../Sequences/Sequences.md) page.

## Function Reference

### General

- [layer\_sequence\_exists](layer_sequence_exists.md)
- [layer\_sequence\_create](layer_sequence_create.md)
- [layer\_sequence\_destroy](layer_sequence_destroy.md)
- [layer\_sequence\_x](layer_sequence_x.md)
- [layer\_sequence\_y](layer_sequence_y.md)
- [layer\_sequence\_angle](layer_sequence_angle.md)
- [layer\_sequence\_xscale](layer_sequence_xscale.md)
- [layer\_sequence\_yscale](layer_sequence_yscale.md)
- [layer\_sequence\_headpos](layer_sequence_headpos.md)
- [layer\_sequence\_headdir](layer_sequence_headdir.md)
- [layer\_sequence\_pause](layer_sequence_pause.md)
- [layer\_sequence\_play](layer_sequence_play.md)
- [layer\_sequence\_speedscale](layer_sequence_speedscale.md)
- [layer\_sequence\_get\_x](layer_sequence_get_x.md)
- [layer\_sequence\_get\_y](layer_sequence_get_y.md)
- [layer\_sequence\_get\_angle](layer_sequence_get_angle.md)
- [layer\_sequence\_get\_xscale](layer_sequence_get_xscale.md)
- [layer\_sequence\_get\_yscale](layer_sequence_get_yscale.md)
- [layer\_sequence\_get\_headpos](layer_sequence_get_headpos.md)
- [layer\_sequence\_get\_headdir](layer_sequence_get_headdir.md)
- [layer\_sequence\_get\_speedscale](layer_sequence_get_speedscale.md)
- [layer\_sequence\_get\_length](layer_sequence_get_length.md)
- [layer\_sequence\_get\_instance](layer_sequence_get_instance.md)
- [layer\_sequence\_get\_sequence](layer_sequence_get_sequence.md)
- [layer\_sequence\_is\_paused](layer_sequence_is_paused.md)
- [layer\_sequence\_is\_finished](layer_sequence_is_finished.md)

### [Sequences](../../Sequences/Sequences.md)
