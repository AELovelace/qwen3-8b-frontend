# gpu\_get\_tex\_max\_aniso

With this function you can get the current maximum level of anisotropy when using the tf\_anisotropic filter mode (see [gpu\_get\_tex\_mip\_filter()](gpu_get_tex_mip_filter.md) for more information). The returned value will range between 1 and 16\.

 

#### Syntax:

gpu\_get\_tex\_max\_aniso()

 

#### Returns:

 (default: 16\)

 

#### Example:

if (gpu\_get\_tex\_max\_aniso() !\= 8\)   

 {  

     gpu\_set\_tex\_max\_aniso(8\);  

 }

The above code will check the current maximum anisotropic filtering level and if it is not 8 it is set to 8\.
