from Config.Modulos.modulos import *
from Config.Functions.functions_db import DB 
from Config.Coolors.style import *



class Functions(DB,Style):
    def get_values(self):

        self.id = str(self.input_id.get())
        self.nome = str(self.input_nome.get()).upper()
        self.endereco = str(self.input_endereco.get()).upper()
        self.telefone = str(self.input_telefone.get())

        print(f'Nome: {self.nome}')
        print(f'Endereço: {self.endereco}')
        print(f'Telefone: {self.telefone}')

    def enter(self, event):
        self.salvar()
                
    def salvar(self):

        # try:
        
            self.get_values()
            self.conect_db()

            self.cursor.execute("""INSERT INTO clientes VALUES (null,(?),(?),(?));""",(self.nome,self.endereco,self.telefone))
            
            self.conexao.commit()

            self.desconect_db()

            self.clear_inputs()

            self.insert_treeview()

            self.insert_devedores()
        # except:
        #     messagebox.showerror('Aviso','Valide os campos!')
        
    def double_click(self,event):

        self.clear_inputs()

        self.treeview_cliente.selection()

        self.input_id.config(state='normal')

        for selected_item in self.treeview_cliente.selection():
            valor = self.treeview_cliente.item(selected_item, 'values')

            self.input_id.insert(END,valor[0])
            self.input_nome.insert(END,valor[1])
            self.input_endereco.insert(END,valor[2])
            self.input_telefone.insert(END,valor[3])
        
        self.input_id.config(state='disabled')

    def select_cliente(self):
        self.conect_db()

        self.cursor.execute("""SELECT * FROM clientes""")

        self.query = self.cursor.fetchall()

        self.desconect_db()

    def insert_treeview(self):
        self.select_cliente()

        self.treeview_cliente.delete(*self.treeview_cliente.get_children())

        for p in self.query:
            self.treeview_cliente.insert('',END,values=p)       
    
    def clear_inputs(self):
         self.input_id.config(state='normal')
         
         self.input_id.delete(0,END)
         self.input_nome.delete(0,END)
         self.input_endereco.delete(0,END)
         self.input_telefone.delete(0,END)

         self.input_id.config(state='disabled')
    
    def editar(self):
        try:
            self.get_values()

            self.conect_db()
            
            self.cursor.execute("""UPDATE clientes
                                SET nome = (?), endereco = (?), telefone = (?)
                                WHERE id = (?)""",(self.nome, self.endereco, self.telefone, self.id,))
            self.conexao.commit()

            print('\nUsuario alterado.')

            self.clear_inputs()

            self.desconect_db()

            self.insert_treeview()
        except:
            messagebox.showerror('Aviso','Valide os campos!')
    
    def excluir(self):
        try:
            self.get_values()
            
            self.conect_db()
            
            self.cursor.execute("""DELETE FROM clientes
                                WHERE id = (?)""",(self.id,))
            print('\nUsuario excluido!')

            self.cursor.execute("""DELETE FROM devedores
                                WHERE id_cliente = (?)""",(self.id,))
            print('\napagado da tabela devedores')
            self.conexao.commit()

            self.desconect_db()

            self.clear_inputs()
            
            self.insert_treeview()
        except:
            messagebox.showerror('Aviso','Valide os campos!')

    def insert_devedores(self):
        
        self.conect_db()

        self.cursor.execute("""SELECT MAX(id) FROM clientes""")
        max_id = self.cursor.fetchall()
        
        self.cursor.execute("""INSERT INTO devedores (id_cliente,nome,endereco,telefone,valor) VALUES ((?),(?),(?),(?),(?));""",(max_id[0][0],self.nome,self.endereco,self.telefone, 0))
        self.conexao.commit()
        print('\nregistrado na tabela devedores')   
        self.desconect_db()