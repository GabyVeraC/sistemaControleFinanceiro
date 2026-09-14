from funcoes import (
    carregarMovimentacoes,
    calcularSaldo,
    mostrarMenu,
    registrarMovimentacao,
    atualizarSaldo,
    salvarMovimentacoes,
    mostrarSaldo,
    listarMovimentacoes
)

movimentacoes = carregarMovimentacoes()
saldoTotal = calcularSaldo(movimentacoes)

while True:

    opcao = mostrarMenu()

    if (opcao == "1"):
        tipo = "Receita"
    
    elif (opcao == "2"):
        tipo = "Despesa"

    if opcao == "1" or opcao == "2":
        movimentacao = registrarMovimentacao(tipo)
        if movimentacao is None:
                continue
        print("Você escolheu adicionar ", tipo)
        
        saldoTotal = atualizarSaldo(saldoTotal, tipo, movimentacao["Valor"])
        movimentacoes.append(movimentacao)
        salvarMovimentacoes(movimentacoes)
        print("Movimentação adicionada com sucesso!")
        continue

    elif (opcao == "3"):
        print("Você escolheu ver o saldo")
        mostrarSaldo(saldoTotal)

    elif (opcao == "4"):
        print("Você escolheu ver as movimentações")
        listarMovimentacoes(movimentacoes)

    elif (opcao == "5"):
        print("Fim da aplicação")
        break

    else:
        print("Opção inválida")