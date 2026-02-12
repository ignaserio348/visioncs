import cv2
import os
import time

print("🎮 EXTRACTOR CS 1.6 - VERSIÓN MEJORADA")
print("="*50)

# Crear carpeta
os.makedirs("fotos", exist_ok=True)

# Abrir video
video = cv2.VideoCapture("video2.mp4")

if not video.isOpened():
    print("❌ ERROR: No se pudo abrir video.mp4")
    exit()

# Obtener fps del video
fps = int(video.get(cv2.CAP_PROP_FPS))
print(f"🎬 Video: {fps} fps")

# Configuración
segundos_entre_fotos = 2  # Cambia este número
frames_entre_fotos = fps * segundos_entre_fotos

contador = 0
fotos = 0
fotos_totales = 200  # Vamos por 200 fotos

print(f"⏱️  Guardando 1 foto cada {segundos_entre_fotos} segundos")
print(f"🎯 Objetivo: {fotos_totales} fotos")
print("="*50)

while True:
    ok, frame = video.read()
    if not ok:
        break
    
    # Guardar cada X frames
    if contador % frames_entre_fotos == 0:
        nombre = f"fotos/cs_{fotos:03d}.jpg"
        cv2.imwrite(nombre, frame)
        print(f"✅ [{fotos + 1}/{fotos_totales}] Guardada: {nombre}")
        fotos += 1
    
    contador += 1
    
    # Parar cuando tengamos todas
    if fotos >= fotos_totales:
        break

video.release()
print("="*50)
print(f"🎯 ¡COMPLETADO! {fotos} fotos guardadas")
print(f"📁 Carpeta: /fotos")
print(f"⏱️  1 foto cada {segundos_entre_fotos} segundos")