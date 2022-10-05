from tkinter import *
import customtkinter
import speedtest

def speed_test():
    sp = speedtest.Speedtest()
    sp.get_servers()
    down = str(round(sp.download()/(10**6), 3)) + ' Mbps'
    up = str(round(sp.upload()/10**6), 3) + ' Mbpls'
    lab_down.config(text=down)
    lab_up.conifg(text=up)

sp = Tk()
sp.title('Internet Speed Tester')
sp.geometry('500x500')
lab_down  = Label(sp, text='Download speed')
lab_down.place(x = 20, y = 20)
lab_up = Label(sp, text='Upload speed')
lab_up.place(x = 40, y = 40)
button = Button(sp, text='Check', command=speed_test)
button.place(x = 60, y = 60)
sp.mainloop()