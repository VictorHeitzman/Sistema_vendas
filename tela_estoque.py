from Config.Modulos.modulos import *
from Config.Coolors.style import  Style
from Config.Functions.functions_estoque import Functions
class Screen_stock(Functions, Style):

    def __init__(self) -> None:

        # self.root_stock = Tk()
        
        self.config()
        # self.frames()
        self.labels()
        self.select_treeview_estoque()
        
        # self.root_stock.mainloop()

    def config(self):
        self.root_stock = Toplevel()
        self.root_stock.title('Estoque')
        self.root_stock.config(background=self.background)
        self.root_stock.iconbitmap('Config\img\icon_estoque.ico')
        self.root_stock.resizable(False,False)
        self.root_stock.geometry('800x600+250+50')
        # self.stock.attributes('-fullscreen',True)

        self.root_stock.focus_force()
        self.root_stock.grab_set()
    
    def frames(self):
        self.frame_tipo = Frame(self.root_stock,background=self.background,highlightbackground=self.collor_button,highlightthickness=1)
        self.frame_tipo.place(relheight=0.09,relwidth=0.20,relx=0.37,rely=0.15)
    
    def labels(self):

# ----------------------------------- descricao ---------------------------------------
        self.txt_codigo = Label(self.root_stock,text='Código:',background=self.background,fg=self.font_color,font=self.font)
        self.txt_codigo.place(relheight=0.04,relwidth=0.15,relx=0.03,rely=0.05)

        self.input_codigo = Entry(self.root_stock)
        self.input_codigo.place(relheight=0.04,relwidth=0.42,relx=0.20,rely=0.05)
# ----------------------------------- ---------------------------------------------------

# ----------------------------------- descricao ---------------------------------------
        self.txt_descricao = Label(self.root_stock,text='Descrição:',background=self.background,fg=self.font_color,font=self.font)
        self.txt_descricao.place(relheight=0.04,relwidth=0.15,relx=0.03,rely=0.10)

        self.input_descricao = Entry(self.root_stock)
        self.input_descricao.place(relheight=0.04,relwidth=0.42,relx=0.20,rely=0.10)
# ----------------------------------- ---------------------------------------------------

# ----------------------------------- quantidade ---------------------------------------
        self.txt_quantidade = Label(self.root_stock,text='Quantidade:',background=self.background,fg=self.font_color,font=self.font)
        self.txt_quantidade.place(relheight=0.04,relwidth=0.15,relx=0.03,rely=0.15)

        self.input_quantidade = Entry(self.root_stock)
        self.input_quantidade.place(relheight=0.04,relwidth=0.15,relx=0.20,rely=0.15)

# ----------------------------------- ---------------------------------------------------

# ----------------------------------- preco venda ---------------------------------------
        self.txt_preco_compra = Label(self.root_stock,text='Preço de Compra:',background=self.background,fg=self.font_color,font=self.font)
        self.txt_preco_compra.place(relheight=0.04,relwidth=0.15,relx=0.03,rely=0.20)

        self.input_preco_compra = Entry(self.root_stock)
        self.input_preco_compra.place(relheight=0.04,relwidth=0.15,relx=0.20,rely=0.20)

# ----------------------------------- ---------------------------------------------------

# ----------------------------------- preco compra ---------------------------------------
        self.txt_preco_venda = Label(self.root_stock,text='Preço de Venda:',background=self.background,fg=self.font_color,font=self.font)
        self.txt_preco_venda.place(relheight=0.04,relwidth=0.15,relx=0.03,rely=0.25)

        self.input_preco_venda = Entry(self.root_stock)
        self.input_preco_venda.place(relheight=0.04,relwidth=0.15,relx=0.20,rely=0.25)

# ----------------------------------- ---------------------------------------------------

# ----------------------------------- Button salvar ---------------------------------------
        self.button_salvar = Button(self.root_stock,fg=self.font_color,background=self.collor_button, text='Salvar',command=self.salvar)
        self.button_salvar.place(relheight=0.04,relwidth=0.09,relx=0.03,rely=0.33)

# ----------------------------------- ---------------------------------------------------

# ----------------------------------- Button salvar ---------------------------------------
        self.button_salvar = Button(self.root_stock,fg=self.font_color,background=self.collor_button, text='Exportar transações',command=self.exportar_transacoes)        
        self.button_salvar.place(relheight=0.04,relwidth=0.15,relx=0.15,rely=0.33)


# ----------------------------------- ---------------------------------------------------

# ----------------------------------- DATA ---------------------------------------

        self.txt_data = Button(self.root_stock,text='Data',background=self.collor_button,fg=self.font_color,font=self.font,command=self.abrir_calendario)
        self.txt_data.place(relheight=0.04,relwidth=0.05,relx=0.40,rely=0.15)

        self.input_data = Entry(self.root_stock)
        self.input_data.place(relheight=0.04,relwidth=0.15,relx=0.47,rely=0.15)

        self.input_data.insert(END,str(date.today().strftime('%d/%m/%Y')))

        self.input_data.config(state='disabled')

# ----------------------------------- ---------------------------------------------------


# ----------------------------------- treeview ---------------------------------------
        self.columns = ('id','id_produto','descricao','quantidade_entrada','quantidade_saida','estoque','total_entrada','total_saida','saldo_estoque')
        self.treeview_estoque = ttk.Treeview(self.root_stock,columns=self.columns,show='headings')
        
        self.treeview_estoque.heading('#1', text='id')
        self.treeview_estoque.heading('#2', text='código')
        self.treeview_estoque.heading('#3', text='descricao')
        self.treeview_estoque.heading('#4', text='quantidade entrada')
        self.treeview_estoque.heading('#5', text='quantidade saida')
        self.treeview_estoque.heading('#6', text='estoque')
        self.treeview_estoque.heading('#7', text='total entrada')
        self.treeview_estoque.heading('#8', text='total saida')
        self.treeview_estoque.heading('#9', text='saldo estoque')

        self.treeview_estoque.column('#1', width=1)
        self.treeview_estoque.column('#2', width=20)
        self.treeview_estoque.column('#3', width=80)
        self.treeview_estoque.column('#4', width=80)
        self.treeview_estoque.column('#5', width=80)
        self.treeview_estoque.column('#6', width=70)
        self.treeview_estoque.column('#7', width=70)
        self.treeview_estoque.column('#8', width=70)
        self.treeview_estoque.column('#9', width=70)

        self.scroolList = Scrollbar(self.root_stock,orient='vertical')
        self.treeview_estoque.config(yscrollcommand=self.scroolList.set)

        self.scroolList.place(relheight=0.50,relwidth=0.02,relx=0.97,rely=0.40)
        self.treeview_estoque.place(relheight=0.50,relwidth=0.95,relx=0.02,rely=0.40)

        self.treeview_estoque.bind('<Double-1>',self.double_click)

# ----------------------------------- ---------------------------------------------------
if __name__ == '__main__':
    root = Screen_stock()