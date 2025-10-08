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
        
    def tela_inicial(self):
        print("Seja bem-vindo ao Banco XXX")
        verif_acc = input("Você já possui conta conosco? [S/N] ").strip().upper()
        
        if verif_acc == "S":
            print("Redirecionando para a tela de login...")
            self.login()
        elif verif_acc == "N":
            print("Redirecionando para a tela de cadastro...")
            self.criar_conta()
        else:
            print("Resposta Invalida! Tente novamente")
            self.tela_inicial()
        
    def login(self):        
        self.titular = input("Insira seu usuário: ")
        self.senha = getpass.getpass("Insira sua senha: ")
        print(f"Seja bem-vindo, {self.titular}!")
        self.tela_app()
        
    def criar_conta(self):
        print("Insira seus dados para realizarmos o cadastro.")
        self.titular = input("Escolha um nome de usuário: ")
        self.senha = getpass.getpass("Defina uma senha: ")
        print("Conta criada com sucesso! Redirecionando para a tela de login...")
        self.login()    
    
    def tela_app(self):
        funcoes = {
            "Extrato": self.extrato,
            "Transferência": self.transferencia,
            "Depósito": self.deposito
        }

        while True:
            print(f"\nSeja bem-vindo, {self.titular}")
            menu = "\n".join([f"{i+1} - {opcao}" for i, opcao in enumerate(funcoes.keys())])
            print("\nEscolha a operação:")
            print(menu)
            print(f"{len(funcoes)+1} - Sair")

            escolha = input("\nDigite o número da operação: ").strip()

            if not escolha.isdigit() or not (1 <= int(escolha) <= len(funcoes)+1):
                print("Opção inválida! Tente novamente.")
                continue

            escolha = int(escolha)
            if escolha == len(funcoes) + 1:
                print("Saindo...")
                break

            list(funcoes.values())[escolha - 1]()
        
    def calcular_saldo(self):
        saldo = 0
        for operacao in self.historico:
            saldo += operacao["valor"]
        return saldo
        
    def extrato(self):
        print("\n--- Extrato ---")
        if not self.historico:
            print("Nenhuma movimentação recente.")
        else:
            for operacao in self.historico:
                tipo = operacao["tipo"].capitalize()    
                valor = operacao["valor"]
                print(f"{tipo}: R$ {abs(valor):.2f}")
            print(f"\nSaldo atual: R$ {self.calcular_saldo():.2f}")
    
    def transferencia(self):
        valor = float(input("Insira o valor da transferência: "))
        saldo = self.calcular_saldo()
        
        if 0 < valor <= saldo:
            self.historico.append({"tipo": "transferência", "valor": -valor})
            print(f"Transferência de R$ {valor:.2f} realizada com sucesso!")
        else:
            print("Saldo insuficiente!")
    
    def deposito(self):
        valor = float(input("Insira o valor do depósito: "))
        if valor > 0:
            self.historico.append({"tipo": "depósito", "valor": valor})
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Valor inválido!")

conta = info_conta("", "")
conta.tela_inicial()
