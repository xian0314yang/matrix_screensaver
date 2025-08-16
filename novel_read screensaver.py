import tkinter as tk 
import random
import os
import sys

# 固定 messages.txt 放在 System32
TXT_FILE = r"C:\Windows\System32\messages.txt"

# 載入訊息
def load_messages(filename):
    if not os.path.exists(filename):
        return ["ERROR: Messages file not found in System32!"]
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()
    return [line for line in lines if line.strip()]

messages = load_messages(TXT_FILE)

FONT_SIZE = 16
CHAR_DELAY_RANGE = (10, 30)  # 打字速度慢
LINE_DELAY = 200

root = tk.Tk()
root.title("Alien Hacker Terminal Screensaver")
root.attributes("-fullscreen", True)
root.configure(bg="black")

text_widget = tk.Text(root, bg="black", fg="lime",
                      font=("Consolas", FONT_SIZE, "bold"))
text_widget.pack(fill=tk.BOTH, expand=True)
text_widget.configure(state=tk.DISABLED)

def quit_screensaver(event=None):
    root.destroy()
    sys.exit()

root.bind("<Key>", quit_screensaver)
root.bind("<Motion>", quit_screensaver)
root.bind("<Button>", quit_screensaver)

def clear_screen():
    text_widget.configure(state=tk.NORMAL)
    text_widget.delete('1.0', tk.END)
    text_widget.configure(state=tk.DISABLED)

def shake_text_widget():
    """整個 Text 控制元件明顯抖動"""
    try:
        # 取得螢幕中央位置
        screen_w = root.winfo_screenwidth()
        screen_h = root.winfo_screenheight()
        x_offset = random.randint(-10, 10)
        y_offset = random.randint(-5, 5)
        root.geometry(f"{screen_w}x{screen_h}+{x_offset}+{y_offset}")
    except:
        pass
    root.after(50, shake_text_widget)  # 更新頻率

def type_line(line, char_index=0, callback=None):
    if char_index < len(line):
        delay = random.randint(*CHAR_DELAY_RANGE)
        text_widget.configure(state=tk.NORMAL)
        text_widget.insert(tk.END, line[char_index])
        text_widget.see(tk.END)
        text_widget.configure(state=tk.DISABLED)
        root.after(delay, lambda: type_line(line, char_index + 1, callback))
    else:
        # 換行
        text_widget.configure(state=tk.NORMAL)
        text_widget.insert(tk.END, "\n")
        text_widget.configure(state=tk.DISABLED)
        if callback:
            callback()

def type_next():
    next_line = random.choice(messages)
    new_lines = [next_line]

    def type_new_lines(lines, index=0):
        if index < len(lines):
            text_widget.configure(state=tk.NORMAL)
            num_lines = int(text_widget.index('end-1c').split('.')[0])
            text_widget.configure(state=tk.DISABLED)
            max_lines = root.winfo_screenheight() // FONT_SIZE
            if num_lines >= max_lines:
                clear_screen()
            type_line(lines[index], callback=lambda: type_new_lines(lines, index + 1))
        else:
            root.after(LINE_DELAY, type_next)

    type_new_lines(new_lines)

# 啟動震動效果
shake_text_widget()
type_next()
root.mainloop()
















