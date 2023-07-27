from tkinter import *
from models_config import Config


class Tela_Register(Config):
    
    bg_bottom = '#347355'
    fg_front = '#60BF81'
    font = 'arial 11'
    font_color = 'white'
    collor_button = '#223240'

    def __init__(self) -> None:
        self.root = Tk()
        super().config_tela_login()

        self.root.mainloop()

