from tkinter import *
from tkinter import Tk
import sqlite3

class Config:
    
    def __init__(self) -> None:
        self.root = Tk()
        self.config_tela_login()
        
    
    def config_tela_login(self):
        self.bg_bottom = '#347355'
        self.fg_front = '#60BF81'
        self.font = 'arial 11'
        self.font_color = 'white'
        self.collor_button = '#223240'

        self.root.title('Tela de login')
        self.root.config(background=self.bg_bottom)
        self.root.iconbitmap('img\icon_login.ico')
        self.root.geometry('240x200+500+250')
        
    #--------------Titulo tela_login----------------- 
        self.titulo_login = Label(self.root,
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

        self.input_login = Entry(self.root,
                            background=self.bg_bottom)
        self.input_login.place(relheight=0.10,relwidth=0.50,relx=0.30,rely=0.25)
    #------------------------------------------------


    #--------------------senha------------------------ 
        self.txt_senha = Label(text='Senha',
                            font=self.font,
                            background=self.bg_bottom,
                            fg=self.font_color)
        self.txt_senha.place(relheight=0.10,relwidth=0.20,relx=0.10,rely=0.45)

        self.input_senha = Entry(self.root,
                            background=self.bg_bottom)
        self.input_senha.place(relheight=0.10,relwidth=0.50,relx=0.30,rely=0.45)
    #------------------------------------------------


    #-----------------button_login--------------------
        self.button_login = Button(self.root,
                                text='Login',
                                font=self.font,
                                background=self.collor_button,
                                fg=self.font_color,
                                command=self.get_login)
        self.button_login.place(relheight=0.13,relwidth=0.20,relx=0.25,rely=0.65)
    #-------------------------------------------------


    #-----------------button_cadastrar--------------------
        self.button_cadastrar = Button(self.root,
                                text='Cadastrar',
                                font=self.font,
                                background=self.collor_button,
                                fg=self.font_color,
                                command=self.tela_register)
        self.button_cadastrar.place(relheight=0.13,relwidth=0.30,relx=0.50,rely=0.65)

    #----------------------------------

        self.root.mainloop()

    def get_login(self):
        self.input_login_ = self.input_login.get()
        self.input_senha_ = self.input_senha.get()

        conexao = sqlite3.connect('BD\projeto_compras.db')
        cursor = conexao.cursor()
        
        cursor.execute('SELECT * FROM usuarios\
                    WHERE nome = ? AND senha = ?',(self.input_login_,self.input_senha_))
        login = cursor.fetchone()
 
        if login:
            self.root.destroy()
            self.tela_register()
            
        else:
            print('user invalid')
            self.txt_login = Label(text='user invalid',
                            font=self.font,
                            background=self.bg_bottom,
                            fg='red')
            self.txt_login.place(relheight=0.10,relwidth=0.30,relx=0.38,rely=0.55)

    def tela_register(self):

        self.root.destroy()
        self.root = Tk()
        
        self.root.title("Tela de Cadastro")
        self.root.geometry('300x200+450+150')
        self.root.config(background=self.bg_bottom)
        
    #----------------título------------------
        self.txt_title = Label(text="register user",
                               background=self.bg_bottom,
                               font=self.font)
        self.txt_title.place(relheight=0.12, relwidth=0.50,relx=0.25,rely=0.05)
    #-----------------------------------------

    #------------------user-------------------
        self.txt_user = Label(text='user',
                            font=self.font,
                            background=self.bg_bottom,
                            fg=self.font_color)
        self.txt_user.place(relheight=0.10,relwidth=0.20,relx=0.10,rely=0.25)

        self.input_user_register = Entry(self.root,
                            background=self.bg_bottom)
        self.input_user_register.place(relheight=0.10,relwidth=0.50,relx=0.30,rely=0.25)
    #-----------------------------------------

    
    #------------------senha------------------
        self.txt_senha = self.txt_user = Label(text='password',
                            font=self.font,
                            background=self.bg_bottom,
                            fg=self.font_color)
        self.txt_senha.place(relheight=0.10,relwidth=0.35,relx=0.01,rely=0.50)

        self.input_senha_register = Entry(self.root,
                            background=self.bg_bottom)
        self.input_senha_register.place(relheight=0.10,relwidth=0.50,relx=0.30,rely=0.50)
    #-----------------------------------------

    #--------------button_salvar--------------

        self.button_salvar = Button(self.root,
                                    text="Save",
                                    background=self.collor_button,
                                    font=self.font,
                                    fg=self.font_color,
                                    command=self.register_user)
        self.button_salvar.place(relheight=0.13,relwidth=0.30,relx=0.50,rely=0.65)

    def register_user(self):

        conexao = sqlite3.connect('BD\projeto_compras.db')
        cursor = conexao.cursor()

        print('conect sucess')

        cursor.execute('INSERT INTO USUARIOS VALUES(?,?,?)',(self.input_user_register.get(),self.input_senha_register.get()))
        conexao.commit()
        
        if conexao.commit():
            print(f'user {self.input_login.get()} and {self.input_senha.get()} insert sucess')
        

