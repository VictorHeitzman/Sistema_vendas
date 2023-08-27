from Modulos.modulos import *
from Functions.functions_login import Functions
class Screen_login(Functions):
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
                                command=self.screen_cadastre_user)
        self.button_cadastrar.place(relheight=0.13,relwidth=0.30,relx=0.50,rely=0.65)
        
if __name__ == '__main__':
    app = Screen_login()