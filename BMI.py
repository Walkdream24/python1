import tkinter

def calc_bmi():
    h = float(textHeight.get()) / 100
    w = float(textWeight.get())
    bmi = w / h ** 2
    rw = h ** 2 * 22
    per = int(w / rw * 100) - 100

    s = "肥満 {0}% (bmi={1})".format(per, bmi)
    labelResult['text'] = s

win = tkinter.Tk()
win.title = ("肥満測定")
win.geometry("500x300")

labelHeight = tkinter.Label(win, text=u"身長(cm):")
labelHeight.pack()

textHeight = tkinter.Entry(win)
textHeight.insert(tkinter.END, "160")
textHeight.pack()

labelWeight = tkinter.Label(win, text=u"体重(kg):")
labelWeight.pack()

textWeight = tkinter.Entry(win)
textWeight.insert(tkinter.END, "70")
textWeight.pack()

labelResult = tkinter.Label(win, text=u"___")
labelResult.pack()

calcButton = tkinter.Button(win, text=u"計算")
calcButton["command"] = calc_bmi
calcButton.pack()

win.mainloop()