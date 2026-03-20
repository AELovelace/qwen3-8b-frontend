# UI Layers

UI layers let you define [Flex Panels](../../GameMaker_Language/GML_Reference/Flex_Panels/Flex_Panels.md) and place sprites, objects and text within them to create responsive user interfaces that are drawn on top of your game, useful for creating HUDs and menus.

You can add a UI layer in [The Room Editor](../Rooms.md) through the  "**Create Layer**" menu:

All UI layers are contained in the global "**UI Folder**", which will be created when you add your first UI layer. The UI Folder (and every UI layer inside it) is shared among all rooms in your project, so UI layers are displayed throughout your game regardless of which room is active.

Once you add a UI layer, you can choose whether it should appear on the main game display or inside your viewports separately. You can then add Flex Panels inside the layer and place [elements](UI_Element_Propert.md) inside Flex Panels.

Mini TOC (placeholder)

1. Heading

## How To Use

You can follow the basic steps below to create your UI with UI layers:

1. Add your first UI layer and add Flex Panels within it to create a structure
2. Set the [properties](UI_Element_Propert.md) of your UI layer and Flex Panels from the Inspector and the canvas, to determine how they are aligned and sized
3. Place Object Instances in your Flex Panels to enable runtime interaction
4. Place Sprites or Font assets to set up the visuals of your Flex Panels
5. Enable or disable a UI layer at runtime using [layer\_set\_visible](../../GameMaker_Language/GML_Reference/Asset_Management/Rooms/General_Layer_Functions/layer_set_visible.md)

At runtime, you can get the root [Flex Panel Node](../../GameMaker_Language/GML_Reference/Flex_Panels/Function_Reference/flexpanel_create_node.md) of a UI layer by calling [layer\_get\_flexpanel\_node](../../GameMaker_Language/GML_Reference/Asset_Management/Rooms/UI_Layers/layer_get_flexpanel_node.md). Any of the [Flex Panel functions](../../GameMaker_Language/GML_Reference/Flex_Panels/Function_Reference/section_index.md) can be called on the returned node.

## UI Folder

The UI folder contains all the UI layers in your project and is shared among all rooms.

The UI folder is not a layer itself despite appearing in the Layers panel. It only exists in the editor to group all UI layers under one menu and cannot be retrieved or operated on as a layer at runtime.

Right\-clicking on the UI folder displays the following options:

- **Create New UI Layer**: This creates a new UI layer.
- **Delete UI Folder**: This deletes the UI folder, deleting all of the UI layers created in the project.

## Layer Structure

UI layers make use of [Flex Panels](../../GameMaker_Language/GML_Reference/Flex_Panels/Flex_Panels.md) for containing assets. UI layers themselves are Flex Panels, which can hold other Flex Panels and each Flex Panel can hold one or more assets.

Flex Panels can hold [Objects](../Objects.md), [Sprites](../Sprites.md), [Sequences](../Sequences.md), [Fonts](../Fonts.md) and other Flex Panels. You can drag such assets into the canvas or into the Element List, any such asset will always be added inside a new Flex Panel with "auto" size unless you are holding CTRL/CMD (this behaviour can be reversed in the [Preferences](../../Setting_Up_And_Version_Information/IDE_Preferences/Room_Editor_Preferences.md)).

When dragging an asset into the Canvas, you can place it inside a particular UI layer or Flex Panel by dropping it inside its area. When placed outside of such areas, you will be prompted to create a new UI layer, which you can set to automatically create or ignore in the [Preferences](../../Setting_Up_And_Version_Information/IDE_Preferences/Room_Editor_Preferences.md).

In the above example, a UI layer holds a Flex Panel which then holds three child Flex Panels. Each child Flex Panel contains a sprite. In the canvas, the sprites are displayed in a row with gaps between them, based on the settings of the parent Flex Panel.

Each element in the canvas will display a label. Clicking on the label will display its parent containers above the label, where you can click on a parent label to select its entry in the Element List.

## Element List

When the UI Folder is selected, the Element List displays all the UI layers in your project. Here you can search for elements and change the orientation of the window.

The list first displays any UI Layers that have "**Game View**" set to "**Display**", and those with "**Game View**" set to "**Viewports**" are displayed under the "**Viewports**" header. UI layers can be made invisible by clicking on the  eye icon and locked with the  button.

You can drag your layers, Flex Panels or assets to place them inside, above or below another item in the list. The order of the elements in this list affects their draw order, e.g. an item above another in the list will also be drawn above it in\-game.

Asset elements inside Flex Panels will have a  checkbox next to them to enable/disable the element.

  Disabling an Object Instance will deactivate it so none of its events run. The same applies when the UI layer containing the instance is set to invisible with the  button or the [layer\_set\_visible](../../GameMaker_Language/GML_Reference/Asset_Management/Rooms/General_Layer_Functions/layer_set_visible.md) function.

Right\-clicking on any item in this list will show the following menu:

- **Add UI Layer**: Adds a new UI Layer. If you right\-clicked on a UI layer with "**Game View**" set to "**Viewports**" (or a child of such a layer), the new UI layer will be created as a viewport layer. The name of each UI layer must be unique.
- **Add Flex Panel**: Adds a new Flex Panel under the selected item.
- **Add Folder**: Adds a new folder, this is only used for organisational purposes.
- **General options**: You can rename the item, cut/copy/paste, duplicate and delete it.
- **Show Instance/Asset names first**: Change whether asset elements should display their asset names or instance names first in the list.
- **List options**: Here you can expand/collapse all children under the item or all items in the list, and select all items.

## Toolbox

Using UI layers will enable the following extra options in the Room Toolbox:

- **Toggle UI canvas preview**: This enables a canvas that is used to display your UI layers. Your UI layers will be previewed at the size set in this menu \-\- you may set a custom size or choose from one of the given presets. You can change the orientation and set an offset. Enable "Clip Contents" to ensure only elements inside the canvas area are drawn.  

  

 When this option is enabled, the canvas preview area can be resized within the room canvas by clicking and dragging your mouse from one of the edges or corners.  

  

  These options are only provided for preview in the canvas and do not affect how UI layers appear in\-game.
- **Show UI Layer node outlines**: This enables outlines for all UI layers and Flex Panels that display the area taken up by each layer/panel. Each layer/panel in the Element List displays a colour that corresponds to the colour of its outline in the Room Canvas.

In the Layer Toolbox, the  button will appear allowing you to place text items in the canvas.

## Canvas Editing

Any Asset Elements placed inside UI layers (e.g. sprites, objects, etc.) can be moved and resized in the canvas as normal, just like you can in other layer types. Asset elements are always placed relative to their parent Flex Panels.

Flex Panels can also be moved and resized in the canvas, however this may be restricted depending on the Flex Panel settings. For example, you can only move Flex Panels that are set to "**Absolute**" as other position types dictate the position of the panel according to the parent panel. You cannot resize Flex Panels that have the size set to "**Auto**" as their size is automatically determined.

You can also adjust the padding (blue) and margin (green) of a Flex Panel by clicking and dragging the coloured selectors inside or outside each of its edges, respectively:

Holding ALT modifies the opposite edge at the same time. Clicking on the margin/padding selector opens a text box where you can enter an exact value for the margin/padding.

You can also drag a Flex Panel to change its position within the parent Flex Panel, in relation to its siblings. While dragging such a panel, you may hold R to move the panel out to be placed into a different container, or hold C to clone/duplicate the panel:

Use of the R and C modifiers is also permitted when moving a Flex Panel with an "**Absolute**" position type.

### Selection Rules

The following rules are followed when clicking on a Flex Panel for selection:

- Within a UI layer, clicking always selects the most top\-level Flex Panel found under the mouse cursor (i.e. the first parent container)
	- Clicking while holding ALT selects the deepest Flex Panel under the mouse cursor
	- This behaviour can be changed from the UI layer preferences under the [Room Editor Preferences](../../Setting_Up_And_Version_Information/IDE_Preferences/Room_Editor_Preferences.md). Enabling the "**Canvas selection selects deepest element by default**" option makes every click select the deepest Flex Panel or element it can find.
- Double\-clicking while a Flex Panel is selected selects the next Flex Panel in the hierarchy that is under the mouse cursor
- Right\-clicking in the canvas displays a menu with all of the Flex Panels under the mouse cursor from the top level to the deepest, where you can choose the Flex Panel to select for manipulation

## Runtime Information

For information regarding the behaviour of UI Layers and its contents at runtime, see: [UI Layers At Runtime](UI_Layers_At_Runtime.md)

## Inspector Properties

You can select a UI layer, Flex Panel or Asset Element in the Element List and its properties will be shown in the Inspector.

For details on the editable properties, see: [UI Element Properties](UI_Element_Propert.md)
