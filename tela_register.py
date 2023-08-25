from modulos import *
from functions import Functions

class Tela_register(Functions):

    bg_bottom = '#347355'
    fg_front = '#60BF81'
    font = 'arial 11'
    font_color = 'white'
    collor_button = '#223240'

    def __init__(self) -> None:
        self.root_register = Tk()

        self.config()
        self.labels()

        self.root_register.mainloop()

    def config(self):
        self.root_register.title('Register')
        self.root_register.geometry('00x200+450+150')
        self.root_register.config(background=self.bg_bottom)
        self.root_register.iconbitmap('img\icon_login.ico')

    def labels(self):
        #----------------título------------------
        self.txt_title = Label(text="register user",
                                font='arial 15',
                                background=self.bg_bottom,
                                fg=self.font_color)
        self.txt_title.place(relheight=0.12, relwidth=0.50,relx=0.25,rely=0.05)
    #-----------------------------------------

    #------------------user-------------------
        self.txt_user = Label(text='user',
                            font=self.font,
                            background=self.bg_bottom,
                            fg=self.font_color)
        self.txt_user.place(relheight=0.10,relwidth=0.20,relx=0.10,rely=0.25)

        self.input_user_register = Entry(self.root_register,
                            background=self.bg_bottom)
        self.input_user_register.place(relheight=0.10,relwidth=0.50,relx=0.30,rely=0.25)
    #-----------------------------------------


    #------------------senha------------------
        self.txt_senha = txt_user = Label(text='password',
                            font=self.font,
                            background=self.bg_bottom,
                            fg=self.font_color)
        self.txt_senha.place(relheight=0.10,relwidth=0.35,relx=0.01,rely=0.50)

        self.input_senha_register = Entry(self.root_register,
                            background=self.bg_bottom)
        self.input_senha_register.place(relheight=0.10,relwidth=0.50,relx=0.30,rely=0.50)
    #-----------------------------------------

    #--------------button_salvar--------------
        self.button_salvar = Button(self.root_register,
                                    text="Save",
                                    background=self.collor_button,
                                    font=self.font,
                                    fg=self.font_color,
                                    command="")
        self.button_salvar.place(relheight=0.13,relwidth=0.30,relx=0.50,rely=0.65)
    #-----------------------------------------

    #--------------button_voltar--------------
        self.img_back = PhotoImage(file= r'img\voltar.png')

        self.button_voltar = Button(self.root_register,
                                    text="back",
                                    background=self.collor_button,
                                    font=self.font,
                                    fg=self.font_color,
                                    command=self.voltar)
        self.button_voltar.place(relheight=0.13,relwidth=0.15,relx=0,rely=0)



if __name__ == '__main__':
    root = Tela_register()