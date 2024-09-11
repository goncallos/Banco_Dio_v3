from abc import ABC, abstractmethod


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        conta.realizar_transacao(transacao)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class Conta:
    def __init__(self, saldo, numero, agencia, cliente):
        self.saldo = saldo
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.historico = Historico()

    def realizar_transacao(self, transacao):
        transacao.registrar(self)

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.historico.adicionar_transacao(Saque(valor))
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Saldo insuficiente.")
            return False

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.historico.adicionar_transacao(Deposito(valor))
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Valor de depósito inválido.")


class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)


class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass


class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        conta.saldo += self.valor
        conta.historico.adicionar_transacao(self)


class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        if conta.saldo >= self.valor:
            conta.saldo -= self.valor
            conta.historico.adicionar_transacao(self)
        else:
            print("Saldo insuficiente para saque.")


clientes = []
contas = []

def criar_cliente():
    endereco = input("Informe o endereço: ")
    cliente = Cliente(endereco)
    clientes.append(cliente)
    print("Cliente criado com sucesso!")

def criar_conta():
    if not clientes:
        print("Nenhum cliente cadastrado.")
        return
    numero = len(contas) + 1
    agencia = input("Informe a agência: ")
    cliente = clientes[0]  
    conta = Conta(0, numero, agencia, cliente)
    cliente.adicionar_conta(conta)
    contas.append(conta)
    print(f"Conta número {numero} criada com sucesso!")


menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[u] Criar Cliente
[c] Criar Conta Corrente
[q] Sair
=> """

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        contas[0].depositar(valor)  

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        contas[0].sacar(valor)  

    elif opcao == "e":
        print(f"Saldo: R$ {contas[0].saldo:.2f}")
        for transacao in contas[0].historico.transacoes:
            if isinstance(transacao, Deposito):
                print(f"Depósito de R$ {transacao.valor:.2f}")
            elif isinstance(transacao, Saque):
                print(f"Saque de R$ {transacao.valor:.2f}")

    elif opcao == "u":
        criar_cliente()

    elif opcao == "c":
        criar_conta()

    elif opcao == "q":
        break

    else:
        print("Operação inválida.")
