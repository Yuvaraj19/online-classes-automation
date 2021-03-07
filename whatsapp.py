import pywhatkit
import time
import mouse


def send_message(message):

    hour = int(time.asctime(time.localtime(time.time()))[11:13])
    minute = int(time.asctime(time.localtime(time.time()))[14:16]) + 1

    pywhatkit.sendwhatmsg("<Country code><Mobile Number>", message, hour, minute)
    time.sleep(3)
    mouse.move(2035, 20)
    mouse.click()
