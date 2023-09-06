from Modulos.modulos import *
from Functions.functions_db import DB 
from Coolors.style import *

class Functions(DB,Style):

    def __init__(self) -> None:
        self.produtos = []
    

    def get_values(self):

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
            self.subtotal = round(float(self.txt_valor.cget('text')),2)
            self.data = str(date.today().strftime('%d/%m/%Y'))

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
        self.set_produto()

        self.atualiza_somatorio_estoque()

        self.treeview_pdv.delete(*self.treeview_pdv.get_children())

        self.txt_valor.config(text='0')

    def excluir(self):
        if self.input_codigo.get() != '':
            
            select = self.treeview_pdv.selection()[0]
            
            self.get_values()
            
            self.treeview_pdv.delete(select)

            self.subtotal -= round(self.total_produto,2)

            self.txt_valor.config(text=str(self.subtotal))

            self.inserir_estoque()

            self.clear_input()
            self.insert_values()

        else:
            messagebox.showerror('Aviso','Selecione um registro!')

    def press_enter(self, event):
        try:
        
            self.get_values()

            self.verifica_estoque()

            self.tem_produto()
        
        except ValueError:
            self.clear_input()
            self.insert_values()
            messagebox.showinfo('Aviso','Um ou mais dados incorretos')    
    
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
        try:
            for item in self.retorno_query:
                self.dados_select.append(list(item))

            self.valor_compra = self.dados_select[0][2] 
        
        
            self.total_produto = round(self.dados_select[0][3] * self.quantidade,2)
            self.subtotal += round(self.total_produto,2)
                

            self.dados_select[0].append(self.quantidade)
            self.dados_select[0].append(self.total_produto)
            
            print(f'valor adcionado: {self.dados_select}')
            
            self.treeview_pdv.insert('',END,values=(self.dados_select[0][0],
                                                    self.dados_select[0][1],
                                                    self.dados_select[0][3],
                                                    self.dados_select[0][4],
                                                    self.dados_select[0][5]))
            
            self.input_descricao.insert(END,self.dados_select[0][1])
            self.txt_valor.config(text=round(self.subtotal,2))
            self.input_preco_unitario.insert(END,self.dados_select[0][3])
            self.input_total_produto.insert(END,self.dados_select[0][5])

            self.criar_tupla_para_insert()
            
        except:
                    messagebox.showerror('Aviso','Verificar estoque')
        self.clear_input()
        self.insert_values()

    def criar_tupla_para_insert(self):
        
        self.get_values()

        
        tupla = (self.codigo, 
                self.descricao, 
                self.data, 
                self.quantidade, 
                self.valor_compra, 
                self.preco_unitario, 
                self.total_produto,
                self.forma_pagamento)

        self.produtos.append(tupla)
        
        print(f'transacao: {self.produtos}\n')
    
    def set_produto(self):
        
        self.conect_db()

        for posicao in self.produtos:
            self.cursor.execute("""INSERT INTO transacoes VALUES (null,(?),(?),(?),'saida',(?),(?),(?),(?),(?));""",
                                (posicao[0], 
                                posicao[1], 
                                posicao[2], 
                                posicao[3], 
                                posicao[4], 
                                posicao[5], 
                                posicao[6],
                                posicao[7]))
            self.conexao.commit()
                
        print('\nProdutos inseridos na tabela transações')

        self.desconect_db()

        self.clear_input()
        self.insert_values()

    def soma_acrescimo(self, event):
        try:
            self.valor_acrescimo = float(self.input_valor_acrescimo.get())
            self.subtotal += self.valor_acrescimo
            self.txt_valor.config(text=round(self.subtotal,2))
            self.treeview_pdv.insert('',END,values=(0,'ACRESCIMO',self.valor_acrescimo,0,self.valor_acrescimo))
        except:
            messagebox.showerror('Aviso','Valor de acrescimo invalido.')
        self.clear_input()
        self.insert_values()
    
    def soma_desconto(self, event):
        try:
            self.valor_desconto = float(self.input_valor_desconto.get())
            self.subtotal -= self.valor_desconto
            self.txt_valor.config(text=round(self.subtotal,2))
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

    def verifica_estoque(self):
    
        self.conect_db()

        self.cursor.execute("""SELECT estoque FROM estoque
                                                    WHERE id_produto = (?);""",(self.codigo,))
        self.conexao.commit()
        self.quantidade_estoque = self.cursor.fetchall()                                          
        self.desconect_db()

    def tem_produto(self):

        try:
            
            if self.quantidade > self.quantidade_estoque[0][0]: 
                messagebox.showinfo('Aviso','Produto sem estoque')
                self.clear_input()
                self.insert_values()
            else: 
                self.busca_produto()
                self.retira_estoque()
        
        except IndexError:
            messagebox.showerror('Aviso','Produto não encontrado')
            
    def retira_estoque(self):
        self.conect_db()

        self.cursor.execute("""UPDATE estoque
                            SET estoque = estoque - (?)
                            WHERE id_produto = (?)""",(self.quantidade,self.codigo))
        self.conexao.commit()

        print('Estoque removido')

        self.desconect_db()

    def inserir_estoque(self):
        self.get_values()

        print(self.quantidade,',',self.codigo)
        
        self.verifica_estoque()
        
        estoque_novo = self.quantidade_estoque[0][0] + self.quantidade
        
        self.conect_db()

        self.cursor.execute("""UPDATE estoque
                    SET estoque = (?)
                    WHERE id_produto = (?)""",(estoque_novo,self.codigo))
        self.conexao.commit()

        print('\nProduto inserido novamente no estoque')

        self.desconect_db()

        self.atualiza_somatorio_estoque()

    def atualiza_somatorio_estoque(self):
        
        self.conect_db()
        # INSERINDO QUANTIDADE DE ENTRADA
        self.cursor.execute("""UPDATE estoque 
                            SET quantidade_entrada = (SELECT sum(quantidade) FROM transacoes where id_produto = ? and tipo = 'entrada') 
                            WHERE id_produto = ?;""",(self.codigo, self.codigo))

        # INSERINDO QUANTIDADE DE SAIDA
        self.cursor.execute("""UPDATE estoque
                            SET quantidade_saida = (SELECT sum(quantidade) FROM transacoes where id_produto = (?) and tipo = 'saida')
                            WHERE id_produto = (?);""",(self.codigo, self.codigo))
        
        # INSERINDO TOTAL DE ENTRADA
        self.cursor.execute("""UPDATE estoque
                            SET total_entrada = (SELECT sum(total) FROM transacoes where id_produto = (?) and tipo = 'entrada')
                            WHERE id_produto = (?);""",(self.codigo, self.codigo))

        # INSERINDO TOTAL DE SAIDA
        self.cursor.execute("""UPDATE estoque
                            SET total_saida = (SELECT sum(total) FROM transacoes where id_produto = (?) and tipo = 'saida')
                            WHERE id_produto = (?);""",(self.codigo, self.codigo))
        
        # INSERINDO SALDO ESTOQUE
        self.cursor.execute("""UPDATE estoque
                            SET saldo_estoque = (SELECT round((total_entrada) - (total_saida))  FROM estoque where id_produto = (?))
                            WHERE id_produto = (?);""",(self.codigo, self.codigo))

        #  ENVIANDO
        self.conexao.commit()

        self.desconect_db()   