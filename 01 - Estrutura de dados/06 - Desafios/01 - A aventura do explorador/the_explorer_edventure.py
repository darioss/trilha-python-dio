# Desafio: A Aventura do Explorador

# Entrada
quantidade_passos = int(input())

#TODO: Adicione uma condição para verificar se a quantidade de passos é positiva.
if(quantidade_passos < 0):
  print("Não seja covarde! Volte e enfrente o seu medo...")
# Se a quantidade de passos for zero, imprima "Nenhum passo dado na floresta."
elif(quantidade_passos == 0):
  print("Nenhum passo dado na floresta.")
# Caso contrário, utilize um loop for para imprimir a mensagem do explorador, indicando o número do passo.
else:
  mapa_passos = range(0, quantidade_passos )
  for passo in mapa_passos:
    if (passo == 0):
      print(f"Explorador: {passo+1} passo")
    else:
      print(f"Explorador: {passo+1} passos")