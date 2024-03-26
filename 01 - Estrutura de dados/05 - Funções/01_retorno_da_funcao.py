def calcular_total(numeros):
    return sum(numeros)


def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor


print(calcular_total([10, 20, 34]))  # 64
print(retorna_antecessor_e_sucessor(10))  # (9, 11)

def function_test():
    print("Hello my friend!")
    #This function auto returns None
    #Is the same to make
    # return None

#This line tests return of function_test()
print(function_test())