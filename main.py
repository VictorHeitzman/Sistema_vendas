from Config.Modulos.modulos import *
from Config.Coolors.style import Style
from Config.Functions.functions_menu import Functions


class Screen_menu(Functions,Style):
    
    
    def __init__(self) -> None:
        
        self.root_menu = Tk()

        self.create_databases()
        self.config()
        self.labels()
        self.menu()

        self.root_menu.mainloop()
    
    def config(self):
        self.root_menu.title('Menu')
        self.root_menu.config(background=self.background)
        self.root_menu.iconbitmap('Config\img\icon_menu.ico')
        self.root_menu.geometry('600x600+500+250')

        self.img_product = PhotoImage(file = "Config\img\img_produto.png").subsample(4,4)
        self.img_pdv = PhotoImage(file= "Config\img\img_pdv.png").subsample(4,4)
        self.estoque = PhotoImage(file= "Config\img\img_estoque.png").subsample(4,4)
        self.nf = PhotoImage(file= "Config\img\img_nf.png").subsample(4,4)

    def labels(self):
        self.icone_product = Button(self.root_menu, text="Cadastro de Produtos", font=self.font_img,fg='White', compound='bottom',image=self.img_product,background=self.background,bd=0, command=self.screen_products_cadastre)
        self.icone_product.place(relheight=0.40,relwidth=0.40,relx=0.05,rely=0.05)

        self.icone_pdv = Button(self.root_menu, text="PDV", font=self.font_img,fg='White', compound='bottom',image=self.img_pdv,background=self.background,bd=0,command=self.screen_pdv)
        self.icone_pdv.place(relheight=0.40,relwidth=0.40,relx=0.55,rely=0.05)

        self.icone_estoque = Button(self.root_menu, text="Estoque", font=self.font_img,fg='White', compound='bottom',image=self.estoque,background=self.background,bd=0, command=self.screen_stock)
        self.icone_estoque.place(relheight=0.40,relwidth=0.40,relx=0.05,rely=0.55)

        self.icone_nf = Button(self.root_menu, text="Nota Fiscal", font=self.font_img,fg='White', compound='bottom',image=self.nf,background=self.background,bd=0,command=self.screen_nf)
        self.icone_nf.place(relheight=0.40,relwidth=0.40,relx=0.55,rely=0.55)
   

if __name__ == '__main__':
    root = Screen_menu()