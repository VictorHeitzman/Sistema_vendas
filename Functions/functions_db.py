from Modulos.modulos import *

class DB:
    
    def conect_db(self) -> None:
        self.conexao = sqlite3.connect('BD/projeto_compras.db')
        self.cursor = self.conexao.cursor()

    def desconect_db(self):     
        self.conexao.close()        
    
    def create_table_user(self):
        self.conect_db()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios (
                            ID	INTEGER,
                            nome	TEXT,
                            senha	TEXT,
                            PRIMARY KEY("ID" AUTOINCREMENT)
                        )"""
        )
        self.conexao.commit()
        if self.conexao.commit(): print('DB user created')
        self.desconect_db()
    
    def create_table_produtos(self):
        self.conect_db()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS produtos (
                            ID	INTEGER,
                            nome_produto TEXT NOT NULL,
                            descricao_produto	TEXT NOT NULL,
                            preco_compra REAL NOT NULL,
                            preco_venda REAL NOT NULL,
                            PRIMARY KEY("ID" AUTOINCREMENT)
                        )"""
        )
        self.conexao.commit()
        if self.conexao.commit(): print('DB product created')
        self.desconect_db()
        