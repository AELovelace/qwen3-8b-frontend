# draw\_primitive\_end

This function ends the definition of a primitive and effectively draws it.

If you do not call this function, *nothing will be drawn* as this effectively tells GameMaker that you have finished and that it can now draw the defined primitive.

 

#### Syntax:

draw\_primitive\_end()

 

#### Returns:

N/A

 

#### Example:

draw\_set\_colour(c\_white);  

 var \_tex \= sprite\_get\_texture(spr\_background, 0\);  

 draw\_primitive\_begin\_texture(pr\_trianglestrip, \_tex);  

 draw\_vertex\_texture(0, 0, 0, 0\);  

 draw\_vertex\_texture(640, 0, 1, 0\);  

 draw\_vertex\_texture(0, 480, 0, 1\);  

 draw\_vertex\_texture(640, 480, 1, 1\);  

 draw\_primitive\_end();

The above code will draw a 4 vertex triangle strip textured with the texture held in the \_tex variable.
