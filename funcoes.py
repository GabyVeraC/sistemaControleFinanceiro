
import json

def adicionarMovimentacao(tipo, descricao, valor):
    movimentacao = {
        "Tipo" : tipo,
        "Descrição" : descricao, 
        "Valor" : valor
        }
    return movimentacao

def salvarMovimentacoes(movimentacoes):
    with open("movimentacoes.json", "w") as arquivo:
        json.dump(movimentacoes, arquivo, indent=4)

def carregarMovimentacoes():
    try:
        with open("movimentacoes.json", "r") as arquivo:
            movimentacoes = json.load(arquivo)
            return movimentacoes
    except FileNotFoundError:
        return[]

def atualizarSaldo(saldoTotal, tipo, valor):
    if tipo == "Receita":
        saldoTotal = saldoTotal + valor

    elif tipo == "Despesa":
        saldoTotal = saldoTotal - valor

    return saldoTotal

def calcularSaldo(movimentacoes):
    saldo = 0

    for movimentacao in movimentacoes:
        if movimentacao["Tipo"] == "Receita":
            saldo = saldo + movimentacao["Valor"]
        elif movimentacao["Tipo"] == "Despesa":
            saldo = saldo - movimentacao["Valor"]
    return saldo

def mostrarMenu():
    print("===== CONTROLE FINANCEIRO =====")
    print("\n1 - Adicionar receita")
    print("2 - Adicionar despesa")
    print("3 - Ver saldo")
    print("4 - Listar movimentações")
    print("5 - Sair")
    
    opcao = input("Digite qual opção deseja: ")
    
    return opcao

def registrarMovimentacao(tipo):
    descricao = input("Descrição: ").strip()
    if not descricao:
        print("A descrição não pode ficar vazia")
        return None
    try:
        valor = float(input("Valor: R$"))
    except ValueError:
        print("Digite apenas números")
        return None
    if valor <= 0:
        print("O valor deve ser maior que zero.")
        return None
    movimentacao = adicionarMovimentacao(tipo, descricao, valor)
    return movimentacao

def listarMovimentacoes(movimentacoes):
    if not movimentacoes:
        print("Nenhuma movimentação cadastrada.")
        return
    for numero, movimentacao in enumerate(movimentacoes, start=1):
        valorFormatado = f"{movimentacao['Valor']:,.2f}".replace(",","X").replace(".",",").replace("X",".")
        print(
            f"{numero} - {movimentacao['Tipo']} | "
            f"{movimentacao['Descrição']} | "
            f"R${valorFormatado}"
        )

def mostrarSaldo(saldoTotal):
    saldoTotalFormatado = f"{saldoTotal:,.2f}".replace(",","X").replace(".",",").replace("X",".")
    print("Seu saldo total é R$" + saldoTotalFormatado)
         