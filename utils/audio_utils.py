from pydub import AudioSegment

def mix_tracks(tracks, output_path):
    if not tracks:
        raise ValueError("No hay pistas para mezclar.")

    base = tracks[0]
    for t in tracks[1:]:
        base = base.overlay(t)

    base.export(output_path, format="wav")
