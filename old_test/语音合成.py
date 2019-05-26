import time
import win32com.client

#获取win32的语音接口
dehua = win32com.client.Dispatch("SAPI.SPVOICE")

while 1:
    dehua.Speak("我不管，我最帅，我是你们的小可爱")
    time.sleep(1)
