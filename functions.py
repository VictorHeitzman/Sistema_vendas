from modulos import *
from tela_bem_vindo import *
class Functions():

    def conect_db(self) -> None:
        self.conexao = sqlite3.connect('BD/projeto_compras.db')
        self.cursor = self.conexao.cursor()

    def desconect_db(self):     
        self.conexao.close()        
    
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
            self.root_bem_vindo = Tela_bem_vindo()

        
        else:
            print('user invalid')
            txt_login = Label(text='user invalid',
                            font=self.font,
                            background=self.bg_bottom,
                            fg='red')
            txt_login.place(relheight=0.10,relwidth=0.30,relx=0.38,rely=0.55)
        
        self.desconect_db()

    def clear_inputs_register(self):
        self.input_user_register.delete(0,END)
        self.input_senha_register.delete(0,END)

    def register_user(self):
        self.name = self.input_user_register.get()
        self.passw = self.input_senha_register.get()
        if self.name != "" or self.passw != "":
            
            self.conect_db()
            self.cursor.execute("""INSERT INTO 
                                usuarios VALUES(?,?,?)""",
                                (None, self.name, self.passw))
            self.conexao.commit()

            print(f'user {self.name} cadastred')

            self.desconect_db()
            self.select_list()
            self.clear_inputs_register()

        else:
            print('Usuario Não cadastrado')
    
    def select_list(self):
        self.treeview.delete(*self.treeview.get_children())
        self.conect_db()

        lista = self.cursor.execute("""SELECT * FROM usuarios
                                    ORDER BY nome ASC""")
        for i in lista:
            self.treeview.insert("",END, values=i)

        self.desconect_db    

    def delete_user(self):

        self.conect_db()

        self.user = self.input_user_register.get()    
        self.passw = self.input_senha_register.get()

        self.cursor.execute("""DELETE FROM usuarios
                            WHERE id = ?""",(self.id,))
        self.conexao.commit()

        print(f'user {self.id} deleted')

        
        self.select_list()
        self.desconect_db()
        self.clear_inputs_register()

    def double_click(self, event):
        self.clear_inputs_register()

        self.treeview.selection()

        for selected_item in self.treeview.selection():
            col1, col2, col3 = self.treeview.item(selected_item,'values')
            
            self.id = col1
            self.input_user_register.insert(END, col2)
            self.input_senha_register.insert(END, col3)

            print(f'id {self.id}')
            print(f'user {self.input_user_register.get()}')
            print(f'pass {self.input_senha_register.get()}')