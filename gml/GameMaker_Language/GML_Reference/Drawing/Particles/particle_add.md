# particle\_add

This function adds a new particle system asset from the given info struct and returns it.

You can either manually define an info struct with the properties that you want to set, or obtain one from an existing asset or instance using [particle\_get\_info](particle_get_info.md) or [part\_system\_get\_info](Particle_Systems/part_system_get_info.md), make changes to it and pass the resulting struct with the desired changes to this function.

An asset created using this function can be removed from memory using [particle\_delete](particle_delete.md).

### Usage Notes

The following applies to the [Particle System Info Struct](particle_get_info.md#particle_system_info_struct) that you pass to the function:

- All entries of the info struct are optional. If you leave out an entry, its default value will be used.
- All entries are checked for valid types. An error is thrown on an invalid type.
- The entries ind are ignored for both emitters and particle types. The entry name is supported only for emitters and ignored for particle systems.
- The entry parttype of emitters can be an existing [Particle Type](Particle_Types/part_type_create.md) ref, or a [Particle Type Info Struct](particle_get_info.md#particle_type_info_struct), which creates a new type with the given properties.
- Particle types created by this function are owned by the asset and will be destroyed with it.

 

#### Syntax:

particle\_add(info)

| Argument | Type | Description |
| --- | --- | --- |
| info | [Particle System Info Struct](particle_get_info.md#particle_system_info_struct) | The particle system info struct |

 

#### Returns:

[Particle System Asset](../../../../The_Asset_Editors/Particle_Systems.md)

 

#### Example 1: Basic Use

 
 

#### Example 2: Manually Created Info Struct

var \_info \=  

 {  

     emitters:  

     \[  

         {  

             mode: ps\_mode\_stream,  

             enabled: true,  

             number: 2,  

             relative: false,  

             xmin: \-10,  

             xmax: 10,  

             ymin: \-10,  

             ymax: 10,  

             distribution: ps\_distr\_invgaussian,  

             shape: ps\_shape\_rectangle,  

             parttype: {  

                 shape: pt\_shape\_flare,  

                 life\_min: 80,  

                 life\_max: 120,  

                 dir\_min: 0,  

                 dir\_max: 360,  

                 speed\_min: 1,  

                 speed\_max: 1,  

                 additive: true  

             }  

         }  

     ]  

 };  

  

 ps\_blob \= particle\_add(\_info);  

  

 ps\_instance \= part\_system\_create(ps\_blob);
 

This code shows how create a new particle system asset from an info struct defined in code. Parameters that are not specified use default values. Note that both the particle system asset and instance should be freed after use, as shown in the previous example.

 

#### Example 3: Using Existing Particle Types

Create Event

var \_info \= particle\_get\_info(ps\_asset\_from\_ide);  

 var \_type \= \_info.emitters\[0].type;  

  

 my\_custom\_type \= part\_type\_create();  

  

 ps\_custom \= particle\_add({  

     emitters:  

     \[  

         {  

             parttype: \_type  

         },  

         {  

             parttype: my\_custom\_type  

         }  

     ]  

 });
 

Clean Up Event

part\_type\_destroy(my\_custom\_type);  

 particle\_delete(ps\_custom);

The code above shows how to use existing particle types in assets created using particle\_add.

In the Create event, the info of an existing particle system asset is retrieved using [particle\_get\_info](particle_get_info.md) and the first emitter's particle type is stored in a temporary variable. After that, a custom particle type is created with [part\_type\_create](Particle_Types/part_type_create.md). A new particle system asset is then created from an info struct, where one emitter takes the first [Particle Type](Particle_Types/part_type_create.md) as the value for the parttype variable, the other takes the second type. None of the emitters takes a [Particle Type Info Struct](particle_get_info.md#particle_type_info_struct) so no new particle types are created.

In the Clean Up event, the particle type created with [part\_type\_create](Particle_Types/part_type_create.md) is manually destroyed. The other type isn't, as it was created for a particle system asset created in the Particle System Editor and might still be in use elsewhere.
