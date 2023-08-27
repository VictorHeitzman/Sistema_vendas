from modulos import *
from functions import Functions





class Tela_login(Functions):
#---------------------- var ---------------------------
    bg_bottom = '#347355'
    fg_front = '#60BF81'
    font = 'arial 11'
    font_color = 'white'
    collor_button = '#223240'

    def __init__(self):
        self.root_login = Tk()
        self.config()
        self.labels()
        
        self.root_login.mainloop()

    def config(self):
        self.root_login.title('Tela de login')
        self.root_login.config(background=self.bg_bottom)
        self.root_login.iconbitmap('img\icon_login.ico')
        self.root_login.geometry('240x200+500+250')

    def labels(self):
#--------------Titulo tela_login----------------- 
        self.titulo_login = Label(self.root_login,
                            text='Tela de Login',
                            font='arial 15',
                            background=self.bg_bottom,
                            fg=self.font_color)
        self.titulo_login.place(relheight=0.12, relwidth=0.50,relx=0.25,rely=0.05)
#------------------------------------------------ 


#--------------------Login------------------------ 
        self.txt_login = Label(text='Login',
                            font=self.font,
                            background=self.bg_bottom,
                            fg=self.font_color)
        self.txt_login.place(relheight=0.10,relwidth=0.20,relx=0.10,rely=0.25)

        self.input_login = Entry(self.root_login,
                            background=self.bg_bottom)
        self.input_login.place(relheight=0.10,relwidth=0.50,relx=0.30,rely=0.25)
    #------------------------------------------------


    #--------------------senha------------------------ 
        self.txt_senha = Label(text='Senha',
                            font=self.font,
                            background=self.bg_bottom,
                            fg=self.font_color)
        self.txt_senha.place(relheight=0.10,relwidth=0.20,relx=0.10,rely=0.45)

        self.input_senha = Entry(self.root_login,
                            background=self.bg_bottom)
        self.input_senha.place(relheight=0.10,relwidth=0.50,relx=0.30,rely=0.45)
    #------------------------------------------------


    #-----------------button_login--------------------
        self.button_login = Button(self.root_login,
                                text='Login',
                                font=self.font,
                                background=self.collor_button,
                                fg=self.font_color,
                                command=self.login)
        self.button_login.place(relheight=0.13,relwidth=0.20,relx=0.25,rely=0.65)
    #-------------------------------------------------


    #-----------------button_cadastrar--------------------
        self.button_cadastrar = Button(self.root_login,
                                text='Cadastrar',
                                font=self.font,
                                background=self.collor_button,
                                fg=self.font_color,
                                command=self.tela_register)
        self.button_cadastrar.place(relheight=0.13,relwidth=0.30,relx=0.50,rely=0.65)
        
    def tela_register(self):
        
        self.config_tela_register()
        self.label_tela_register()
        self.select_list()

    def config_tela_register(self):
        self.root_register = Toplevel()
        self.root_register.title("Tela de Cadastro")
        self.root_register.geometry('400x400+450+150')
        self.root_register.config(background=self.bg_bottom)
        self.root_register.transient(self.root_login)
        self.root_register.focus_force()
        self.root_register.grab_set()

    def label_tela_register(self):
        #----------------título------------------
        self.txt_title = Label(self.root_register,
                                text="register user",
                                font='arial 15',
                                background=self.bg_bottom,
                                fg=self.font_color)
        self.txt_title.place(relheight=0.12, relwidth=0.50,relx=0.25,rely=0.05)
    #-----------------------------------------

    #------------------user-------------------
        self.txt_user = Label(self.root_register,
                            text='User',
                            font=self.font,
                            background=self.bg_bottom,
                            fg=self.font_color)
        self.txt_user.place(relheight=0.10,relwidth=0.20,relx=0.10,rely=0.20)

        self.input_user_register = Entry(self.root_register,
                            background=self.bg_bottom)
        self.input_user_register.place(relheight=0.08,relwidth=0.50,relx=0.30,rely=0.20)
    #-----------------------------------------


    #------------------senha------------------
        self.txt_senha = Label(self.root_register,
                            text='Password',
                            font=self.font,
                            background=self.bg_bottom,
                            fg=self.font_color)
        self.txt_senha.place(relheight=0.08,relwidth=0.35,relx=0.01,rely=0.35)

        self.input_senha_register = Entry(self.root_register,
                            background=self.bg_bottom)
        self.input_senha_register.place(relheight=0.08,relwidth=0.50,relx=0.30,rely=0.35)
    #-----------------------------------------

    #--------------button_salvar--------------
        self.button_salvar = Button(self.root_register,
                                    text="Save",
                                    background=self.collor_button,
                                    font=self.font,
                                    fg=self.font_color,
                                    command=self.register_user)
        self.button_salvar.place(relheight=0.08,relwidth=0.20,relx=0.60,rely=0.50)
    #-----------------------------------------

    #--------------button_delete--------------
        self.button_delete = Button(self.root_register,
                                    text="Delete",
                                    background=self.collor_button,
                                    font=self.font,
                                    fg=self.font_color,
                                    command=self.delete_user)
        self.button_delete.place(relheight=0.08,relwidth=0.20,relx=0.30,rely=0.50)
    #-----------------------------------------

    #--------------Treeview-------------------
        self.treeview = ttk.Treeview(self.root_register,columns=('col1','col2','col3'))
        
        self.treeview.heading('#0',text='')
        self.treeview.heading('#1',text='Código')
        self.treeview.heading('#2',text='User')
        self.treeview.heading('#3',text='Password')

        self.treeview.column('#0',width=1)
        self.treeview.column('#1',width=100)
        self.treeview.column('#2',width=100)
        self.treeview.column('#3',width=100)

        self.scroolList = Scrollbar(self.root_register,
                                    orient='vertical')
        self.treeview.config(yscrollcommand=self.scroolList.set)
        self.scroolList.place(relheight=0.30, relwidth=0.05, relx=0.93,rely=0.65)

        self.treeview.place(relheight=0.30,relwidth=0.96,relx=0.02,rely=0.65)
        self.treeview.bind('<<TreeviewSelect>>', self.double_click)
    #-----------------------------------------

if __name__ == '__main__':
    app = Tela_login()