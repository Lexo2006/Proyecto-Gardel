import note_seq
import magenta
from magenta.models.shared import sequence_generator_bundle
from magenta.music.sequences_lib import concatenate_sequences
from magenta.music import sequence_proto_to_midi_file
from magenta.music import chords_lib
from magenta.models.music_rnn import music_rnn_sequence_generator
import os

def generar_acompanamiento():
    print("Generando nuevo acompañamiento con Magenta...")

    # Ruta al bundle preentrenado
    BUNDLE_PATH = 'basic_rnn.mag'  # asegúrate de tener este archivo en tu proyecto

    # Generador
    bundle = sequence_generator_bundle.read_bundle_file(BUNDLE_PATH)
    generator_map = music_rnn_sequence_generator.get_generator_map()
    generator = generator_map['basic_rnn'](checkpoint=None, bundle=bundle)
    generator.initialize()

    # Crear secuencia base con acordes simples (ejemplo)
    primer_seq = note_seq.protobuf.music_pb2.NoteSequence()
    chords_lib.add_chords_to_sequence(primer_seq, [('C', 1.0), ('Am', 1.0), ('F', 1.0), ('G', 1.0)])

    # Parámetros de generación
    generator_options = note_seq.protobuf.generator_pb2.GeneratorOptions()
    generate_section = generator_options.generate_sections.add(start_time=0, end_time=16)

    # Generar secuencia
    resultado = generator.generate(primer_seq, generator_options)

    # Guardar como MIDI
    os.makedirs('output/accompaniment_remake', exist_ok=True)
    sequence_proto_to_midi_file(resultado, 'output/accompaniment_remake/remake.mid')

    print("Remake del acompañamiento generado correctamente.")

if __name__ == '__main__':
    generar_acompanamiento()
