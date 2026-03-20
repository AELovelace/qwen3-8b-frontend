# Sprite Manipulation

The functions below are all related to changing the sprite asset (resource) itself.

This means that the majority of these functions will affect *all instances, sprite elements, code, etc.* that reference the sprite being changed. It also means that you must take great care to ensure that a sprite exists before referencing it, or to make sure it is not being referenced before changing it.

## Function Reference

### Asset Properties

- [sprite\_collision\_mask](sprite_collision_mask.md)
- [sprite\_set\_offset](sprite_set_offset.md)
- [sprite\_set\_bbox\_mode](sprite_set_bbox_mode.md)
- [sprite\_set\_bbox](sprite_set_bbox.md)
- [sprite\_set\_speed](sprite_set_speed.md)
- [sprite\_set\_nineslice](sprite_set_nineslice.md)

### Creating \& Modifying Sprites

- [sprite\_add](sprite_add.md)
- [sprite\_add\_ext](sprite_add_ext.md)
- [sprite\_delete](sprite_delete.md)
- [sprite\_replace](sprite_replace.md)
- [sprite\_duplicate](sprite_duplicate.md)
- [sprite\_assign](sprite_assign.md)
- [sprite\_merge](sprite_merge.md)
- [sprite\_set\_alpha\_from\_sprite](sprite_set_alpha_from_sprite.md)
- [sprite\_nineslice\_create](sprite_nineslice_create.md)
- [sprite\_create\_from\_surface](sprite_create_from_surface.md)
- [sprite\_add\_from\_surface](sprite_add_from_surface.md)

### Saving Sprites

- [sprite\_save](sprite_save.md)
- [sprite\_save\_strip](sprite_save_strip.md)

### Blending (HTML5\)

- [sprite\_set\_cache\_size](sprite_set_cache_size.md)
- [sprite\_set\_cache\_size\_ext](sprite_set_cache_size_ext.md)

### Prefetching

- [sprite\_prefetch](sprite_prefetch.md)
- [sprite\_prefetch\_multi](sprite_prefetch_multi.md)
- [sprite\_flush](sprite_flush.md)
- [sprite\_flush\_multi](sprite_flush_multi.md)

### Vector Sprite Caching

- [vector\_sprite\_cache\_get\_limit](vector_sprite_cache_get_limit.md)
- [vector\_sprite\_cache\_get\_max\_used](vector_sprite_cache_get_max_used.md)
- [vector\_sprite\_cache\_get\_oldest\_entry\_age](vector_sprite_cache_get_oldest_entry_age.md)
- [vector\_sprite\_cache\_get\_prune\_age](vector_sprite_cache_get_prune_age.md)
- [vector\_sprite\_cache\_get\_prune\_fraction](vector_sprite_cache_get_prune_fraction.md)
- [vector\_sprite\_cache\_get\_used](vector_sprite_cache_get_used.md)
- [vector\_sprite\_cache\_limit](vector_sprite_cache_limit.md)
- [vector\_sprite\_cache\_prune\_age](vector_sprite_cache_prune_age.md)
- [vector\_sprite\_cache\_prune\_fraction](vector_sprite_cache_prune_fraction.md)
