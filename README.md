<h1 align="center"> Organizador Automático de Carpetas </h1>
<p align="center">
  <img src="https://github.com/user-attachments/assets/f02d7b0b-d5d3-4363-9b06-eb4ce3d7c475" alt="logo" width="100" />
</p>

Esta herramienta es un organizador automático de archivos que clasifica los diferentes tipos de archivos en carpetas específicas, manteniendo tus directorios limpios y organizados con un solo clic.

<h2 align="center"> ¡Simplemente coloca el ejecutable en cualquier carpeta y ejecútalo! </h2>

<img alt="Static Badge" src="https://img.shields.io/badge/build-ESTABLE-green?logoColor=violet&label=STATUS">
<img alt="Static Badge" src="https://img.shields.io/badge/Abril%202025-maker?label=UPDATE&color=0000FF">
<img alt="Static Badge" src="https://img.shields.io/badge/Python-powered-yellow?logo=python&logoColor=white">

## 🚀 Descarga directa

<p align="center">
  <a href="https://github.com/ChrispoMichigan/OrganizadorCarpetas/releases/download/v1.0/organizar.exe">
    <img src="https://img.shields.io/badge/Descargar-Ejecutable-brightgreen?style=for-the-badge&logo=github" alt="Descargar Ejecutable">
  </a>
</p>

## 🌟 Características principales

- **Plug and Play**: Colócalo en cualquier carpeta y ejecútalo sin configuración.
- **Detección automática**: Identifica automáticamente su ubicación sin necesidad de configuración.
- **Organización inteligente**: Clasifica archivos según su extensión en carpetas específicas.
- **Autónomo**: No se mueve a sí mismo, quedando siempre en la ubicación original.
- **Sin dependencias**: No requiere instalación de software adicional.

## 📁 Categorías de organización

El programa organiza los archivos en las siguientes carpetas:

| Carpeta | Tipos de archivos |
|---------|------------------|
| Imagenes | .jpg, .jpeg, .png, .gif, .bmp, .avif, .webp |
| Videos | .mp4, .avi, .mkv, .mov |
| Ejecutables | .exe, .msi |
| Documentos | .pdf, .docx, .xlsx, .pptx, .txt |
| Musica | .mp3, .wav, .aac, .m4a |
| Código C | .c, .h |
| Código C++ | .cpp, .hpp |
| Archivos | .zip, .rar, .tar, .gz |
| Código EV3 | .lmsp |
| Torrents | .torrent |
| Otros | Cualquier otro tipo de archivo |

## 🛠️ Tecnologías utilizadas

- ![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)  
  Utilizado como lenguaje principal para implementar la lógica de organización.
- **PyInstaller**: Para la creación del ejecutable independiente.
- **Módulos estándar de Python**:
  - **os**: Para la manipulación de directorios y archivos.
  - **shutil**: Para mover archivos entre directorios.
  - **sys**: Para detectar la ubicación del ejecutable.

## 💻 Uso

1. **Descarga** el ejecutable desde el botón de descarga en este README.
2. **Coloca** el archivo `organizar.exe` en la carpeta que deseas organizar.
3. **Ejecuta** el programa haciendo doble clic sobre él.
4. **¡Listo!** Los archivos se organizarán automáticamente en subcarpetas.

## 🔧 Código fuente

```python
import os
import shutil
import sys

# Obtener el directorio donde se está ejecutando el script/ejecutable
if getattr(sys, 'frozen', False):
    # Si se ejecuta como ejecutable compilado
    application_path = os.path.dirname(sys.executable)
else:
    # Si se ejecuta como script
    application_path = os.path.dirname(os.path.abspath(__file__))

# Usar la ubicación del ejecutable como directorio fuente
source_dir = application_path

print(f"Organizando archivos en: {source_dir}")

dest_dirs = {
    "Imagenes": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".avif", ".webp"],
    "Videos": [".mp4", ".avi", ".mkv", ".mov"],
    "Ejecutables": [".exe", ".msi"],
    "Documentos": [".pdf", ".docx", ".xlsx", ".pptx", ".txt"],
    "Musica": [".mp3", ".wav", ".aac", ".m4a"],
    "Código C": [".c", ".h"],
    "Código C++": [".cpp", ".hpp"],
    "Archivos": [".zip", ".rar", ".tar", ".gz"],
    "Código EV3": [".lmsp"],
    "Torrents": [".torrent"],
    "Otros": []  # Para cualquier otro tipo de archivo
}

# Crear directorios de destino si no existen
for dest_dir in dest_dirs.keys():
    os.makedirs(os.path.join(source_dir, dest_dir), exist_ok=True)

# Obtener el nombre del ejecutable actual
if getattr(sys, 'frozen', False):
    # Cuando se ejecuta como ejecutable compilado
    executable_name = os.path.basename(sys.executable)
else:
    # Cuando se ejecuta como script
    executable_name = os.path.basename(__file__)

# Archivos a ignorar
ignore_files = [
    "Organizar Carpetas - Acceso directo.lnk",  # El acceso directo original
    executable_name,                            # El propio archivo ejecutándose
    "organizar.exe"                             # Nombre específico del ejecutable
]

# Organizar archivos
for filename in os.listdir(source_dir):
    # Ignorar directorios
    file_path = os.path.join(source_dir, filename)
    if not os.path.isfile(file_path):
        continue
        
    # Ignorar archivos específicos
    if filename in ignore_files:
        continue

    file_ext = os.path.splitext(filename)[1].lower()
    moved = False
    for dest_dir, extensions in dest_dirs.items():
        if file_ext in extensions:
            shutil.move(file_path, os.path.join(source_dir, dest_dir, filename))
            moved = True
            break
    if not moved:
        shutil.move(file_path, os.path.join(source_dir, "Otros", filename))

print("Archivos organizados correctamente.")
```

## 📥 Compilación del ejecutable

Si deseas compilar el ejecutable por tu cuenta:

1. Instala PyInstaller:
```bash
pip install pyinstaller
```

2. Compila el script:
```bash
pyinstaller --onefile --noconsole organizar.py
```

3. El ejecutable se generará en la carpeta `dist`.

## 👨‍💻 Desarrollador

Desarrollado por [Chrispo Michigan](https://github.com/ChrispoMichigan)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Perfil-blue?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/chrispomichigan/)

---

<p align="center">
  <i>¡Si te fue útil deja una estrella en el repositorio!</i>
</p>
