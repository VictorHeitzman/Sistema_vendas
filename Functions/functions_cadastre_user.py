from Modulos.modulos import *
from Functions.functions_db import DB

class Functions(DB):
    
    def clear_inputs_register(self):
        self.input_user_register.delete(0,END)
        self.input_senha_register.delete(0,END)
    
    def register_user(self):
        self.name = self.input_user_register.get()
        self.passw = self.input_senha_register.get()
        if self.name != "" and self.passw != "":
            
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
            messagebox.showerror('Aviso','Preencha todos os valores')
            print('Usuario Não cadastrado')
        
    def select_list(self):

        self.treeview.delete(*self.treeview.get_children())
        self.conect_db()

        lista = self.cursor.execute("""SELECT * FROM usuarios
                                    ORDER BY nome ASC""")
        for i in lista:
            self.treeview.insert("",END, values=i)

        self.desconect_db()

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

