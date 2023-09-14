from Config.Modulos.modulos import *

from Config.Coolors.style import  Style
from Config.Functions.functions_NF import Functions

class Screen_NF(Functions,Style):

    def __init__(self):
        
        self.root_nf = Tk()
        
        self.config()
        self.frames()
        self.labels()


        self.root_nf.mainloop()
    
    def config(self):

        # self.root_nf = Toplevel()
        self.root_nf.title('Cadastro de clientes')
        self.root_nf.config(background=self.background)
        self.root_nf.iconbitmap('Config\img\icon_nf.ico')
        self.root_nf.resizable(False,False)
        self.root_nf.geometry('600x600+250+50')
        # self.root_nf.attributes('-fullscreen',True)

        # self.root_nf.focus_force()
        # self.root_nf.grab_set()


    
    def labels(self):
    #--------------------------------------numero-------------------------------------
        self.txt_numero = Label(self.root_nf,text='Número NF',background=self.background,font=self.font,fg=self.font_color)
        self.txt_numero.place(relx=0.03,rely=0.05)

        self.input_numero = Entry(self.root_nf)
        self.input_numero.place(relwidth=0.53,relx=0.23,rely=0.05)

        self.input_numero.bind('<Return>',self.enter)
    #-------------------------------------------------------------------------------------

    #--------------------------------------fornecedor-------------------------------------
        self.txt_fornecedor = Label(self.root_nf,text='Fornecedor',background=self.background,font=self.font,fg=self.font_color)
        self.txt_fornecedor.place(relx=0.03,rely=0.10)

        self.input_fornecedor = Entry(self.root_nf)
        self.input_fornecedor.place(relwidth=0.53,relx=0.23,rely=0.10) 
    #-------------------------------------------------------------------------------------

    #--------------------------------------data_emissao-------------------------------------
        self.txt_data_emissao = Button(self.root_nf,text='Data Emissão',background=self.collor_button,font=self.font,fg=self.font_color,command=self.abrir_calendario_emissao)
        self.txt_data_emissao.place(relheight=0.04,relx=0.03,rely=0.15)

        self.input_data_emissao = Entry(self.root_nf)
        self.input_data_emissao.place(relwidth=0.15,relx=0.23,rely=0.15) 
        
        self.input_data_emissao.insert(END,str(date.today().strftime('%d/%m/%y')))
        self.input_data_emissao.config(state='disabled')
    #-------------------------------------------------------------------------------------

    #--------------------------------------data_vencimento-------------------------------------
        self.txt_data_vencimento = Button(self.root_nf,text='Data Vencimento',background=self.collor_button,font=self.font,fg=self.font_color,command=self.abrir_calendario_vencimento)
        self.txt_data_vencimento.place(relheight=0.04,relx=0.39,rely=0.15)

        self.input_data_vencimento = Entry(self.root_nf)
        self.input_data_vencimento.place(relwidth=0.15,relx=0.61,rely=0.15) 

        self.input_data_vencimento.insert(END,str(date.today().strftime('%d/%m/%y')))
        self.input_data_vencimento.config(state='disabled')
    #-------------------------------------------------------------------------------------

    #--------------------------------------valor_produto-------------------------------------
        self.txt_valor_produto = Label(self.root_nf,text='Valor Produto',background=self.background,font=self.font,fg=self.font_color)
        self.txt_valor_produto.place(relx=0.03,rely=0.20)

        self.input_valor_produto = Entry(self.root_nf)
        self.input_valor_produto.place(relwidth=0.20,relx=0.23,rely=0.20) 
    #-------------------------------------------------------------------------------------

    #--------------------------------------valor_nf-------------------------------------
        self.txt_valor_nf = Label(self.root_nf,text='Valor NF',background=self.background,font=self.font,fg=self.font_color)
        self.txt_valor_nf.place(relx=0.03,rely=0.25)

        self.input_valor_nf = Entry(self.root_nf)
        self.input_valor_nf.place(relwidth=0.20,relx=0.23,rely=0.25)  
    #-------------------------------------------------------------------------------------

    #--------------------------------------descricao-------------------------------------
        self.txt_descricao = Label(self.root_nf,text='Descrição',background=self.background,font=self.font,fg=self.font_color)
        self.txt_descricao.place(relx=0.03,rely=0.30)

        self.input_descricao = Text(self.root_nf)
        self.input_descricao.place(relheight=0.15,relwidth=0.53,relx=0.23,rely=0.30) 
    #-------------------------------------------------------------------------------------

    #--------------------------------------salvar-------------------------------------
        self.button_salvar = Button(self.root_nf,text='Salvar',background=self.collor_button,font=self.font,fg=self.font_color,command=self.salvar)
        self.button_salvar.place(relwidth=0.15,relx=0.03,rely=0.46)
    #-------------------------------------------------------------------------------------

    #--------------------------------------frame total produto-------------------------------------
        self.txt_total_produto = Label(self.frame_total_produto,text='Total Produto',background=self.background,font='arial 15 bold',fg=self.font_color)
        self.txt_total_produto.pack()

        self.txt_valor_total_produto = Label(self.frame_total_produto,text='0',background=self.background,font='arial 13',fg=self.font_color)
        self.txt_valor_total_produto.pack()
    #-------------------------------------------------------------------------------------
        
    #--------------------------------------frame total nf-------------------------------------
        self.txt_total_nf = Label(self.frame_total_nf,text='Total NF',background=self.background,font='arial 15 bold',fg=self.font_color)
        self.txt_total_nf.pack()

        self.txt_valor_total_nf = Label(self.frame_total_nf,text='0',background=self.background,font='arial 13',fg=self.font_color)
        self.txt_valor_total_nf.pack()
    #-------------------------------------------------------------------------------------
    
    #--------------------------------------frame quantidade-------------------------------------
        self.txt_quantidade_nf = Label(self.frame_quantidade_nf,text='Quantidade',background=self.background,font='arial 15 bold',fg=self.font_color)
        self.txt_quantidade_nf.pack()

        self.txt_total_quantidade = Label(self.frame_quantidade_nf,text='0',background=self.background,font='arial 13',fg=self.font_color)
        self.txt_total_quantidade.pack()
    #-------------------------------------------------------------------------------------
    
    #--------------------------------------button exportar transações-------------------------------------
        self.button_exportar = Button(self.root_nf,text='Exportar Notas Fiscais',background=self.collor_button,font=self.font,fg=self.font_color)
        self.button_exportar.place(relwidth=0.26,relx=0.20,rely=0.46)
    #-------------------------------------------------------------------------------------

    

    
    

    def frames(self):
    # -------------------------------------------frame total produto------------------------------------
        self.frame_total_produto = Frame(self.root_nf,background=self.background,highlightthickness=2,highlightbackground=self.collor_button)
        self.frame_total_produto.place(relheight=0.20,relwidth=0.25,relx=0.03,rely=0.56)
    # -------------------------------------------------------------------------------------------------

    # -------------------------------------------frame total total NF------------------------------------
        self.frame_total_nf = Frame(self.root_nf,background=self.background,highlightthickness=2,highlightbackground=self.collor_button)
        self.frame_total_nf.place(relheight=0.20,relwidth=0.25,relx=0.30,rely=0.56)
    # -------------------------------------------------------------------------------------------------

    # -------------------------------------------frame quantidade NF------------------------------------
        self.frame_quantidade_nf = Frame(self.root_nf,background=self.background,highlightthickness=2,highlightbackground=self.collor_button)
        self.frame_quantidade_nf.place(relheight=0.20,relwidth=0.25,relx=0.57,rely=0.56)
    # -------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    root = Screen_NF()