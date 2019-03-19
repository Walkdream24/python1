import tkinter
from tkinter import messagebox

win = tkinter.Tk()
win.title("BMI")
win.geometry("500x300")

label = tkinter.Label(win, text="名前は？")
label.pack()

text = tkinter.Entry(win)
text.pack()
text.insert(tkinter.END, "クジラ")

def ok_click():
    s = text.get()
    messagebox.showinfo("挨拶", s + "さん、こんにちは")

okButton = tkinter.Button(win, text= "OK", command=ok_click)
okButton.pack()

win.mainloop()