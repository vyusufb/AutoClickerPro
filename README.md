# 👁️ AutoClicker Pro v5.0 - Gelişmiş Masaüstü Otomasyonu

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![MSS](https://img.shields.io/badge/MSS-Screen%20Capture-orange?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-gray?style=for-the-badge)

**AutoClicker Pro**, bilgisayar ekranını sürekli izleyerek önceden tanımlanmış butonları (Örn: *"Continue"*, *"Next"*, *"Skip"*) görüntü işleme teknolojisi ile algılayan ve otomatik tıklayan profesyonel bir otomasyon aracıdır.

Standart makrolardan farklı olarak; koordinata değil **görüntüye** odaklanır. Bu sayede **Sanal Makineler (VM)**, **Çoklu Monitör Sistemleri** ve **Dinamik Pencereler** üzerinde sorunsuz çalışır.

---

## 🚀 Öne Çıkan Özellikler

* **🖥️ MSS Teknolojisi:** `pyautogui` yerine `mss` kütüphanesi kullanılarak çoklu monitörlerde ve yüksek DPI ekranlarda ultra hızlı ekran yakalama sağlanır.
* **☁️ Sanal Makine (VM) Modu:** VMware veya VirtualBox gibi sanal makinelerdeki renk farklılıklarını ve bulanıklığı tolere eden özel "Confidence" (Güven) algoritması içerir.
* **📸 Görsel Hata Ayıklama (Visual Debug):** Programın nereye tıkladığını veya neyi buton sandığını anlamanız için, algılanan nesnenin etrafına **Kırmızı Kare** çizer ve kaydeder (`debug_found_target.png`).
* **🛡️ Siyah Ekran Koruması:** Tarayıcıların donanım hızlandırma kaynaklı siyah ekran (black screen) sorunlarını aşar.
* **🖱️ Akıllı Mouse Hareketi:** Tıklama işleminden sonra mouse imlecini milisaniyeler içinde eski konumuna geri getirir, iş akışınızı bozmaz.
* **📝 Aktivite Loglama:** Tıklama zamanlarını ve başarı oranlarını `activity_log.txt` dosyasına kaydeder.

---

## 📂 Proje Klasör Yapısı

Programın hatasız çalışması için aşağıdaki dosya yapısını koruyun:

```text
AutoClickerPro/
│
├── main.py                  # Ana kaynak kod (v5.0 - MSS Entegreli)
├── requirements.txt         # (Opsiyonel) Gerekli kütüphane listesi
├── assets/                  # ⚠️ Hedef resimlerin koyulacağı klasör
│   ├── continue.png         # Örnek buton resmi
│   ├── next.png             # Örnek buton resmi
│   └── play.png             # Örnek buton resmi
├── activity_log.txt         # (Otomatik oluşur) Log kayıtları
├── debug_found_target.png   # (Otomatik oluşur) Başarılı tespit görseli
├── debug_final_check.png    # (Otomatik oluşur) Monitör kontrol görseli
└── README.md                # Proje dokümantasyonu
