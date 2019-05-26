import win32con
import win32gui
import time

while True:
    QQWin = win32gui.FindWindow("TXGuiFoundation", "QQ")
    win32gui.ShowWindow(QQWin, win32con.SW_HIDE)
    time.sleep(2)
    win32gui.ShowWindow(QQWin, win32con.SW_SHOW)
    time.sleep(2)
