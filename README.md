# 👁️ AutoClicker Pro v5.0 - Gelişmiş Masaüstü Otomasyonu

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![MSS](https://img.shields.io/badge/MSS-Screen%20Capture-orange?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-gray?style=for-the-badge)

**AutoClicker Pro**, bilgisayar ekranını sürekli izleyerek önceden tanımlanmış butonları (Örn: *"Continue"*, *"Next"*, *"Skip"*) görüntü işleme teknolojisi ile algılayan ve otomatik tıklayan akıllı bir bottur.

Standart makrolardan farklı olarak; koordinata değil **görüntüye** odaklanır. Bu sayede **Sanal Makineler (VM)**, **Çoklu Monitör Sistemleri** ve **Dinamik Pencereler** üzerinde sorunsuz çalışır.

---

## 🚀 Öne Çıkan Özellikler

* **🖥️ Çoklu Monitör Desteği:** Sistemdeki tüm monitörleri (MSS teknolojisi ile) tarar ve sadece kullanıcının seçtiği ekranı izler.
* **☁️ Sanal Makine (VM) Modu:** VMware, VirtualBox gibi sanal makinelerdeki renk/render farklılıklarını ve bulanıklığı tolere eden özel algoritma içerir.
* **📸 Görsel Hata Ayıklama (Visual Debug):** Hatalı tıklamaları önlemek için algılanan nesnenin etrafına **Kırmızı Kare** çizer ve kaydeder (`debug_found_target.png`).
* **🛡️ Siyah Ekran Koruması:** `MSS` kütüphanesi sayesinde, tarayıcıların donanım hızlandırma kaynaklı siyah ekran (black screen) sorunlarını aşar.
* **🖱️ Akıllı Mouse Hareketi:** Tıklama işleminden sonra mouse imlecini milisaniyeler içinde eski konumuna geri getirir, iş akışınızı bozmaz.
* **📝 Aktivite Loglama:** Tıklama zamanlarını ve başarı oranlarını `activity_log.txt` dosyasına kaydeder.

---

## 📂 Proje Klasör Yapısı

Programın çalışması için aşağıdaki yapının korunması gerekir:

```text
AutoClickerPro/
│
├── main.py                  # Ana kaynak kod (v5.0)
├── requirements.txt         # Gerekli kütüphaneler (Opsiyonel)
├── assets/                  # ⚠️ Hedef resimlerin koyulacağı klasör
│   ├── continue.png         # Örnek buton resmi
│   ├── next.png             # Örnek buton resmi
│   └── play.png             # Örnek buton resmi
├── activity_log.txt         # (Otomatik oluşur) Log kayıtları
├── debug_found_target.png   # (Otomatik oluşur) Tespit edilen son görsel
└── README.md                # Proje dokümantasyonu
🛠️ Kurulum
1. Gereksinimleri Yükleyin
Python 3.x yüklü olduğundan emin olun. Gerekli kütüphaneleri terminal üzerinden yükleyin:

Bash

pip install pyautogui opencv-python mss numpy
2. Hedef Görselleri Hazırlayın (Kritik Adım)
Programın neye tıklayacağını bilmesi için butonların ekran görüntüsüne ihtiyacı vardır.

Proje dizininde assets adında bir klasör oluşturun.

Ekranda tıklanmasını istediğiniz buton belirdiğinde ekran görüntüsü alın (Win + Shift + S).

ÖNEMLİ: Görüntüyü kırparken sadece butonu alın, arka planı minimumda tutun.

Görseli .png formatında assets klasörüne kaydedin.

VM Notu: Eğer video bir sanal makinede çalışıyorsa, ekran görüntüsünü sanal makinenin içinden değil, Ana Bilgisayarınızdan (Host) alın.

▶️ Kullanım
Terminali (CMD veya VS Code) proje klasöründe açın ve başlatın:

Bash

python main.py
Program Akışı:
Monitör Listeleme: Program bağlı ekranları listeler (Örn: [1] 1920x1080, [2] 1536x864).

Seçim: İzlenecek monitörün numarasını girin.

VM Modu Sorgusu: "Video Sanal Makine içinde mi?" sorusuna:

e (Evet): Güven eşiği (Confidence) %85'e düşürülür.

h (Hayır): Güven eşiği %92 olarak ayarlanır.

Çalışma: Program döngüye girer. Durdurmak için terminalde Ctrl + C yapın.

⚠️ Sorun Giderme (Troubleshooting)
🔴 Sorun 1: Ekran Görüntüsü Yarım / Yanlış Yere Tıklıyor
Sebep: Windows Ölçeklendirme (DPI Scaling) ayarı. Çözüm:

Masaüstüne sağ tıkla -> Görüntü Ayarları.

İşlem yaptığınız monitörü seçin.

"Ölçek ve düzen" (Scale) ayarını %100 yapın. (%125 veya %150 ise koordinatlar kayar).

⚫ Sorun 2: Debug Resimleri Simsiyah Çıkıyor
Sebep: Donanım Hızlandırma (Hardware Acceleration) çakışması. Çözüm:

Tarayıcıda: Ayarlar > Sistem > "Kullanılabilir olduğunda grafik hızlandırmayı kullan" -> KAPALI.

VM'de: VM Ayarları > Display > "3D Acceleration" -> KAPALI.

🟡 Sorun 3: Buton Ekranda Var Ama Tıklamıyor
Çözüm:

Program çalışırken oluşan debug_found_target.png dosyasına bakın.

Eğer butonun etrafında kırmızı kare yoksa: main.py içindeki VM_CONFIDENCE değerini 0.80'e çekin.

assets klasöründeki resmi yenileyin (Çözünürlük değişmiş olabilir).

📜 Yasal Uyarı
Bu yazılım; otomasyon yeteneklerini geliştirmek, Python ve Görüntü İşleme (Computer Vision) öğrenmek amacıyla hazırlanmıştır. Kurumsal eğitim sistemlerinde, sınavlarda veya hizmet şartlarına (TOS) aykırı platformlarda kullanımdan doğabilecek her türlü sorumluluk kullanıcıya aittir.
