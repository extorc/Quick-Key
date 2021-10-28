import bpy
from bpy.types import Menu
from .operators import *

class QUICKY_MT_insert_loc_menu(Menu):
    bl_label = "Insert Location Keyframes"
    def draw(self, context):
        layout = self.layout

        layout.operator(QUICKKEY_OT_x_loc_insert_key_frame.bl_idname)
        layout.operator(QUICKKEY_OT_y_loc_insert_key_frame.bl_idname)
        layout.operator(QUICKKEY_OT_z_loc_insert_key_frame.bl_idname)

class QUICKY_MT_insert_rot_menu(Menu):
    bl_label = "Insert Rotation Keyframes"
    def draw(self, context):
        layout = self.layout

        layout.operator(QUICKKEY_OT_x_rot_insert_key_frame.bl_idname)
        layout.operator(QUICKKEY_OT_y_rot_insert_key_frame.bl_idname)
        layout.operator(QUICKKEY_OT_z_rot_insert_key_frame.bl_idname)

class QUICKY_MT_insert_scale_menu(Menu):
    bl_label = "Insert Scale Keyframes"
    def draw(self, context):
        layout = self.layout

        layout.operator(QUICKKEY_OT_x_scale_insert_key_frame.bl_idname)
        layout.operator(QUICKKEY_OT_y_scale_insert_key_frame.bl_idname)
        layout.operator(QUICKKEY_OT_z_scale_insert_key_frame.bl_idname)

class QUICKKEY_MT_main_menu(Menu):
    bl_label = "Main menu"
    
    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()

        col1 = pie.column()
        col1.menu_contents("QUICKY_MT_insert_loc_menu")
        col1 = pie.column()
        col1.menu_contents("QUICKY_MT_insert_rot_menu")
        col1 = pie.column()
        col1.menu_contents("QUICKY_MT_insert_scale_menu")