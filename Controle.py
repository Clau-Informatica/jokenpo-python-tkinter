from tkinter import *
class Controle():
    opcoes = ['Pedra', 'Papel', 'Tesoura']
    escolha = ''

    def criar_lbl_escolha(self, escolha, x):
        self.escolha_usuario = Label(
            self.interactions,
            text=(f'Você escolheu: {escolha}'),
            font=('Arial', 16),
            bg='#dfe3ee')
        self.escolha_usuario.place(relx=x, rely=0.1, relwidth=0.50)

    def set_pedra(self, event):
        escolha = self.opcoes[0]
        print(escolha)
        self.criar_lbl_escolha('Pedra', 0.15)

    def set_papel(self, event):
        escolha = self.opcoes[1]
        print(escolha)
        self.criar_lbl_escolha('Papel', 0.15)

    def set_tesoura(self, event):
        escolha = self.opcoes[2]
        print(escolha)
        self.criar_lbl_escolha('Tesoura', 0.15)



    def get_escolha(self):
        return self.escolha






