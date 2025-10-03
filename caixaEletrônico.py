#modelo de caixa eletronico.
#funções:
#criar conta (login, senha, saldo inicial)
#Login
#mostrar extrato
#realizar saque, pix, ted etc(considerando valor na conta)
#realizar depósito
#sair.
import getpass

class info_conta:
    def __init__(self, titular, senha, saldo=0):
        self.titular = titular
        self.senha = senha
        self.saldo = saldo
        self.historico = []
        
    def login(self):        
        self.titular = input("Insira seu usuário: ")
        self.senha = getpass.getpass("Insira sua senha: ")
        print(f"Seja bem-vindo {self.titular}! ")
        
    def criar_conta(self):
        print("Insira seus dados para realizarmos o cadastro.")
        self.titular = input("Escolha um nome de usuário: ")
        self.senha = getpass.getpass("Defina uma senha: ")
        print("Conta criada com sucesso! Redirecionando para a tela de login...")
        self.login()

    def tela_inicial(self):
        print("Seja bem vindo ao Banco XXX")
        verif_acc = input("Você já possui conta conosco? [S/N] ")
        
        if verif_acc == "S":
            print("Redirecionando para a tela de login...")
            self.login()
        else:
            print("Redirecionando para a tela de cadastro...")
            self.criar_conta()
    
    def tela_app (self):
        print(f"Seja bem-vindo {self.titular}")
        print("Escolha uma das opçoes abaixo para continuarmos: ")
    
    def extrato(self):
        
    
    def transferencia(self):
    
    def deposito(self, valor):
        valor = float(input("Insira o valor do depósito: "))
        self.valor += valor
        self.historico.append(f"Deposito no valor de R$ {valor: 2f}")
        print (f"Deposito realizado com Sucesso!")
            
        
conta = info_conta("","")
conta.tela_inicial()   