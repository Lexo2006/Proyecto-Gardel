from spleeter.separator import Separator
import os

def split_audio(audio_path, output_path):
    separator = Separator('spleeter:4stems')
    separator.separate_to_file(audio_path, output_path)
