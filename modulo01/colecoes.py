# Coleções: Listas, Tuplas, Dicionários e Conjuntos

# Listas é uma coleção ordenada e mutável, Permite membros duplicados
palavras = ['carro', 'bicicleta', 'avião', 'barco']
print(type(palavras))
print(palavras)
# index:  0         1    2   3
listas = ['carro', True, 2, 3.5]
print(type(listas))
print(listas)
print(listas[0])  # Acessando o primeiro elemento da lista
print("=" *30)

# Tupla é uma coleção ordenada e imutável. Permite membros duplicados
# index:   0       1    2   3  
tupla = ('carro', True, 2 , 3.5)
print(tupla)
print(type(tupla))
print(tupla[0])  # Acessando o primeiro elemento da tupla
print(tupla[1:3])  # Acessando uma fatia da tupla
print("." *30)

# Dicionarios são uma coleção ordenada e mutável. Não permite membros duplicados
              # chave: Valor              
dicionario = {'nome': 'João', 'idade': 25, 'cidade': 'São Paulo'}
print(dicionario)
print(type(dicionario))
print(dicionario['nome'])  # Acessando o valor associado à chave 'nome'
print("." *30)

# Set é uma coleção não ordenada e mutável. Nenhum membro duplicado.

conjunto = {'carro', True , 2 , 4.5 }
print(conjunto)
print(type(conjunto))
# print(conjunto['carro'])  # Acessando o primeiro elemento do conjunto (não é garantido a ordem)
print("." *30)

pessoa = {"nome": "João", "idade": 25, "cidade": "Madri"}


print(pessoa.keys())    # Imprime dict_keys(["nome", "idade", "cidade"])
print(pessoa.values())  # Imprime dict_values(["João", 25, "Madri"])
print(pessoa.items())   # Imprime dict_items([("nome", "João"), ("idade", 25), ("cidade", "Madri")])


pessoa.update({"profissao": "Engenheiro"})
print(pessoa)  # Imprime {"nome": "João", "idade": 25, "cidade": "Madri", "profissao": "Engenheiro"}

# Exemplos Conjuntos

conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}

uniao = conjunto1 | conjunto2
print(uniao)  # Imprime {1, 2, 3, 4, 5}

intersecao = conjunto1 & conjunto2
print(intersecao)  # Imprime {3}

diferenca = conjunto1 - conjunto2
print(diferenca)  # Imprime {1, 2}

diferenca_simetrica = conjunto1 ^ conjunto2
print(diferenca_simetrica)  # Imprime {1, 2, 4, 5}

# Conjuntos exemplos

frutas = {"maçã", "banana", "laranja"}

frutas.add("pera")
print(frutas)  # Imprime {"maçã", "banana", "laranja", "pera"}

frutas.remove("banana")
print(frutas)  # Imprime {"maçã", "laranja", "pera"}

frutas.discard("uva")
print(frutas)  # Imprime {"maçã", "laranja", "pera"}

frutas.clear()
print(frutas)  # Imprime set()