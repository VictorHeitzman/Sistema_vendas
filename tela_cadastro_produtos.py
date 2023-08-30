from Modulos.modulos import *
from Functions.functions_product_cadastre import Functions
from Coolors.style import  Style
class Screen_products_cadastre(Functions, Style):

    def __init__(self) -> None:

        self.root_products_cadastre = Tk()

        self.config()
        self.labels()

        self.root_products_cadastre.mainloop()

    def config(self):
        self.root_products_cadastre = Toplevel()
        self.root_products_cadastre.title('Cadastro produtos')
        self.root_products_cadastre.config(background=self.background)
        self.root_products_cadastre.iconbitmap('img\product.ico')
        self.root_products_cadastre.resizable(False,False)
        self.root_products_cadastre.geometry('600x550+250+50')
        
        self.root_products_cadastre.focus_force()
        self.root_products_cadastre.grab_set()
    
    def labels(self):
        # -------------------- Produto ------------------------------------
        self.txt_produto = Label(self.root_products_cadastre,
                                 text='Produto:',
                                 bg=self.background,
                                 fg='White',
                                 font=self.font)
        self.txt_produto.place(relheight=0.05,relwidth=0.20,rely=0.10,relx=0.03)
        
        self.input_produto = Entry(self.root_products_cadastre,
                                 font=self.font)
        self.input_produto.place(relheight=0.05,relwidth=0.60,rely=0.10,relx=0.35)
        # -------------------------------------------------------------------

        # -------------------- descricao ------------------------------------
        self.txt_descricao = Label(self.root_products_cadastre,
                                   text='Descricao:',
                                 bg=self.background,
                                 fg='White',
                                 font=self.font)
        self.txt_descricao.place(relheight=0.05,relwidth=0.20,rely=0.17,relx=0.03)
        
        self.input_descricao = Entry(self.root_products_cadastre,
                                 font=self.font)
        self.input_descricao.place(relheight=0.05,relwidth=0.60,rely=0.17,relx=0.35)
        # -------------------------------------------------------------------

        # -------------------- preço compra ------------------------------------
        self.txt_preco_compra = Label(self.root_products_cadastre,
                                      text='Preço de compra:',
                                 bg=self.background,
                                 fg='White',
                                 font=self.font)
        self.txt_preco_compra.place(relheight=0.05,relwidth=0.20,rely=0.24,relx=0.03)
        
        self.input_preco_compra = Entry(self.root_products_cadastre,
                                 font=self.font)
        self.input_preco_compra.place(relheight=0.05,relwidth=0.25,rely=0.24,relx=0.35)
        # -------------------------------------------------------------------

        # -------------------- preço venda ------------------------------------
        self.txt_preco_venda = Label(self.root_products_cadastre,
                                     text='Preço de venda:',
                                 bg=self.background,
                                 fg='White',
                                 font=self.font)
        self.txt_preco_venda.place(relheight=0.05,relwidth=0.20,rely=0.31,relx=0.03)
        
        self.txt_preco_venda = Entry(self.root_products_cadastre,
                                 font=self.font)
        self.txt_preco_venda.place(relheight=0.05,relwidth=0.25,rely=0.31,relx=0.35)
        # -------------------------------------------------------------------

        # -------------------- Button salvar ------------------------------------
        self.button_salvar = Button(self.root_products_cadastre,
                                    text='Salvar',
                                 bg=self.collor_button,
                                 fg='White',
                                 font=self.font,
                                 command=self.insert_product)
        self.button_salvar.place(relheight=0.05,relwidth=0.10,rely=0.39,relx=0.03)
        # -------------------------------------------------------------------

        # -------------------- treeview ------------------------------------
        self.treeview_produto = ttk.Treeview(self.root_products_cadastre,columns=('col1','col2','col3','col4','col5'))

        self.treeview_produto.heading('#0',text='')
        self.treeview_produto.heading('#1',text='Códido')
        self.treeview_produto.heading('#2',text='Produto')
        self.treeview_produto.heading('#3',text='Descrição')
        self.treeview_produto.heading('#4',text='Preço Compra')
        self.treeview_produto.heading('#5',text='Preço Venda')

        self.treeview_produto.column('#0',width=0)
        self.treeview_produto.column('#1',width=1)
        self.treeview_produto.column('#2',width=25)
        self.treeview_produto.column('#3',width=35)
        self.treeview_produto.column('#4',width=10)
        self.treeview_produto.column('#5',width=10)

        self.treeview_produto.place(relheight=0.40,relwidth=0.90,rely=0.45,relx=0.03)
        # -------------------------------------------------------------------


if __name__ == '__main__':
    root = Screen_products_cadastre()