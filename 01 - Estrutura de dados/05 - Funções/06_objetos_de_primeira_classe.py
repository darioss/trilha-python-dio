def somar(a, b):
    return a + b

def subtract(a, b):
    return a - b 

def division(a, b):
    return a / b

def multiply(a, b):
    return a * b

def exponential(a, b):
    return a**b

def rest_of_division(a, b): #Modulus
    return a % b 

def integer_division(a, b):
    return a // b

#Receives two numbers and a function name 
def exibir_resultado(a, b, funcao):
    # The result variable receives the result of function received like argument, using the numbers
    # received like arguments within method of this function
    resultado = funcao(a, b)
    print(f"O resultado da operação é {resultado}")


exibir_resultado(10, 10, somar)  # O resultado da operação 10 + 10 = 20
exibir_resultado(9, 8, subtract)
exibir_resultado(10976, 37, division)
exibir_resultado(9, 3, multiply)
exibir_resultado(2, 8, exponential)
exibir_resultado(8763, 98, rest_of_division)
exibir_resultado(33, 9, integer_division)

variable_test = subtract

print(variable_test(1,24))