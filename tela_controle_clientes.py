from Config.Modulos.modulos import *
from Config.Coolors.style import Style
from Config.Functions.functions_controle_clientes import Functions

class Screen_controle_cliente(Functions,Style):
    
    
    def __init__(self) -> None:
        # self.root_controle_cliente = Tk()

        self.config()
        self.labels()
        self.select_treeview()

        # self.root_controle_cliente.mainloop()
    
    def config(self):
        self.root_controle_cliente = Toplevel()
        self.root_controle_cliente.title('Controle de Clientes')
        self.root_controle_cliente.config(background=self.background)
        self.root_controle_cliente.iconbitmap('Config\img\icon_cliente.ico')

        self.root_controle_cliente.geometry('700x600+250+50')
        # self.stock.attributes('-fullscreen',True)

        self.root_controle_cliente.focus_force()
        self.root_controle_cliente.grab_set()

    def labels(self):
        self.txt_nome = Label(self.root_controle_cliente,background=self.background,fg=self.font_color,font='arial 11',text='Nome')
        self.txt_nome.pack(ipady=15)

        self.txt_endereco = Label(self.root_controle_cliente,background=self.background,fg=self.font_color,font='arial 11',text='Endereço')
        self.txt_endereco.pack(ipady=15)

        self.txt_numero = Label(self.root_controle_cliente,background=self.background,fg=self.font_color,font='arial 11',text='Telefone')
        self.txt_numero.pack(ipady=10)

        self.resp = StringVar()
        self.tipo_pagando = Radiobutton(self.root_controle_cliente,background=self.background, text='Pagando',variable=self.resp, value='Pagando',command=self.get_tipo)
        self.tipo_devendo = Radiobutton(self.root_controle_cliente,background=self.background, text='Devendo',variable=self.resp, value='Devendo',command=self.get_tipo)
        self.tipo_pagando.pack()
        self.tipo_devendo.pack()

        self.txt_valor = Label(self.root_controle_cliente,text='Valor:',font='arial 15',background=self.background,fg=self.font_color)
        self.txt_valor.place(relx=0.32,rely=0.34)
        
        self.input_valor = Entry(self.root_controle_cliente,font='arial 15')
        self.input_valor.place(relheight=0.05,relwidth=0.15,relx=0.43,rely=0.34)

        self.txt_descricao = Label(self.root_controle_cliente,background=self.background,fg=self.font_color,font='arial 11',text='Descrição')
        self.txt_descricao.place(relx=0.32,rely=0.40)

        self.input_descricao = Text(self.root_controle_cliente)
        self.input_descricao.place(relheight=0.15,relwidth=0.30,relx=0.43,rely=0.40)

        self.button_salvar = Button(self.root_controle_cliente,text='Salvar',background=self.collor_button,fg=self.font_color,command=self.salvar)
        self.button_salvar.place(relheight=0.05,relwidth=0.10,relx=0.15,rely=0.50)

        self.txt_devedores = Label(self.root_controle_cliente,text='Devedores',font=self.font,background=self.background,fg=self.font_color)
        self.txt_devedores.place(relheight=0.05,relwidth=0.10,relx=0.03,rely=0.55)

        columns = ('id','nome','endereco','numero','valor')
        self.treeview_cliente = ttk.Treeview(self.root_controle_cliente,columns=columns, show='headings')

        self.treeview_cliente.heading('#1',text='ID')
        self.treeview_cliente.heading('#2',text='Nome')
        self.treeview_cliente.heading('#3',text='Endereço')
        self.treeview_cliente.heading('#4',text='Numero')
        self.treeview_cliente.heading('#5',text='Valor Devendo')

        self.treeview_cliente.column('#1',width=1)
        self.treeview_cliente.column('#2',width=50)
        self.treeview_cliente.column('#3',width=50)
        self.treeview_cliente.column('#4',width=50)
        self.treeview_cliente.column('#5',width=40)

        self.scrollist = Scrollbar(self.root_controle_cliente)
        self.treeview_cliente.config(yscrollcommand=self.scrollist)

        self.scrollist.place(relheight=0.35,relwidth=0.03,relx=0.91,rely=0.60)

        self.treeview_cliente.place(relheight=0.35,relwidth=0.90,relx=0.03,rely=0.60)
        self.treeview_cliente.bind('<Double-1>',self.double_click)


if __name__ == '__main__':
    root = Screen_controle_cliente()