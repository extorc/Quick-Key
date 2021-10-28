# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

from os import remove
import bpy
from bpy.types import Menu, Operator
from .modules.key_binding import *
from .modules.operators import *
from .modules.menus import *

bl_info = {
    "name" : "QuickKey",
    "author" : "extorc",
    "description" : "",
    "blender" : (2, 80, 0),
    "version" : (1, 0, 0),
    "category" : "Generic"
}

classes = [
    QUICKKEY_OT_x_loc_insert_key_frame,
    QUICKKEY_OT_y_loc_insert_key_frame,
    QUICKKEY_OT_z_loc_insert_key_frame,
    QUICKKEY_OT_x_rot_insert_key_frame,
    QUICKKEY_OT_y_rot_insert_key_frame,
    QUICKKEY_OT_z_rot_insert_key_frame,
    QUICKKEY_OT_x_scale_insert_key_frame,
    QUICKKEY_OT_y_scale_insert_key_frame,
    QUICKKEY_OT_z_scale_insert_key_frame,
    QUICKKEY_MT_insert_menu_call,
    QUICKKEY_MT_main_menu,
    QUICKKEY_OT_call_menu,
    QUICKY_MT_insert_loc_menu,
    QUICKY_MT_insert_rot_menu,
    QUICKY_MT_insert_scale_menu
]

def register():
    for c in classes:
        bpy.utils.register_class(c)
    key_map(QUICKKEY_OT_call_menu,"D","ctrl")

def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)
    remove_key_map()