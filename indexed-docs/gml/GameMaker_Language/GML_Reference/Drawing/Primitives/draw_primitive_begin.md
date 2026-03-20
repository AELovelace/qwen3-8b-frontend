# draw\_primitive\_begin

This function starts drawing a primitive of the given type (this must be called before you can define any primitives).

There are 6 types of primitives you can define as the following constants:

 
The following image illustrates basically how these should look and also the order in which you should define the vertices:

  On some platforms (Windows, Xbox) the pr\_trianglefan type is not natively supported and so GameMaker does a conversion when the game is compiled to make them work. This means that on those platforms the pr\_trianglefan type will be much slower to use than the others.

 
 

#### Syntax:

draw\_primitive\_begin(kind)

| Argument | Type | Description |
| --- | --- | --- |
| kind | [Primitive Type Constant](draw_primitive_begin.md) | The kind of primitive you are going to draw |

 

#### Returns:

N/A

 

#### Example:

var \_steps \= 20;  

 var \_xx \= 50;  

 var \_yy \= 50;  

 var \_radius \= 30;  

 draw\_primitive\_begin(pr\_trianglefan);  

 draw\_vertex(\_xx, \_yy);  

 for(var i \= 0; i \<\= \_steps; \+\+i)  

 {  

     draw\_vertex(\_xx \+ lengthdir\_x(\_radius, 270 \* i / \_steps), \_yy \+ lengthdir\_y(\_radius, 270 \* i / \_steps));  

 }  

 draw\_primitive\_end();

The above code will draw three quarters of a circle made from primitives.
