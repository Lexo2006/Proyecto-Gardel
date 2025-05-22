import sys
import os

# Ajusta el path para importar magenta
sys.path.append(os.path.join(os.path.dirname(__file__), 'magenta', 'magenta'))

import note_seq
from magenta.models.shared import sequence_generator_bundle
from magenta.music import midi_file_to_sequence_proto, sequence_proto_to_midi_file
from magenta.models.melody_rnn import melody_rnn_sequence_generator

def generar_acompanamiento():
    print("Generando remake del acompañamiento real...")

    # Ruta al bundle preentrenado
    BUNDLE_PATH = os.path.join('..', 'basic_rnn.mag')  # asegúrate de que esté allí

    # Cargar modelo
    bundle = sequence_generator_bundle.read_bundle_file(BUNDLE_PATH)
    generator_map = melody_rnn_sequence_generator.get_generator_map()
    generator = generator_map['basic_rnn'](checkpoint=None, bundle=bundle)
    generator.initialize()

    # Ruta al MIDI convertido desde WAV
    INPUT_MIDI_PATH = 'output/audio_separado/song/accompaniment.mid'

    # Cargar la secuencia original desde el archivo MIDI real
    input_sequence = midi_file_to_sequence_proto(INPUT_MIDI_PATH)

    # Configurar opciones de generación: generar a partir del final del archivo
    generator_options = note_seq.protobuf.generator_pb2.GeneratorOptions()
    last_note_time = max((n.end_time for n in input_sequence.notes), default=0)
    generate_section = generator_options.generate_sections.add(start_time=last_note_time, end_time=last_note_time + 16)

    # Generar nueva secuencia
    output_sequence = generator.generate(input_sequence, generator_options)

    # Crear carpeta de salida
    os.makedirs('output/accompaniment_remake', exist_ok=True)

    # Guardar como MIDI
    sequence_proto_to_midi_file(output_sequence, 'output/accompaniment_remake/remake.mid')

    print("Remake generado con éxito.")

if __name__ == '__main__':
    generar_acompanamiento()
