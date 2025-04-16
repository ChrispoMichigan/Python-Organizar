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