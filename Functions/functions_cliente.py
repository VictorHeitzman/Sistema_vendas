from Modulos.modulos import *
from Functions.functions_db import DB 
from Coolors.style import *



class Functions(DB,Style):
    def get_values(self):
        try:
            self.id = int(self.input_id.get())
            self.nome = str(self.input_nome.get())
            self.endereco = str(self.input_endereco.get())
            self.telefone = int(self.input.get())
        except:
            messagebox.showinfo('Aviso','Preencha todos os campos')
    