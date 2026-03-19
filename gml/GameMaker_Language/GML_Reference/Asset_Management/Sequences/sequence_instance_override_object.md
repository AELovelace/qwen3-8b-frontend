# sequence\_instance\_override\_object

With this function you can override (replace) all instances of an object used in a sequence with another object or only the first instance of the given object with a given instance.

You supply the sequence instance struct (as returned when the sequence instance was created in the room or by using one of the room layer functions \- see [Sequence Elements](../Rooms/Sequence_Layers/Sequence_Layers.md)) as well as the object index for the object that you want to override (as defined in the Asset Browser). Finally you give an object index or an instance ID to use as the object (or single instance) that is going to override the sequence. Note that this can only be done on sequence instances (not sequence objects) and must be done before the sequence starts to play, otherwise it won't work.

  If you use this function with a sequence instance that has multiple object tracks of the same object asset and you provide an instance ID as the third argument then only the first instance of the object is replaced with the given instance. The other object tracks will not get an instance.

  If you provide an existing instance ID, the instance will stay on the layer it is already on, however its drawing will be taken over by the Sequence and it will be drawn at the Sequence's depth. To disable this and return the instance's drawing control back to it, set the instance's [drawn\_by\_sequence](drawn_by_sequence.md) variable to false.

#### Syntax:

sequence\_instance\_override\_object(sequence\_instance\_struct, object\_id, instance\_or\_object\_id)

| Argument | Type | Description |
| --- | --- | --- |
| sequence\_instance\_struct | [Sequence Instance Struct](Sequence_Structs/The_Sequence_Instance_Struct.md) | The sequence instance struct to modify |
| object\_id | [Object Asset](../../../../The_Asset_Editors/Objects.md) | The object index of the object within the sequence to override |
| instance\_or\_object\_id | [Object Asset](../../../../The_Asset_Editors/Objects.md) or [Object Instance](../Instances/Instance_Variables/id.md) | The object index or instance ID to use to override the sequence objects |

 

#### Returns:

N/A

 

#### Example 1: Replace an object ID with another object ID

var \_seq \= layer\_sequence\_create("Background", 0, 0, seq\_animated\_background);  

 var \_seq\_inst \= layer\_sequence\_get\_instance(\_seq);  

sequence\_instance\_override\_object(\_seq\_inst, obj\_trees\_winter, obj\_trees\_summer);
 

The above code creates a new sequence instance on the given layer and then modifies it so that all instances of the object obj\_trees\_winter are replaced by instances of the object obj\_trees\_summer.

#### Example 2: Replace the first instance of an object ID with an instance ID

var \_seq \= layer\_sequence\_create("Background", 0, 0, seq\_animated\_background);  

 var \_seq\_inst \= layer\_sequence\_get\_instance(\_seq);  

 var \_inst \= instance\_find(obj\_tree\_christmas, 0\);  

 if (\_inst !\= noone)  

 {  

     sequence\_instance\_override\_object(\_seq\_inst, obj\_trees\_winter, \_inst);  

 }

The above code creates a new sequence instance on the "Background" layer. It then tries to find an instance of obj\_tree\_christmas using [instance\_find](../Instances/instance_find.md). If an instance of this object is found, that instance replaces the first instance of object obj\_trees\_winter in the sequence by this instance using sequence\_instance\_override\_object. All other object tracks with obj\_trees\_winter as the object will *not* have an instance.
