from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
import numpy as np
import tensorflow
import tensorflow.keras
from tensorflow.keras import models
def PageOne(widgetlist):
    widgetlist[3].configure(text="""Ета графический интерфейс
     для распознавания котиков и собак. 
     Моя задумка была такова - сделать так,
     чтоб можно было легко подправить
     циферки на свои и пользоваться:)""")
def PageTwo(widgetlist):
    def askimpath():
        impath = filedialog.askopenfilename(title="Выберите изображение",
                                        filetypes=[["jpeg files", "*.jpg"],
                                                   ("all files", "*.*")])
        widgetlist[5].insert(INSERT, impath)
        #return impath
    def askmodpath():
        modpath = filedialog.askopenfilename(title="Выберите вашу модель",
                                            filetypes=[("all files", "*.*")])
        #modpath = str(modpath)
        widgetlist[8].insert(INSERT, modpath)
        #return modpath
    #widgetlist[0].pack_forget()
    #img = Image.open(impath)
    #img = img.resize((280, 200), Image.ANTIALIAS)
    #img = ImageTk.PhotoImage(img)
    #widgetlist[4].pack(side=TOP)
    #widgetlist[4].configure(image=img)
    #widgetlist[4].image_ref = img
    #widgetlist[3].configure(text="")
    #widgetlist[3].pack()
    widgetlist[5].pack(side=TOP, anchor=NW, pady=10, padx=5)
    widgetlist[6].configure(text="...", command=askimpath)
    widgetlist[6].place(x=100, y=20)
    widgetlist[8].pack(side=TOP, anchor=NW, pady=10, padx=5)
    widgetlist[7].configure(text="...", command=askmodpath)
    widgetlist[7].place(x=100, y=40)
    #data = np.array((cv2.resize(cv2.imread(impath), (x, y)).reshape(1, x, y, ch)), dtype='float') / 255.0
    #return modpath, impath
def PageThree(widgetlist, x, y, ch):
    #widgetlist[3].pack_forget()
    modpath = widgetlist[8].get()
    impath = widgetlist[5].get()
    data = np.array((cv2.resize(cv2.imread(impath), (x, y)).reshape(1, x, y, ch)), dtype='float') / 255.0
    img = Image.open(impath)
    img = img.resize((280, 200), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    widgetlist[4].pack(side=TOP)
    widgetlist[4].configure(image=img)
    widgetlist[4].image_ref = img
    widgetlist[3].configure(text="Ваше изображение")
    model = models.load_model(modpath)
    print('Predicting...')
    predictRaw = model.predict(data)
    predict = np.argmax(predictRaw)
    if predict == 1:
        widgetlist[3].configure(text="Это кошак")
    if predict == 0:
        widgetlist[3].configure(text="Это пес")
    widgetlist[3].pack()