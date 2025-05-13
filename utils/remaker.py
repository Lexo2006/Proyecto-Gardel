import os
from config import SOUNDFONT_PATH
from pydub import AudioSegment
import pyfluidsynth

def render_midi_to_audio(midi_files):
    audio_tracks = []

    for midi_file in midi_files:
        print(f"Renderizando {midi_file} con SoundFont...")
        output_wav = midi_file.replace(".mid", "_rendered.wav")

        fs = pyfluidsynth.Synth()
        fs.start(driver="file", filename=output_wav)
        sfid = fs.sfload(SOUNDFONT_PATH)
        fs.program_select(0, sfid, 0, 0)
        fs.midi_file_play(midi_file)
        fs.delete()

        audio = AudioSegment.from_wav(output_wav)
        audio_tracks.append(audio)

    return audio_tracks
