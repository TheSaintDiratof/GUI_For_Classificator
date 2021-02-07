from filewithfunctions import *
from tkinter import *
root = Tk()
i=1
#modpath, impath = str() мусор
def NextStep():
    global i
    if i <= 2:
        i = i+1
    Step(i)
def BackStep():
    global i
    if i >=2:
        i = i-1
    Step(i)
def Step(i):
    for a in widgetlist:
        a.pack_forget()
        a.place_forget()
    widgetlist[0].pack(side=BOTTOM, anchor=SE)
    widgetlist[1].pack(side=TOP, anchor=NE)
    widgetlist[2].pack(side=TOP, anchor=NE)
    global modpath, impath
    if i == 1:
        PageOne(widgetlist)
        widgetlist[3].pack()
    if i == 2:
        PageTwo(widgetlist)
    if i == 3:
        PageThree(widgetlist, 64, 64, 3)
frame = Frame(root, width=200, height=300, relief=RAISED, borderwidth=1)
frame.pack(side=LEFT, expand=True, fill=Y)
widgetlist = [Button(root, command=root.destroy, text="Закрыть"),
              Button(root, command=NextStep, text=" Далее  "), Button(root, command=BackStep, text="  Назад "), Label(frame),
              Label(frame), Entry(frame), Button(frame), Button(frame), Entry(frame)]
#widgetlist[2].pack(side=TOP) ежели потом не понадобится уберу
root.geometry('350x300+500+500')
Step(i)
#
#print(file) отладочная функция
root.mainloop()