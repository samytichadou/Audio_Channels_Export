import bpy
import os

addon_name = os.path.basename(os.path.dirname(__file__))

class AudioChannelsExportPrefs(bpy.types.AddonPreferences) :
    bl_idname = addon_name
    
    debug_toggle : bpy.props.BoolProperty(name = "Debug")

    def draw(self, context) :
        layout = self.layout
        
        layout.prop(self, 'debug_toggle')       

# get addon preferences
def get_addon_preferences():
    addon = bpy.context.preferences.addons.get(addon_name)
    return getattr(addon, "preferences", None)