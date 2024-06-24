import pyautogui
import time
import datetime

def click_at_time(hour, minute, second, millisecond=0):
    # Đợi đến thời gian định trước
    target_time = datetime.datetime.combine(datetime.date.today(), datetime.time(hour, minute, second, millisecond * 1000))
    while datetime.datetime.now() < target_time:
        time.sleep(0.1)  # Kiểm tra mỗi 0.1 giây để giảm tải CPU

    # Click vào vị trí chuột hiện tại (giả sử bạn đã đặt chuột đúng vị trí nút gửi)
    pyautogui.click()

# Ví dụ: đặt thời gian gửi tin nhắn là 10:08:00 với 900 milliseconds
click_at_time(10, 27, 0, 0)
