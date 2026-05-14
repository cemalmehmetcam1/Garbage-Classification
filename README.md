# 🌍 Akıllı Atık Sınıflandırma Sistemi (Smart Waste Classification)

Bu proje, sürdürülebilir bir gelecek ve geri dönüşüm süreçlerini optimize etmek amacıyla geliştirilmiş, Yapay Zeka tabanlı bir **Görüntü Sınıflandırma (Image Classification)** sistemidir. Derin öğrenme algoritmalarını kullanarak nesnelerin hangi atık kategorisine (Plastik, Cam, Kağıt, Metal vb.) ait olduğunu gerçek zamanlı olarak tespit eder.

## 🚀 Projenin Özellikleri
- **YOLOv8 mimarisi:** Son teknoloji nesne tanıma ve sınıflandırma modeli kullanılmıştır.
- **48.000+ Görsel:** Model, geniş kapsamlı bir veri seti ile eğitilerek yüksek doğruluk oranına (Accuracy) ulaşmıştır.
- **Web Arayüzü:** Gradio kütüphanesi ile kullanıcı dostu, tarayıcı tabanlı bir kontrol paneli eklenmiştir.
- **Çift Giriş Desteği:** İster bilgisayardan fotoğraf yükleyerek, ister **canlı webcam** görüntüsü ile anlık analiz yapılabilir.

## 🛠️ Kullanılan Teknolojiler
- **Python 3.9+**
- **Ultralytics YOLOv8** (Model mimarisi)
- **Gradio** (Web UI framework)
- **Google Colab** (Model eğitim ortamı - T4 GPU)
- **Roboflow** (Veri seti yönetimi)

## 💻 Kurulum ve Çalıştırma

### 1. Proje Dosyalarını Hazırlama
Öncelikle bir terminal açın ve proje klasörüne gidin:
```bash
cd Final_Projesi_Atik_Siniflandirma
