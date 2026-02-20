import cv2, mediapipe as mp, pyautogui, webbrowser, time, threading, os, ctypes
import numpy as np

# ===== Mediapipe Setup =====
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.7, min_tracking_confidence=0.7)

# ===== Screen & Layout =====
SCREEN_W, SCREEN_H = 1366, 768
TOP_MARGIN = 60
U = 55 
G = 6  
LEFT_START = (SCREEN_W - int(23.5 * U)) // 2

pyautogui.PAUSE = 0
pyautogui.FAILSAFE = False

# Colors (Professional HUD Theme - SOLID)
BG_COLOR       = (25, 15, 5)      
KEY_COLOR      = (50, 35, 15)     
KEY_BORDER     = (255, 200, 50)   
HOVER_COLOR    = (255, 255, 255)  
PRESS_COLOR    = (0, 140, 255)    
TEXT_COLOR     = (255, 255, 250)  
SEC_TEXT_COLOR = (220, 180, 80)   
ACCENT_COLOR   = (0, 180, 255)    
INPUT_BG       = (15, 10, 5)

SHIFT_MAP = {
    "1":"!", "2":"@", "3":"#", "4":"$", "5":"%", "6":"^", "7":"&", "8":"*", "9":"(", "0":")",
    "-":"_", "=":"+", "[":"{", "]":"}", "\\":"|", ";":":", "'":'"', ",":"<", ".":">", "/":"?", "`":"~"
}

# Optimized Full HP Keyboard Layout Config
KEYBOARD_CONFIG = [
    # Row 0
    {"label": "Esc", "code": "esc", "x": 0, "y": 0},
    {"label": "F1 Emoji", "code": "f1", "x": 1.5, "y": 0}, {"label": "F2 Br-", "code": "f2", "x": 2.5, "y": 0},
    {"label": "F3 Br+", "code": "f3", "x": 3.5, "y": 0}, {"label": "F4 Light", "code": "f4", "x": 4.5, "y": 0},
    {"label": "F5 Mute", "code": "f5", "x": 6, "y": 0}, {"label": "F6 Vol-", "code": "f6", "x": 7, "y": 0},
    {"label": "F7 Vol+", "code": "f7", "x": 8, "y": 0}, {"label": "F8 Mic", "code": "f8", "x": 9, "y": 0},
    {"label": "F9 Prev", "code": "f9", "x": 10.5, "y": 0}, {"label": "F10 Play", "code": "f10", "x": 11.5, "y": 0},
    {"label": "F11 Next", "code": "f11", "x": 12.5, "y": 0}, {"label": "F12 Hub", "code": "f12", "x": 13.5, "y": 0},
    {"label": "Del", "code": "delete", "x": 14.5, "y": 0},
    {"label": "PrtSc", "code": "prtsc", "x": 15.5, "y": 0}, {"label": "ScrLk", "code": "scrolllock", "x": 16.5, "y": 0}, 
    {"label": "Pause", "code": "pause", "x": 17.5, "y": 0}, {"label": "Pwr", "code": "sleep", "x": 18.5, "y": 0},
    # Row 1
    {"label": "~ `", "code": "`", "x": 0, "y": 1.2}, {"label": "! 1", "code": "1", "x": 1, "y": 1.2},
    {"label": "@ 2", "code": "2", "x": 2, "y": 1.2}, {"label": "# 3", "code": "3", "x": 3, "y": 1.2},
    {"label": "$ 4", "code": "4", "x": 4, "y": 1.2}, {"label": "% 5", "code": "5", "x": 5, "y": 1.2},
    {"label": "^ 6", "code": "6", "x": 6, "y": 1.2}, {"label": "& 7", "code": "7", "x": 7, "y": 1.2},
    {"label": "* 8", "code": "8", "x": 8, "y": 1.2}, {"label": "( 9", "code": "9", "x": 9, "y": 1.2},
    {"label": ") 0", "code": "0", "x": 10, "y": 1.2}, {"label": "_ -", "code": "-", "x": 11, "y": 1.2},
    {"label": "+ =", "code": "=", "x": 12, "y": 1.2}, {"label": "Back", "code": "backspace", "x": 13, "y": 1.2, "w": 2},
    {"label": "Ins", "code": "insert", "x": 15.5, "y": 1.2}, {"label": "Home", "code": "home", "x": 16.5, "y": 1.2}, {"label": "PgUp", "code": "pageup", "x": 17.5, "y": 1.2},
    # Row 2
    {"label": "Tab", "code": "tab", "x": 0, "y": 2.2, "w": 1.5}, {"label": "Q", "code": "q", "x": 1.5, "y": 2.2},
    {"label": "W", "code": "w", "x": 2.5, "y": 2.2}, {"label": "E", "code": "e", "x": 3.5, "y": 2.2},
    {"label": "R", "code": "r", "x": 4.5, "y": 2.2}, {"label": "T", "code": "t", "x": 5.5, "y": 2.2},
    {"label": "Y", "code": "y", "x": 6.5, "y": 2.2}, {"label": "U", "code": "u", "x": 7.5, "y": 2.2},
    {"label": "I", "code": "i", "x": 8.5, "y": 2.2}, {"label": "O", "code": "o", "x": 9.5, "y": 2.2},
    {"label": "P", "code": "p", "x": 10.5, "y": 2.2}, {"label": "{ [", "code": "[", "x": 11.5, "y": 2.2},
    {"label": "} ]", "code": "]", "x": 12.5, "y": 2.2}, {"label": "| \\", "code": "\\", "x": 13.5, "y": 2.2, "w": 1.5},
    {"label": "Del", "code": "delete", "x": 15.5, "y": 2.2}, {"label": "End", "code": "end", "x": 16.5, "y": 2.2}, {"label": "PgDn", "code": "pagedown", "x": 17.5, "y": 2.2},
    # Row 3
    {"label": "Caps", "code": "capslock", "x": 0, "y": 3.2, "w": 1.8}, {"label": "A", "code": "a", "x": 1.8, "y": 3.2},
    {"label": "S", "code": "s", "x": 2.8, "y": 3.2}, {"label": "D", "code": "d", "x": 3.8, "y": 3.2},
    {"label": "F", "code": "f", "x": 4.8, "y": 3.2}, {"label": "G", "code": "g", "x": 5.8, "y": 3.2},
    {"label": "H", "code": "h", "x": 6.8, "y": 3.2}, {"label": "J", "code": "j", "x": 7.8, "y": 3.2},
    {"label": "K", "code": "k", "x": 8.8, "y": 3.2}, {"label": "L", "code": "l", "x": 9.8, "y": 3.2},
    {"label": ": ;", "code": ";", "x": 10.8, "y": 3.2}, {"label": "\" '", "code": "'", "x": 11.8, "y": 3.2},
    {"label": "Enter", "code": "enter", "x": 12.8, "y": 3.2, "w": 2.2},
    # Row 4
    {"label": "Shift", "code": "shiftleft", "x": 0, "y": 4.2, "w": 2.4}, {"label": "Z", "code": "z", "x": 2.4, "y": 4.2},
    {"label": "X", "code": "x", "x": 3.4, "y": 4.2}, {"label": "C", "code": "c", "x": 4.4, "y": 4.2},
    {"label": "V", "code": "v", "x": 5.4, "y": 4.2}, {"label": "B", "code": "b", "x": 6.4, "y": 4.2},
    {"label": "N", "code": "n", "x": 7.4, "y": 4.2}, {"label": "M", "code": "m", "x": 8.4, "y": 4.2},
    {"label": "< ,", "code": ",", "x": 9.4, "y": 4.2}, {"label": "> .", "code": ".", "x": 10.4, "y": 4.2},
    {"label": "? /", "code": "/", "x": 11.4, "y": 4.2}, {"label": "Shift", "code": "shiftright", "x": 12.4, "y": 4.2, "w": 2.6},
    {"label": "Up", "code": "up", "x": 16.5, "y": 4.2},
    # Row 5
    {"label": "Ctrl", "code": "ctrlleft", "x": 0, "y": 5.2, "w": 1.25}, {"label": "Win", "code": "winleft", "x": 1.25, "y": 5.2, "w": 1},
    {"label": "Fn", "code": "fn", "x": 2.25, "y": 5.2, "w": 1},
    {"label": "Alt", "code": "altleft", "x": 3.25, "y": 5.2, "w": 1.25}, {"label": "Space", "code": "space", "x": 4.5, "y": 5.2, "w": 6.25},
    {"label": "Alt", "code": "altright", "x": 10.75, "y": 5.2, "w": 1.25}, {"label": "Menu", "code": "apps", "x": 12, "y": 5.2, "w": 1},
    {"label": "Ctrl", "code": "ctrlright", "x": 13, "y": 5.2, "w": 1.25},
    {"label": "Left", "code": "left", "x": 15.5, "y": 5.2}, {"label": "Down", "code": "down", "x": 16.5, "y": 5.2}, {"label": "Right", "code": "right", "x": 17.5, "y": 5.2},
    # Numpad
    {"label": "Num", "code": "numlock", "x": 19.5, "y": 1.2}, {"label": "/", "code": "divide", "x": 20.5, "y": 1.2},
    {"label": "*", "code": "multiply", "x": 21.5, "y": 1.2}, {"label": "-", "code": "subtract", "x": 22.5, "y": 1.2},
    {"label": "7 Home", "code": "numpad7", "x": 19.5, "y": 2.2}, {"label": "8 Up", "code": "numpad8", "x": 20.5, "y": 2.2},
    {"label": "9 PgUp", "code": "numpad9", "x": 21.5, "y": 2.2}, {"label": "+", "code": "add", "x": 22.5, "y": 2.2, "h": 2},
    {"label": "4 Left", "code": "numpad4", "x": 19.5, "y": 3.2}, {"label": "5 _", "code": "numpad5", "x": 20.5, "y": 3.2}, {"label": "6 Right", "code": "numpad6", "x": 21.5, "y": 3.2},
    {"label": "1 End", "code": "numpad1", "x": 19.5, "y": 4.2}, {"label": "2 Down", "code": "numpad2", "x": 20.5, "y": 4.2},
    {"label": "3 PgDn", "code": "numpad3", "x": 21.5, "y": 4.2}, {"label": "Ent", "code": "numpadenter", "x": 22.5, "y": 4.2, "h": 2},
    {"label": "0 Ins", "code": "numpad0", "x": 19.5, "y": 5.2, "w": 2}, {"label": ". Del", "code": "decimal", "x": 21.5, "y": 5.2},
]

# ===== State Variables =====
typed_text = ""
caret_visible = True
caret_timer = time.time()
locked_keys = set()
caps_lock, num_lock, fn_lock = False, True, False

FINGERS = [8, 12, 16, 20] 
smoothed_pos = [None] * 10
last_tap_time = [0] * 10
tap_base_y = [0] * 10
hover_start_time = [0] * 10
prev_key_per_finger = [None] * 10
mouse_hover_key = None
mouse_pressed_key_timestamp = (None, 0)

def smooth(current, previous, alpha=0.92): 
    if previous is None: return current
    return (int(alpha * current[0] + (1 - alpha) * previous[0]),
            int(alpha * current[1] + (1 - alpha) * previous[1]))

def get_key_geometry(key):
    x, y = LEFT_START + int(key['x'] * U), TOP_MARGIN + int(key['y'] * U)
    w, h = int(key.get('w', 1) * U) - G, int(key.get('h', 1) * U) - G
    return x, y, w, h

def render_keyboard_base():
    base = np.zeros((SCREEN_H, SCREEN_W, 3), dtype=np.uint8)
    base[:] = BG_COLOR
    for key in KEYBOARD_CONFIG:
        x, y, w, h = get_key_geometry(key)
        cv2.rectangle(base, (x, y), (x+w, y+h), KEY_BORDER, 2, cv2.LINE_AA)
        cv2.rectangle(base, (x+2, y+2), (x+w-2, y+h-2), KEY_COLOR, -1)
        l = 10
        cv2.line(base, (x, y), (x+l, y), KEY_BORDER, 3)
        cv2.line(base, (x, y), (x, y+l), KEY_BORDER, 3)
    return base

keyboard_base = render_keyboard_base()

def get_key_from_point(px, py):
    for key in KEYBOARD_CONFIG:
        x, y, w, h = get_key_geometry(key)
        if x <= px <= x+w and y <= py <= y+h: return key
    return None

def execute_key_action(key_obj):
    global typed_text, caps_lock, num_lock, fn_lock
    code = key_obj['code']
    
    if code == "sleep": os._exit(0); return
    if code == "fn": fn_lock = not fn_lock; return
    if code == "numlock": num_lock = not num_lock; pyautogui.press("numlock"); return

    # F-Key Media logic
    if code.startswith("f") and len(code) <= 3 and not fn_lock:
        if code == "f1": pyautogui.hotkey("win", ".")
        elif code == "f2": os.system("powershell (Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1, (Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightness).CurrentBrightness - 10)")
        elif code == "f3": os.system("powershell (Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1, (Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightness).CurrentBrightness + 10)")
        elif code == "f4": pyautogui.press("scrolllock") 
        elif code == "f5": pyautogui.press("volumemute")
        elif code == "f6": pyautogui.press("volumedown")
        elif code == "f7": pyautogui.press("volumeup")
        elif code == "f8": pyautogui.hotkey("win", "alt", "m") 
        elif code == "f9": pyautogui.press("prevtrack")
        elif code == "f10": pyautogui.press("playpause")
        elif code == "f11": pyautogui.press("nexttrack")
        elif code == "f12": os.system("start omenhub:") 
        return

    # Sticky Modifiers
    if code in ["ctrlleft", "ctrlright", "altleft", "altright", "shiftleft", "shiftright", "winleft"]:
        k = code.replace("left", "").replace("right", "")
        if code in locked_keys: locked_keys.remove(code); pyautogui.keyUp(k)
        else: locked_keys.add(code); pyautogui.keyDown(k)
        return

    # Trigger Key
    pyautogui.press(code)

    # Numpad internal
    if code.startswith("numpad"):
        if num_lock: typed_text += code[-1] if code[-1].isdigit() else ""
        else:
            k = {"numpad5":"_"}.get(code)
            if k: typed_text += k
        return

    # Normal key internal update
    if code == "capslock": caps_lock = not caps_lock
    elif code == "decimal":
        if num_lock: typed_text += "."
    elif code == "space": typed_text += " "
    elif code == "backspace": typed_text = typed_text[:-1]
    elif len(code) == 1:
        is_shift = any("shift" in k for k in locked_keys)
        char = SHIFT_MAP.get(code, code.upper()) if is_shift else code.upper() if caps_lock else code
        typed_text += char

def mouse_event(event, mx, my, flags, param):
    global mouse_hover_key, mouse_pressed_key_timestamp
    mouse_hover_key = get_key_from_point(mx, my)
    if event == cv2.EVENT_LBUTTONDOWN and mouse_hover_key:
        mouse_pressed_key_timestamp = (mouse_hover_key, time.time())
        threading.Thread(target=execute_key_action, args=(mouse_hover_key,), daemon=True).start()

cap = cv2.VideoCapture(0)
cap.set(3, SCREEN_W); cap.set(4, SCREEN_H)
WIN_NAME = "Virtual Keyboard"
cv2.namedWindow(WIN_NAME); cv2.setMouseCallback(WIN_NAME, mouse_event)

window_styled = False

while True:
    ret, frame = cap.read()
    if not ret: break
    frame = cv2.flip(frame, 1); frame = cv2.resize(frame, (SCREEN_W, SCREEN_H))
    result = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    
    display = cv2.addWeighted(keyboard_base.copy(), 0.8, frame, 0.2, 0)
    hover_keys, pressed_keys, dwell_progress = [], [], {}

    if result.multi_hand_landmarks:
        for h_idx, hand in enumerate(result.multi_hand_landmarks):
            wrist, m_base = hand.landmark[0], hand.landmark[9]
            hand_scale = np.sqrt((wrist.x - m_base.x)**2 + (wrist.y - m_base.y)**2) * SCREEN_H
            tap_threshold = max(8, int(hand_scale * 0.08))
            mp_drawing.draw_landmarks(display, hand, mp_hands.HAND_CONNECTIONS)
            for f_idx, f_id in enumerate(FINGERS):
                fi = h_idx * 4 + f_idx 
                if fi >= 8: break
                raw_pos = (int(hand.landmark[f_id].x * SCREEN_W), int(hand.landmark[f_id].y * SCREEN_H))
                smoothed_pos[fi] = smooth(raw_pos, smoothed_pos[fi])
                px, py = smoothed_pos[fi]
                key = get_key_from_point(px, py)
                if key != prev_key_per_finger[fi]:
                    tap_base_y[fi] = py; hover_start_time[fi] = time.time(); prev_key_per_finger[fi] = key
                if key:
                    code = key['code']; hover_keys.append(key); now = time.time()
                    v_dip, dwell_dur = py - tap_base_y[fi], now - hover_start_time[fi]
                    dwell_progress[code] = min(1.0, dwell_dur / 0.6)
                    if (v_dip > tap_threshold or dwell_dur > 0.6) and (now - last_tap_time[fi]) > 0.12:
                        pressed_keys.append(key); last_tap_time[fi] = now; tap_base_y[fi] = py
                        threading.Thread(target=execute_key_action, args=(key,), daemon=True).start()
                    if py < tap_base_y[fi]: tap_base_y[fi] = py

    if mouse_hover_key: hover_keys.append(mouse_hover_key)
    if mouse_pressed_key_timestamp[0] and (time.time() - mouse_pressed_key_timestamp[1] < 0.12):
        pressed_keys.append(mouse_pressed_key_timestamp[0])

    for key in KEYBOARD_CONFIG:
        x, y, w, h = get_key_geometry(key); label, code = key['label'], key['code']
        is_pressed = any(k['code'] == code for k in pressed_keys)
        is_hovered = any(k['code'] == code for k in hover_keys)
        if is_pressed: cv2.rectangle(display, (x, y), (x+w, y+h), PRESS_COLOR, -1)
        elif is_hovered:
            prog = dwell_progress.get(code, 0)
            if prog > 0: cv2.rectangle(display, (x, y+h-int(h*prog)), (x+w, y+h), (120, 120, 120), -1)
            cv2.rectangle(display, (x, y), (x+w, y+h), HOVER_COLOR, 3)
        parts = label.split()
        if len(parts) >= 2:
            cv2.putText(display, parts[1], (x+8, y+h-12), cv2.FONT_HERSHEY_SIMPLEX, 0.45, TEXT_COLOR, 2)
            cv2.putText(display, parts[0], (x+8, y+18), cv2.FONT_HERSHEY_SIMPLEX, 0.4, SEC_TEXT_COLOR, 1)
        else:
            fs = 0.5 if len(label) > 3 else 0.6
            (tw, th), _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, fs, 2)
            if tw > w - 10: fs *= (w - 10) / tw
            cv2.putText(display, label, (x+8, y+int(h*0.75)), cv2.FONT_HERSHEY_SIMPLEX, fs, TEXT_COLOR, 2 if fs > 0.4 else 1)
        if code in locked_keys or (code == "capslock" and caps_lock) or (code == "numlock" and num_lock) or (code == "fn" and fn_lock):
            cv2.circle(display, (x+w-10, y+10), 5, ACCENT_COLOR, -1)

    if time.time()-caret_timer>0.5: caret_visible, caret_timer = not caret_visible, time.time()
    cv2.rectangle(display, (0, SCREEN_H-90), (SCREEN_W, SCREEN_H), BG_COLOR, -1)
    cv2.rectangle(display, (10, SCREEN_H-80), (SCREEN_W-10, SCREEN_H-10), KEY_BORDER, 2)
    txt = typed_text[-45:] + ("|" if caret_visible else "")
    cv2.putText(display, txt, (30, SCREEN_H-35), cv2.FONT_HERSHEY_SIMPLEX, 1.2, TEXT_COLOR, 2)
    cv2.imshow(WIN_NAME, display)
    if not window_styled:
        hwnd = ctypes.windll.user32.FindWindowW(None, WIN_NAME)
        if hwnd:
            ctypes.windll.user32.SetWindowLongW(hwnd, -20, 0x08000000 | 0x00000008 | 0x00040000)
            window_styled = True
    if cv2.waitKey(1)&0xFF==ord('q'): break
cap.release(); cv2.destroyAllWindows()
