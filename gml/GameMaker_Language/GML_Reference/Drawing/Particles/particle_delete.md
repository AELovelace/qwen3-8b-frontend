# particle\_delete

This function deletes a particle system asset, freeing the memory used by it.

The function can delete both particle system assets created at runtime using [particle\_add](particle_add.md) and assets created in the IDE. Deleting a particle system asset created at runtime also destroys the particle types owned by it.

 

#### Syntax:

particle\_delete(ind)

| Argument | Type | Description |
| --- | --- | --- |
| ind | [Particle System Asset](../../../../The_Asset_Editors/Particle_Systems.md) | The particle system asset to delete |

 

#### Returns:

N/A

 

#### Example:
