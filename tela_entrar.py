from Modulos.modulos import *
from tela_cadastro_produtos import Screen_products_cadastre
from Coolors.style import  Style
class Screen_open(Style):

    def __init__(self) -> None:
        self.open = Tk()

        self.config()
        self.menu()

        self.open.mainloop()

    def config(self):
        self.open.title('Cadastro produtos')
        self.open.config(background=self.background)
        self.open.iconbitmap('img\product.ico')
        self.open.resizable(False,False)
        self.open.geometry('800x600+250+50')
        # self.open.attributes('-fullscreen',True)
        

    def menu(self):
        self.barra_menu = Menu(self.open)
        self.open.config(menu=self.barra_menu) 

        self.sobre = Menu(self.barra_menu, tearoff=0)
        self.contatos = Menu(self.barra_menu, tearoff=0)
        self.opcoes = Menu(self.barra_menu, tearoff=0)

        self.barra_menu.add_cascade(label='Sobre',menu=self.sobre)
        self.barra_menu.add_cascade(label='Contatos', menu=self.contatos)
        self.barra_menu.add_cascade(label='Opções',menu=self.opcoes)

        self.opcoes.add_command(label='Sair', command=self.open.quit)
        self.opcoes.add_command(label='Cadastrar', command=self.menu_cadastrar)
        
    def menu_cadastrar(self):
            Screen_products_cadastre()
    
    def menu_contatos(self):
         pass

if __name__ == '__main__':
    root = Screen_open()