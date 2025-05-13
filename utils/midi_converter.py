import os
from basic_pitch.inference import predict_and_save
import torchaudio

def audio_to_midi(stems_dir, midi_out_dir):
    os.makedirs(midi_out_dir, exist_ok=True)
    midi_files = []

    for root, dirs, files in os.walk(stems_dir):
        for file in files:
            if file.endswith('.wav') and "vocals" not in file:
                input_path = os.path.join(root, file)
                output_path = os.path.join(midi_out_dir, file.replace('.wav', '.mid'))

                print(f"Convirtiendo {file} a MIDI...")
                predict_and_save([input_path], output_directory=midi_out_dir)
                midi_files.append(output_path)

    return midi_files
