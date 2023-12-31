from Config.Modulos.modulos import *
from Config.Functions.functions_db import DB

class Functions(DB):

    def insert_product(self):

        self.get_values()
        try:
            if self.codigo != "" and self.descricao != "":
                
                self.conect_db()
                self.cursor.execute("""INSERT INTO produtos(id, descricao_produto) VALUES (?,?);""",
                                    (self.codigo, self.descricao))
                print('produto inserido na tabela produtos')

                self.cursor.execute("""INSERT INTO estoque (id_produto, descricao, estoque) VALUES ((?),(?), 0)""",(self.codigo,self.descricao))
                print('produto inserido na tabela estoque')
                
                self.conexao.commit()
                
                self.select_treeview_produtos()

                self.clear_inputs()

                self.desconect_db()

                self.input_codigo.focus()
            else:
                    messagebox.showerror('Aviso', 'Preencha todos os valores')
                    print('Produto Não cadastrado')
        except erro_sql:
            self.desconect_db()
            messagebox.showerror('Aviso','Código já cadastrado')  
    
    def clear_inputs(self):
        self.input_codigo.delete(0,END)
        self.input_descricao.delete(0,END)
        # self.input_preco_compra.delete(0,END)
        # self.input_preco_venda.delete(0,END)

    def select_treeview_produtos(self):
        self.treeview_produto.delete(*self.treeview_produto.get_children())

        self.conect_db()

        lista = self.cursor.execute("""SELECT * FROM produtos
                                    ORDER BY descricao_produto ASC""")
        
        for i in lista:
            self.treeview_produto.insert("",END,values=i)
        
        self.desconect_db()

    def double_click_treeview_product(self, event):
        
        self.clear_inputs()

        self.treeview_produto.selection()

        for selected_item in self.treeview_produto.selection():
            
            col1 = self.treeview_produto.item(selected_item,'values')
            
            self.input_codigo.insert(END,col1[0])
            self.input_descricao.insert(END,str(col1[1]).upper())
            # self.input_preco_compra.insert(END,col3)
            # self.input_preco_venda.insert(END,col4)

        self.get_values()

    def delete_product(self):

        self.conect_db()

        self.get_values()

        print(f'id {self.codigo}')

        if self.codigo != "" and self.descricao != "":
            
            self.cursor.execute("""DELETE FROM produtos WHERE id = (?);""",(self.codigo,))
            self.cursor.execute("""DELETE FROM estoque WHERE id_produto = (?);""",(self.codigo,))
            self.conexao.commit()
            
            self.select_treeview_produtos()

            self.clear_inputs()

            print(f'produto {self.descricao} deletado')
        
        else:
            messagebox.showerror('Aviso', 'Preencha todos os valores')
            print('Produto Não Deletado')

        self.desconect_db()
    
    def get_values(self):
        try:
            self.codigo = int(self.input_codigo.get())
            self.descricao = str(self.input_descricao.get()).upper()
            # self.preco_compra = self.input_preco_compra.get()
            # self.preco_venda = self.input_preco_venda.get()

            print(f'id {self.codigo}')
            print(f'descrição {self.descricao}')
            # print(f'preço compra {self.preco_compra}')
            # print(f'preço venda {self.preco_venda}')
        except:
            messagebox.showerror('Aviso','Valores invalidos!')
        
    def enter(self, event):
        self.input_descricao.focus()
    
    def alterar_descricao(self):
        
        self.get_values()
        
        self.conect_db()

        self.cursor.execute("""UPDATE produtos
                            SET descricao_produto = (?)
                            WHERE id = (?);""",(self.descricao,self.codigo))
        
        self.cursor.execute("""UPDATE estoque
                            SET descricao = (?)
                            WHERE id_produto = (?);""",(self.descricao,self.codigo))
        
        self.conexao.commit()

        self.desconect_db()
        
        self.clear_inputs()
        self.select_treeview_produtos()

        messagebox.showinfo('Aviso','Descrição do produto alterado.')