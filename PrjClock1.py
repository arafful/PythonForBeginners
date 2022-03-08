"""
    Relógio
"""
import winsound           # Biblioteca de sons
import datetime
import time
from tkinter import *


def clock_alarm(timer_set_up):
    while True:
        time.sleep(1)
        time_is_now = datetime.datetime.now()
        time_now = time_is_now.strftime("%H:%M:%S")
        date_now = time_is_now.strftime("%d/%m/%Y")
        print("Date is set to:", date_now)
        print(time_now)

        if time_now == timer_set_up:
            print("Its now time to wake up!")
            # Use um som de beep para alarme
            frequency = 440
            duration = 200
            for i in range(0, 9):
                winsound.Beep(frequency, duration)
                frequency += 440
                duration += 200

            break

# Ajusta a hora atual do relógio
def clock_time():
    timer_set_up = f"{hour.get()}:{min.get()}:{sec.get()}"
    clock_alarm(timer_set_up)


# Criando a GUI do relógio
timeclock = Tk()
timeclock.title("My alarm clock")
timeclock.geometry("400x200")
settime_in = Label(timeclock, text="24 Hour Format", fg="blue", bg="white", font="Georgia").place(x=60, y=120)
settime = Label(timeclock, text="Hour: Min: Sec: ", font=60).place(x=110)
setalarm = Label(timeclock, text="Wake up at: ", fg="blue", relief="solid",
                 font=("Georgia", 7, "bold")).place(x=0, y=29)
hour = StringVar()
min = StringVar()
sec = StringVar()

# Entre a hora
enter_hour = Entry(timeclock, textvariable=hour, bg="pink", width=15).place(x=110, y=30)
enter_minute = Entry(timeclock, textvariable=min, bg="pink", width=15).place(x=150, y=30)
enter_hour = Entry(timeclock, textvariable=sec, bg="pink", width=15).place(x=200, y=30)

# Para receber a hora do usuário
accept_time = Button(timeclock, text="Set Alarm", fg="red", width=10, command=clock_time).place(x=110, y=70)

timeclock.mainloop()






