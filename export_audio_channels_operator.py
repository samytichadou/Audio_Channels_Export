import bpy
import os


def check_for_audio_channel(context):

    print()
    print("starting audio channels export")
    seq = context.scene.sequence_editor

    channels = []

    for strip in seq.sequences_all:
        
        if strip.type == "SOUND" and not strip.mute:
            if strip.channel not in channels:
                channels.append(strip.channel)
    
    print("returning valid audio channels : " + str(channels))
    
    return channels


def main(self, context):
    
    #check export folder
    if not os.path.isdir(self.export_folder):
        print("export folder does not exist")
        return 
    
    seq = context.scene.sequence_editor
    
    # per channels
    for channel in self.channels:

        if self.export_name.endswith("_"):
            name = self.export_name
        else:
            name = self.export_name + "_"
            
        file = name + "channel_" + str(channel).zfill(2) + ".wav"
        export_filepath = os.path.join(self.export_folder, file)

        export_audio_channel(seq, channel, export_filepath)

    print("audio channels successfully exported")


def export_audio_channel(sequencer, channel, export_filepath):

    audio_to_unhide = []

    print()
    print("processing --- channel " + str(channel))
    print()
    
    # hide audio from different channels
    for strip in sequencer.sequences_all:
        
        if strip.channel != channel:
            
            if strip.type == "SOUND" and not strip.mute:
                
                print("hiding --- " + strip.name)
                audio_to_unhide.append(strip)
                strip.mute = True
    
    # export audio
    print()
    print("exporting --- " + export_filepath)
    bpy.ops.sound.mixdown(
        filepath=export_filepath,
        check_existing=False,
        relative_path=False, 
        container='WAV',
        codec='PCM',
        )
    print()

    # unhide audio
    for strip in audio_to_unhide:
        print("unhiding --- " + strip.name)
        strip.mute = False

    print()
    print("finished processing --- channel " + str(channel))


class ExportAudioChannelsSeparately(bpy.types.Operator):
    """Export every audio channels from sequencer to a separated audio file"""
    bl_idname = "sound.export_channels"
    bl_label = "Export Audio Channels"
    
    channels = []
    export_folder : bpy.props.StringProperty(name = "Export folder", default = r"C:\Users\tonton\Desktop\test_audio_split")
    export_name : bpy.props.StringProperty(name = "Export name")

    # channels enabled
    channel1 : bpy.props.BoolProperty(name = "Channel 1")
    channel2 : bpy.props.BoolProperty(name = "Channel 2")
    channel3 : bpy.props.BoolProperty(name = "Channel 3")
    channel4 : bpy.props.BoolProperty(name = "Channel 4")
    channel5 : bpy.props.BoolProperty(name = "Channel 5")
    channel6 : bpy.props.BoolProperty(name = "Channel 6")
    channel7 : bpy.props.BoolProperty(name = "Channel 7")
    channel8 : bpy.props.BoolProperty(name = "Channel 8")
    channel9 : bpy.props.BoolProperty(name = "Channel 9")
    channel10 : bpy.props.BoolProperty(name = "Channel 10")
    channel11 : bpy.props.BoolProperty(name = "Channel 11")
    channel12 : bpy.props.BoolProperty(name = "Channel 12")
    channel13 : bpy.props.BoolProperty(name = "Channel 13")
    channel14 : bpy.props.BoolProperty(name = "Channel 14")
    channel15 : bpy.props.BoolProperty(name = "Channel 15")
    channel16 : bpy.props.BoolProperty(name = "Channel 16")
    channel17 : bpy.props.BoolProperty(name = "Channel 17")
    channel18 : bpy.props.BoolProperty(name = "Channel 18")
    channel19 : bpy.props.BoolProperty(name = "Channel 19")
    channel20 : bpy.props.BoolProperty(name = "Channel 20")
    channel21 : bpy.props.BoolProperty(name = "Channel 21")
    channel22 : bpy.props.BoolProperty(name = "Channel 22")
    channel23 : bpy.props.BoolProperty(name = "Channel 23")
    channel24 : bpy.props.BoolProperty(name = "Channel 24")
    channel25 : bpy.props.BoolProperty(name = "Channel 25")
    channel26 : bpy.props.BoolProperty(name = "Channel 26")
    channel27 : bpy.props.BoolProperty(name = "Channel 27")
    channel28 : bpy.props.BoolProperty(name = "Channel 28")
    channel29 : bpy.props.BoolProperty(name = "Channel 29")
    channel30 : bpy.props.BoolProperty(name = "Channel 30")
    channel31 : bpy.props.BoolProperty(name = "Channel 31")
    channel32 : bpy.props.BoolProperty(name = "Channel 32")


    @classmethod
    def poll(cls, context):
        return True
    
    def invoke(self, context, event):
        self.channels = check_for_audio_channel(context)

        for channel in range(1,33):
            prop = "channel" + str(channel)
            if channel in self.channels:
                setattr(self, prop, True)
            else:
                setattr(self, prop, False)

        return context.window_manager.invoke_props_dialog(self)
    
    def draw(self, context):
        layout = self.layout
        layout.prop(self, "export_folder")
        layout.prop(self, "export_name")

        col = layout.column(align=True)
        col.label(text="Audio Channels : ")

        for channel in self.channels:
            prop = "channel" + str(channel)
            col.prop(self, prop)

    def execute(self, context):
        main(self, context)
        return {'FINISHED'}
