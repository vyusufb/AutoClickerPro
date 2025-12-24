import pyautogui
import time
import os
import sys
import mss
import mss.tools
import numpy as np
import cv2
from datetime import datetime
import ctypes


VM_CONFIDENCE = 0.85     
NORMAL_CONFIDENCE = 0.92

TARGET_IMAGES = ["continue.png", "play.png"]
CLICK_COOLDOWN = 5


def log_event(msg):
    t = datetime.now().strftime("%H:%M:%S")
    print(f"[{t}] {msg}")

def list_monitors_mss():
    print("\n--- 🖥️ MSS MONİTÖR LİSTESİ ---")
    with mss.mss() as sct:
        monitors = sct.monitors
        for i, m in enumerate(monitors):
            if i == 0: continue 
            print(f"[{i}] {m['width']}x{m['height']} (x={m['left']}, y={m['top']})")
        print("------------------------------")
        return monitors


def save_visual_debug(screen_img, top_left, bottom_right, filename="debug_found_target.png"):
    """Bulunan nesnenin etrafına kırmızı kare çizip kaydeder."""
    debug_img = screen_img.copy()
    # Kırmızı Kare Çiz (BGR formatında 0,0,255 Kırmızıdır)
    cv2.rectangle(debug_img, top_left, bottom_right, (0, 0, 255), 3)
    cv2.imwrite(filename, debug_img)
    log_event(f"⚠️ TESPİT KARESİ KAYDEDİLDİ: '{filename}' dosyasına bak!")


def start_watching(monitor_idx, confidence_level):
    if not os.path.exists("assets"):
        log_event("❌ 'assets' klasörü yok!")
        return

    templates = []
    for img_name in TARGET_IMAGES:
        path = os.path.join("assets", img_name)
        if os.path.exists(path):
            img = cv2.imread(path, 0)
            if img is not None:
                templates.append((img_name, img))
    
    if not templates:
        log_event("❌ Görsel yok.")
        return

    log_event(f"🚀 Motor Başladı. Güven Eşiği: %{int(confidence_level*100)}")
    print("Durdurmak için: Ctrl+C")

    pyautogui.FAILSAFE = False

    try:
        with mss.mss() as sct:
            while True:
                found = False
                monitor_area = sct.monitors[monitor_idx]
                
                # Ekranı al
                sct_img = sct.grab(monitor_area)
                img_np = np.array(sct_img)
                
                # Renkli kopyayı sakla 
                screen_color = cv2.cvtColor(img_np, cv2.COLOR_BGRA2BGR)
                # İşleme için gri kopya
                screen_gray = cv2.cvtColor(img_np, cv2.COLOR_BGRA2GRAY)

                for name, template in templates:
                    # Eşleştirme yap
                    res = cv2.matchTemplate(screen_gray, template, cv2.TM_CCOEFF_NORMED)
                    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

                    # EŞİK KONTROLÜ
                    if max_val >= confidence_level:
                        log_event(f"✅ BULUNDU: {name} (Güven: %{int(max_val*100)})")
                        
                        
                        match_w = template.shape[1]
                        match_h = template.shape[0]
                        top_left = max_loc
                        bottom_right = (top_left[0] + match_w, top_left[1] + match_h)
                        
                        
                        save_visual_debug(screen_color, top_left, bottom_right)
                        

                        
                        center_x = monitor_area['left'] + max_loc[0] + match_w // 2
                        center_y = monitor_area['top'] + max_loc[1] + match_h // 2
                        
                        
                        print('\a') 
                        current_mouse = pyautogui.position()
                        pyautogui.click(center_x, center_y)
                        pyautogui.moveTo(current_mouse)
                        
                        log_event("⏳ Bekleniyor...")
                        time.sleep(CLICK_COOLDOWN)
                        found = True
                        break 

                if not found:
                    time.sleep(1)

    except KeyboardInterrupt:
        log_event("🛑 Durduruldu.")
    except Exception as e:
        log_event(f"❌ HATA: {e}")

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    monitors = list_monitors_mss()
    
    try:
        sel = int(input("Hangi ekran izlenecek? [ID]: "))
    except: sys.exit()

    vm_inp = input("Sanal Makine (VM) içinde mi? (e/h): ").lower()
    
    
    if vm_inp == 'e':
        conf = VM_CONFIDENCE  
    else:
        conf = NORMAL_CONFIDENCE 

    start_watching(sel, conf)