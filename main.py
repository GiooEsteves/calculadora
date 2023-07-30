from tkinter import *
from tkinter import ttk

color1 = "#1e1f1e"      #black
color2 = "#feffff"      #white
color3 = "#38576b"      #blue
color4 = "#ECEFF1"      #gray
color5 = "#FFAB40"      #orange

window = Tk()
window.title("Calculadora")
window.geometry("235x310")
window.config(bg=color1)

#frames
frame_screen = Frame(window, width=235, height=60, bg = color3)
frame_screen.grid(row=0, column=0)

frame_body = Frame(window, width=235, height=258)
frame_body.grid(row=1, column=0)

def calculate():
    result = eval('9/9')
    app_label.set(result)
    
calculate()

#label
string_value = StringVar()
app_label = Label(frame_screen, textvariable=string_value, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18'), bg=color3, fg=color2)
app_label.place(x=0, y=0)

#button
b_1 = Button(frame_body, text="C", width=11, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)

b_2 = Button(frame_body, text="%", width=5, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=118, y=0)

b_3 = Button(frame_body, text="/", width=5, height=2, bg = color5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=0)

b_4 = Button(frame_body, text="7", width=5, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=50)

b_5 = Button(frame_body, text="8", width=5, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=59, y=50)

b_6 = Button(frame_body, text="9", width=5, height=2, bg = color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=118, y=50)

b_7 = Button(frame_body, text="*", width=5, height=2, bg = color5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=177, y=50)

b_8 = Button(frame_body, text="4", width=5, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=100)

b_9 = Button(frame_body, text="5", width=5, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=59, y=100)

b_10 = Button(frame_body, text="6", width=5, height=2, bg = color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=118, y=100)

b_11 = Button(frame_body, text="-", width=5, height=2, bg = color5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=177, y=100)

b_12 = Button(frame_body, text="1", width=5, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=150)

b_13 = Button(frame_body, text="2", width=5, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=59, y=150)

b_14 = Button(frame_body, text="3", width=5, height=2, bg = color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=118, y=150)

b_15 = Button(frame_body, text="+", width=5, height=2, bg = color5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=177, y=150)

b_16 = Button(frame_body, text="0", width=11, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_16.place(x=0, y=200)

b_17 = Button(frame_body, text=".", width=5, height=2, bg=color4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_17.place(x=118, y=200)

b_18 = Button(frame_body, text="=", width=5, height=2, bg = color5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_18.place(x=177, y=200)

window.mainloop()
