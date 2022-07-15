from logging import exception
try:
    teste = True
    nome = input("Digite seu Nome: ")
    while teste:
        anoNascimento = str(input("Digite seu ano de nascimento: "))
        if len(anoNascimento) == 4 & anoNascimento.isnumeric:
            anoNascimento = int(anoNascimento)
            if anoNascimento <= 1922 & anoNascimento >= 2021:
                idadeAtual = 2022 - anoNascimento
                print('Você ira completar: ', idadeAtual, " Em 2022" )
                tete = False
        else:
            print("Error < Digite Um numero valido para Ano > ")
except Exception as erro :
    print(f'Ocorreu um erro {erro.__class__}')
    
