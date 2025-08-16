import sys
import random
import tkinter as tk

# ====== 亂碼字元集 ======
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-=[]{}|;:,.<>?/"

# ====== 參數設定 ======
font_size = 20
speed = 50  # 更新速度（毫秒）

# ====== 螢幕保護程式 ======
def run_screensaver():
    root = tk.Tk()
    root.attributes("-fullscreen", True)
    root.configure(bg="black")

    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()

    canvas = tk.Canvas(root, width=width, height=height, bg="black", highlightthickness=0)
    canvas.pack()

    columns = width // font_size

    # 每列文字下落資料
    drops = []
    for i in range(columns):
        column_length = random.randint(15, 30)
        drop = []
        y = random.randint(-height//2, 0)
        for j in range(column_length):
            drop.append([y - j*font_size, random.choice(chars), 0.05 * j])
        drops.append(drop)

    # 更新函式
    def update():
        canvas.delete("all")
        for i, drop in enumerate(drops):
            new_drop = []
            for y, char, brightness in drop:
                green = int(255 * (1 - brightness))
                green = max(0, min(255, green))
                color = f'#00{green:02x}00'

                canvas.create_text(i*font_size, y, text=char, fill=color, font=("Consolas", font_size))

                y += font_size
                brightness += 0.01
                if y < height:
                    new_drop.append([y, random.choice(chars), min(brightness, 1)])
            drops[i] = new_drop

            # 如果列消失，重新生成
            if not drops[i]:
                column_length = random.randint(15, 30)
                drop = []
                y = random.randint(-height//2, 0)
                for j in range(column_length):
                    drop.append([y - j*font_size, random.choice(chars), 0.05 * j])
                drops[i] = drop

        root.after(speed, update)

    # ====== 退出事件 ======
    root.bind("<Escape>", lambda e: root.destroy())
    root.bind("<Motion>", lambda e: root.destroy())
    root.bind("<Button>", lambda e: root.destroy())

    update()
    root.mainloop()

# ====== 設定視窗（簡單提示） ======
def show_settings():
    from tkinter import messagebox
    messagebox.showinfo("設定", "這個螢幕保護程式沒有額外設定。")

# ====== 程式入口 ======
if __name__ == "__main__":
    if len(sys.argv) > 1:
        arg = sys.argv[1].lower()
        if arg == "/s":
            run_screensaver()
        elif arg == "/c":
            show_settings()
        else:
            run_screensaver()
    else:
        run_screensaver()




