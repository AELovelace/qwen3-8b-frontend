# layer\_text\_get\_font

This function returns the [Font Asset](../../../../../The_Asset_Editors/Fonts.md) used by the given Text Element. This can be changed with [layer\_text\_font](layer_text_font.md).

 

#### Syntax:

layer\_text\_get\_font(text\_element\_id)

| Argument | Type | Description |
| --- | --- | --- |
| text\_element\_id | [Text Element ID](layer_text_get_id.md) | The text element ID, retrieved from [layer\_text\_create](layer_text_create.md) or [layer\_text\_get\_id](layer_text_get_id.md). |

 

#### Returns:

[Font Asset](../../../../../The_Asset_Editors/Fonts.md)

 

#### Example:

var \_text1\_id \= layer\_text\_get\_id("Assets", "text1");  

  

 var \_text1\_font \= layer\_text\_get\_font(\_text1\_id);  

  

 if (!font\_exists(\_text1\_font))  

 {  

     layer\_text\_font(\_text1\_id, Font2\);  

 }
 

This gets the ID of the Text Element text1 from the layer Assets, and then gets its font. If the font does not exist, it applies the font Font2 to the element.
