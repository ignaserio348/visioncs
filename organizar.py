import os
import shutil
import random

print("🎮 ORGANIZANDO DATASET...")
print("="*40)

# Crear carpetas
os.makedirs("dataset/images/train", exist_ok=True)
os.makedirs("dataset/images/val", exist_ok=True)
os.makedirs("dataset/labels/train", exist_ok=True)
os.makedirs("dataset/labels/val", exist_ok=True)

# Obtener todas las fotos que TIENEN etiqueta .txt
fotos = []
for archivo in os.listdir("fotos"):
    if archivo.endswith(".jpg"):
        txt = archivo.replace(".jpg", ".txt")
        if os.path.exists(f"fotos/{txt}"):
            fotos.append(archivo)

print(f"📸 Fotos con etiquetas: {len(fotos)}")

# Mezclar y separar
random.shuffle(fotos)
limite = int(len(fotos) * 0.8)

train_fotos = fotos[:limite]
val_fotos = fotos[limite:]

# Copiar archivos
for foto in train_fotos:
    # Copiar imagen
    shutil.copy(f"fotos/{foto}", f"dataset/images/train/{foto}")
    # Copiar etiqueta
    txt = foto.replace(".jpg", ".txt")
    shutil.copy(f"fotos/{txt}", f"dataset/labels/train/{txt}")

for foto in val_fotos:
    shutil.copy(f"fotos/{foto}", f"dataset/images/val/{foto}")
    txt = foto.replace(".jpg", ".txt")
    shutil.copy(f"fotos/{txt}", f"dataset/labels/val/{txt}")

print("✅ Archivos copiados")
print(f"🎯 Train: {len(train_fotos)} fotos")
print(f"🎯 Val: {len(val_fotos)} fotos")
print("="*40)
print("📁 Dataset listo en /dataset")