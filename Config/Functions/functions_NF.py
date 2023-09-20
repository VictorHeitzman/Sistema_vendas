from Config.Modulos.modulos import *
from Config.Functions.functions_db import DB

class Functions(DB):

    def salvar(self):
        self.get_values()

        self.conect_db()
        
        self.cursor.execute("""INSERT INTO nf VALUES(null,(?),(?),(?),(?),(?),(?),(?));""",
                            (self.numero,
                             self.fornecedor,
                             self.data_emissao,
                             self.data_vencimento,
                             self.valor_produto,
                             self.valor_nf,
                             self.descricao))
        self.conexao.commit()
        print('\nnf registrado na tabela')
        self.desconect_db()

        self.clear_inputs()

        self.carregarSomas()

        messagebox.showinfo('Aviso','Nf Salva')
    
    def enter(self, event):

        self.numero = self.input_numero.get()

        self.conect_db()

        self.cursor.execute("""SELECT * FROM nf
                            WHERE numero_nf = (?)""",(self.numero,))
        data = self.cursor.fetchall()

        if len(data) != 0:
            self.input_data_vencimento.config(state='normal')
            self.input_data_emissao.config(state='normal')
            
            self.clear_inputs()

            self.input_data_vencimento.delete(0,END)
            self.input_data_emissao.delete(0,END)
            
            for p in data:
                self.input_fornecedor.insert(0,p[2])
                self.input_data_emissao.insert(0,p[3])
                self.input_data_vencimento.insert(0,p[4])
                self.input_valor_produto.insert(0,p[5])
                self.input_valor_nf.insert(0,p[6])
                self.input_descricao.insert(END,p[7])

            self.input_data_vencimento.config(state='disabled')
            self.input_data_emissao.config(state='disabled')
        else:
            messagebox.showerror('Aviso','Nota Fiscal não encontrada!')
        self.desconect_db()

    def get_values(self):
        try:
            self.numero = int(self.input_numero.get())
            self.fornecedor = str(self.input_fornecedor.get()).upper()
            self.data_emissao = self.data_emissao_str.get()
            self.data_vencimento = self.data_emissao_str.get()
            self.valor_produto = round(float(str(self.input_valor_produto.get()).replace(',','.')),2)
            self.valor_nf = round(float(str(self.input_valor_nf.get()).replace(',','.')),2)
            self.descricao = str(self.input_descricao.get(1.0, "end-1c")).upper()

            print(f"""numero: {self.numero}
                    \ndescricao: {self.descricao}
                    \ndata_emissao: {self.data_emissao}
                    \ndata_vencimento: {self.data_vencimento}
                    \nvalor_produto: {self.valor_produto}
                    \nvalor_nf: {self.valor_nf}
                    \ndescricao: {self.descricao}""")
        except ValueError:
            messagebox.showerror('Aviso','Valide os campos')
    
    def clear_inputs(self):
        self.input_numero.delete(0,END)
        self.input_fornecedor.delete(0,END)
        self.input_valor_produto.delete(0,END)
        self.input_valor_nf.delete(0,END)
        self.input_descricao.delete("1.0", "end")
    
    def carregarSomas(self):
        self.soma_nf()
        self.soma_produto()
        self.quantidade_nf()

    def soma_nf(self):
        self.conect_db()

        self.cursor.execute("""SELECT SUM(valor_nota) FROM nf;""")

        query = self.cursor.fetchall()

        if query[0][0] != None:
            self.txt_valor_total_nf.config(text=f'{query[0][0]:,.2f}')
        else:
            self.txt_valor_total_nf.config(text=f'{0:,.2f}')
    
    def soma_produto(self):
        self.conect_db()

        self.cursor.execute("""SELECT SUM(valor_produto) FROM nf;""")

        query = self.cursor.fetchall()
        if query[0][0] != None:
            self.txt_valor_total_produto.config(text=f'{query[0][0]:,.2f}')
        else:
            self.txt_valor_total_produto.config(text=f'{0:,.2f}')
        
    def quantidade_nf(self):
        self.conect_db()

        self.cursor.execute("""SELECT count(id) FROM nf;""")

        query = self.cursor.fetchall()
        
        self.txt_total_quantidade.config(text=int(query[0][0]))
        
        self.desconect_db()

    def exportar_nf(self):

        self.conect_db()

        self.cursor.execute("""SELECT * FROM nf""")

        data = self.cursor.fetchall()

        lista = list(map(list,data))

        columns = ('id','numero_nf','fornecedor','data_emissao','data_vencimento','valor_produto','valor_nota','descricao')

        df = pd.DataFrame(lista,columns=columns)

        df.to_csv(f'Config/Transacoes/relatorio_nf_{date.today()}.csv',index=None, decimal=',', encoding='latin-1')

        self.desconect_db()

        messagebox.showinfo('Aviso','Arquivo de nf exportado.')