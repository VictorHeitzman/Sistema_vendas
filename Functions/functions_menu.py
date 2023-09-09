from Modulos.modulos import *

from tela_pdv import Screen_pdv
from tela_cadastro_produtos import Screen_products_cadastre
from tela_estoque import Screen_stock
class Functions():

    def screen_products_cadastre(self):

        Screen_products_cadastre()
    
    def screen_stock(self):
        
        Screen_stock()
        
    def screen_pdv(self):

        Screen_pdv()

    def menu(self):
        self.barra_menu = Menu(self.root_menu)
        self.root_menu.config(menu=self.barra_menu) 

        self.sobre = Menu(self.barra_menu, tearoff=0)
        self.sobre.add_cascade(label='Este Sistema',command='')

        self.contatos = Menu(self.barra_menu, tearoff=0)

        self.opcoes = Menu(self.barra_menu, tearoff=0)
        self.opcoes.add_command(label='Sair', command=self.root_menu.quit)
        self.opcoes.add_command(label='Cadastro de clientes', command='')

        self.barra_menu.add_cascade(label='Sobre',menu=self.sobre)
        self.barra_menu.add_cascade(label='Contatos', menu=self.contatos)
        self.barra_menu.add_cascade(label='Opções',menu=self.opcoes)

        

        
