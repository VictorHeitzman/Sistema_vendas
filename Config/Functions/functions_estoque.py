from Config.Modulos.modulos import *
from Config.Functions.functions_db import DB 
from Config.Coolors.style import *


class Functions(DB,Style):

    def getValues(self):

        try:

            self.data = self.date_str.get()
            self.codigo = int(self.input_codigo.get())
            self.descricao = str(self.input_descricao.get()).upper()
            self.preco_venda = float(str(self.input_preco_venda.get()).replace(',','.'))
            self.preco_compra = float(str(self.input_preco_compra.get()).replace(',','.'))
            
            if self.input_quantidade.get() == "":
                self.quantidade = 0
            else: self.quantidade = int(self.input_quantidade.get())

            print(f'codigo: {self.codigo}\ndescrição: {self.descricao}\npreco venda: {self.preco_venda}\npreco compra: {self.preco_compra}\nquantidade: {self.quantidade}\ndata: {self.data}')
        except ValueError:
                                    
            messagebox.showerror('Error', 'Um ou mais dados com valores incorretos')
    
    def double_click(self, event):
        
        self.clear_inputs_estoque()

        self.treeview_estoque.selection()

        for selected_item in self.treeview_estoque.selection():

            tupla = self.treeview_estoque.item(selected_item,'values')

            self.input_codigo.insert(END,tupla[1])
            self.input_descricao.insert(END,tupla[2])

    def clear_inputs_estoque(self):

        self.input_codigo.delete(0,END)
        self.input_descricao.delete(0,END)
        self.input_preco_venda.delete(0,END)
        self.input_quantidade.delete(0,END)
        self.input_preco_compra.delete(0,END)

    def salvar(self):
               
        self.getValues()

        try:
            if self.input_descricao.get() != "" and self.input_codigo.get() != "" and self.input_preco_compra.get() != "" and self.input_preco_venda.get() != "" and self.input_data.get() != "":
                

                self.total = round(float(self.preco_compra * self.quantidade), 2)
                print(self.total)
                
                self.conect_db()
                
                self.cursor.execute("""INSERT INTO transacoes VALUES(null,(?),(?),(?),'entrada',(?),(?),(?),(?),null);""",(self.codigo,self.descricao,self.data,self.quantidade,round(self.preco_compra,2),round(self.preco_venda,2),round(self.total,2)))

                self.conexao.commit()

                self.desconect_db()

                self.atualizando_estoque()

                self.clear_inputs_estoque()

                self.select_treeview_estoque()

                self.input_codigo.focus()

            else: 
                return messagebox.showinfo('Aviso','Preencha todos os campos!')
        except AttributeError:
            messagebox.showinfo('aviso','Um ou mais dados com valores incorretos')
    
    def atualizando_estoque(self):

        self.conect_db()

        # iNSERINDO ESTOQUE
        self.cursor.execute("""UPDATE estoque 
                            SET estoque = estoque + (?) 
                            WHERE id_produto = (?);""",
                            (self.quantidade,self.codigo))

        self.conexao.commit()

        self.desconect_db()
        
        self.atualiza_somatorio_estoque()

        self.setando_ultimo_valor_em_produtos()
        
    def atualiza_somatorio_estoque(self):
        
        self.conect_db()

        self.cursor.execute("""SELECT id_produto FROM estoque;""")
        query = self.cursor.fetchall()
        print(query)

        for p in query:
            print(f'\natuzalizando estoque {p[0]}')
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

    def setando_ultimo_valor_em_produtos(self):
        self.conect_db()

        self.cursor.execute("""UPDATE produtos
                            SET ultimo_preco_compra = (?), ultimo_preco_venda = (?)
                            WHERE id =  (?)""",(self.preco_compra, self.preco_venda, self.codigo))
        
        self.conexao.commit()

        self.desconect_db()

        print('atualizado ultimos precos da tabela produto.')

    def select_treeview_estoque(self):
        self.treeview_estoque.delete(*self.treeview_estoque.get_children())

        self.conect_db()

        lista = self.cursor.execute("""SELECT * FROM estoque""")

        for i in lista:
            self.treeview_estoque.insert('',END,values=i)
        
        self.desconect_db()
    
    def enter(self, event):

        self.codigo = self.input_codigo.get()

        self.conect_db()

        self.cursor.execute("""SELECT * FROM estoque
                            WHERE id_produto = (?);""",(self.codigo,))
        query = self.cursor.fetchall()
        
        self.input_descricao.insert(END,query[0][2])
        
        self.desconect_db()

    def exportar_transacoes(self):
        
        self.conect_db()

        self.cursor.execute("""SELECT * FROM transacoes""")
        
        self.conexao.commit()

        data = self.cursor.fetchall()
        
        lista = list(map(list,data))

        columns = ('id','id_produto','descicao','data_registro','tipo','quantidade','preco_entrada','preco_saida','total','pagamento')
        df = pd.DataFrame(lista,columns=columns)

        df.to_csv(f'Config/Transacoes/transacoes_{date.today()}.csv',index=None, decimal=',', encoding='latin-1')

        self.desconect_db()
        
        messagebox.showinfo('Aviso','Arquivo de transações exportado.')