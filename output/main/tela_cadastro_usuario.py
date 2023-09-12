from Config.Modulos.modulos import *
from Config.Functions.functions_cadastre_user import Functions
from Config.Coolors.style import  Style
class Screen_cadastre_user(Functions, Style):

    def __init__(self):


        
        self.config()
        self.labels()
        self.select_list()
        


    def config(self):
        self.root_register = Toplevel()
        self.root_register.title("Tela de Cadastro")
        self.root_register.iconbitmap('Config\img\icon_login.ico')
        self.root_register.geometry('400x400+450+150')
        self.root_register.config(background=self.background)
 
        self.root_register.focus_force()
        self.root_register.grab_set()

    def labels(self):
        #----------------título------------------
        self.txt_title = Label(self.root_register,
                                text="register user",
                                font='arial 15',
                                background=self.background,
                                fg=self.font_color)
        self.txt_title.place(relheight=0.12, relwidth=0.50,relx=0.25,rely=0.05)
    #-----------------------------------------

    #------------------user-------------------
        self.txt_user = Label(self.root_register,
                            text='User',
                            font=self.font,
                            background=self.background,
                            fg=self.font_color)
        self.txt_user.place(relheight=0.10,relwidth=0.20,relx=0.10,rely=0.20)

        self.input_user_register = Entry(self.root_register,
                            background=self.background)
        self.input_user_register.place(relheight=0.08,relwidth=0.50,relx=0.30,rely=0.20)
    #-----------------------------------------


    #------------------senha------------------
        self.txt_senha = Label(self.root_register,
                            text='Password',
                            font=self.font,
                            background=self.background,
                            fg=self.font_color)
        self.txt_senha.place(relheight=0.08,relwidth=0.35,relx=0.01,rely=0.35)

        self.input_senha_register = Entry(self.root_register,
                            background=self.background)
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
        self.treeview.bind('<Double-1>', self.double_click)
    #-----------------------------------------


if __name__ == '__main__':
    screen_cadastre_user = Screen_cadastre_user()