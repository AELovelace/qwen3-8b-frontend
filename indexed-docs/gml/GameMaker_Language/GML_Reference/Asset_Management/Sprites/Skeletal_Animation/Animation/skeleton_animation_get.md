# skeleton\_animation\_get

With this function you can get the current animation set being used by your skeletal animation sprite. The return value is a string, which will be the name of the set as you defined it in your skeletal animation program.

 

#### Syntax:

skeleton\_animation\_get()

 

#### Returns:

[String](../../../../../GML_Overview/Data_Types.md)

 

#### Example:

if (keyboard\_check\_pressed(vk\_space))  

 {  

     if (skeleton\_animation\_get() !\= "jump")  

     {  

         skeleton\_animation\_set("jump");  

     }  

 }

The above code will change the animation set being used to the "jump" set when the space key is pressed, but only if the current set being used is not already "jump".
