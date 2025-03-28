import tkinter as tk
from tkinter import ttk
root=tk.Tk()
root.geometry("100x100+25+25")
root.minsize(width=500,height=500)
tk.Button(root,activebackground="white",default="active",text="Boo! did i scare you?",bg="black",width=20,height=10,font="Arial,50").pack()
tk.Entry(root,bd=100,bg="white",width=10000,state="normal",font="Arial,100",).pack()
tk.Label(root,text="hi",relief="sunken",width=20,height=11,bg="gray",font="Arial,100").pack()
root.title("Hi!")
root.maxsize(width=1000,height=1000)
tk.mainloop()
