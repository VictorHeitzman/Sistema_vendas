from Config.Modulos.modulos import *
from Config.Coolors.style import Style

from tela_pdv import Screen_pdv
from tela_cadastro_produtos import Screen_products_cadastre
from tela_estoque import Screen_stock
from tela_cadastro_clientes import Screen_cadastro_cliente
from tela_controle_clientes import Screen_controle_cliente
from tela_NF import Screen_NF
from Config.Functions.functions_db import DB

class Functions(DB,Style):

    def screen_products_cadastre(self):

        Screen_products_cadastre()
    
    def screen_stock(self):
        
        Screen_stock()
        
    def screen_pdv(self):

        Screen_pdv()

    def screen_cadastro_cliente(self):
        
        Screen_cadastro_cliente()

    def screen_controle_cliente(self):
        
        Screen_controle_cliente()
    
    def screen_nf(self):
        
        Screen_NF()

    def menu(self):
        self.barra_menu = Menu(self.root_menu)
        self.root_menu.config(menu=self.barra_menu)

        self.sobre = Menu(self.barra_menu, tearoff=0)
        self.sobre.add_cascade(label='Este Sistema',command=self.este_sistema)

        self.transacoes = Menu(self.barra_menu, tearoff=0)
        self.transacoes.add_cascade(label='Transações Notas Fiscais',command=self.notas_fiscais)
        self.transacoes.add_cascade(label='Transações de entrada e saída',command=self.transasoes_venda)
        
        self.contatos = Menu(self.barra_menu, tearoff=0)
        self.contatos.add_cascade(label='Whatsapp',command=self.contatos_)
        self.contatos.add_cascade(label='E-mail',command=self.email)

        self.clientes = Menu(self.barra_menu, tearoff=0)
        self.clientes.add_command(label='Cadastro de clientes', command=self.screen_cadastro_cliente)
        self.clientes.add_command(label='Controle de clientes', command=self.screen_controle_cliente)
        
        # Adicionando ao label ao menu
        self.barra_menu.add_cascade(label='Sobre',menu=self.sobre)
        self.barra_menu.add_cascade(label='Contatos Dev', menu=self.contatos)
        self.barra_menu.add_cascade(label='Clientes',menu=self.clientes)
        self.barra_menu.add_cascade(label='Relatórios',menu=self.transacoes)
        
    def contatos_(self):
        self.root_contatos = Toplevel()
        self.root_contatos.title('Whatsapp')
        self.root_contatos.config(background=self.background)
        self.root_contatos.iconbitmap('Config\img\icon_contatos.ico')
        self.root_contatos.resizable(False,False)
        self.root_contatos.geometry('400x400+250+50')
        # self.root_cadastro_cliente.attributes('-fullscreen',True)

        self.root_contatos.focus_force()
        self.root_contatos.grab_set()
        
        self.txt_whatsapp = Label(self.root_contatos,text='Whatsapp',background=self.background,font='arial 15')
        self.txt_whatsapp.pack()

        self.img = PhotoImage(file='Config/img/qr_whatsapp.png')
        self.img_label = Label(self.root_contatos, image=self.img)
        self.img_label.pack()

        self.button = Button(self.root_contatos, text="Gerar novo QR", font=self.font,fg=self.font_color,background=self.collor_button,command=self.criar_novo_qr)
        self.button.pack()
    
    def este_sistema(self):
        self.root_este_sistema = Toplevel()
        self.root_este_sistema.title('Este_sistema')
        self.root_este_sistema.config(background=self.background)
        self.root_este_sistema.iconbitmap('Config\img\icon_dev.ico')
        self.root_este_sistema.resizable(False,False)
        self.root_este_sistema.geometry('900x500+250+50')
        # self.root_este_sistema.attributes('-fullscreen',True)

        self.root_este_sistema.focus_force()
        self.root_este_sistema.grab_set()

        text = """
Nosso sistema é uma plataforma de gerenciamento de informações e operações projetada para facilitar a gestão eficiente de minimercados, mercearias ou lojas. Esse sistema desempenha um papel fundamental na otimização de várias atividades, desde o controle de inventário até o atendimento ao cliente. Aqui está um resumo das principais características e funcionalidades do sistema:

Gestão de Inventário:
Registra e rastreia os produtos em estoque, facilitando o controle de quantidades disponíveis. Permite a atualização automática de estoque conforme as vendas são registradas.

Registro de Vendas:
Registra todas as transações de vendas, incluindo itens, quantidades, preços e métodos de pagamento.
Calcula o total de vendas e impostos automaticamente.

Gerenciamento de Preços:
Facilita a definição de preços de produtos, novos preços e descontos.
Atualiza os preços de forma consistente em todos os pontos de venda.

Controle de Caixa:
Acompanha todas as transações de caixa e o movimento de dinheiro.

Gestão de Clientes:
Mantém registros de clientes, com a possibilidade informar se o cliente está devendo ou já pagou.
Fornece um sistema de checkout rápido e eficiente, incluindo leitores de código de barras.

Erros:
Minimiza erros de preço e estoque durante o processo de compra.

Relatórios e Análises:
Gera relatórios detalhados sobre vendas, estoque, desempenho de produtos e lucratividade.
Facilita análises de negócios e tomadas de decisão informadas.

Segurança:
Protege dados sensíveis e transações financeiras.
Controla o acesso ao sistema com permissões de usuário.

Em resumo, o nosso sistema é uma ferramenta essencial para a gestão eficiente de um minimercado, mercearias ou lojas, auxiliando na otimização de processos, no controle de estoque e nas operações de vendas. Isso resulta em um melhor atendimento ao cliente e na maximização da lucratividade do negócio.
"""


        self.txt = Text(self.root_este_sistema,background=self.background,font=self.font,fg=self.font_color,highlightcolor=self.background)
        self.txt.place(relheight=0.99,relwidth=0.99)

        self.txt.insert(END,text)
        self.txt.config(state='disabled')
    
    def criar_novo_qr(self):
        img = qr.make('https://api.whatsapp.com/send/?phone=5511998338754&text&type=phone_number&app_absent=0')

        img.save('Config/img/qr_whatsapp.png', scale=5) 

        messagebox.showinfo('Aviso','Feche e abra a tela novamente')

    def transasoes_venda(self):
        self.conect_db()

        self.cursor.execute("""SELECT * FROM transacoes""")
        
        self.conexao.commit()

        data = self.cursor.fetchall()
        
        lista = list(map(list,data))

        columns = ('id','id_produto','descicao','data_registro','tipo','quantidade','preco_entrada','preco_saida','total','pagamento')
        df = pd.DataFrame(lista,columns=columns)

        df.to_csv(f'Config/Transacoes/transacoes_{date.today()}.csv',index=None, decimal=',',encoding='latin-1')

        self.desconect_db()
        
        messagebox.showinfo('Aviso','Arquivo de transações exportado.')

    def notas_fiscais(self):
        self.conect_db()

        self.cursor.execute("""SELECT * FROM nf""")

        data = self.cursor.fetchall()

        lista = list(map(list,data))

        columns = ('id','numero_nf','fornecedor','data_emissao','data_vencimento','valor_produto','valor_nota','descricao')

        df = pd.DataFrame(lista,columns=columns)

        df.to_csv(f'Config/Transacoes/relatorio_nf_{date.today()}.csv',index=None, decimal=',',encoding='latin-1')

        self.desconect_db()

        messagebox.showinfo('Aviso','Arquivo de nf exportado.')
    
    def email(self):

        self.root_contatos = Toplevel()
        self.root_contatos.title('E-mail')
        self.root_contatos.config(background=self.background)
        self.root_contatos.iconbitmap('Config\img\icon_contatos.ico')
        self.root_contatos.resizable(False,False)

        # self.root_cadastro_cliente.attributes('-fullscreen',True)

        self.root_contatos.focus_force()
        self.root_contatos.grab_set()

        self.txt_email = Label(self.root_contatos,text='Email: heitzmam@gmail.com',background=self.background,font='arial 15 bold')
        self.txt_email.pack()

        
