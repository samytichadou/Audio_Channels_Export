'''
Copyright (C) 2018 Samy Tichadou (tonton)
samytichadou@gmail.com

Created by Samy Tichadou

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

bl_info = {
    "name": "Audio Channels Export",
    "description": "Export Audio Channels from Sequencer separately",
    "author": "Samy Tichadou (tonton)",
    "version": (1, 0, 0),
    "blender": (2, 83, 0),
    "location": "File > Export > Export Audio Channels",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Import-Export",
}

import bpy

from .gui import export_audio_channels_menu
from .export_audio_channels_operator import ExportAudioChannelsSeparately

def register():
    bpy.utils.register_class(ExportAudioChannelsSeparately)
    bpy.types.TOPBAR_MT_file_export.append(export_audio_channels_menu)


def unregister():
    bpy.utils.unregister_class(ExportAudioChannelsSeparately)
    bpy.types.TOPBAR_MT_file_export.remove(export_audio_channels_menu)
