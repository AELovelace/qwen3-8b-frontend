# UI Element Properties

The Element List displays all UI layers and all parts of a UI layer, including Flex Panels and assets:

You can select a UI layer, Flex Panel or Asset Element in the Element List and its properties will be shown in [The Inspector](../../IDE_Tools/The_Inspector.md). Besides being able to change the Element name and associated asset (if any), there are other properties which are described below for each type of Element.

These properties are represented at runtime by the [Flex Panel Struct Members](../../GameMaker_Language/GML_Reference/Flex_Panels/Flex_Panels_Styling.md).

## UI Layer Properties

A UI layer contains the following main properties:

[UI Layer Main Properties](#)

### Game View

You can choose between "**Display**" and "**Viewports**".

- **Display**: The layer contents will be rendered directly to the game screen.
- **Viewports**: The layer contents will be rendered separately for each active viewport in the game.

Details about the runtime rendering order are given here: [Draw Order](UI_Layers_At_Runtime.md#h).

  Viewports must be enabled for UI layers to be drawn to viewports and viewport settings must be consistent between rooms for UI layers to behave the same. See: [Cameras And Viewports](Room_Properties.md#h), [view\_enabled](../../GameMaker_Language/GML_Reference/Cameras_And_Display/Cameras_And_Viewports/view_enabled.md), [view\_visible](../../GameMaker_Language/GML_Reference/Cameras_And_Display/Cameras_And_Viewports/view_visible.md)

A UI layer also contains the following flex properties:

[UI Layer Flex Properties](#)

### Direction

The flex direction, i.e. in which direction the child items should be laid out. "**Column**" displays them from top\-to\-bottom, "**Row**" displays them from left\-to\-right, and there are reverse options.

The direction set becomes the **main axis** for alignment and the axis perpendicular to it becomes the **cross axis**.

### Align Items

This controls how the non\-absolute children of a container are aligned along its **cross axis** (i.e. the direction perpendicular to the flex direction). You can stretch the children to fit the size of the cross axis, or align them to the start, end or centre.

In the example image below, the direction is set to **column**.

### Justify Content

This controls how the non\-absolute children of a flex container are aligned along its **main axis** (i.e. the flex direction). You can align them to the start, end or centre, or align them from start to end with various spacing options.

In the example image below, the direction is set to **column**.

### Layout Direction

The layout direction of this panel and its children. You can choose to inherit from the parent container or choose between Left to Right and Right to Left.

This setting determines which sides "Flex Start" and "Flex End" correspond to (e.g., when using Left to Right, "Flex Start" is the left side).

### Wrap

This controls what happens when children in the container have overflown on the main axis. You can enable wrapping on the cross axis in case of overflow.

### Align Content

If wrapping is enabled, any items overflowing along the main axis will be laid out across new lines on the cross axis. This property controls how all lines are distributed along the cross axis, overriding the setting set for "Align Items".

### Spacing

This lets you set the margin and padding for the panel (margin will not be available for UI layers). Clicking on any side in the border preview will allow you to edit its size, allowing you to also set all sides at once using the  button. You can also set the horizontal and vertical gap used by the children of the container.

Margin and padding can also be modified in the Room canvas. See: [Canvas Editing](UI_Layers.md#h2)

The above flex properties are also present in Flex Panels.

## Flex Panel Properties

A Flex Panel contains flex and spacing properties, which are the same as described in the previous section for "**UI Layer Flex Properties**".

In addition to that, Flex Panels show these extra properties:

[Flex Panel Properties](#)

### Size

The width and height of the panel. You can set the units to either pixels, percentage of the [Containing Block](../../GameMaker_Language/GML_Reference/Flex_Panels/Flex_Panels.md#h) or automatic, which allows the panel to be automatically resized based on its contents (e.g. size of a Sprite placed inside it).

The size can be modified in the Room canvas if the units are set to pixels or percentage.

  If the size of a Flex Panel is set to "Auto" and it contains Asset Elements as well as other Flex Panels inside it, the Asset Elements are ignored when the size of the panel is calculated and only the Flex Panels contribute to the size.

### Min/Max Size

Set the minimum and maximum size of the panel in either pixels or a percentage.

### Grow/Shrink

The grow and shrink values determine how a panel is sized in a container in relation to its siblings. A higher grow value will allow it to be larger in relation to other growing/shrinking panels in its container, and a higher shrink value will make it smaller.

### Clip Contents

Enable this to clip drawing any contents under this container that exceed its current size. This is useful for windows that may contain more items that it can display at once

### Position

Set the position type of the panel:

- **Relative (default)**: This panel will participate in the flow of its parent container and will take up space in it. Offsets will be relative to the panel's position within the flow.
- **Absolute**: This panel is removed from the flow of its parent and will not take up space. Offsets will be relative to the [Containing Block](../../GameMaker_Language/GML_Reference/Flex_Panels/Flex_Panels.md#h) which may not be its direct parent.
- **Static**: The panel will behave like relative except it will ignore offsets and will not form a [Containing Block](../../GameMaker_Language/GML_Reference/Flex_Panels/Flex_Panels.md#h) for its children.

Only **Absolute** panels can be moved using the mouse in the Room canvas.

Changing the position type of an **Absolute** panel to **Relative** or **Static** will reset its offset values.

### Align Self

This controls how this panel is aligned within its container on its cross\-axis. This is a way of overriding the "**Align Items**" property set for the parent but only for this individual panel.

### Offset

Set the offset for this panel from its left, right, top and bottom edges.

## Asset Element Properties

For elements of all asset types, you can change the alignment, set the anchor for rotation, change the position, scale, rotation, colour, frame and animation speed..

### Fill Container

The "**Fill Container**" settings allow the element to be stretched to fit its containing Flex Panel either on one of the axes or both axes. You can choose whether to maintain aspect ratio or not.

These settings can be set to stretch and maintain aspect ratio by default through the [Preferences](../../Setting_Up_And_Version_Information/IDE_Preferences/Room_Editor_Preferences.md).

### Extra Options

You will see some extra options based on the asset type:

- **Sprites**: You can choose to tile the sprite horizontally, vertically or in both directions.
- **Objects**: You can modify the Variable Definitions of the instance and apply Creation Code.
- **Text (Fonts)**: You can set text properties such as alignment, various spacing values and wrapping

You can also double\-click on an Asset Element in the Room Canvas to open its properties window.
