import pyautogui as pg
import time

spam_message = input("ข้อความของคุณ : ")
spam_repeat = int(input("คุณต้องการทำซ้ำกี่ครั้ง : "))

print("โปรดรอ 5 วินาที เตรียมตัวให้พร้อม")
time.sleep(5)

for i in range(spam_repeat):
    pg.typewrite(spam_message)
    pg.press('enter')

print("เสร็จสิ้น")