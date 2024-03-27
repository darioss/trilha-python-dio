# Lista para armazenar os itens
itens = []
count_items = 0
#TODO: Solicite os itens ao usuário
while True:
  if count_items == 3:
    break

  item = input()
  itens.append(item.title())
  count_items+=1


# Exibe a lista de itens
print("Lista de itens:")
for item in itens:
    print(f"- {item}")