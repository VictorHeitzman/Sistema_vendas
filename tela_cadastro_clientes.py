from Modulos.modulos import *

from Coolors.style import  Style
from Functions.functions_cliente import Functions

class Screen_cadastro_cliente(Functions,Style):

    def __init__(self):
        
        self.root_cadastro_cliente = Tk()
        
        self.config()
        self.labels()


        self.root_cadastro_cliente.mainloop()
    
    def config(self):

        # self.root_cadastro_cliente = Toplevel()
        self.root_cadastro_cliente.title('Cadastro de clientes')
        self.root_cadastro_cliente.config(background=self.background)
        self.root_cadastro_cliente.iconbitmap('img\icon_cliente.ico')
        self.root_cadastro_cliente.resizable(False,False)
        self.root_cadastro_cliente.geometry('400x200+250+50')
        # self.root_cadastro_cliente.attributes('-fullscreen',True)

        # self.root_cadastro_cliente.focus_force()
        # self.root_cadastro_cliente.grab_set()


    
    def labels(self):

    # --------------------------- ID ---------------------------------
        self.txt_id = Label(self.root_cadastro_cliente,text='ID:',font=self.font,background=self.background,fg=self.font_color)
        self.txt_id.place(relheight=0.08,relwidth=0.20, relx=0.03,rely=0.10)

        self.input_id = Entry(self.root_cadastro_cliente)
        self.input_id.place(relheight=0.08,relwidth=0.50, relx=0.25,rely=0.10)

        self.input_id.config(state='disabled')
    # --------------------------------------------------------------------

    # --------------------------- Nome ---------------------------------
        self.txt_nome = Label(self.root_cadastro_cliente,text='Nome:',font=self.font,background=self.background,fg=self.font_color)
        self.txt_nome.place(relheight=0.08,relwidth=0.20, relx=0.03,rely=0.25)

        self.input_nome = Entry(self.root_cadastro_cliente)
        self.input_nome.place(relheight=0.08,relwidth=0.50, relx=0.25,rely=0.25)
    # --------------------------------------------------------------------
        
    # --------------------------- Endereço ---------------------------------
        self.txt_endereco = Label(self.root_cadastro_cliente,text='Endereço:',font=self.font,background=self.background,fg=self.font_color)
        self.txt_endereco.place(relheight=0.08,relwidth=0.20, relx=0.03,rely=0.40)

        self.input_endereco = Entry(self.root_cadastro_cliente)
        self.input_endereco.place(relheight=0.08,relwidth=0.50, relx=0.25,rely=0.40)
    # -------------------------------------------------------------------------
    
    # --------------------------- Telefone -------------------------------------
        self.txt_telefone = Label(self.root_cadastro_cliente,text='Telefone:',font=self.font,background=self.background,fg=self.font_color)
        self.txt_telefone.place(relheight=0.08,relwidth=0.20, relx=0.03,rely=0.55)

        self.input_telefone = Entry(self.root_cadastro_cliente)
        self.input_telefone.place(relheight=0.08,relwidth=0.50, relx=0.25,rely=0.55)
    # ---------------------------------------------------------------------------

    # --------------------------- button salvar ---------------------------------
        self.button_adicionar = Button(self.root_cadastro_cliente,text='Adicionar',font=self.font,background=self.collor_button,fg=self.font_color)
        self.button_adicionar.place(relheight=0.10,relwidth=0.20, relx=0.03,rely=0.70)
    # ---------------------------------------------------------------------------

    # --------------------------- button Editar ---------------------------------
        self.button_adicionar = Button(self.root_cadastro_cliente,text='Editar',font=self.font,background=self.collor_button,fg=self.font_color)
        self.button_adicionar.place(relheight=0.10,relwidth=0.20, relx=0.25,rely=0.70)
    # ---------------------------------------------------------------------------

    # --------------------------- button Excluir ---------------------------------
        self.button_adicionar = Button(self.root_cadastro_cliente,text='Excluir',font=self.font,background=self.collor_button,fg=self.font_color)
        self.button_adicionar.place(relheight=0.10,relwidth=0.20, relx=0.47,rely=0.70)
    # ----------------------------------------------------------------------------






if __name__ == '__main__':
    root = Screen_cadastro_cliente()