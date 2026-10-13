#Apenas a tela de visualização
while True:
    print("===================")
    print("Sistema de Cadastro")
    print("===================")

    print("1 - Cadastrar")
    print("2 - Fazer login")
    print("3 - Sair")
    
    opção = int(input("Escolha uma opção:"))
    #Funcionalidades
    #Se o usuario digitar o valor 1, vai ser exebido
    #a ação abaixo:
    if(opção == 1) :
        print("==========================")
        print("=====Tela de Cadastro=====")
        print("==========================")
    elif (opção == 2):
        print("==========================")
        print("===Tela de Login===")
        print("==========================")
       else:
           print("Você esá saindo do cadastro, até mais!")
           break