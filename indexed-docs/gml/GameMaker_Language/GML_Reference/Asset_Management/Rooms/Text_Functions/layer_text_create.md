# layer\_text\_create

This function creates a new Text Element in a room layer, and returns its element ID.

The function will return \-1 if the given layer does not exist.

 

#### Syntax:

layer\_text\_create(layer\_name\_or\_id, x, y, font, text)

| Argument | Type | Description |
| --- | --- | --- |
| layer\_name\_or\_id | [String](../../../../GML_Overview/Data_Types.md) or [Layer](../General_Layer_Functions/layer_get_id.md) | The layer where you want to create the element. |
| x | [Real](../../../../GML_Overview/Data_Types.md) | The X position in the room where the text element should be created. Note that the actual X position where the text appears will be negatively offset by its [xorigin](layer_text_xorigin.md) value. |
| y | [Real](../../../../GML_Overview/Data_Types.md) | The Y position in the room where the text element should be created. Note that the actual Y position where the text appears will be negatively offset by its [yorigin](layer_text_yorigin.md) value. |
| font | [Font Asset](../../../../../The_Asset_Editors/Fonts.md) | The font asset to use for rendering the text. |
| text | [String](../../../../GML_Overview/Data_Types.md) | The actual text string that appears on this element. |

 

#### Returns:

[Text Element ID](layer_text_get_id.md)

 

#### Example:

text \= layer\_text\_create("Assets", x, y, Font1, "Place the key here.");

This creates a new Text Element in the Assets layer, at the instance's position, using the Font1 font asset.
