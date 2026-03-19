# path\_get\_precision

This function returns with what precision the given path has been "smoothed", and will be an integer value from 1 to 8\. Although you can get (and set) this value for a straight\-line path it will have no influence over how an instance uses the path as it is only relevant when the path kind is set to "smooth".

 

#### Syntax:

path\_get\_precision(index)

| Argument | Type | Description |
| --- | --- | --- |
| index |  | The index of the path to check. |

 

#### Returns:

 

#### Example:

if (path\_get\_kind(pth\_Patrol))  

 {  

     if (path\_get\_precision(pth\_Patrol)) !\= 8  

     {  

         path\_set\_precision(pth\_Patrol, 8\);  

     }  

 }

The above code checks the path indexed in "pth\_Patrol" to see what kind it is and if it is smooth, it then checks how precise the smoothing is. If it is less than 8, it is then set to a value of 8\.
