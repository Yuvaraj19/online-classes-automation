import webbrowser
import mouse
import time
import datetime
from whatsapp import send_message


erp = ""
other = ""

time_table = {
    "Monday": ["CD", "ES", "SE", "TCSS"],
    "Tuesday": ["ERP", "AI", "PP", "TCSS"],
    "Wednesday": ["AI", "ES", "ERP", "CD"],
    "Thursday": ["SE", "PP", "ES", "ERP"],
    "Friday": ["PP", "CD", "AI", "SE"]
}

day = datetime.datetime.now().strftime("%A")
day = 'Tuesday'


def join(url, subject):
    x = [1550, 1550, 1881]
    y = [750, 65, 75]

    send_message(subject + " : Class Joined")
    webbrowser.open(url)  # Open Url

    time.sleep(18)
    mouse.move(x[0], y[0])
    time.sleep(2)
    mouse.click()  # JOIN

    time.sleep(10)
    mouse.move(x[1], y[1])
    mouse.click()  # MAXIMIZE

    time.sleep(60*60)  # After 1 hour
    mouse.move(x[2], y[2])
    mouse.click()  # LEAVE

    send_message(subject + " : Class Complete")


def join_no_message(url, subject):
    x = [1550, 1550, 1881]
    y = [750, 65, 75]

    webbrowser.open(url)  # Open Url

    time.sleep(18)
    mouse.move(x[0], y[0])
    time.sleep(2)
    mouse.click()  # JOIN

    time.sleep(10)
    mouse.move(x[1], y[1])
    mouse.click()  # MAXIMIZE

    time.sleep(60*60)  # After 1 hour
    mouse.move(x[2], y[2])
    mouse.click()  # LEAVE


def start(n=-1):

    if n == -1 and day == 'Monday':
        join(other, "CD")
        join(other, "ES")

        time.sleep(2*60*60)  # 2hrs Lunch break

        join(other, "SE")
        join(other, "TCSS")

    elif n == -1 and day == 'Friday':
        join(other, "PP")
        join(other, "CD")

        time.sleep(2*60*60)  # 2hrs Lunch break

        join(other, "AI")
        join(other, "SE")
    else:

        if n == 0:
            join(erp, "ERP")
            join(other, "AI")

            time.sleep(2*60*60)  # 2hrs Lunch break

            join(other, "PP")
            join(other, "TCSS")

        elif n == 2:
            join(other, "AI")
            join(other, "ES")

            time.sleep(2*60*60)  # 2hrs Lunch break

            join(erp, "ERP")
            join(other, "CD")

        elif n == 3:
            join(other, "SE")
            join(other, "PP")

            time.sleep(2*60*60)  # 2hrs Lunch break

            join(other, "ES")
            join(erp, "ERP")


def start_no_message(n=-1):

    if n == -1 and day == 'Monday':
        join_no_message(other, "CD")
        join_no_message(other, "ES")

        time.sleep(2*60*60)  # 2hrs Lunch break

        join_no_message(other, "SE")
        join_no_message(other, "TCSS")

    elif n == -1 and day == 'Friday':
        join_no_message(other, "PP")
        join_no_message(other, "CD")

        time.sleep(2*60*60)  # 2hrs Lunch break

        join_no_message(other, "AI")
        join_no_message(other, "SE")
    else:

        if n == 0:
            join_no_message(erp, "ERP")
            join_no_message(other, "AI")

            time.sleep(2*60*60)  # 2hrs Lunch break

            join_no_message(other, "PP")
            join_no_message(other, "TCSS")

        elif n == 2:
            join_no_message(other, "AI")
            join_no_message(other, "ES")

            time.sleep(2*60*60)  # 2hrs Lunch break

            join_no_message(erp, "ERP")
            join_no_message(other, "CD")

        elif n == 3:
            join_no_message(other, "SE")
            join_no_message(other, "PP")

            time.sleep(2*60*60)  # 2hrs Lunch break

            join_no_message(other, "ES")
            join_no_message(erp, "ERP")


def Main(whatsapp):

    if whatsapp == 1:
        send_message("Date : " + str(datetime.datetime.now())
                     [0:10] + ", Day : " + day)
        if "ERP" in time_table[day]:
            start(time_table[day].index("ERP"))
        else:
            start()
    else:
        if "ERP" in time_table[day]:
            start_no_message(time_table[day].index("ERP"))
        else:
            start_no_message()
