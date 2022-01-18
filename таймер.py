from tkinter import *
import winsound
import math
def timer():
    global timerStart
    seconds = math.fmod(timerStart,60) # Получаем секунды
    minutes = math.fmod(timerStart/60, 60) # Получаем минуты
    hour = math.fmod(timerStart/60/60, 60) # Получаем часы
    
    # Условие если время закончилось то...
    if (timerStart <= 0):
        # Таймер удаляется
        timerStart = 0;
        # Выводит сообщение что время закончилось
        print ("Время закончилось");
        winsound.PlaySound("m1.wav", winsound.SND_ALIAS)
    else: # Иначе
        # Создаём строку с выводом времени
        timeNow = str(math.trunc(hour)) + ' : ' + str(math.trunc(minutes)) + ' : ' + str(math.trunc(seconds));
        # Выводим строку в блок для показа таймера
        time.config(text = '{}'.format(timeNow))
        timerStart = timerStart - 1
        #print (timerStart)
        root.after(1000, timer)
        
    

timerS = 1200 # Кількість хвилин
timerStart = timerS * 60 # Кількість хвилин


root = Tk() 

root.geometry("600x150")
time = Label(text = "", font = 'Arial 84')    
time.pack()
root.after(1000, timer)
root.mainloop()