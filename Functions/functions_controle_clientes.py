from Modulos.modulos import *
from Functions.functions_db import DB 
from Coolors.style import *



class Functions(DB,Style):
    
    def select_treeview(self):

        self.conect_db()

        self.cursor.execute("""SELECT * FROM devedores""")
        self.query = self.cursor.fetchall()

        for p in self.query:
            self.treeview_cliente.insert('',END,values=(p[1],p[2],p[3],p[4],p[5],p[6]))

        self.desconect_db()
    
    def double_click(self, event):

        for selected_item in self.treeview_cliente.selection():

            self.tupla = self.treeview_cliente.item(selected_item,'values')

            self.txt_nome.config(text=self.tupla[1])
            self.txt_endereco.config(text=self.tupla[2])
            self.txt_numero .config(text=self.tupla[3])
    
    def get_tipo(self):

        self.tipo = str(self.resp.get())
        print(self.tipo)
        return self.tipo
    
    def get_value(self):
        try:
            self.valor = float(round(self.input_valor.get()))
            return self.valor
        except TypeError:
            messagebox.showerror('Aviso','Valide o campo valor!')
    
    def salvar(self):
        self.get_tipo()

        if self.tipo == None:
            pass

        else:
            messagebox.showerror('Aviso','Clique duas vezes em um cliente!')

            