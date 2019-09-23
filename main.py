# -*-coding:utf8;-*-
# Leonardo dos santos motta
# 13/09/2019

from datetime import datetime, date

class Usuario:

    'Classe para a criação de usuario'

    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

class Conta:
    
    'Classe para criação de contas Bancarias'

    _total_contas = 0

    def __init__(self, numero, cliente, saldo, limite=1500.0):
        'metodo para a criaçao de uma conta'
        print("Inicializando uma conta!")
        self.numero = numero
        self.cliente = cliente
        self.saldo = saldo
        self.limite = limite
        self.imposto = Imposto()
        self.historico = Historico()
        Conta._total_contas += 1

    def set_saldo(self, saldo):
        if (saldo < 0):
            print("saldo não pode ser negativo")
        else:
            self.saldo = saldo

    @staticmethod
    def get_total_contas():
        return Conta._total_contas

    def depositar(self, valor):
        self.saldo += valor
        self.historico.transacoes.append("Realizado o depósito de {} reais".format(valor))

    def retirar(self, valor):
        if (self.saldo < valor):
            print('Saldo Insuficiente!')
            return False 
        else:
            self.saldo -= valor
            self.historico.transacoes.append("Realizado saque de {} reais".format(valor))
            print('Transação efetuada com sucesso!')
            return True 

    def transferir(self, destino, valor):
        transferencia = self.retirar(valor)
        if (transferencia == False):
            return False
        else:
            destino.depositar(valor)
            self.historico.transacoes.append("Realizada a transferencia de {} reais para a conta {}".format(valor, destino.numero))
            return True
        
    def extrato(self):
        self.juros = self.imposto.juros
        self.saldo = self.saldo + self.juros
        print("numero: {} saldo: {} juros: {}".format(self.numero , self.saldo, self.juros))
        self.historico.transacoes.append("Extrato - Saldo de {}".format(self.saldo))

class Historico:

    'Classe para criação de um breve historico'

    def __init__(self):
        self.data_abertura = datetime.today()
        self.transacoes = []
        self.data_rendimento = date.today()
        self.dia_1 = []
        self.dia_1.append(self.data_rendimento)
        self.dia_hoje = date.today()
        

    def imprimir(self):
        print("Data de Abertura da conta: {}".format(self.data_abertura))
        print("Transações: ")
        for i in self.transacoes:
            print("-", i)

class Imposto:
    
    'Classe para calcular juros bancario considerando taxa referencial o CDI e liquidez diaria'
    
    def __init__(self):
        self.info = Historico()
        self.taxa = (5.9 * 0.7)
        self.dias = abs((self.info.dia_1[0] - self.info.dia_hoje).days)
        self.juros = (self.taxa * self.dias)

    def get_juross(self):
        return self.juros