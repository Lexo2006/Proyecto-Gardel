@echo off
SETLOCAL

echo =======================================
echo Creando entorno virtual para Magenta...
echo =======================================
python -m venv venv_magenta

echo =======================================
echo Activando entorno virtual Magenta...
echo =======================================
call venv_magenta\Scripts\activate

echo =======================================
echo Instalando dependencias para Magenta...
echo =======================================
pip install --upgrade pip
pip install magenta==2.1.3 tensorflow==2.3.0 protobuf==3.20.3 librosa==0.7.2

if %errorlevel% neq 0 (
    echo Error durante la instalación de paquetes.
    pause
    exit /b %errorlevel%
)

deactivate

pause
