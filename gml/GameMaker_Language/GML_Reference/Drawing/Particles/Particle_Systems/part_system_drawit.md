# part\_system\_drawit

This function draws the given particle system instance.

By default, every particle system that you create is drawn automatically by GameMaker. You can also draw it *manually* using this function.

If [part\_system\_automatic\_draw](part_system_automatic_draw.md) is switched off then this function will show the particles when used in the Draw event of an instance. It can also be used when the drawing target is set to a surface (using [surface\_set\_target](../../Surfaces/surface_set_target.md)) to draw the particles in the system to that surface.

  This function takes any transformations applied to the layer element into account. See [Particle System Elements](../../../Asset_Management/Rooms/Particle_System_Layers/Particle_System_Elements.md).

  Call this function in any of the [Draw Events](../../../../../The_Asset_Editors/Object_Properties/Draw_Events.md) to draw the particle system whenever you want. Call it in a Draw End event to draw the particles in front of other graphics or in one of the Draw GUI events to draw them on the GUI layer.

 

#### Syntax:

part\_system\_drawit(ind)

| Argument | Type | Description |
| --- | --- | --- |
| ind | [Particle System Instance](part_system_create.md) | The particle system to draw |

 

#### Returns:

N/A

 

#### Example:

if (surface\_exists(surf))  

 {  

     surface\_set\_target(surf);  

     part\_system\_drawit(global.psys);  

     surface\_reset\_target();  

 }

The above code checks to see if the surface indexed in the variable surf exists. If it does it then sets the drawing target to the surface, draws the particle system with the ID stored in the global variable, and then resets the drawing target so all normal drawing appears on the screen once more.
