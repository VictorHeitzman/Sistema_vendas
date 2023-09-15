from Config.Modulos.modulos import *


root = Tk()

root.geometry('200x200')

datstr = StringVar()

def get_data():
    print(datstr.get())


data = DateEntry(root, locale='pt_BR',textvariable=datstr)
data.pack()

button = Button(root,text='get',command=get_data)
button.pack()

root.mainloop()