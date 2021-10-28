import bpy
from bpy.types import Operator
        

class QUICKKEY_OT_x_loc_insert_key_frame(Operator):

    """Insert Single Keyframe on X Axis Location"""
 
    bl_label = "Location X"
    bl_idname = "quickkeymain.insert_frame_loc_x"
    bl_options = {'REGISTER','UNDO'}

    def execute(self, context):
        current_frame = bpy.data.scenes['Scene'].frame_current

        for obj in context.selected_objects:
            obj.keyframe_insert(data_path = "location",frame = current_frame, index = 0)
        context.area.tag_redraw()
        return {'FINISHED'}

class QUICKKEY_OT_y_loc_insert_key_frame(Operator):

    """Insert Single Keyframe on Y Axis Location"""
 
    bl_label = "Location Y"
    bl_idname = "quickkeymain.insert_frame_loc_y"
    bl_options = {'REGISTER','UNDO'}

    def execute(self, context):
        current_frame = bpy.data.scenes['Scene'].frame_current
        objs = context.selected_objects

        for obj in objs:
            obj.keyframe_insert(data_path = "location",frame = current_frame, index = 1)
        context.area.tag_redraw()
        return {'FINISHED'}

class QUICKKEY_OT_z_loc_insert_key_frame(Operator):

    """Insert Single Keyframe on Z Axis Location"""
 
    bl_label = "Location Z"
    bl_idname = "quickkeymain.insert_frame_loc_z"
    bl_options = {'REGISTER','UNDO'}

    def execute(self, context):
        current_frame = bpy.data.scenes['Scene'].frame_current
        objs = context.selected_objects

        for obj in objs:
            obj.keyframe_insert(data_path = "location",frame = current_frame, index = 2)
        context.area.tag_redraw()
        return {'FINISHED'}

class QUICKKEY_OT_x_rot_insert_key_frame(Operator):

    """Insert Single Keyframe on X Axis Rotation"""
 
    bl_label = "Rotation X"
    bl_idname = "quickkeymain.insert_frame_rot_x"
    bl_options = {'REGISTER','UNDO'}

    def execute(self, context):
        current_frame = bpy.data.scenes['Scene'].frame_current

        for obj in context.selected_objects:
            obj.keyframe_insert(data_path = "rotation_euler",frame = current_frame, index = 0)
        context.area.tag_redraw()
        return {'FINISHED'}

class QUICKKEY_OT_y_rot_insert_key_frame(Operator):

    """Insert Single Keyframe on Y Axis Rotation"""
 
    bl_label = "Rotation Y"
    bl_idname = "quickkeymain.insert_frame_rot_y"
    bl_options = {'REGISTER','UNDO'}

    def execute(self, context):
        current_frame = bpy.data.scenes['Scene'].frame_current
        objs = context.selected_objects

        for obj in objs:
            obj.keyframe_insert(data_path = "rotation_euler",frame = current_frame, index = 1)
        context.area.tag_redraw()
        return {'FINISHED'}

class QUICKKEY_OT_z_rot_insert_key_frame(Operator):

    """Insert Single Keyframe on Z Axis Rotation"""
 
    bl_label = "Rotation Z"
    bl_idname = "quickkeymain.insert_frame_rot_z"
    bl_options = {'REGISTER','UNDO'}

    def execute(self, context):
        current_frame = bpy.data.scenes['Scene'].frame_current
        objs = context.selected_objects

        for obj in objs:
            obj.keyframe_insert(data_path = "rotation_euler",frame = current_frame, index = 2)
        context.area.tag_redraw()
        return {'FINISHED'}

class QUICKKEY_OT_x_scale_insert_key_frame(Operator):

    """Insert Single Keyframe on X Axis Scale"""
 
    bl_label = "scale X"
    bl_idname = "quickkeymain.insert_frame_scale_x"
    bl_options = {'REGISTER','UNDO'}

    def execute(self, context):
        current_frame = bpy.data.scenes['Scene'].frame_current

        for obj in context.selected_objects:
            obj.keyframe_insert(data_path = "scale",frame = current_frame, index = 0)
        context.area.tag_redraw()
        return {'FINISHED'}

class QUICKKEY_OT_y_scale_insert_key_frame(Operator):

    """Insert Single Keyframe on Y Axis Scale"""
 
    bl_label = "scale Y"
    bl_idname = "quickkeymain.insert_frame_scale_y"
    bl_options = {'REGISTER','UNDO'}

    def execute(self, context):
        current_frame = bpy.data.scenes['Scene'].frame_current
        objs = context.selected_objects

        for obj in objs:
            obj.keyframe_insert(data_path = "scale",frame = current_frame, index = 1)
        context.area.tag_redraw()
        return {'FINISHED'}

class QUICKKEY_OT_z_scale_insert_key_frame(Operator):

    """Insert Single Keyframe on Z Axis Scale"""
 
    bl_label = "scale Z"
    bl_idname = "quickkeymain.insert_frame_scale_z"
    bl_options = {'REGISTER','UNDO'}

    def execute(self, context):
        current_frame = bpy.data.scenes['Scene'].frame_current
        objs = context.selected_objects

        for obj in objs:
            obj.keyframe_insert(data_path = "scale",frame = current_frame, index = 2)
        context.area.tag_redraw()
        return {'FINISHED'}
        
class QUICKKEY_MT_insert_menu_call(Operator):
    bl_label = "Insert Frame"
    bl_idname = "quickkeymain.insert_menu_call"
    def execute(self, context):
        bpy.ops.wm.call_menu_pie(name = "QUICKY_MT_insert_menu")
        return {'FINISHED'}


class QUICKKEY_OT_call_menu(Operator):
    bl_idname = "quickkey.main_menu_call"
    bl_label = "Main Menu Call"

    def execute(self, context):
        bpy.ops.wm.call_menu_pie(name="QUICKKEY_MT_main_menu")
        return {'FINISHED'}

