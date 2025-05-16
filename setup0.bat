@echo off
setlocal

REM ===== Crear entorno virtual para Spleeter =====
echo =======================================
echo Creando entorno virtual para Spleeter...
echo =======================================
python -m venv venv_spleeter

echo =======================================
echo Activando entorno virtual Spleeter...
echo =======================================
call venv_spleeter\Scripts\activate.bat

echo =======================================
echo Instalando dependencias para Spleeter...
echo =======================================
pip install --upgrade pip
pip install spleeter==2.1.0 tensorflow==2.3.0 librosa==0.8.0 soundfile==0.12.1 protobuf==3.20.3

deactivate

REM ===== Crear entorno virtual para Magenta =====
echo =======================================
echo Creando entorno virtual para Magenta...
echo =======================================
python -m venv venv_magenta

echo =======================================
echo Activando entorno virtual Magenta...
echo =======================================
call venv_magenta\Scripts\activate.bat

echo =======================================
echo Instalando dependencias para Magenta...
echo =======================================
pip install --upgrade pip
pip install magenta==2.1.0 protobuf==3.20.3

deactivate

echo =======================================
echo Setup finalizado correctamente.
echo =======================================

endlocal
pause
