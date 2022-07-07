# criando a função calculadora 
def calculadora(x , y, opc):
# fazendo as vericações da operação desejada e calculado de acordo
    if(opc == "+"):
        res = x + y
        print("Resultado: ", res )
    elif(opc == "-"):
        res = x - y
        print("Resultado: ", res )
    elif(opc == "*"):
        res = x * y
        print("Resultado: ", res)
    elif(opc == "/"):
        res = x / y
        print("Resultado: ", res)
    else:
        res = 0
        print('Operação escolhida não existe', res)

# incio do programa 
teste = False
while (teste == False):
    print('-------------------- Calculadora ---------------------')
    num1 = float(input('Digite do Primeiro numero: '))
    num2 = float(input('digite o segundo numero: ')) 
    opc = input('''
    Escolha qual operação você deseja fazer:
    "+" - Para soma
    "-" - Para subtração 
    "*" - Para multiplicação
    "/" - Para divisão
    ''')        

    calculadora(num1, num2, opc)

# teste para continuar o fazendo operações na calculadora 
    escolha = int(input('''
    Você deseja fazer outro calculo? 
    1 . Sim 
    2 . Não
    '''))
    if(escolha == 1):
        teste = False
    elif(escolha == 2):
        teste = True
        print("Fechando a calculadora: ")
    else:
        print("Opção não valida")
    
    

# Outra forma de fazer a calculadora
# def soma(x , y):
#     return x + y
# def sub(x,y):
#     return x - y
# def mult(x,y):
#     return x * y
# def div(x,y):
#     return x / y 

# teste = False
# while(teste == False):
#     print('-------------------- Calculadora ---------------------')
#     num1 = float(input('Digite do Primeiro numero: '))
#     num2 = float(input('digite o segundo numero: ')) 
#     opc = input('''
#     Escolha qual operação você deseja fazer:
#     "+" - Para soma
#     "-" - Para subtração 
#     "*" - Para multiplicação
#     "/" - Para divisão
#     ''')

#     if(opc == "+"):
#         print("Resultado: ", soma(num1, num2))
#     elif(opc == "-"):
#         print("Resultado: ", sub(num1, num2))
#     elif(opc == "*"):
#         print("Resultado: ", mult(num1, num2))
#     elif(opc == "/"):
#         print("Resultado: ", div(num1, num2))
#     else:
#         print('Operação escolhida não existe, Rode o programa novamente')
#     escolha = int(input('''
#     Você deseja fazer outro calculo? 
#     1 . Sim 
#     2 . Não
#     '''))
#     if(escolha == 1):
#         teste = False
#     elif(escolha == 2):
#         teste = True
#         print("Fechando a calculadora: ")
#     else:
#         print("Opção não valida")
    
   

    