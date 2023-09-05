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
            self.data = str(date.today().strftime('%d/%m/%Y'))

        except ValueError:
            self.clear_input()
            self.insert_values()
            messagebox.showinfo('Aviso','Um ou mais dados incorretos')

    def double_click(self, event):
        self.clear_input()

        self.treeview_pdv.selection()

        for selected_item in self.treeview_pdv.selection():

            tupla = self.treeview_pdv.item(selected_item,'values')
            print(tupla)
            self.input_codigo.insert(END,tupla[0])
            self.input_descricao.insert(END,tupla[1])
            self.input_preco_unitario.insert(END,tupla[2])
            self.input_quantidade.insert(END,tupla[3])
            self.input_total_produto.insert(END,tupla[4])

            self.input_valor_acrescimo.insert(END,0)
            self.input_valor_desconto.insert(END,0)     

    def finalizar(self):
        print('--------------------')
        curItem = self.treeview_pdv.focus()
        print(self.treeview_pdv.item(curItem,'values'))

    def excluir(self):
        if self.input_codigo.get() != '':
            
            select = self.treeview_pdv.selection()[0]
            
            self.get_values()
            
            self.treeview_pdv.delete(select)

            print(self.subtotal,' antes')
            self.subtotal -= self.total_produto
            print(self.subtotal,' depois')
            self.txt_valor.config(text=self.subtotal)

        else:
            messagebox.showerror('Aviso','Selecione um registro!')

    def press_enter(self, event):

        self.get_values()

        self.busca_produto()

    def busca_produto(self):

        self.conect_db()

        self.cursor.execute("""SELECT * 
                                    FROM produtos
                                    WHERE id = (?);""",(self.codigo,))
        self.conexao.commit()

        self.retorno_query = self.cursor.fetchall()
        
        self.desconect_db()

        self.tratamento_de_dados()
    
    def tratamento_de_dados(self):
        self.dados_select = []

        for item in self.retorno_query:
            self.dados_select.append(list(item))

        self.valor_compra = self.dados_select[0][2] 
  
        self.total_produto = self.dados_select[0][3] * self.quantidade
        self.subtotal += self.total_produto

        self.dados_select[0].append(self.quantidade)
        self.dados_select[0].append(self.total_produto)
        
        print(self.dados_select)
        
        self.treeview_pdv.insert('',END,values=(self.dados_select[0][0],
                                                self.dados_select[0][1],
                                                self.dados_select[0][3],
                                                self.dados_select[0][4],
                                                self.dados_select[0][5]))
        
        self.input_descricao.insert(END,self.dados_select[0][1])
        self.txt_valor.config(text=self.subtotal)
        self.input_preco_unitario.insert(END,self.dados_select[0][3])
        self.input_total_produto.insert(END,self.dados_select[0][5])

        self.set_produto()

        self.clear_input()
        self.insert_values()
    
    def set_produto(self):
        self.conect_db()

        self.get_values()

        self.cursor.execute("""insert into transacoes values (null,(?),(?),(?),'saida',(?),(?),(?),(?))""",
                            (self.codigo, 
                             self.descricao, 
                             self.data, 
                             self.quantidade, 
                             self.valor_compra, 
                             self.preco_unitario, 
                             self.total_produto))
        self.conexao.commit()
        print('Produto inserido na tabela transações')

        self.desconect_db()

    def soma_acrescimo(self, event):
        try:
            self.valor_acrescimo = float(self.input_valor_acrescimo.get())
            self.subtotal += self.valor_acrescimo
            self.txt_valor.config(text=self.subtotal)
            self.treeview_pdv.insert('',END,values=(0,'ACRESCIMO',self.valor_acrescimo,0,self.valor_acrescimo))
        except:
            messagebox.showerror('Aviso','Valor de acrescimo invalido.')
        self.clear_input()
        self.insert_values()
    
    def soma_desconto(self, event):
        try:
            self.valor_desconto = float(self.input_valor_desconto.get())
            self.subtotal -= self.valor_desconto
            self.txt_valor.config(text=self.subtotal)
            self.treeview_pdv.insert('',END,values=(00,'DESCONTO',self.valor_desconto,0,self.valor_desconto))
        except:
            messagebox.showerror('Aviso','Valor de desconto invalido.')
 
        self.clear_input()
        self.insert_values()

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