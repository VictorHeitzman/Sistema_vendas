from Config.Modulos.modulos import *
from Config.Functions.functions_db import DB

class Functions(DB):

    def salvar(self):
        self.get_values()

        self.conect_db()
        
        self.cursor.execute("""INSERT INTO nf VALUES(null,(?),(?),(?),(?),(?),(?),(?));""",
                            (self.numero,
                             self.descricao,
                             self.data_emissao,
                             self.data_vencimento,
                             self.valor_produto,
                             self.valor_nf,
                             self.descricao))
        self.conexao.commit()
        print('\nnf registrado na tabela')
        self.desconect_db()

        self.clear_inputs()
        messagebox.showerror('Aviso','Nf Salva')
    
    def enter(self, event):
        pass
# ------------------------Calendarios --------------------------------------
    def abrir_calendario_emissao(self):
        self.calendario_emissao = Calendar(self.root_nf, locale='pt_br')
        self.calendario_emissao.place(relheight=0.30,relwidth=0.35,relx=0.23,rely=0.15)
        
        self.button_insert_date_emissao = Button(self.root_nf,font=self.font,background=self.collor_button,fg=self.font_color,text='Iserir data',command=self.getDate_emissao)
        self.button_insert_date_emissao.place(relheight=0.03,relwidth=0.35,relx=0.23,rely=0.45) 

    def getDate_emissao(self):
        
        self.data = self.calendario_emissao.get_date()
        self.calendario_emissao.destroy()
        self.button_insert_date_emissao.destroy()
        self.input_data_emissao.config(state='normal')
        self.input_data_emissao.delete(0,END)
        self.input_data_emissao.insert(END,self.data)
        self.input_data_emissao.config(state='disabled')

    def abrir_calendario_vencimento(self):
        self.calendario_vencimento = Calendar(self.root_nf, locale='pt_br')
        self.calendario_vencimento.place(relheight=0.30,relwidth=0.35,relx=0.61,rely=0.15)
        
        self.button_insert_date_vencimento = Button(self.root_nf,font=self.font,background=self.collor_button,fg=self.font_color,text='Iserir data',command=self.getDate_vencimento)
        self.button_insert_date_vencimento.place(relheight=0.03,relwidth=0.35,relx=0.61,rely=0.45) 

    def getDate_vencimento(self):
        
        self.data = self.calendario_vencimento.get_date()
        self.calendario_vencimento.destroy()
        self.button_insert_date_vencimento.destroy()
        self.input_data_vencimento.config(state='normal')
        self.input_data_vencimento.delete(0,END)
        self.input_data_vencimento.insert(END,self.data)
        self.input_data_vencimento.config(state='disabled')
    
# ---------------------------------------------------------------------------

    def get_values(self):
        try:
            self.numero = int(self.input_numero.get())
            self.fornecedor = str(self.input_fornecedor).upper()
            self.data_emissao = str(self.input_data_emissao.get())
            self.data_vencimento = str(self.input_data_vencimento.get())
            self.valor_produto = round(float(str(self.input_valor_produto.get()).replace(',','.')),2)
            self.valor_nf = round(float(str(self.input_valor_nf.get()).replace(',','.')),2)
            self.descricao = str(self.input_descricao.get(1.0, "end-1c")).upper()

            # print(f"""numero: {self.numero}
            #         \ndescricao: {self.descricao}
            #         \ndata_emissao: {self.data_emissao}
            #         \ndata_vencimento: {self.data_vencimento}
            #         \nvalor_produto: {self.valor_produto}
            #         \nvalor_nf: {self.valor_nf}
            #         \ndescricao: {self.descricao}""")
        except ValueError:
            messagebox.showerror('Aviso','Valide os campos')
    
    def clear_inputs(self):
        self.input_numero.delete(0,END)
        self.input_fornecedor.delete(0,END)
        self.input_valor_produto.delete(0,END)
        self.input_valor_nf.delete(0,END)
        self.input_descricao.delete("1.0", "end")
    
    def soma_nf(self):
        pass

    def soma_produto(self):
        pass

    def quantidade_nf(self):
        pass