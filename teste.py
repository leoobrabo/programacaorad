# -*-coding:utf8;-*-
# Leonardo dos santos motta
# 13/09/2019

from main import Conta, Usuario

#cadastro de um cliente
cliente = Usuario('Leonardo','Motta', '0000000000-1')

#cadastro da conta do cliente 
conta = Conta('123-4', cliente, 120.0, 1000.0)

#cadastro realizado com sucesso e o saldo do cliente na conta cadastrada 
conta.extrato()

#Realizaçao de um deposito 
conta.depositar(20.0)

#Novo extrato com a adiçao do deposito 
conta.extrato()

#Realizaçao de um saque
conta.retirar(30)

#Extrato com a subtraçao do saque
conta.extrato()

#Retirada de um valor maior que o saldo "Recebendo a resposta de saldo insuficiente"
conta.retirar(120.0)

#Extrato da conta barrando a retirada nao autorizada
conta.extrato()

#criaçao de um novo cliente
cliente1 = Usuario('Rita', 'Motta', '00000000000-2')

#criaçao de uma nova conta
conta1 = Conta('123-5', cliente1, 150.0, 1000.0)

#extrato da conta criada
conta1.extrato()

#Realizaçao de uma transferencia entre contas 
conta.transferir(conta1, 50)

#Novo extrato apos o recebimento do saldo
conta1.extrato()

#Novo extrato apos a subtraçao da transferencia
conta.extrato()

#Forma de visualizar o nome do cliente
print(conta1.cliente.nome)

#tetativa de transferencia com saldo insuficiente
conta.transferir(conta1, 200)

#Historico com a data da abertura e as transaçoes realizadas da conta
conta1.historico.imprimir()

#Historico com a data da abertura e as transaçoes realizadas da conta
conta.historico.imprimir()

#Criaçao de uma nova conta
cliente2 = Usuario('fulano', 'ciclano', '0000000000-3')
conta2 = Conta('123-6', cliente2, -100.0, 1000.0)

#Tentativa de adicionar saldo negativo
conta2.set_saldo(-100.0)

#Metodo para saber o total de contas cadastradas no banco
print(Conta.get_total_contas())

#Imprimindo a taxa de juros do banco
print(conta.imposto.taxa)