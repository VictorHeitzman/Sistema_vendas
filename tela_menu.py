from Modulos.modulos import *
from Functions.functions_menu import Functions
from Coolors.style import  Style

class Screen_menu(Functions,Style):
    
    
    def __init__(self) -> None:
        self.root_menu = Tk()

        self.config()
        self.labels()

        self.root_menu.mainloop()
    
    def config(self):
        self.root_menu.title('Menu')
        self.root_menu.config(background=self.background)
        self.root_menu.iconbitmap('img\icon_menu.ico')
        self.root_menu.geometry('600x600+400+50')

        self.img = PhotoImage(file = "img\img_produto.png").subsample(4,4)

    def labels(self):
        self.icone_product = Button(self.root_menu, text="Cadastro de Produtos", font=self.font_img,fg='White', compound='bottom',image=self.img,background=self.background,bd=0)
        self.icone_product.place(relheight=0.40,relwidth=0.40)


if __name__ == '__main__':
    root = Screen_menu()