from tkinter import *
import base64
from Imagens import Imagens
from Controle import Controle
import awesometkinter as atk  # Você deve instalar essa biblioteca com o PIP Install
root = Tk()


#  Criando a classe aplicação e inicializando os métodos
class Application(Imagens, Controle):
    def __init__(self):
        self.root = root
        self.imagens_b64()
        self.tela()
        self.frame_da_tela()
        self.widget_options()
        self.widgets_interactions()
        root.mainloop()

    def tela(self):  # Criação da Tela
        self.root.title('Pedra, Papel e Tesoura')
        self.root.configure(background='#FFDEAD')
        self.root.geometry('650x500')
        self.root.resizable(False, False)
        #  Logo do desenvolvedor no topo
        self.img_logo = PhotoImage(data=base64.b64decode(self.logo_b64))
        self.img_logo = self.img_logo.subsample(1, 1)
        self.lbl_logo = Label(self.root, image=self.img_logo, background='#FFDEAD')
        self.lbl_logo.place(relx=0.10, rely=0.0, relwidth=0.80)
        # Botões no rodapé
        self.bt_zerar_placar = Button(self.root, text="Reiniciar", background='#FFA500', bd=2,
                                      font=('arial', 11, 'bold'))
        self.bt_zerar_placar.place(relx=0.35, rely=0.93, relwidth=0.15)
        self.bt_sair = Button(self.root, text="Sair", background='#FFA500', bd=2, font=('arial', 11, 'bold'))
        self.bt_sair.place(relx=0.51, rely=0.93, relwidth=0.15)

    def frame_da_tela(self):  # Criando Frames para as opções e as interações
        self.options = Frame(self.root,
                             bd=4,
                             bg='#F5F5F5',
                             highlightbackground='#FFA500',
                             highlightthickness=3)
        self.options.place(relx=0.1, rely=0.20, relwidth=0.80, relheight=0.35)
        self.interactions = Frame(self.root,
                                  bd=4,
                                  bg='#F5F5F5',
                                  highlightbackground='#FFA500',
                                  highlightthickness=3)
        self.interactions.place(relx=0.1, rely=0.57, relwidth=0.80, relheight=0.35)

    def widget_options(self):
        self.lbl_option = Label(self.options,  # Label com texto
                                text="Escolha sua opção: ",
                                font=('Arial', 14, 'bold'),
                                bg='#F5F5F5')
        self.lbl_option.place(relx=0.33, rely=0.05)
        # Imagem e botão da pedra
        self.img_pedra = PhotoImage(data=base64.b64decode(self.imgpedra_b64))
        self.img_pedra = self.img_pedra.subsample(3, 2)
        self.lbl_pedra = Label(self.options,
                               image=self.img_pedra,
                               background='white')
        self.lbl_pedra.place(relx=0.22, rely=0.30, relwidth=0.15)
        self.bt_pedra = Button(self.options,
                               text="Pedra",
                               background='#FFDEAD',
                               bd=2,
                               font=('arial', 11, 'bold'))
        self.bt_pedra.place(relx=0.22, rely=0.75, relwidth=0.15)
        # Balão de mensagem
        atk.tooltip(self.bt_pedra, 'A Pedra ganha da Tesoura e perde pro Papel.')
        # Imagem e botão do Papel
        self.img_papel = PhotoImage(data=base64.b64decode(self.imgpapel_b64))
        self.img_papel = self.img_papel.subsample(3, 2)
        self.lbl_papel = Label(self.options,
                               image=self.img_papel,
                               background='white')
        self.lbl_papel.place(relx=0.42, rely=0.30, relwidth=0.15)
        self.bt_papel = Button(self.options,
                               text="Papel",
                               background='#FFDEAD',
                               bd=2,
                               font=('arial', 11, 'bold'))
        self.bt_papel.place(relx=0.42, rely=0.75, relwidth=0.15)
        #  Balão de mensagem
        atk.tooltip(self.bt_papel, 'O Papel ganha da Pedra e perde pra Tesoura.')
        # Imagem e botão da Tesoura
        self.img_tesoura = PhotoImage(data=base64.b64decode(self.imgtesoura_b64))
        self.img_tesoura = self.img_tesoura.subsample(3, 2)
        self.lbl_tesoura = Label(self.options,
                                 image=self.img_tesoura,
                                 background='white')
        self.lbl_tesoura.place(relx=0.62, rely=0.30, relwidth=0.15)
        self.bt_tesoura = Button(self.options,
                                 text="Tesoura",
                                 background='#FFDEAD',
                                 bd=2,
                                 font=('arial', 11, 'bold'))
        self.bt_tesoura.place(relx=0.62, rely=0.75, relwidth=0.15)
        #  Balão de mensagem
        atk.tooltip(self.bt_tesoura, 'A Tesoura ganha do Papel e perde pra Pedra.')

    def widgets_interactions(self):  # Interações quando os botões forem clicados
        self.bt_pedra.bind("<1>", self.set_pedra)
        self.bt_papel.bind("<1>", self.set_papel)
        self.bt_tesoura.bind("<1>", self.set_tesoura)
        self.bt_zerar_placar.bind("<1>", self.zerar_placar)
        self.bt_sair.bind("<1>", self.encerrar)

    def encerrar(self, event):  # Evento para fechar o jogo
        self.root.destroy()

#  Inicializar aplicação
Application()
