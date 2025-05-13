# Separador de Instrumentos y Predicción de Notas

Este proyecto permite separar instrumentos de una canción utilizando **Spleeter**, y luego predecir las notas de la melodía vocal utilizando **Magenta**.

## Características

- Separación de pistas (voz, acompañamiento, etc.) usando Spleeter.
- Predicción de notas MIDI con Magenta.
- Soporte para entorno virtual automatizado mediante scripts.

## Requisitos

- Python 3.8 o superior.
- ffmpeg (necesario para el funcionamiento de Spleeter).
- Git (opcional, para clonar el repositorio).

## Pasos para que funcione el proyecto

-Una vez instalado, abrir la carpeta output y pegar una canción en formato mp3
-Abrir la carpeta output y modificar el archivo test_split.py para que el nombre de la canción coincida
-Ejecutar test_split.py

## Instalación

### Opción 1: Instalación completa (Magenta + Spleeter)

Ejecuta el siguiente archivo para instalar ambos entornos virtuales y todas las dependencias necesarias:

```bash
setup_full.bat
