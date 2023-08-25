from modulos import *

class Tela_bem_vindo():

    bg_bottom = '#347355'
    fg_front = '#60BF81'
    font = 'arial 11'
    font_color = 'white'
    collor_button = '#223240'

    def __init__(self) -> None:
        self.root_bem_vindo = Tk()

        self.config()

        self.root_bem_vindo.mainloop()

    def config(self):
        self.root_bem_vindo.title('Tela Bem vindo')
        self.root_bem_vindo.config(background=self.bg_bottom)
        self.root_bem_vindo.iconbitmap('img\icon_login.ico')
        self.root_bem_vindo.geometry('250x200+500+250')

if __name__ == '__main__':
    root = Tela_bem_vindo()