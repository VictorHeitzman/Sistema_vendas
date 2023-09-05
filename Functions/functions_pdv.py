from Modulos.modulos import *
from Functions.functions_db import DB 
from Coolors.style import *

class Functions(DB,Style):

    def get_values(self):
        
        try:

            self.codigo = int(self.input_codigo.get())
            self.descricao = str(self.input_descricao.get())
            
            if self.input_quantidade.get() == "":
                self.quantidade = 1
                self.input_quantidade.insert(END,self.quantidade)
            
            elif int(self.input_quantidade.get()) <= 0:
                self.quantidade = 1
                self.input_quantidade.insert(END,1)
            
            else: self.quantidade = int(self.input_quantidade.get())
            
            self.preco_unitario = float(self.input_preco_unitario.get())
            self.total_produto = float(self.input_total_produto.get())
            self.valor_acrescimo = float(self.input_valor_acrescimo.get())
            self.valor_desconto = float(self.input_valor_desconto.get())
            self.forma_pagamento = str(self.input_forma_pagamento.get())
            self.subtotal = float(self.txt_valor.cget('text'))

        except ValueError:
            self.clear_input()
            self.insert_values()
            messagebox.showinfo('Aviso','Um ou mais dados incorretos')
            quit()

    def double_click(self):
        pass
    
    def finalizar(self):
        pass

    def excluir(self):
        pass

    def press_enter(self, event):

        self.get_values()

        self.select_treeview()

    def select_treeview(self):

        self.conect_db()

        self.cursor.execute("""SELECT id, descricao_produto, ultimo_preco_venda 
                                    FROM produtos
                                    WHERE id = (?);""",(self.codigo,))
        self.conexao.commit()

        lista = self.cursor.fetchall()
        self.dados_select = []

        for item in lista:
            self.dados_select.append(list(item))

        
        self.total_produto = self.dados_select[0][2] * self.quantidade
        
        self.dados_select[0].append(self.quantidade)
        self.dados_select[0].append(self.total_produto)
        
        print(self.dados_select)
        
        for i in self.dados_select:
            self.treeview_pdv.insert('',END,values=i)
        
        self.input_descricao.insert(END,self.descricao)
        
        self.clear_input()

        self.insert_values()

        self.desconect_db()

    def clear_input(self):

        self.input_codigo.delete(0,END)
        self.input_descricao.delete(0,END)
        self.input_quantidade.delete(0,END)
        self.input_preco_unitario.delete(0,END)
        self.input_total_produto.delete(0,END)
        self.input_valor_acrescimo.delete(0,END)
        self.input_valor_desconto.delete(0,END)
    
    def insert_values(self):
        self.input_preco_unitario.insert(END,0)
        self.input_total_produto.insert(END,0)
        self.input_valor_acrescimo.insert(END,0)
        self.input_valor_desconto.insert(END,0)