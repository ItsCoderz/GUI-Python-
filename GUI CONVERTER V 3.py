from tkinter import Tk,Label,Entry,Button
class TempConverter(Tk):
    def __init__ (self):
        super().__init__()
        self.minsize(300,200)
        self.maxsize(500,400)
        self.title('Temperature Converter')
        self.createConverter()
        self.mainloop()

    def createConverter(self):
        l1=Label(self,text='Enter temperature in Celsius: ')
        l1.pack()
        self.e1=Entry(self)
        self.e1.pack()
        b1=Button(self,text='Convert',command=self.convertToFah)
        b1.pack()

    def convertToFah(self):
        answer=int(self.e1.get())*9/5+32
        l2=Label(self,text='Equivalent temperature...'+str(answer))
        l2.pack()
t=TempConverter()


