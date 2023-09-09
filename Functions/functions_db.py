from Modulos.modulos import *

class DB:
    
    def conect_db(self) -> None:
        self.conexao = sqlite3.connect('BD/projeto_compras.db')
        self.cursor = self.conexao.cursor()

    def desconect_db(self):     
        self.conexao.close()        
    
    def create_databases(self):
        self.conect_db()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios (
                            id	INTEGER,
                            nome	TEXT,
                            senha	TEXT,
                            PRIMARY KEY("ID" AUTOINCREMENT)
                        );"""
        )
        print('DB user created')

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS produtos (
                            id	INTEGER,
                            descricao_produto	TEXT NOT NULL,
                            ultimo_preco_compra REAL,
							ultimo_preco_venda REAL,
                            PRIMARY KEY("ID")
                        );"""
        )

        print('DB product created')

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS estoque (
                            id integer not NULL,
                            id_produto integer NOT NULL,
                            descricao text NOT NULL,
                            quantidade_entrada integer,
                            quantidade_saida integer,
                            estoque integer,
                            total_entrada real,
                            total_saida real,
                            saldo_estoque real,
                            PRIMARY	KEY(id),
                            FOREIGN key(id_produto) REFERENCES produtos(id)
                        );"""
        )


        print('DB estoque created')

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS transacoes (
                            id INTEGER NOT NULL,
                            id_produto INTEGER NOT NULL,
                            descricao TEXT NOT NULL,
                            data_registro Date NOT NULL,
                            tipo TEXT NOT NULL,
                            quantidade INTEGER NOT NULL,
                            preco_entrada REAL NOT NULL,
                            preco_saida REAL NOT NULL,
                            total REAL NOT NULL,
                            pagamento TEXT,
                            PRIMARY KEY(id),
                            FOREIGN KEY(id_produto) REFERENCES produtos(id)
                        )"""
        )

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS	clientes(
                            id INT NOT NULL,
                            nome TEXT NOT NULL,
                            endereco TEXT NOT NULL,
                            telefone INT NOT NULL,
                            PRIMARY KEY(id)
                        );"""
        )

        self.conexao.commit()
        print('DB transacoes created')
        self.desconect_db()            

        