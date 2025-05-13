@echo off
setlocal enabledelayedexpansion

:: Nombre del entorno virtual
set ENV=venv_spleeter

echo =======================================
echo Creando entorno virtual para Spleeter...
echo =======================================
python -m venv %ENV%
call %ENV%\Scripts\activate

echo Instalando dependencias para Spleeter...
pip install --upgrade pip

:: Instalación con versiones fijas
pip install spleeter==2.3.2 tensorflow==2.10.0 librosa==0.10.1 numpy==1.23.5 soundfile==0.12.1 matplotlib==3.7.1

deactivate

echo =====================================
echo Instalación completada.
echo Para activar el entorno:
echo    call %ENV%\Scripts\activate
echo =====================================
pause
