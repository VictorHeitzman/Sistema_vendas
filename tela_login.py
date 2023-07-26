from tkinter import *
from tkinter import Tk
from tela_register import *
from models_DB import DB



def config_login():
    global bg_bottom
    global fg_front
    global font
    global font_color
    global collor_button

    bg_bottom = '#347355'
    fg_front = '#60BF81'
    font = 'arial 11'
    font_color = 'white'
    collor_button = '#223240'

    root.title('Tela de login')
    root.config(background=bg_bottom)
    root.iconbitmap('img\icon_login.ico')
    root.geometry('240x200+500+250') 


def labels():

#--------------Titulo tela_login----------------- 
    titulo_login = Label(root,
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

    input_login = Entry(root,
                        background=bg_bottom)
    input_login.place(relheight=0.10,relwidth=0.50,relx=0.30,rely=0.25)
#------------------------------------------------


#--------------------senha------------------------ 
    txt_senha = Label(text='Senha',
                        font=font,
                        background=bg_bottom,
                        fg=font_color)
    txt_senha.place(relheight=0.10,relwidth=0.20,relx=0.10,rely=0.45)

    input_senha = Entry(root,
                        background=bg_bottom)
    input_senha.place(relheight=0.10,relwidth=0.50,relx=0.30,rely=0.45)
#------------------------------------------------


#-----------------button_login--------------------
    button_login = Button(root,
                            text='Login',
                            font=font,
                            background=collor_button,
                            fg=font_color,
                            command=( input_login.get(),input_senha.get()))
    button_login.place(relheight=0.13,relwidth=0.20,relx=0.25,rely=0.65)
#-------------------------------------------------


#-----------------button_cadastrar--------------------
    button_cadastrar = Button(root,
                            text='Cadastrar',
                            font=font,
                            background=collor_button,
                            fg=font_color,
                            command=register_user)
    button_cadastrar.place(relheight=0.13,relwidth=0.30,relx=0.50,rely=0.65)



root = Tk()
config_login()
labels()



root.mainloop()