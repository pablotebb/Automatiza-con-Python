import os
import shutil
import getpass

from tkinter import Tk, filedialog
from datetime import datetime

usuario = getpass.getuser()

#Ruta donde están los archivos a ordenar

#ruta = ""  # poner aquí la ruta a ordenar (debemos cambiar los slashes de windows a /)

#Crear carpetas en destino si no existen

#tipos = ["Imágenes", "PDFs", "Videos", "Documentos_Word", "Documentos_txt"]

ventana = Tk()
ventana.withdraw()

ruta = filedialog.askdirectory(title="Seleccione la carpeta a ordenar")

extensiones = {
  ".jpg": "Imágenes",
  ".png": "Imágenes",
  ".pdf": "PDFs",
  ".mp4": "Vídeos",
  ".docx": "Documentos_Word",
  ".txt": "Documentos_txt",
}

for carpeta in set(extensiones.values()):
  
  ruta_carpeta = os.path.join(ruta, carpeta)
  
  if not os.path.exists(ruta_carpeta):
    os.makedirs(ruta_carpeta) 
    
for archivo in os.listdir(ruta):
  
  ruta_archivo = os.path.join(ruta, archivo)
  
  if os.path.isfile(ruta_archivo):
    nombre, ext = os.path.splitext(archivo)
    ext = ext.lower()
    
    if ext in extensiones:
      #destino = os.path.join(ruta, extensiones[ext], archivo)
      
      #Obtener la fecha de la última modificación 
      fecha_mod = datetime.fromtimestamp(os.path.getmtime(ruta_archivo))
      subcarpeta_fecha = fecha_mod.strftime("%Y-%m") # Formatea a "2025-04"
      
      #Crear la subcarpeta si no existe
      
      carpeta_tipo = os.path.join(ruta, extensiones[ext])
      carpeta_fecha = os.path.join(carpeta_tipo, subcarpeta_fecha)
      
      if not os.path.exists(carpeta_fecha):
        os.makedirs(carpeta_fecha)
        
      # Ruta destino final
      destino = os.path.join(carpeta_fecha, archivo)
      
      shutil.move(ruta_archivo, destino)
      
      with open(os.path.join(ruta, "log_movimientos.txt"), "a", encoding="utf-8") as log:
        log.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Usuario: {usuario} - Movido: {archivo} -> {destino}\n")
  
  
    
 