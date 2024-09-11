# Banco_Dio_v3
 implementação Banco-Dio_v3


Sistema Bancário Simples
Este projeto é um sistema bancário básico desenvolvido em Python que permite a criação de clientes, contas bancárias, e a realização de transações, como depósitos, saques e consulta de extratos.

Funcionalidades
Criar Cliente: Adiciona um novo cliente ao sistema com seu endereço.
Criar Conta Corrente: Vincula uma conta a um cliente previamente cadastrado.
Depósito: Permite que o cliente deposite um valor em sua conta.
Saque: Realiza saques, desde que haja saldo suficiente na conta.
Extrato: Exibe o saldo atual da conta e o histórico de todas as transações realizadas.
Estrutura do Projeto
Cliente: Representa um cliente do banco, com atributos como endereço e contas associadas.
Conta: Representa uma conta bancária, contendo saldo, número da conta, agência e cliente.
Transação: Interface para transações bancárias. Duas implementações são fornecidas: depósito e saque.
Histórico: Armazena o histórico de transações realizadas em uma conta.
Interagir com o Sistema: Ao executar o programa, você verá um menu com as seguintes opções:

[d] Depositar
[s] Sacar
[e] Extrato
[u] Criar Cliente
[c] Criar Conta Corrente
[q] Sair
Criar Clientes e Contas: Antes de realizar transações, crie um cliente ([u]) e, em seguida, associe uma conta corrente a ele ([c]).

Realizar Transações: Após a criação de uma conta, é possível realizar depósitos ([d]) e saques ([s]), além de consultar o extrato da conta ([e]).

Exemplo de Execução
=> [u] Criar Cliente
Informe o endereço: Rua ABC, 123
Cliente criado com sucesso!

=> [c] Criar Conta Corrente
Informe a agência: 001
Conta número 1 criada com sucesso!

=> [d] Depositar
Informe o valor do depósito: 500
Depósito de R$ 500.00 realizado com sucesso!

=> [s] Sacar
Informe o valor do saque: 200
Saque de R$ 200.00 realizado com sucesso!

=> [e] Extrato
Saldo: R$ 300.00
Depósito de R$ 500.00
Saque de R$ 200.00

Requisitos
Python 3.x
Melhorias Futuras
Implementar autenticação de clientes com login e senha.
Permitir a criação de múltiplas contas por cliente.
Limitar o número de saques diários e o valor máximo de saque.
Adicionar taxas e juros para saques e depósitos.
Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

