from modulos import *


class Functions():

    def conect_db(self) -> None:
        self.conexao = sqlite3.connect('BD/projeto_compras.db')
        self.cursor = self.conexao.cursor()
        print('Conectado')

    def desconect_db(self):     
        self.conexao.close()        
    
    def login(self):
        self.conect_db()

        self.cursor.execute('SELECT * FROM usuarios\
                            WHERE nome = ? AND senha = ?',(self.input_login.get(),self.input_senha.get()))
        
        login = self.cursor.fetchall()
        if login:
            print(login)

            self.root_login.destroy()

        
        else:
            print('user invalid')
            txt_login = Label(text='user invalid',
                            font=self.font,
                            background=self.bg_bottom,
                            fg='red')
            txt_login.place(relheight=0.10,relwidth=0.30,relx=0.38,rely=0.55)
        
        self.desconect_db()
