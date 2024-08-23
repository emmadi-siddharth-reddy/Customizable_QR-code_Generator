import tkinter as tk
from tkinter import *
import back as bck

def Front1():
    root= tk.Tk()

    root.geometry("720x720")
    root.title(" Logo at center QR code ")

    intro_text1=Label(root, text="Welcome",bg="#E8D579")
    intro_text1.grid(row=1, column=1, pady=7, padx=14)

    intro_text2=Label(root, text="This will create QR code",bg="#E8D579")
    intro_text2.grid(row=2, column=1, pady=7, padx=14)

    text_label =Label(root, text="Enter the Text", bg="#E8D579")
    text_label.grid(row=3, column=0, pady=7, padx=30)

    root.text_entry1 = Entry(root, width=65)
    root.text_entry1.grid(row=3, column=1, pady=7)

    color_label =Label(root, text="Enter the Color", bg="#E8D579")
    color_label.grid(row=4, column=0, pady=7, padx=30)

    root.text_entry2 = Entry(root, width=65, )
    root.text_entry2.grid(row=4, column=1, pady=7)

    img_label =Label(root, text="Enter the Image name", bg="#E8D579")
    img_label.grid(row=5, column=0, pady=7, padx=30)

    root.text_entry3 = Entry(root, width=65)
    root.text_entry3.grid(row=5, column=1, pady=7)

    gen_but = Button(root,text="Generate QR Code", command = lambda: bck.Source(root.text_entry1.get(),root.text_entry2.get(),root.text_entry3.get()), width=15, bg="#05E8E0")
    gen_but.grid(row=6, column=1,pady=7)

    root.config(background="aqua")
    root.mainloop()
#https://www.mallareddyuniversity.ac.in/
Front1()