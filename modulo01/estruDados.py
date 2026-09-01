# Estrutura de Dados --- Listas

frutas = ["maça", "banana", "laranja", "uva", "pera"]

print(frutas[0])  # Acessando o primeiro elemento da lista
print(frutas[1])  # Acessando o segundo elemento da lista
print(frutas[2])  # Acessando o terceiro elemento da lista
print(frutas[3])  # Acessando o quarto elemento da lista
print(frutas[4])  # Acessando o quinto elemento da lista

print("A lista de frutas é:", frutas)  # Imprimindo a lista completa

frutas = ["maçã", "banana", "laranja"]


frutas.append("pera")
print(frutas)  # Imprime ["maçã", "banana", "laranja", "pera"]


frutas.insert(1, "uva")
print(frutas)  # Imprime ["maçã", "uva", "banana", "laranja", "pera"]


frutas.remove("banana")
print(frutas)  # Imprime ["maçã", "uva", "laranja", "pera"]


fruta_removida = frutas.pop(2)
print(frutas)  # Imprime ["maçã", "uva", "pera"]
print(fruta_removida)  # Imprime "laranja"


frutas.sort()
print(frutas)  # Imprime ["maçã", "pera", "uva"]


frutas.reverse()
print(frutas)  # Imprime ["uva", "pera", "maçã"] 

# Listas de compreensão
numeros = [1, 2, 3, 4, 5]
quadrados = [x**2 for x in numeros if x % 2 == 0]
print(quadrados)  # Imprime [4, 16]



