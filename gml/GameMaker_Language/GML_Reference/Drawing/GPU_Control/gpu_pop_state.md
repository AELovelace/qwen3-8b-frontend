# gpu\_pop\_state

This function pops the previous GPU state from the stack and applies it. See [gpu\_push\_state()](gpu_push_state.md) for more information.

 

#### Syntax:

gpu\_pop\_state()

 

#### Returns:

 

#### Example:

gpu\_push\_state();  

 gpu\_set\_blendmode(bm\_add);  

 gpu\_set\_blendenable(false);  

 gpu\_set\_cullmode(true);  

 with (obj\_Effect\_Parent)  

 {  

     draw\_self();  

 }  

 gpu\_pop\_state();

The above code will "save" the current GPU state on the stack, then change certain GPU settings and draw a group of instances before resetting the GPU state to what it was previously.
