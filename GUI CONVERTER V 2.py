from tkinter import Tk,Label,Entry,Button
class TempConverter:
    def __init__ (self):
        self.root=Tk()
        self.root.minsize(300,200)
        self.root.maxsize(500,400)
        self.root.title('Temperature Converter')
        self.createConverter()
        self.root.mainloop()

    def createConverter(self):
        l1=Label(self.root,text='Enter temperature in Celsius: ')
        l1.pack()
        self.e1=Entry(self.root)
        self.e1.pack()
        b1=Button(self.root,text='Convert',command=self.convertToFah)
        b1.pack()
        
    def convertToFah(self):
        answer=int(self.e1.get())*9/5+32
        l2=Label(self.root,text='Equivalent temperature...'+str(answer))
        l2.pack()

t=TempConverter()

