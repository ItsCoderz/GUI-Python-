def convertToFah():
    answer=int(e1.get())*9/5+32
    l2=Label(root,text='Equivalent temperature in Fahrenheit is '+str(answer))
    l2.pack()

from tkinter import Tk,Label,Entry,Button
root=Tk()
root.minsize(300,200)
root.maxsize(500,400)
root.title('Temperature Converter')
l1=Label(root,text='Enter temperature in Celsius: ')
l1.pack()
e1=Entry(root)
e1.pack()
b1=Button(root,text='Convert',command=convertToFah)
b1.pack()
root.mainloop()



