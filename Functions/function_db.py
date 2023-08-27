from Modulos.modulos import *

class DB:
    
    def conect_db(self) -> None:
        self.conexao = sqlite3.connect('BD/projeto_compras.db')
        self.cursor = self.conexao.cursor()

    def desconect_db(self):     
        self.conexao.close()        
    