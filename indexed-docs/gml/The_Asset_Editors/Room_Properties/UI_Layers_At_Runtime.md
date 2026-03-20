# UI Layers At Runtime

This page covers the runtime behaviour of UI layers and of Object Instances placed inside UI layers.

## Runtime Order

### Creation

UI Layers are initialised when the first room in the game begins. All elements (including Object Instances) in a UI Layer stay persistent throughout the rest of the game, regardless of the active room changing.

You can modify the order of creation for Object Instances in UI Layers in the [Instance Creation Order](Room_Properties.md#creation_order) menu of the first room set in [The Room Manager](../../Settings/The_Room_Manager.md).

### Draw Order

When UI layers are present, the runtime draw order is as follows:

- **Draw Event**: Contents of all layers are drawn including the Draw Begin and Draw events of any Object instances in the room.
- **Viewport UI Layers**: Any UI layers with "**Game View**" set to "**Viewports**" are rendered for the current viewport. The position and size of the viewport is used as the position and size of each UI layer.
- **Draw End Event**: The Draw End event is run.
 

---
- **Draw GUI Begin**: The Draw GUI Begin Event is run.
- **Display UI Layers**: Any UI layers with "**Game View**" set to "**Display**" are drawn to the screen. The size of the [GUI layer](../../GameMaker_Language/GML_Reference/Cameras_And_Display/display_set_gui_size.md) is used as the size of each UI layer.
- **Draw GUI, Draw GUI End**: The remaining Draw GUI events are run.

## Runtime Editing

At runtime, you can get the root [Flex Panel Node](../../GameMaker_Language/GML_Reference/Flex_Panels/Function_Reference/flexpanel_create_node.md) of a UI layer by calling [layer\_get\_flexpanel\_node](../../GameMaker_Language/GML_Reference/Asset_Management/Rooms/UI_Layers/layer_get_flexpanel_node.md). Any of the [Flex Panel functions](../../GameMaker_Language/GML_Reference/Flex_Panels/Function_Reference/section_index.md) can be called on the returned node.

For example, you can search for a child Flex Panel recursively under the root node by calling [flexpanel\_node\_get\_child](../../GameMaker_Language/GML_Reference/Flex_Panels/Function_Reference/flexpanel_node_get_child.md) and call [flexpanel\_node\_get\_struct](../../GameMaker_Language/GML_Reference/Flex_Panels/Function_Reference/flexpanel_node_get_struct.md) to get the properties of a [node as a struct](../../GameMaker_Language/GML_Reference/Flex_Panels/Flex_Panels_Styling.md).

Element handles returned from a node struct (from its layerElements array) can be operated on by the relevant [layer element functions](../../GameMaker_Language/GML_Reference/Asset_Management/Rooms/Rooms.md#room_layers_elements) (e.g. [layer\_text\_text](../../GameMaker_Language/GML_Reference/Asset_Management/Rooms/Text_Functions/layer_text_text.md) to change a text element's string or [layer\_sprite\_change](../../GameMaker_Language/GML_Reference/Asset_Management/Rooms/Sprite_Layers/layer_sprite_change.md) to change a sprite element's sprite). All elements in a UI layer can collectively be offset by calling [layer\_x](../../GameMaker_Language/GML_Reference/Asset_Management/Rooms/General_Layer_Functions/layer_x.md) and [layer\_y](../../GameMaker_Language/GML_Reference/Asset_Management/Rooms/General_Layer_Functions/layer_y.md).

You can get the type of a layer at runtime with [layer\_get\_type](../../GameMaker_Language/GML_Reference/Asset_Management/Rooms/General_Layer_Functions/layer_get_type.md) and check if an Object Instance is in a UI layer using the [on\_ui\_layer](../../GameMaker_Language/GML_Reference/Asset_Management/Instances/Instance_Variables/on_ui_layer.md) instance variable.

## Runtime Changes For Object Instances

As Object Instances can be placed in UI Layers, the following behaviours for them are different from regular Instance layers:

- The [x](../../GameMaker_Language/GML_Reference/Asset_Management/Instances/Instance_Variables/x.md) and [y](../../GameMaker_Language/GML_Reference/Asset_Management/Instances/Instance_Variables/y.md) position variables return the position of the instance on the [GUI layer](../Object_Properties/Draw_Events.md) or viewport instead of inside the room area, i.e. they are unaffected by cameras and stick to their positions on the on\-screen GUI or viewport area. The same applies to the bbox\_\* variables.
- All Mouse events for instances on UI layers work with the mouse coordinates in the UI space (GUI layer or viewport), so you can use the Left Pressed, Mouse Enter etc. events to detect mouse interaction with the instance when it is placed on a UI layer.
	- The [mouse\_x](../../GameMaker_Language/GML_Reference/Game_Input/Mouse_Input/mouse_x.md) and [mouse\_y](../../GameMaker_Language/GML_Reference/Game_Input/Mouse_Input/mouse_y.md) variables for instances on UI layers will also be in UI space instead of the room space.
	- For instances on "Display" UI layers, you can use the x/y position or bbox\_\* variables to do manual checks against the mouse using the [mouse\_x](../../GameMaker_Language/GML_Reference/Game_Input/Mouse_Input/mouse_x.md) / [mouse\_y](../../GameMaker_Language/GML_Reference/Game_Input/Mouse_Input/mouse_y.md) variables.
- The Draw event will draw to the same space where the UI instance is present, i.e. either the viewport or the GUI layer, to the same "depth" as defined for the instance in the Element List.
- Draw GUI events do nothing.
-
