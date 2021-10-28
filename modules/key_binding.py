import bpy

addon_keymaps = []

def key_map(operator, key, hold):
    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.new(name='Object Mode', space_type='EMPTY')
    kmi = km.keymap_items.new(operator.bl_idname, key, 'PRESS', ctrl=(hold == "ctrl"), shift=(hold == "shift"))
    addon_keymaps.append((km, kmi))   

def remove_key_map():
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()