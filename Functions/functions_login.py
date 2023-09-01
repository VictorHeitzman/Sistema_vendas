from Modulos.modulos import *
from Functions.functions_db import DB

from tela_cadastro_usuario import Screen_cadastre_user
from tela_menu import Screen_menu


class Functions(DB):

    def login(self):
        self.conect_db()

        self.user = self.input_login.get()
        self.password = self.input_senha.get()

        self.cursor.execute('SELECT * FROM usuarios\
                            WHERE nome = ? AND senha = ?',(self.user, self.password))
        
        login = self.cursor.fetchall()
        if login:
            print(login)

            self.root_login.destroy()
            Screen_menu()

        else:
            print('user invalid')
            txt_login = Label(text='user invalid',
                            font=self.font,
                            background=self.background,
                            fg='red')
            txt_login.place(relheight=0.10,relwidth=0.30,relx=0.38,rely=0.55)
        
        self.desconect_db()

    
    def screen_cadastre_user(self):

        self.user = self.input_login.get()
        self.password = self.input_senha.get()

        self.admin = 'admin'
        self.senha_admin = 'admin'

        if self.user == 'admin' and self.password == 'admin':
        
            Screen_cadastre_user()

        else:
            print('user invalid')
            txt_login = Label(text='user invalid',
                            font=self.font,
                            background=self.background,
                            fg='red')
            txt_login.place(relheight=0.10,relwidth=0.30,relx=0.38,rely=0.55)
        