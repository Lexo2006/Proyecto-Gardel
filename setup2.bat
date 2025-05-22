@echo off
echo [🛠️] Creando entorno virtual para WAV to MIDI...
py -3.7 -m venv venv_note_seq

echo [⏳] Activando entorno y actualizando pip...
call venv_note_seq\Scripts\activate
python -m pip install --upgrade pip

echo [⬇️] Instalando dependencias necesarias...
pip install tensorflow==1.15.5 note-seq librosa

echo [✅] Entorno 'venv_note_seq' listo para convertir WAV a MIDI.
pause
