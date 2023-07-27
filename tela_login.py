from tkinter import *
from tkinter import Tk
from tela_register import *
import sqlite3



class Tela_Login:

    bg_bottom = '#347355'
    fg_front = '#60BF81'
    font = 'arial 11'
    font_color = 'white'
    collor_button = '#223240'

    def config(self):
        self.root = Tk()
        
        self.root.title('Tela de login')
        self.root.config(background=self.bg_bottom)
        self.root.iconbitmap('img\icon_login.ico')
        self.root.geometry('240x200+500+250')
   
        self.root.mainloop()

    def labels(self):

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
                                command=Tela_register)
        self.button_cadastrar.place(relheight=0.13,relwidth=0.30,relx=0.50,rely=0.65)

    #----------------------------------

    def get_login(self):
        self.input_login_ = self.input_login.get()
        self.input_senha_ = self.input_senha.get()

        conexao = sqlite3.connect('BD\projeto_compras.db')
        cursor = conexao.cursor()
        
        cursor.execute('SELECT * FROM usuarios\
                    WHERE nome = ? AND senha = ?',(self.input_login_,self.input_senha_))
        login = cursor.fetchone()
 
        if login:
            print(login)
        else:
            print('user invalid')
            self.txt_login = Label(text='user invalid',
                            font=self.font,
                            background=self.bg_bottom,
                            fg='red')
            self.txt_login.place(relheight=0.10,relwidth=0.30,relx=0.38,rely=0.55)

        
