from Config.Modulos.modulos import *
from Config.Functions.functions_db import DB 
from Config.Coolors.style import *



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
            self.valor_acrescimo = float(str(self.input_valor_acrescimo.get()).replace(',','.'))
            self.valor_desconto = float(str(self.input_valor_desconto.get()).replace(',','.'))
            self.forma_pagamento = str(self.input_forma_pagamento.get())
            self.subtotal = round(float(self.txt_valor.cget('text')),2)
            self.data = str(date.today().strftime('%d/%m/%Y'))

    def double_click(self, event):
        
        # self.input_codigo.config(state='disabled')


            self.treeview_pdv.selection()

            for selected_item in self.treeview_pdv.selection():

                tupla = self.treeview_pdv.item(selected_item,'values')

                self.codigo = int(tupla[0])
                self.descricao = tupla[1]
                self.preco_unitario = float(tupla[2])
                self.quantidade = int(tupla[3])
                self.total_produto = float(tupla[4])
    
            resp = messagebox.askyesno('Aviso','Deseja cancelar o produto da transação?')
            if resp == True:
                    self.excluir()
            else:
                self.root_pdv.focus_force()
                self.root_pdv.grab_set()

    def finalizar(self):
        if len(self.produtos) != 0:
            self.set_produto()

            self.atualiza_somatorio_estoque()

            self.treeview_pdv.delete(*self.treeview_pdv.get_children())

            self.txt_valor.config(text='0')

            self.produtos.clear()

            messagebox.showinfo('Finalizado','Transação efetuada!')
            self.root_pdv.focus_force()
            self.root_pdv.grab_set()
        else: 
            messagebox.showerror('Erro','Sem produtos no carrinho!')
            self.root_pdv.focus_force()
            self.root_pdv.grab_set()

    def excluir(self):

        # if self.input_codigo != '':
    
        select = self.treeview_pdv.selection()[0]

        # excluindo produtos da lista de compras
        self.index = self.treeview_pdv.index(select)
        self.produtos.pop(self.index)        

        self.treeview_pdv.delete(select)

        self.subtotal -= round(self.total_produto,2)

        self.txt_valor.config(text=str(round(self.subtotal,2)))

        self.inserir_estoque()

        self.clear_input()
        self.insert_values()

        # else:
        #     messagebox.showerror('Aviso','Selecione um registro!')

    def press_enter(self, event):
        
        try:
        
            self.get_values()

            self.verifica_estoque()

            self.tem_produto()

        except ValueError:
            messagebox.showinfo('Aviso','Um ou mais dados incorretos')
            self.root_pdv.focus_force()
            self.root_pdv.grab_set()
        
        
        self.clear_input()
        self.insert_values()
            
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
            
            print(f'\nvalor adcionado: {self.dados_select}')
            
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

            self.clear_input()
            self.insert_values()
            
        except:
            messagebox.showerror('Aviso','Verificar estoque')
            self.root_pdv.focus_force()
            self.root_pdv.grab_set()
        
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
        
        print(f'\ntransacao: {self.produtos}\n')
    
    def set_produto(self):

        self.forma_pagamento = str(self.input_forma_pagamento.get())
        
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
                                self.forma_pagamento))
            self.conexao.commit()
                
        print('\nProdutos inseridos na tabela transações')

        self.desconect_db()

        self.clear_input()
        self.insert_values()

    def soma_acrescimo(self, event):

        try:
            self.valor_acrescimo = float(str(self.input_valor_acrescimo.get()).replace(',','.'))
            self.subtotal += self.valor_acrescimo
            self.txt_valor.config(text=round(self.subtotal,2))
            self.treeview_pdv.insert('',END,values=(0,'ACRESCIMO',self.valor_acrescimo,0,self.valor_acrescimo))

            self.codigo = 0
            self.descricao = 'ACRESCIMO'
            self.data = str(date.today().strftime('%d/%m/%Y'))   
            self.quantidade = 1
            self.valor_compra = 0
            self.preco_unitario = self.valor_acrescimo
            self.total_produto = self.valor_acrescimo
            self.forma_pagamento = 'ACRESCIMO'

            tupla = (self.codigo, 
            self.descricao, 
            self.data, 
            self.quantidade, 
            self.valor_compra, 
            self.preco_unitario, 
            self.total_produto,
            self.forma_pagamento)

            self.produtos.append(tupla)
        
            print(f'\ntransacao: {self.produtos}\n')

        except:
            messagebox.showerror('Aviso','Valor de acrescimo invalido.')
        self.clear_input()
        self.insert_values()
        self.root_pdv.focus_force()
        self.root_pdv.grab_set()
    
    def soma_desconto(self, event):
        try:
            self.valor_desconto = float(str(self.input_valor_desconto.get()).replace(',','.'))
            self.subtotal -= self.valor_desconto
            self.txt_valor.config(text=round(self.subtotal,2))
            self.treeview_pdv.insert('',END,values=(00,'DESCONTO',self.valor_desconto,0,self.valor_desconto))

            self.codigo = 0
            self.descricao = 'DESCONTO'
            self.data = str(date.today().strftime('%d/%m/%Y'))   
            self.quantidade = 1
            self.valor_compra = 0
            self.preco_unitario = self.valor_desconto
            self.total_produto = self.valor_desconto
            self.forma_pagamento = 'DESCONTO'

            tupla = (self.codigo, 
            self.descricao, 
            self.data, 
            self.quantidade, 
            self.valor_compra, 
            self.preco_unitario, 
            self.total_produto,
            self.forma_pagamento)

            self.produtos.append(tupla)
        
            print(f'\ntransacao: {self.produtos}\n')
        except:
            messagebox.showerror('Aviso','Valor de desconto invalido.')
        
        self.root_pdv.focus_force()
        self.root_pdv.grab_set()
        self.clear_input()
        self.insert_values()

    def clear_input_delete_pro(self):

        self.input_codigo_delete_prod.delete(0,END)
        self.input_descricao_delete_prod.delete(0,END)
        self.input_quantidade_delete_prod.delete(0,END)
        self.input_preco_unitario_delete_prod.delete(0,END)
        self.input_total_produto_delete_prod.delete(0,END)
  
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
        self.input_descricao.delete(0,END)

    def verifica_estoque(self):
    
        self.conect_db()

        self.cursor.execute("""SELECT estoque, quantidade_saida FROM estoque
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
                self.root_pdv.focus_force()
                self.root_pdv.grab_set()
            else: 
                self.busca_produto()
                self.retira_estoque()
        
        except IndexError:
            self.root_pdv.focus_force()
            self.root_pdv.grab_set()
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
        # self.get_values()

        print(self.quantidade,',',self.codigo)
        
        self.verifica_estoque()
        
        estoque_novo = self.quantidade_estoque[0][0] + self.quantidade

        
        self.conect_db()

        self.cursor.execute("""UPDATE estoque
                    SET estoque = (?)
                    WHERE id_produto = (?);""",(estoque_novo,self.codigo))
        
        # self.cursor.execute("""UPDATE estoque
        #             SET quantidade_saida = (?)
        #             WHERE id_produto = (?);""",(quantidade_saida,self.codigo))
        
        self.conexao.commit()

        print('\nProduto inserido novamente no estoque')

        self.desconect_db()

        self.atualiza_somatorio_estoque()

        self.clear_input()
        self.insert_values()

    def atualiza_somatorio_estoque(self):
        
        self.conect_db()
        self.cursor.execute("""SELECT id_produto FROM estoque;""")
        query = self.cursor.fetchall()
        # self.conexao.commit()
        # self.desconect_db()

        # self.conect_db()
        for p in query:

            print(f'\npassando por produto: {p[0]}')

            # INSERINDO QUANTIDADE DE ENTRADA
            self.cursor.execute("""UPDATE estoque 
                                SET quantidade_entrada = (SELECT sum(quantidade) FROM transacoes where id_produto = ? and tipo = 'entrada') 
                                WHERE id_produto = ?;""",(p[0],p[0]))

            # INSERINDO QUANTIDADE DE SAIDA
            self.cursor.execute("""UPDATE estoque
                                SET quantidade_saida = (SELECT sum(quantidade) FROM transacoes where id_produto = (?) and tipo = 'saida')
                                WHERE id_produto = (?);""",(p[0],p[0]))
            
            # INSERINDO TOTAL DE ENTRADA
            self.cursor.execute("""UPDATE estoque
                                SET total_entrada = (SELECT sum(total) FROM transacoes where id_produto = (?) and tipo = 'entrada')
                                WHERE id_produto = (?);""",(p[0],p[0]))

            # INSERINDO TOTAL DE SAIDA
            self.cursor.execute("""UPDATE estoque
                                SET total_saida = (SELECT sum(total) FROM transacoes where id_produto = (?) and tipo = 'saida')
                                WHERE id_produto = (?);""",(p[0],p[0]))
            
            # INSERINDO SALDO ESTOQUE
            # self.cursor.execute("""UPDATE estoque
            #                     SET saldo_estoque = (SELECT round((total_entrada) - (total_saida))  FROM estoque where id_produto = (?))
            #                     WHERE id_produto = (?);""",(p[0],p[0]))

            #  ENVIANDO
            
        self.conexao.commit()

        self.desconect_db()   

        print('\nEstoque atualizado.')

    def selecionar_produto(self):

        self.treeview_selecao_produto.delete(*self.treeview_selecao_produto.get_children())

        self.conect_db()
        
        self.query = self.cursor.execute("""SELECT * FROM produtos""")
        self.conexao.commit()

        for produto in self.query:
            self.treeview_selecao_produto.insert('',END,values=(produto[0],produto[1]))
        
        self.desconect_db()
    
    def double_click_selec_produtos(self,event):

        self.treeview_selecao_produto.selection()

        for i in self.treeview_selecao_produto.selection():
            produto = self.treeview_selecao_produto.item(i,'values')
        
        self.codigo = produto[0]
        self.descricao = produto[1]

        self.input_codigo.insert(END,self.codigo)
        # self.input_descricao.insert(END, self.descricao)

        self.root_selecao_produto.destroy()
    
    def chamar_produtos(self, event):
    
        self.root_selecao_produto = Toplevel()
        self.root_selecao_produto.title('PDV')
        self.root_selecao_produto.config(background=self.background)
        self.root_selecao_produto.iconbitmap('config\img\icon_pdv.ico')
        self.root_selecao_produto.resizable(False,False)
        self.root_selecao_produto.geometry('500x400+250+50')
        # self.stock.attributes('-fullscreen',True)
        self.root_selecao_produto.grab_set()
        self.root_selecao_produto.focus_force()

        columns = ('codigo','decricao')
        self.treeview_selecao_produto = ttk.Treeview(self.root_selecao_produto, columns=columns, show='headings')

        self.treeview_selecao_produto.heading('#1',text='Codigo')
        self.treeview_selecao_produto.heading('#2',text='Descrição')

        self.treeview_selecao_produto.column('#1',width=50)
        self.treeview_selecao_produto.column('#2',width=50)

        self.scroollist = Scrollbar(self.root_selecao_produto,orient='vertical')

        self.treeview_selecao_produto.config(yscrollcommand=self.scroollist.set)
        
        self.scroollist.place(relheight=0.90,relwidth=0.04,relx=0.91,rely=0.03)
        self.treeview_selecao_produto.place(relheight=0.90,relwidth=0.90,relx=0.03,rely=0.03)

        self.treeview_selecao_produto.bind('<Double-1>',self.double_click_selec_produtos)       

        self.selecionar_produto()

    def quit(self):
        
        children = self.treeview_pdv.get_children()
        if len(children) > 0:
            messagebox.showwarning("Aviso", "Você possui produtos em transação.\nCancele os produtos para sair do PDV!")
            self.root_pdv.focus_force()
            self.root_pdv.grab_set()
        else:
            self.root_pdv.destroy()

