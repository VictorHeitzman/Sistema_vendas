import sqlite3


class DB:
    def __init__():
        global cursor 

        conexao = sqlite3.connect('projeto_compras.db')
        cursor = conexao.cursor()
        
        if cursor:
            print('conect sucess')
            return cursor

        else: 
            print('not conect')

    def validade(_login,_senha):

        cursor.execute('SELECT * FROM usuarios\
                    WHERE nome = ? AND senha = ?',(_login,_senha))
        login = cursor.fetchone()

        return print(login)