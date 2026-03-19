# physics\_pause\_enable

This function sets whether the physics simulation should be paused or not.

Normally for a physics simulation to work, it must be continuous and cannot be stopped and started, or have instances suddenly moved from one place to another in the room. However, there are moments when you *need* to pause the simulation as (for example) the device OS has paused, and so you would use this function. It pauses the simulation if the flag is set to true and no further physics calculations will be done until the flag is set to false again.

  This is of particular use should you wish to deactivate all the instances in a room as even when deactivated a physical body will still continue being calculated and simulated in the physics world.

 

#### Syntax:

physics\_pause\_enable(flag)

| Argument | Type | Description |
| --- | --- | --- |
| flag | [Boolean](../../../GML_Overview/Data_Types.md) | This can be set to true to pause the simulation, or false to start it again. |

 

#### Returns:

N/A

 

#### Example:

if (os\_is\_paused())  

 {  

     physics\_pause\_enable(true);  

     instance\_deactivate\_all(true);  

     instance\_create\_layer(x, y, "Controllers", obj\_pause\_menu);  

 }

The code above checks to see if the OS has been paused and if it has then it pauses the physics world, deactivates everything except itself, and then creates a pause menu instance.
