import sqlite3
from tela import *

def validate_user():
    conexao = sqlite3.connect('projeto_compras.db')
    cursor = conexao.cursor()
    
    cursor.execute('SELECT * FROM usuarios\
                   WHERE nome = ? AND senha = ?',(tela.input_login.get(),input_senha.get()))
    
    login = cursor.fetchone()

    if login:
        root.destroy()

        root2 = Tk()
        root2.title('Tela 2')
        config_tela2

    else:
        txt_incorrect_user = Label(root,
                                   text='Login or Password incorrect!',
                                   font='arial 8',
                                   fg='red',
                                   background=bg_bottom)
        txt_incorrect_user.place(relheight=0.10,relwidth=0.60,relx=0.23,rely=0.55)

        
    cursor.close()
    conexao.close()