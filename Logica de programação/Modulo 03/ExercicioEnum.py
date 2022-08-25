from enum import Enum

class voto (Enum):
    candidato_x = 889
    candidato_y = 847
    candidato_z = 515
    branco = 0

constx = 0
consty = 0
cosntz = 0
cosnt0 = 0

def votacao(): 
    global constx 
    global consty 
    global cosntz 
    global cosnt0
    try:
        print('--------------- Sistema de votação -----------------')
        votos = int(input('Digite o codigo do candidato: '))
        if votos == voto.candidato_x.value:
            print('Seu candidato é: ', voto.candidato_x.name)
            comfirm = int(input('''
            Digite: 
            1. para confirma 
            2. para Cancelar
            '''))
            if comfirm == 1:
                constx = constx + 1
            elif comfirm == 2:
                votacao()
        elif votos == voto.candidato_y.value:
            print('Seu candidato foi: ', voto.candidato_y.name)
            comfirm = int(input('''
            Digite: 
            1. para confirma 
            2. para Cancelar
            '''))
            if comfirm == 1:
                consty = consty + 1
            elif comfirm == 2:
                votacao()
        elif votos == voto.candidato_z.value:
            print('Seu candidato é: ', voto.candidato_z.name)
            comfirm = int(input('''
            Digite: 
            1. para confirma 
            2. para Cancelar
            '''))
            if comfirm == 1:
                constz = constz + 1
            elif comfirm == 2:
                votacao()
        elif votos == voto.branco.value:
            print('Você estar votando em Branco')
            comfirm = int(input('''
            Digite: 
            1. para confirma 
            2. para Cancelar
            '''))
            if comfirm == 1:
                const0 = const0 + 1
            elif comfirm == 2:
                votacao()
        else:
            print('Você estar votando em nulo')
            comfirm = int(input('''
            Digite: 
            1. para confirma 
            2. para Cancelar
            '''))
            if comfirm == 1:
                const0 = const0 + 1
            elif comfirm == 2:
                votacao()
        opc = int(input('''
        Desja votar novamente ?
        1. Para SIM
        2. Para NÂO
        '''))
        if opc == 1:
            votacao()
        else:
            print('Finalizando votação, Obrigado pela colaboração')
   
    except:
        print('Você digitou um valor não valido por favor vote novamente')
        votacao()

votacao()
    
print(constx)
print(consty)
print(cosntz)

if constx > consty and constx > cosntz:
     print('O candidato com maior votos foi: ', voto.candidato_x.name, 'com: ', constx, ' votos')
     print('candidato_y teve: ', consty, ' vostos')
     print('candidato_z teve: ', cosntz, ' vostos')
     print('zeros e nulos tiveram: ', cosnt0, ' vostos')
elif consty > constx and consty > cosntz:
    print('O candidato com maior votos foi: ', voto.candidato_y.name, 'com: ', consty, ' votos')
    print('candidato_y teve: ', constx, ' vostos')
    print('candidato_z teve: ', cosntz, ' vostos')
    print('zeros e nulos tiveram: ', cosnt0, ' vostos')
elif cosntz > constx and cosntz > consty:
    print('O candidato com maior votos foi: ', voto.candidato_z.name, 'com: ', cosntz, ' votos')
    print('candidato_y teve: ', constx, ' vostos')
    print('candidato_z teve: ', consty, ' vostos')
    print('zeros e nulos tiveram: ', cosnt0, ' vostos')
