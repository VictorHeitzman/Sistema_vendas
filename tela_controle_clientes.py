from Modulos.modulos import *
from Coolors.style import Style
from Functions.functions_controle_clientes import Functions

class Screen_controle_cliente(Functions,Style):
    
    
    def __init__(self) -> None:
        self.root_controle_cliente = Tk()

        self.config()
        self.labels()
        self.select_treeview()

        self.root_controle_cliente.mainloop()
    
    def config(self):
        # self.root_stock = Toplevel()
        self.root_controle_cliente.title('Controle de Clientes')
        self.root_controle_cliente.config(background=self.background)
        self.root_controle_cliente.iconbitmap('img\icon_cliente.ico')
        self.root_controle_cliente.resizable(False,False)
        self.root_controle_cliente.geometry('700x600+250+50')
        # self.stock.attributes('-fullscreen',True)

        # self.root_stock.focus_force()
        # self.root_stock.grab_set()

    def labels(self):
        self.txt_nome = Label(self.root_controle_cliente,background=self.background,fg=self.font_color,font='arial 20',text='Nome')
        self.txt_nome.pack(ipady=15)

        self.txt_endereco = Label(self.root_controle_cliente,background=self.background,fg=self.font_color,font='arial 20',text='Endereço')
        self.txt_endereco.pack(ipady=15)

        self.txt_numero = Label(self.root_controle_cliente,background=self.background,fg=self.font_color,font='arial 20',text='Telefone')
        self.txt_numero.pack(ipady=10)

        self.resp = StringVar()
        self.tipo_pagando = Radiobutton(self.root_controle_cliente,background=self.background, text='Pagando',variable=self.resp, value='Pagando',command=self.get_tipo)
        self.tipo_devendo = Radiobutton(self.root_controle_cliente,background=self.background, text='Devendo',variable=self.resp, value='Devendo',command=self.get_tipo)
        self.tipo_pagando.pack()
        self.tipo_devendo.pack()

        self.txt_valor = Label(self.root_controle_cliente,text='Valor:',font='arial 20',background=self.background,fg=self.font_color)
        self.txt_valor.place(relheight=0.09,relwidth=0.15,relx=0.30,rely=0.42)
        
        self.input_valor = Entry(self.root_controle_cliente,font='arial 15')
        self.input_valor.place(relheight=0.09,relwidth=0.15,relx=0.43,rely=0.42)

        self.button_salvar = Button(self.root_controle_cliente,text='Salvar',background=self.collor_button,fg=self.font_color,command=self.salvar)
        self.button_salvar.place(relheight=0.05,relwidth=0.10,relx=0.15,rely=0.50)

        columns = ('id','nome','endereco','numero','tipo','valor')
        self.treeview_cliente = ttk.Treeview(self.root_controle_cliente,columns=columns, show='headings')

        self.treeview_cliente.heading('#1',text='ID')
        self.treeview_cliente.heading('#2',text='Nome')
        self.treeview_cliente.heading('#3',text='Endereço')
        self.treeview_cliente.heading('#4',text='Numero')
        self.treeview_cliente.heading('#5',text='Tipo')
        self.treeview_cliente.heading('#6',text='Valor')

        self.treeview_cliente.column('#1',width=1)
        self.treeview_cliente.column('#2',width=50)
        self.treeview_cliente.column('#3',width=50)
        self.treeview_cliente.column('#4',width=50)
        self.treeview_cliente.column('#5',width=50)
        self.treeview_cliente.column('#6',width=30)

        self.scrollist = Scrollbar(self.root_controle_cliente)
        self.treeview_cliente.config(yscrollcommand=self.scrollist)

        self.scrollist.place(relheight=0.40,relwidth=0.03,relx=0.91,rely=0.57)

        self.treeview_cliente.place(relheight=0.40,relwidth=0.90,relx=0.03,rely=0.57)
        self.treeview_cliente.bind('<Double-1>',self.double_click)


if __name__ == '__main__':
    root = Screen_controle_cliente()