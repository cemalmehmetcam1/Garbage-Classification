import gradio as gr
from ultralytics import YOLO
from PIL import Image

# 1. Eğittiğimiz modeli yüklüyoruz (best.pt dosyası kodla aynı klasörde olmalı)
model = YOLO('best.pt')

# 2. Tahmin işlemini yapacak fonksiyon
def atik_tahmin_et(image):
    results = model.predict(source=image)
    
    # En yüksek ihtimalli sonucu çekiyoruz
    tahmin = results[0].names[results[0].probs.top1]
    oran = float(results[0].probs.top1conf) * 100
    
    return f"♻️ Tahmin Edilen Sınıf: {tahmin.upper()}\n🎯 Başarı Oranı: %{oran:.2f}"

# 3. Hocanın göreceği şık web arayüzünü tasarlıyoruz
arayuz = gr.Interface(
    fn=atik_tahmin_et,
    inputs=gr.Image(type="pil", label="Çöp/Atık Fotoğrafı Yükle"),
    outputs=gr.Textbox(label="Yapay Zeka Analiz Sonucu"),
    title="🌍 Akıllı Atık Sınıflandırma Sistemi",
    description="YOLOv8 Sınıflandırma (Classification) Modeli. \nLütfen analiz etmek istediğiniz atık fotoğrafını yükleyin.",
    theme="default"
)

# 4. Uygulamayı localde başlat
if __name__ == "__main__":
    arayuz.launch()