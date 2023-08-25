from tkinter import *
from tkinter import Tk
import sqlite3

bg_bottom = '#347355'
fg_front = '#60BF81'
font = 'arial 11'
font_color = 'white'
collor_button = '#223240'


def tela_login():

    global root_login
    global input_login
    global input_senha

    root_login = Tk()

    root_login.title('Tela de login')
    root_login.config(background=bg_bottom)
    root_login.iconbitmap('img\icon_login.ico')
    root_login.geometry('240x200+500+250')
    
#--------------Titulo tela_login----------------- 
    titulo_login = Label(root_login,
                            text='Tela de Login',
                            font='arial 15',
                            background=bg_bottom,
                            fg=font_color)
    titulo_login.place(relheight=0.12, relwidth=0.50,relx=0.25,rely=0.05)
#------------------------------------------------ 


#--------------------Login------------------------ 
    txt_login = Label(text='Login',
                        font=font,
                        background=bg_bottom,
                        fg=font_color)
    txt_login.place(relheight=0.10,relwidth=0.20,relx=0.10,rely=0.25)

    input_login = Entry(root_login,
                        background=bg_bottom)
    input_login.place(relheight=0.10,relwidth=0.50,relx=0.30,rely=0.25)
#------------------------------------------------


#--------------------senha------------------------ 
    txt_senha = Label(text='Senha',
                        font=font,
                        background=bg_bottom,
                        fg=font_color)
    txt_senha.place(relheight=0.10,relwidth=0.20,relx=0.10,rely=0.45)

    input_senha = Entry(root_login,
                        background=bg_bottom)
    input_senha.place(relheight=0.10,relwidth=0.50,relx=0.30,rely=0.45)
#------------------------------------------------


#-----------------button_login--------------------
    button_login = Button(root_login,
                            text='Login',
                            font=font,
                            background=collor_button,
                            fg=font_color,
                            command=login)
    button_login.place(relheight=0.13,relwidth=0.20,relx=0.25,rely=0.65)
#-------------------------------------------------


#-----------------button_cadastrar--------------------
    button_cadastrar = Button(root_login,
                            text='Cadastrar',
                            font=font,
                            background=collor_button,
                            fg=font_color,
                            command=tela_register)
    button_cadastrar.place(relheight=0.13,relwidth=0.30,relx=0.50,rely=0.65)

#----------------------------------
    root_login.mainloop()

def login():
    input_login_ = input_login.get()
    input_senha_ = input_senha.get()

    conexao = sqlite3.connect('BD/projeto_compras.db')
    cursor = conexao.cursor()
    
    cursor.execute('SELECT * FROM usuarios\
            WHERE nome = ? AND senha = ?',(input_login_,input_senha_))

    login = cursor.fetchone()

    if login:
        print(login)
        
        root_login.destroy()

        root_bem_vindo = Tk()

        root_bem_vindo.title('Tela Cem vindo')
        root_bem_vindo.config(background=bg_bottom)
        root_bem_vindo.iconbitmap('img\icon_login.ico')
        root_bem_vindo.geometry('240x200+500+250')

        root_bem_vindo.mainloop()
        
    else:
        print('user invalid')
        txt_login = Label(text='user invalid',
                        font=font,
                        background=bg_bottom,
                        fg='red')
        txt_login.place(relheight=0.10,relwidth=0.30,relx=0.38,rely=0.55)

def tela_register():

    global root_register

    root_login.destroy()

    root_register = Tk()

    root_register.title("Tela de Cadastro")
    root_register.geometry('00x200+450+150')
    root_register.config(background=bg_bottom)
    
#----------------título------------------
    txt_title = Label(text="register user",
                            font='arial 15',
                            background=bg_bottom,
                            fg=font_color)
    txt_title.place(relheight=0.12, relwidth=0.50,relx=0.25,rely=0.05)
#-----------------------------------------

#------------------user-------------------
    txt_user = Label(text='user',
                        font=font,
                        background=bg_bottom,
                        fg=font_color)
    txt_user.place(relheight=0.10,relwidth=0.20,relx=0.10,rely=0.25)

    input_user_register = Entry(root_register,
                        background=bg_bottom)
    input_user_register.place(relheight=0.10,relwidth=0.50,relx=0.30,rely=0.25)
#-----------------------------------------


#------------------senha------------------
    txt_senha = txt_user = Label(text='password',
                        font=font,
                        background=bg_bottom,
                        fg=font_color)
    txt_senha.place(relheight=0.10,relwidth=0.35,relx=0.01,rely=0.50)

    input_senha_register = Entry(root_register,
                        background=bg_bottom)
    input_senha_register.place(relheight=0.10,relwidth=0.50,relx=0.30,rely=0.50)
#-----------------------------------------

#--------------button_salvar--------------
    button_salvar = Button(root_register,
                                text="Save",
                                background=collor_button,
                                font=font,
                                fg=font_color,
                                command=register_user)
    button_salvar.place(relheight=0.13,relwidth=0.30,relx=0.50,rely=0.65)
#-----------------------------------------

#--------------button_voltar--------------
    img_back = PhotoImage(file= r'img\voltar.png')

    button_voltar = Button(root_register,
                                text="back",
                                background=collor_button,
                                font=font,
                                fg=font_color,
                                command=voltar)
    button_voltar.place(relheight=0.13,relwidth=0.15,relx=0,rely=0)

    root_register.mainloop()

def voltar():
    root_register.destroy()
    tela_login()
    
def register_user():

    conexao = sqlite3.connect('BD\projeto_compras.db')
    cursor = conexao.cursor()

    print('conect sucess')

    cursor.execute('INSERT INTO usuarios VALUES(?,?,?)',(None, input_user_register.get(),input_senha_register.get(),))
    conexao.commit()
    
    if conexao.commit():
        print(f'user {input_login.get()} and {input_senha.get()} insert sucess')
    else:
        print('nenhum usuario inserido')

    cursor.close()
    conexao.close()        