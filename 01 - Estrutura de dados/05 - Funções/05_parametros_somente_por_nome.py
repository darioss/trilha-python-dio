# After (*) the params must be named form in call function (like this - motor="V8")
# Before (/) the params must call for position (like this - (modelo, placa, ano)) 
# Between (/) and (*) the params must be two formats (like this (marca) or like this (marca=marca))
def criar_carro(modelo, ano, placa, /, marca,*,  motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)


criar_carro("Palio", 1997, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") #Valid
criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # inválido
