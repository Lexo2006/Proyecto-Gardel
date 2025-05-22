def separar_audio():
    print("Separando audio, esto puede tardar un poco...")

    # Crear el separador para dos pistas: voz y acompañamiento
    separator = Separator('spleeter:2stems')

    # Crear la carpeta output si no existe
    os.makedirs('output/audio_separado', exist_ok=True)

    # Separar el archivo
    separator.separate_to_file('song.mp3', 'output/audio_separado')

    print("Audio separado correctamente.")

# ✅ Protección para multiprocessing en Windows
if __name__ == '__main__':
    separar_audio()
