print("****Calculadora PY****")
print("1.Adição")
print("2.Subtração")
print("3.Multiplicação")
print("4.Divisão")
print("5.All")
print("6.Sair")
print("***********************")
 
menu=input("Escolha uma opção: ")
 
if menu == "1":
    print("Escolha um valor.")
    n1 = float(input())
    print("Escolha outro valor.")
    n2 = float(input())
    so = n1 + n2
    print(so)

elif menu == "2":
    print("Escolha um valor.")
    n1 = float(input())
    print("Escolha outro valor.")
    n2 = float(input())
    su = n1 - n2
    print(su) 

elif menu == "3":
    print("Escolha um valor.")
    n1 = float(input())
    print("Escolha outro valor.")
    n2 = float(input())
    mu = n1 * n2
    print(mu)

elif menu == "4":
    print("Escolha um valor")
    n1 = float(input())
    print("Escolha outro valor")
    n2 = float(input())
    di = n1 / n2
    print(di)

elif menu == "5":
    print("Escolha um valor")
    n1 = float(input())
    print("Escolha outro valor.")
    n2 = float(input())
    
    print("Adição") #adição
    so = n1 + n2
    print(so)
    print("-----------------------")
    print("Subtração") #subtração
    su = n1 - n2 
    print(su)
    print("-----------------------")
    print("Multiplicação") #multiplicação
    mu = n1 * n2
    print(mu)
    print("-----------------------")
    print("Divisão") #divisão
    di = n1 / n2
    print(di)

else:
    print("Valor incorreto!")




    
