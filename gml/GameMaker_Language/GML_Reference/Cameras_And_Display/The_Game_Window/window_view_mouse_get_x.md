# window\_view\_mouse\_get\_x

This function will return the mouse x position relative to the view selected.

 
 

#### Syntax:

window\_view\_mouse\_get\_x( id )

| Argument | Type | Description |
| --- | --- | --- |
| id | [Real](GameMaker_Language/GML_Overview/Data_Types.md) | The id of the view to compare the mouse position to. |

 

#### Returns:

[Real](GameMaker_Language/GML_Overview/Data_Types.md)

 

#### Example:

if (mouse\_check\_button\_pressed(mb\_left))   

 {  

     var xx, yy;  

     xx \= window\_view\_mouse\_get\_x(0\);  

     yy \= window\_view\_mouse\_get\_y(0\);  

  

     if (xx \> 0 \&\& xx \ 0 \&\& yy \< 32\)   

     {  

         b\_press\[0] \= true;  

     }  

 }
 

The above code will check for a mouse button being pressed, and if it is it then gets the mouse position relative to the view\[0] and compares it to see if a variable should be set to true.
