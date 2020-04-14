def soma():
    n1 = float(input("Escolha um valor: "))
    n2 = float(input("Escolha outro valor: "))
    print(n1 + n2)

def sub():    
    n1 = float(input("Escolha um valor: "))
    n2 = float(input("Escolha outro valor: "))
    print(n1 - n2)

def mu():
    n1 = float(input("Escolha um valor: "))
    n2 = float(input("Escolha outro valor: "))
    print(n1 * n2)

def di():
    n1 = float(input("Escolha um valor: "))
    n2 = float(input("Escolha outro valor: "))
    print(n1 / n2)

def imprimir_menu():
    print("****Calculadora PY****")
    print("1.Adição")
    print("2.Subtração")
    print("3.Multiplicação")
    print("4.Divisão")
    print("5.All")
    print("0.Sair")
    print("***********************")
    
while True: 
    imprimir_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        soma()

    elif opcao == "2":
        sub() 

    elif opcao == "3":
        mu()
        
    elif opcao == "4":
        try:
            di()
        except ZeroDivisionError:
            print(">>>Impossivel fazer a divisão")

    elif opcao == "5":
        n1 = float(input("Escolha um valor: "))
        n2 = float(input("Escolha outro valor: "))
        print("--------------")
        print("Adição:", n1 + n2)
        print("--------------")
        print("Subtração:", n1 - n2)
        print("--------------")
        print("Multiplicação:", n1 * n2)
        print("--------------")
        try:
            print("Divisão:", n1 / n2)
            print("--------------")
        except ZeroDivisionError:
            print(">>>Impossivel fazer a divisão")
            print("--------------")

    elif opcao == "0":
        print(">>>Fechando programa")
        break

    else:
        print(">>>Valor incorreto")





        






    
