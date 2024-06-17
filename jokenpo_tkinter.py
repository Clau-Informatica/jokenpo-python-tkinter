import tkinter
from tkinter import *
root = Tk()


class Application:
    def __init__(self):
        self.root = root
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
        self.lbl_option = Label(self.options, text="Escolha sua opção", font=('Arial', 12, 'bold'), bg= '#dfe3ee')
        self.lbl_option.place(relx=0.35, rely=0.05)
        



Application()
