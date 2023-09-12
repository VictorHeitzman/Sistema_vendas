from Modulos.modulos import *
from Functions.functions_db import DB 
from Coolors.style import *



class Functions(DB,Style):
    
    def select_treeview(self):

        self.conect_db()

        self.treeview_cliente.delete(*self.treeview_cliente.get_children())

        self.cursor.execute("""SELECT * FROM devedores;""")
        self.query = self.cursor.fetchall()

        for p in self.query:
            self.treeview_cliente.insert('',END,values=(p[1],p[2],p[3],p[4],p[6]))

        self.desconect_db()
    
    def double_click(self, event):

        for selected_item in self.treeview_cliente.selection():

            self.tupla = self.treeview_cliente.item(selected_item,'values')

            self.txt_nome.config(text=self.tupla[1])
            self.txt_endereco.config(text=self.tupla[2])
            self.txt_numero .config(text=self.tupla[3])
        print('tupla: ',self.tupla)
    
    def get_tipo(self):
        
        self.tipo = str(self.resp.get())

        if self.tipo == '':
            messagebox.showerror('Aviso','Escolha o tipo de transação')
    
    def get_value(self):
        try:
            self.valor = round(float(str(self.input_valor.get()).replace(',','.')),2)

        except ValueError:
            messagebox.showerror('Aviso','Valide o campo valor!')
    
    def get_text(self):
        
        if self.txt_nome.cget('text') != 'Nome':
            self.text = self.txt_nome.cget('text')
        else:
            messagebox.showerror('Aviso','Clique duas vezes em um cliente!')

    def get_data(self):
        self.data = date.today().strftime('%d/%m/%Y')

    def salvar(self):
        self.get_tipo()
        self.get_value()
        self.get_text()
        self.get_data()

        self.conect_db()

        self.validar_valor()

        self.cursor.execute("""UPDATE devedores
                            SET tipo = (?), valor = (?), data = (?)
                            WHERE id_cliente = (?);""",(self.tipo, self.total, self.data, self.tupla[0]))
        self.conexao.commit()

        print('\nvalor atualizado')

        self.desconect_db()

        self.select_treeview()

        self.clear_input()

        self.insert_transacoes_clientes()
    
    def clear_input(self):
        self.input_valor.delete(0,END)
        self.txt_nome.config(text='Nome')
        self.txt_endereco.config(text='Endereço')
        self.txt_numero.config(text='Telefone')

    def pegando_ultimo_valor(self):

        self.cursor.execute("""SELECT valor FROM devedores
                            WHERE id_cliente = (?);""",(self.tupla[0],))
        self.ultimo_valor = self.cursor.fetchall()

        print('\nfoi pego saldo cliente:', self.ultimo_valor[0][0])

    def validar_valor(self):

        self.pegando_ultimo_valor()

        if self.tipo == 'Devendo':
            self.total = self.valor + float(self.ultimo_valor[0][0])
            print('devendo :', self.valor)
            print('saldo: ',self.total)
        elif self.tipo == 'Pagando':
            self.total = float(self.ultimo_valor[0][0]) - self.valor
            print('pagando: ',self.valor)
            print('saldo: ',self.total)
        
    def insert_transacoes_clientes(self):
        self.conect_db()

        self.cursor.execute("""INSERT INTO transacoes_devedores VALUES (null,(?),(?),(?),(?),(?),(?),(?))""",(self.tupla[0],self.tupla[1],self.tupla[2],self.tupla[3],self.tupla[4],self.valor,self.data))
        self.conexao.commit()

        print('\ntransação adicionada!')
        self.desconect_db()
            