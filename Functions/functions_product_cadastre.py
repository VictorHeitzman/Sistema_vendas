from Modulos.modulos import *
from Functions.function_db import DB

class Functions(DB):

    def insert_product(self):

        self.produto = self.input_produto.get()
        self.descricao = self.input_descricao.get()
        self.preco_compra = self.input_preco_compra.get()
        self.preco_venda = self.txt_preco_venda.get()

        self.conect_db()
        self.cursor.execute("""INSERT INTO produtos VALUES (?,?,?,?,?)""",
                            (None, self.produto, self.descricao, self.preco_compra, self.preco_venda))

        self.conexao.commit()
        print(f'Produto: {self.produto}\nPreco compra: {self.preco_compra}\nPreco venda: {self.preco_venda}\nCadastrado com sucesso')
        # self.refresh_treeview()
        
        self.desconect_db()

    def clear_inputs(self):
        pass
