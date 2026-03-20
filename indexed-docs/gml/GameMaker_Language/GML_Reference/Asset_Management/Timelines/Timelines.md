# Timelines

 
Timelines are used for controlling events in your game, and are based on "moments", where a "moment" is simply a single game step. These timelines are generally created from the **Asset Browser** using the [Timeline Editor](../../../../The_Asset_Editors/Timelines.md) in a similar way to an object, ie: you create a timeline, then in each moment that you require it to perform an action you add some code or a GML Visual icon for it to perform. Once created, you can then stop, start, and manipulate timelines through code. You can even modify individual moments by defining a [script function](../../../GML_Overview/Script_Functions.md) and adding it into the timeline dynamically from a controller object (for example), making this a very powerful and versatile tool when creating your games.

The following functions are for adding and manipulating Timelines from within your game:

- [timeline\_exists](timeline_exists.md)
- [timeline\_get\_name](timeline_get_name.md)
- [timeline\_add](timeline_add.md)
- [timeline\_delete](timeline_delete.md)
- [timeline\_moment\_add\_script](timeline_moment_add_script.md)
- [timeline\_moment\_clear](timeline_moment_clear.md)
- [timeline\_clear](timeline_clear.md)
- [timeline\_size](timeline_size.md)
- [timeline\_max\_moment](timeline_max_moment.md)

 

The following variables are "built\-in" to all instances to make working with Timelines easier and give you control over them:

- [timeline\_index](timeline_index.md)
- [timeline\_running](timeline_running.md)
- [timeline\_speed](timeline_speed.md)
- [timeline\_position](timeline_position.md)
- [timeline\_loop](timeline_loop.md)

 

Note that you can find further information on built\-in instance variables here: [Built\-In Instance Variables](../Instances/Instance_Variables/Instance_Variables.md).
