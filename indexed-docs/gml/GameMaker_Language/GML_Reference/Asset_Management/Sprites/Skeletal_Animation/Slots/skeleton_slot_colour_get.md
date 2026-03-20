# skeleton\_slot\_colour\_get

With this function you can get an attachment slot colour. You supply the slot name (a string) and the function will return an integer value for the colour.

 

#### Syntax:

skeleton\_slot\_colour\_get(slot)

| Argument | Type | Description |
| --- | --- | --- |
| slot | String | The slot name to check, a string |

 

#### Returns:

Real

 

#### Example:

slot\_list \= ds\_list\_create();  

 skeleton\_find\_slot(mouse\_x, mouse\_y, slot\_list);  

 if (!ds\_list\_empty(slot\_list))   

 {  

     for (var i \= 0; i \< ds\_list\_size(slot\_list); \+\+i)  

     {  

         if skeleton\_slot\_colour\_get(slot\_list\[\| i]) !\= c\_white  

         {  

             skeleton\_slot\_colour\_set(slot\_list\[\| i], c\_white, 1\);  

         }  

     }  

 }

The above code creates a DS list and then populates it with the slot names found at the position of the mouse in the room. It then loops through the slot list and resets the colour for the found slots to white with an alpha of 1 if the colour is not already white.
