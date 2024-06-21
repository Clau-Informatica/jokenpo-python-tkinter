import random
from tkinter import *


class Controle:
    opcoes = ['Pedra', 'Papel', 'Tesoura']
    usuario = ''
    pc = ''
    cor = ''
    placar = [0, 0]

    def criar_lbl_escolha(self, escolha):  # Criar label com a escolha do jogador
        self.escolha_usuario = Label(
            self.interactions,
            text=f'Escolha do jogador: {escolha}',
            font=('Arial', 16, 'bold'),
            bg='#F5F5F5')
        self.escolha_usuario.place(relx=0.18, rely=0.1, relwidth=0.60)

    def criar_lbl_escolha_pc(self):  # Criar label com a escolha do computador
        self.pc = self.opcoes[random.randint(0, 2)]  # Random para escolha aleatória
        self.escolhapc = Label(
            self.interactions,
            text=f'Escolha da máquina: {self.pc}',
            font=('Arial', 16, 'bold'),
            bg='#F5F5F5')
        self.escolhapc.place(relx=0.18, rely=0.27, relwidth=0.60)

    def criar_lbl_resultado(self):  # Criar label com o resultado do jogo
        resultado = self.get_resultado()
        self.escolha_usuario = Label(
            self.interactions,
            text=resultado,
            font=('Arial', 16, 'bold'),
            bg='#F5F5F5',
            foreground=self.set_cor(self.cor))
        self.escolha_usuario.place(relx=0.18, rely=0.45, relwidth=0.55)

    def criar_lbl_placar(self):  # Criar label com o placar do jogo
        self.lbl_placar = Label(
            self.interactions,
            text=f'Jogador {self.placar[0]} x {self.placar[1]} Máquina',
            font=('Arial', 16, 'bold'),
            bg='#FFDEAD',)
        self.lbl_placar.place(relx=0.20, rely=0.70, relwidth=0.55)

    def set_pedra(self, event):  # Evento quando o jogador escolher pedra
        self.usuario = self.opcoes[0]
        self.criar_lbl_escolha('Pedra')
        self.criar_lbl_escolha_pc()
        self.criar_lbl_resultado()
        self.criar_lbl_placar()

    def set_papel(self, event):  # Evento quando o jogador escolher papel
        self.usuario = self.opcoes[1]
        self.criar_lbl_escolha('Papel')
        self.criar_lbl_escolha_pc()
        self.criar_lbl_resultado()
        self.criar_lbl_placar()

    def set_tesoura(self, event):  # Evento quando o jogador escolher tesoura
        self.usuario = self.opcoes[2]
        self.criar_lbl_escolha('Tesoura')
        self.criar_lbl_escolha_pc()
        self.criar_lbl_resultado()
        self.criar_lbl_placar()

    def set_cor(self, cor):  # Alterar a cor do texto dependendo do resultado
        self.cor = cor
        return cor

    def get_resultado(self):  # Lógica para pegar o resultado do jogo
        jogador = self.usuario
        computador = self.pc
        if jogador == computador:
            self.set_cor('black')
            return 'O jogo empatou!!'
        elif (jogador == 'Pedra' and computador == 'Tesoura') or (
                jogador == 'Papel' and computador == 'Pedra') or (
            jogador == 'Tesoura' and computador == 'Papel'
        ):
            self.placar[0] += 1
            self.set_cor('green')
            return 'Você Ganhou!!'
        self.set_cor('red')
        self.placar[1] += 1
        return 'Você Perdeu!!'

    def zerar_placar(self, event):  # Zerar o placar do jogo
        self.placar = [0,0]
        self.lbl_placar = Label(
            self.interactions,
            text=f'Jogador {self.placar[0]} x {self.placar[1]} Máquina',
            font=('Arial', 16, 'bold'),
            bg='#FFDEAD', )
        self.lbl_placar.place(relx=0.20, rely=0.70, relwidth=0.55)
