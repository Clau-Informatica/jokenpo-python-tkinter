from tkinter import *
import base64
from Imagens import *
root = Tk()


class Application(Imagens):
    def __init__(self):
        self.root = root
        self.imagens_b64()
        self.tela()
        self.frame_da_tela()
        self.widget_options()
        root.mainloop()

    def tela(self):
        self.root.title('Pedra, Papel e Tesoura')
        self.root.configure(background='#FFDEAD')
        self.root.geometry('700x500')
        self.root.resizable(True, True)
        self.root.maxsize(width=900, height=700)
        self.root.minsize(width=500, height=300)

    def frame_da_tela(self):
        self.options = Frame(self.root, bd=4, bg='#dfe3ee', highlightbackground='#759fe6', highlightthickness=3)
        self.options.place(relx=0.1, rely=0.1, relwidth=0.80, relheight=0.35)
        self.interactions = Frame(self.root, bd=4, bg='#dfe3ee', highlightbackground='#759fe6', highlightthickness=3)
        self.interactions.place(relx=0.1, rely=0.50, relwidth=0.80, relheight=0.35)

    def widget_options(self):
        self.lbl_option = Label(self.options, text="Escolha sua opção", font=('Arial', 12, 'bold'), bg='#dfe3ee')
        self.lbl_option.place(relx=0.35, rely=0.05)
        # Imagem e botão da pedra
        self.img_pedra = PhotoImage(data=base64.b64decode(self.imgpedra_b64))
        self.img_pedra = self.img_pedra.subsample(3, 2)
        self.lbl_pedra = Label(self.options, image=self.img_pedra)
        self.lbl_pedra.place(relx=0.22, rely=0.30, relwidth=0.15)
        self.bt_pedra = Button(self.options, text="Pedra", background='#FFDEAD', bd=2, font=('arial', 11, 'bold'))
        self.bt_pedra.place(relx=0.22, rely=0.75, relwidth=0.15)
        # Imagem e botão do Papel
        self.img_papel = PhotoImage(data=base64.b64decode(self.imgpapel_b64))
        self.img_papel = self.img_papel.subsample(3, 2)
        self.lbl_papel = Label(self.options, image=self.img_papel)
        self.lbl_papel.place(relx=0.42, rely=0.30, relwidth=0.15)
        self.bt_papel = Button(self.options, text="Papel", background='#FFDEAD', bd=2, font=('arial', 11, 'bold'))
        self.bt_papel.place(relx=0.42, rely=0.75, relwidth=0.15)
        # Imagem e botão da Tesoura
        self.img_tesoura = PhotoImage(data=base64.b64decode(self.imgtesoura_b64))
        self.img_tesoura = self.img_tesoura.subsample(3, 2)
        self.lbl_tesoura = Label(self.options, image=self.img_tesoura)
        self.lbl_tesoura.place(relx=0.62, rely=0.30, relwidth=0.15)
        self.bt_tesoura = Button(self.options, text="Tesoura", background='#FFDEAD', bd=2, font=('arial', 11, 'bold'))
        self.bt_tesoura.place(relx=0.62, rely=0.75, relwidth=0.15)


Application()
