from utils.splitter import split_audio
from utils.midi_converter import audio_to_midi
from utils.remaker import render_midi_to_audio
from utils.audio_utils import mix_tracks
import os

def main():
    audio_path = input("Ruta del audio: ").strip()
    stems_dir = "output/stems"
    midi_dir = "output/midi"
    output_path = "output/remake.wav"

    print("Separando audio en pistas...")
    split_audio(audio_path, stems_dir)

    print("Convirtiendo cada pista a MIDI...")
    midi_files = audio_to_midi(stems_dir, midi_dir)

    print("Generando audio con SoundFont...")
    audio_tracks = render_midi_to_audio(midi_files)

    print("Mezclando pistas generadas...")
    mix_tracks(audio_tracks, output_path)

    print(f"Remake final guardado en: {output_path}")

if __name__ == "__main__":
    main()
