import os

print("🎮 ENTRENANDO IA - VISIÓN CS")
print("="*50)

# Crear archivo de configuración
yaml = """
path: C:/Users/usuario/Desktop/visioncs/dataset
train: images/train
val: images/val

nc: 1
names: ['player']
"""

with open("cs_dataset.yaml", "w") as f:
    f.write(yaml)
print("✅ Configuración creada: cs_dataset.yaml")

# Clonar YOLOv5 (solo la primera vez)
if not os.path.exists("yolov5"):
    print("📦 Descargando YOLOv5...")
    os.system("git clone https://github.com/ultralytics/yolov5")
    os.system("cd yolov5 && pip install -r requirements.txt")
else:
    print("✅ YOLOv5 ya está descargado")

print("="*50)
print("🎯 COMENZANDO ENTRENAMIENTO...")
print("⏱️  Esto tarda 10-30 minutos dependiendo tu PC")
print("☕ Ve por un café o haz flexiones")
print("="*50)

# Entrenar
os.system("cd yolov5 && python train.py --img 640 --batch 4 --epochs 50 --data ../cs_dataset.yaml --weights yolov5s.pt --device cpu")

print("="*50)
print("✅ ¡ENTRENAMIENTO COMPLETADO!")
print("📁 Modelo guardado en: yolov5/runs/train/exp/weights/best.pt")