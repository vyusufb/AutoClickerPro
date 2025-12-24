# 🖱️ AutoClicker Pro - Akıllı Masaüstü Otomasyonu

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![MSS](https://img.shields.io/badge/MSS-Screen%20Capture-orange?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-gray?style=for-the-badge)

**AutoClicker Pro**, ekranınızda beliren belirli butonları (örn: *"Continue"*, *"Next"*, *"Skip"*) görüntü işleme teknolojisi kullanarak otomatik algılayan ve tıklayan gelişmiş bir Python botudur.

Özellikle **Sanal Makineler (VM)**, **Çoklu Monitör Kurulumları** ve **Online Eğitim Sistemleri** için optimize edilmiştir. Siyah ekran (Black Screen) sorunlarını ve DPI ölçekleme hatalarını aşmak için `MSS` ve `OpenCV` kullanır.

---

## 🌟 Öne Çıkan Özellikler

* ✅ **Çoklu Monitör Desteği:** Sistemdeki tüm ekranları tarar ve sadece sizin seçtiğiniz monitöre odaklanır.
* ✅ **VM (Sanal Makine) Modu:** VMware veya VirtualBox içindeki bulanık/ölçeklenmiş görüntülerde bile yüksek başarıyla çalışır.
* ✅ **Görsel Dedektif (Visual Debug):** Hatalı tıklamaları önlemek için algıladığı nesnenin etrafına **Kırmızı Kare** çizer ve kaydeder.
* ✅ **Akıllı Algılama:** `MSS` kütüphanesi sayesinde donanım hızlandırma kaynaklı siyah ekran sorunlarını aşar.
* ✅ **Güvenli Tıklama:** Tıklama sonrası mouse imlecini orijinal konumuna geri getirir, iş akışınızı bozmaz.
* ✅ **Detaylı Loglama:** Tüm aktiviteleri zaman damgasıyla dosyaya kaydeder.

---

## 📂 Proje Yapısı

```text
AutoClickerPro/
│
├── main.py                  # Ana otomasyon motoru
├── assets/                  # Hedef görseller klasörü (PNG formatında)
│   ├── continue.png         # Örnek: Devam butonu
│   ├── next.png             # Örnek: İleri butonu
│   └── play.png             # Örnek: Oynat butonu
├── activity_log.txt         # (Otomatik) Aktivite kayıtları
├── debug_found_target.png   # (Otomatik) Görsel hata ayıklama çıktısı
└── README.md                # Proje dokümantasyonu
