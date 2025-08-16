# matrix_screensaver
a screensaver for windows
![駭客任務亂碼雨](images/matrix_rain.png)


使用方法

打包 & 變成 .scr

先安裝 PyInstaller：

pip install pyinstaller


打包：

pyinstaller --onefile --noconsole matrix_screensaver.py


打包後到 dist 資料夾找到 matrix_screensaver.exe，改名成：

matrix_screensaver.scr


把它放到：

C:\Windows\System32


到 Windows 螢幕保護程式設定裡就能看到它。
