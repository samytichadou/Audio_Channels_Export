import bpy

# export menu
def export_audio_channels_menu(self, context) :
    self.layout.operator('sound.export_channels', icon='FILE_SOUND')
