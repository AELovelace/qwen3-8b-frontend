# font\_get\_italic

With this function you can check any font asset to see if it has the *italic* flag or not. If it does the function will return true, otherwise it will return false.

 

#### Syntax:

font\_get\_italic(ind)

| Argument | Type | Description |
| --- | --- | --- |
| ind |  | Index of the font to check. |

 

#### Returns:

 

#### Example:

if (font\_get\_italic(fnt\_Main))   

 {  

     draw\_set\_font(fnt\_Main);  

 }

This will set the active drawing font to fnt\_Main if it is set as italic in its font properties.
