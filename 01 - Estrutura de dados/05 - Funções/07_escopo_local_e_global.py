salario = 2000

#this is not a good practice, because modify variable in global scope
def salario_bonus(bonus):
    global salario 
    salario += bonus
    return salario

#this is a good practice, because modify variable only local scope
def salary_bonus(salario, bonus):
    salario += bonus
    return salario


print(salary_bonus(salario, 500))
print(f" Salary after function good practice {salario}")

print(salario_bonus(500))  # 2500
print(f" Salary after function bad practice {salario}")