# If position of element is not defined, .pop removes the last element of list

linguagens = ["python", "js", "c", "java", "csharp"]

print(linguagens)

print(f"Remove {linguagens.pop()}") # csharp
print(linguagens)

print(f"Remove {linguagens.pop()}") # java
print(linguagens)

print(f"Remove {linguagens.pop()}") # c
print(linguagens)

print(f"Remove {linguagens.pop(0)}") # python
print(linguagens)