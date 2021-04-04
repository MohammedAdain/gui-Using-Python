from tkinter import *

root=Tk()
root.title("Calculator")

en=Entry(root,width=30,borderwidth=4)
en.grid(row=0,column=0,columnspan=3)

button_clear=Button(root,text="C",width=10,pady=5,padx=5)
button_clear.grid(row=0,column=3 )

button_1=Button(root,text="1",width=10,pady=5,padx=5)
button_2=Button(root,text="2",width=10,pady=5,padx=5)
button_3=Button(root,text="3",width=10,pady=5,padx=5)
button_add=Button(root,text="+",width=10,pady=5,padx=5)

button_4=Button(root,text="4",width=10,pady=5,padx=5)
button_5=Button(root,text="5",width=10,pady=5,padx=5)
button_6=Button(root,text="6",width=10,pady=5,padx=5)
button_sub=Button(root,text="-",width=10,pady=5,padx=5)

button_7=Button(root,text="7",width=10,pady=5,padx=5)
button_8=Button(root,text="8",width=10,pady=5,padx=5)
button_9=Button(root,text="9",width=10,pady=5,padx=5)
button_mul=Button(root,text="*",width=10,pady=5,padx=5)

button_0=Button(root,text="0",width=10,pady=5,padx=5)
button_dec=Button(root,text=".",width=10,pady=5,padx=5)
button_equ=Button(root,text="=",width=10,pady=5,padx=5)
button_div=Button(root,text="/",width=10,pady=5,padx=5)

button_1.grid(row=1,column=0)
button_2.grid(row=1,column=1)
button_3.grid(row=1,column=2)
button_add.grid(row=1,column=3)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_sub.grid(row=2,column=3)

button_7.grid(row=3,column=0)
button_8.grid(row=3,column=1)
button_9.grid(row=3,column=2)
button_mul.grid(row=3,column=3)

button_0.grid(row=4,column=0)
button_dec.grid(row=4,column=1)
button_equ.grid(row=4,column=2)
button_div.grid(row=4,column=3)

root.mainloop()