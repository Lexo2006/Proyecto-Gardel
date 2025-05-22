import note_seq
import os

def wav_a_midi(input_wav, output_midi):
    print(f"Convirtiendo {input_wav} a {output_midi}...")
    sequence = note_seq.audio_to_sequence_proto(input_wav)
    note_seq.sequence_proto_to_midi_file(sequence, output_midi)
    print("✅ Conversión completa.")

if __name__ == '__main__':
    input_path = 'output/audio_separado/song/accompaniment.wav'
    output_path = 'output/audio_separado/song/accompaniment.mid'

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    wav_a_midi(input_path, output_path)
