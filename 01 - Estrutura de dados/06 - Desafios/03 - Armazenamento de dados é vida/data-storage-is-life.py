capacidade_atual, aumento_percentual = map(int, input().split())

# TODO: Calcule a nova capacidade do disco de Mithril
def calculate_new_capacity(capacidade_atual, aumento_percentual):
  return ((capacidade_atual*aumento_percentual)//100) + capacidade_atual

# TODO: Imprima a nova capacidade
print(calculate_new_capacity(capacidade_atual, aumento_percentual))