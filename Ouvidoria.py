opcao = -1
reclamacoes = []
while opcao != 6:
  print("Opções \n1-Adicionar manifestação \n2-Consultar manifestações \n3-Relatório de manifestações \n4-Pesquisar manifestações \n5-Excluir manifestação \n6-Sair ")
  opcao = int(input("Digite a sua opção: "))

  if opcao == 1:
    novaReclamacao = input("Digite sua manifestação: ")
    reclamacoes.append(novaReclamacao)
    print("Manifestação adicionada com sucesso!")

  elif opcao == 2:
    if len(reclamacoes) > 0:
        print("Lista de manifestações")
        for i in reclamacoes:
              print("-",i)
    else:
      print("Ainda não existem manifestações!")

  elif opcao == 3:
    quantidadeReclamacoes = len(reclamacoes)
    print("A empresa tem",quantidadeReclamacoes,"manifestações")

  elif opcao == 4:
    codigoPesquisa = int(input("Digite o código da manifestação: "))
    if codigoPesquisa > 0 and codigoPesquisa <= len(reclamacoes):
      print("A reclamação Pesquisada foi:",reclamacoes[codigoPesquisa-1])
    else:
      print("Código informado inválido!")

  elif  opcao == 5:
    codigoExcluir = int(input("Digite o código da manifestação: "))
    if codigoExcluir > 0 and codigoExcluir <= len(reclamacoes):
      reclamacoes.pop(codigoExcluir-1)
    print("Manifestação exluída com sucesso!")

  elif opcao != 6:
    print("Opção inválida!")

print("Obrigado por usar o nosso sistema")