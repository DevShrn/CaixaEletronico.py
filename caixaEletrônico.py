#modelo de caixa eletronico.
#funções:
#criar conta (login, senha, saldo inicial)
#Login
#mostrar extrato
#realizar saque(considerando valor na conta)
#realizar depósito
#sair.
import getpass

class info_conta:
    def __init__(self, titular, senha, extrato=0):
        self.titular = titular
        self.senha = senha
        self.extrato = extrato
        
    def login(self):        
        self.titular = input("Insira seu usuário: ")
        self.senha = getpass.getpass("Insira sua senha: ")
        print(f"Seja bem-vindo{self.titular}! ")
        
    def criar_conta(self, valor):
        print("Insira seus dados para realizarmos o cadastro.")
        self.titular = input("Escolha um nome de usuário: ")
        self.senha = getpass.getpass("Defina uma senha: ")

    def tela_inicial(self):
        print("Seja bem vindo ao Banco XXX")
        verif_acc = input("Você já possui conta conosco? [S/N] ")
        
        if verif_acc.isupper() == "S":
            print("Redirecionando para a tela de login...")
            self.login()
        else:
            print("Redirecionando para a tela de cadastro...")
            self.criar_conta()
            
    tela_inicial()
        
    