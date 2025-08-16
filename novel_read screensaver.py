import tkinter as tk
import random
import os
import sys

# txt 檔案路徑
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TXT_FILE = os.path.join(BASE_DIR, "messages.txt")

# 載入訊息
def load_messages(filename):
    if not os.path.exists(filename):
        return ["ERROR: Messages file not found!"]
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()
    return [line for line in lines]

messages = load_messages(TXT_FILE)

FONT_SIZE = 16
# 打字速度放慢
CHAR_DELAY_RANGE = (25, 60)   # 每個字之間延遲 (毫秒)
LINE_DELAY = 200               # 行與行間延遲 (毫秒)

root = tk.Tk()
root.title("Alien Hacker Terminal Screensaver")

# 設定全螢幕
root.attributes("-fullscreen", True)
root.configure(bg="black")

# 建立 Text 控制元件（全螢幕適配）
text_widget = tk.Text(root, bg="black", fg="lime",
                      font=("Consolas", FONT_SIZE, "bold"))
text_widget.pack(fill=tk.BOTH, expand=True)
text_widget.configure(state=tk.DISABLED)

# 退出函數
def quit_screensaver(event=None):
    root.destroy()
    sys.exit()

# 綁定按鍵和滑鼠事件
root.bind("<Key>", quit_screensaver)
root.bind("<Motion>", quit_screensaver)
root.bind("<Button>", quit_screensaver)

def clear_screen():
    text_widget.configure(state=tk.NORMAL)
    text_widget.delete('1.0', tk.END)
    text_widget.configure(state=tk.DISABLED)

def type_line(line, char_index=0, callback=None):
    if char_index < len(line):
        delay = random.randint(*CHAR_DELAY_RANGE)
        text_widget.configure(state=tk.NORMAL)
        text_widget.insert(tk.END, line[char_index])
        text_widget.see(tk.END)  # 自動滾動到底部
        text_widget.configure(state=tk.DISABLED)
        root.after(delay, lambda: type_line(line, char_index + 1, callback))
    else:
        # 在訊息後換行
        text_widget.configure(state=tk.NORMAL)
        text_widget.insert(tk.END, "\n")
        text_widget.configure(state=tk.DISABLED)
        if callback:
            callback()

def type_next():
    next_line = random.choice(messages)

    # 直接一行訊息，不加空白行
    new_lines = [next_line]

    def type_new_lines(lines, index=0):
        if index < len(lines):
            # 判斷行數超過螢幕可容納的高度時清屏
            text_widget.configure(state=tk.NORMAL)
            num_lines = int(text_widget.index('end-1c').split('.')[0])
            text_widget.configure(state=tk.DISABLED)

            # 用 root 高度估算最大行數
            max_lines = root.winfo_screenheight() // FONT_SIZE
            if num_lines >= max_lines:
                clear_screen()

            type_line(lines[index], callback=lambda: type_new_lines(lines, index + 1))
        else:
            root.after(LINE_DELAY, type_next)

    type_new_lines(new_lines)

# 開始打字
type_next()
root.mainloop()














