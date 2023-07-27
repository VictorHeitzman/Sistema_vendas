from tkinter import *
from tkinter import Tk

class Config:
    
    def __init__(self) -> None:
        self.root = Tk()

        self.root.mainloop()
    
    def config_tela_login(self):

        self.root.title('Tela de login')
        self.root.config(background=self.bg_bottom)
        self.root.iconbitmap('img\icon_login.ico')
        self.root.geometry('240x200+500+250')