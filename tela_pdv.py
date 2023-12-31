from Config.Modulos.modulos import *

from Config.Coolors.style import  Style
from Config.Functions.functions_pdv import Functions

class Screen_pdv(Functions,Style):

    def __init__(self):
        
        # self.root_pdv = Tk()
        self.config()
        self.labels()
        self.produtos = []

        # self.root_pdv.mainloop()
    
    def config(self):
# # 
        self.root_pdv = Toplevel()
        self.root_pdv.title('PDV')
        self.root_pdv.config(background=self.background)
        self.root_pdv.iconbitmap('Config\img\icon_pdv.ico')

        self.root_pdv.geometry('800x600+250+50')
        # self.root_pdv.attributes('-fullscreen',True)

        self.root_pdv.focus_force()
        self.root_pdv.grab_set()

        self.root_pdv.protocol("WM_DELETE_WINDOW",self.quit)

    
    def labels(self):

        # --------------------------- Código --------------------------------------------------------------
        self.txt_codigo = Label(self.root_pdv, text='Código:',background=self.background,font=self.font,fg=self.font_color)
        self.txt_codigo.place(relheight=0.05,relwidth=0.06,relx=0.01,rely=0.10)

        self.return_cod = StringVar()
                
        self.input_codigo = Entry(self.root_pdv, textvariable=self.return_cod)
        self.input_codigo.place(relheight=0.05,relwidth=0.58,relx=0.11,rely=0.10)
        self.input_codigo.focus()

        # self.return_cod.trace_add('write', self.press_enter)

        self.input_codigo.bind('<Double-1>',self.chamar_produtos)
        self.input_codigo.bind('<Return>',self.press_enter)
        
        # -----------------------------------------------------------------------------------------------

        # --------------------------- Descrição --------------------------------------------------------------
        self.txt_descricao = Label(self.root_pdv, text='Descrição:',background=self.background,font=self.font,fg=self.font_color)
        self.txt_descricao.place(relheight=0.05,relwidth=0.09,relx=0.01,rely=0.17)

        self.input_descricao = Entry(self.root_pdv, )
        self.input_descricao.place(relheight=0.05,relwidth=0.58,relx=0.11,rely=0.17)
        # -----------------------------------------------------------------------------------------------

        # --------------------------- quantidade --------------------------------------------------------------
        self.txt_quantidade = Label(self.root_pdv, text='Quantidade:',background=self.background,font=self.font,fg=self.font_color)
        self.txt_quantidade.place(relheight=0.05,relwidth=0.10,relx=0.01,rely=0.24)

        self.input_quantidade = Entry(self.root_pdv, )
        self.input_quantidade.place(relheight=0.05,relwidth=0.10,relx=0.11,rely=0.24)

        self.input_quantidade.bind('<Return>',self.press_enter)

        # -----------------------------------------------------------------------------------------------
        
        # --------------------------- preço unitario --------------------------------------------------------------
        self.txt_preco_unitario = Label(self.root_pdv, text='Preço Unitario:',background=self.background,font=self.font,fg=self.font_color)
        self.txt_preco_unitario.place(relheight=0.05,relwidth=0.13,relx=0.22,rely=0.24)

        self.input_preco_unitario = Entry(self.root_pdv, )
        self.input_preco_unitario.place(relheight=0.05,relwidth=0.10,relx=0.35,rely=0.24)
        self.input_preco_unitario.insert(END,0)
        # -----------------------------------------------------------------------------------------------
        
        # --------------------------- total produto --------------------------------------------------------------
        self.txt_total_produto = Label(self.root_pdv, text='Total Produto:',background=self.background,font=self.font,fg=self.font_color)
        self.txt_total_produto.place(relheight=0.05,relwidth=0.13,relx=0.46,rely=0.24)

        self.input_total_produto = Entry(self.root_pdv, )
        self.input_total_produto.place(relheight=0.05,relwidth=0.10,relx=0.59,rely=0.24)
        self.input_total_produto.insert(END,0)
        # -----------------------------------------------------------------------------------------------

        # --------------------------- Valor acréscimo --------------------------------------------------------------
        self.txt_valor_acrescimo = Label(self.root_pdv, text='Valor acréscimo:',background=self.background,font=self.font,fg=self.font_color)
        self.txt_valor_acrescimo.place(relheight=0.05,relwidth=0.14,relx=0.72,rely=0.30)

        self.input_valor_acrescimo = Entry(self.root_pdv, )
        self.input_valor_acrescimo.place(relheight=0.05,relwidth=0.10,relx=0.86,rely=0.30)
        self.input_valor_acrescimo.insert(END,0)

        self.input_valor_acrescimo.bind('<Return>',self.soma_acrescimo)
        # -----------------------------------------------------------------------------------------------

        # --------------------------- Valor desconto --------------------------------------------------------------
        self.txt_total_desconto = Label(self.root_pdv, text='Valor desconto:',background=self.background,font=self.font,fg=self.font_color)
        self.txt_total_desconto.place(relheight=0.05,relwidth=0.14,relx=0.72,rely=0.37)

        self.input_valor_desconto = Entry(self.root_pdv, )
        self.input_valor_desconto.place(relheight=0.05,relwidth=0.10,relx=0.86,rely=0.37)
        self.input_valor_desconto.insert(END,0)
        self.input_valor_desconto.bind('<Return>',self.soma_desconto)
        # -----------------------------------------------------------------------------------------------

        # --------------------------- Forma de Pagamento --------------------------------------------------------------
        self.opcoes = ['Dinheiro','Cartão','Pix']

        self.txt_forma_pagamento = Label(self.root_pdv, text='Forma de Pagamento',background=self.background,font=self.font,fg=self.font_color)
        self.txt_forma_pagamento.place(relheight=0.05,relwidth=0.18,relx=0.72,rely=0.44)

        self.input_forma_pagamento = ttk.Combobox(self.root_pdv, values=self.opcoes)
        self.input_forma_pagamento.set(self.opcoes[0])
        self.input_forma_pagamento.place(relheight=0.05,relwidth=0.18,relx=0.72,rely=0.49)
        # -----------------------------------------------------------------------------------------------

        # # --------------------------- Button Excluir --------------------------------------------------------------
        # self.button_excluir = Button(self.root_pdv, text='Excluir',background=self.collor_button,font=self.font,fg=self.font_color,command=self.quit)
        # self.button_excluir.place(relheight=0.05,relwidth=0.10,relx=0.72,rely=0.60)
        # -----------------------------------------------------------------------------------------------
        
        # --------------------------- Button Finalizar --------------------------------------------------------------
        self.button_finalizar = Button(self.root_pdv, text='Finalizar',background=self.collor_button,font=self.font,fg=self.font_color,command=self.finalizar)
        self.button_finalizar.place(relheight=0.05,relwidth=0.10,relx=0.72,rely=0.66)
        # -----------------------------------------------------------------------------------------------
        
        # --------------------------- SubTotal --------------------------------------------------------------
        self.frame_subtotal = Frame(self.root_pdv,background=self.background,highlightbackground=self.collor_button,highlightthickness=1)
        self.frame_subtotal.place(relheight=0.19,relwidth=0.25,relx=0.71,rely=0.10)

        self.txt_subtotal = Label(self.frame_subtotal, text='Subtotal',background=self.background,font='arial 23',fg=self.font_color)
        self.txt_subtotal.pack(anchor='center')

        self.txt_valor = Label(self.frame_subtotal,text=0,background=self.background,font='arial 23',fg=self.font_color)
        self.txt_valor.pack(anchor='center')
        # -----------------------------------------------------------------------------------------------
        
            

        # --------------------------- treeview --------------------------------------------------------------
        self.columns = ('codigo','descricao','preco','quantidade','total')
        self.treeview_pdv = ttk.Treeview(self.root_pdv, columns=self.columns,show='headings')

        self.treeview_pdv.heading('#1',text='Código')
        self.treeview_pdv.heading('#2',text='Descrição')
        self.treeview_pdv.heading('#3',text='Preço')
        self.treeview_pdv.heading('#4',text='Quantidade')
        self.treeview_pdv.heading('#5',text='Total')

        self.treeview_pdv.column('#1',width=1)
        self.treeview_pdv.column('#2',width=100)
        self.treeview_pdv.column('#3',width=5)
        self.treeview_pdv.column('#4',width=5)
        self.treeview_pdv.column('#5',width=5)

        self.scrollbar = ttk.Scrollbar(self.root_pdv,orient='vertical')
        self.treeview_pdv.config(yscrollcommand=self.scrollbar.set)

        self.scrollbar.place(relheight=0.60,relwidth=0.02,relx=0.69,rely=0.30)
        self.treeview_pdv.place(relheight=0.60,relwidth=0.69,relx=0.01,rely=0.30)

        self.treeview_pdv.bind('<Double-1>',self.double_click)
        # self.treeview_pdv.bind('<ButtonRelease-1>', self.print_produtos)
        # -----------------------------------------------------------------------------------------------


if __name__ == '__main__':
    root = Screen_pdv()