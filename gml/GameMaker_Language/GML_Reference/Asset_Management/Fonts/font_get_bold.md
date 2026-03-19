# font\_get\_bold

With this function you can check any font asset to see if it has the **bold** flag or not. If it does the function will return true, otherwise it will return false.

 

#### Syntax:

font\_get\_bold(ind)

| Argument | Type | Description |
| --- | --- | --- |
| ind |  | Index of the font to check. |

 

#### Returns:

 

#### Example:

if (font\_get\_bold(fnt\_Main))   

 {  

     draw\_set\_font(fnt\_Main);  

 }

This will set the active drawing font to fnt\_Main if it is set as bold in its font properties.
