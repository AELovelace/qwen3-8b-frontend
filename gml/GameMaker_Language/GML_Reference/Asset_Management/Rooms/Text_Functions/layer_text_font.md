# layer\_text\_font

This function changes the font used by the given Text Element.

 

#### Syntax:

layer\_text\_font(text\_element\_id, font)

| Argument | Type | Description |
| --- | --- | --- |
| text\_element\_id | [Text Element ID](layer_text_get_id.md) | The text element ID, retrieved from [layer\_text\_create](layer_text_create.md) or [layer\_text\_get\_id](layer_text_get_id.md). |
| font | [Font Asset](../../../../../The_Asset_Editors/Fonts.md) | The Font to use to render the element's text. |

 

#### Returns:

N/A

 

#### Example:

var \_text1\_id \= layer\_text\_get\_id("Assets", "text1");  

  

 var \_text1\_font \= layer\_text\_get\_font(\_text1\_id);  

  

 if (!font\_exists(\_text1\_font))  

 {  

     layer\_text\_font(\_text1\_id, Font2\);  

 }
 

This gets the ID of the Text Element text1 from the layer Assets, and then gets its font. If the font does not exist, it applies the font Font2 to the element.
