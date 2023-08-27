from Modulos.modulos import *
from Functions.functions_product_cadastre import Functions

class Screen_products_cadastre(Functions):

    background = '#347355'
    fg_front = '#60BF81'
    font = 'arial 11'
    font_color = 'white'
    collor_button = '#223240'

    def __init__(self) -> None:
        self.root_products_cadastre = Tk()

        self.config()

        self.root_products_cadastre.mainloop()

    def config(self):
        self.root_products_cadastre.title('Cadastro produtos')
        self.root_products_cadastre.config(background=self.background)
        self.root_products_cadastre.iconbitmap('img\product.ico')
        self.root_products_cadastre.resizable(False,False)
        self.root_products_cadastre.geometry('800x600+250+50')



if __name__ == '__main__':
    root = Screen_products_cadastre()