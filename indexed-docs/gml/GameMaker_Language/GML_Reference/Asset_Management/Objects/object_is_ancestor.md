# object\_is\_ancestor

This function can be used to check an object and see if it is an ancestor or not of another object. So, both arguments need to be object indices and *not* the instance ids, and the first one is always the object that you want to find out if it is a child of the second argument, which is always the object that want to check as the ancestor (parent).

 

#### Syntax:

object\_is\_ancestor(obj, par)

| Argument | Type | Description |
| --- | --- | --- |
| obj | Object Asset | The object that is being checked as the child. |
| par | Object Asset | The object that is being checked as the ancestor (parent). |

 

#### Returns:

Boolean

 

#### Example:

if (object\_is\_ancestor(object\_index, obj\_Enemy))   

 {  

     instance\_destroy();  

 }

The above code checks to see if the instance running the code is a child of the object "obj\_Enemy", and if so it is destroyed.
