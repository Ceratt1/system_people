import os
os.system('cls')

lista_pessoas = list()

class cidadao():
    def __init__(self, nome, idade,cpf) -> None:
        self.nome = nome
        self.idade = idade
        self.__cpf = cpf

    def __str__(self) -> str:
        return f"""
    aluno : {self.nome}
    idade : {self.idade}
    cpf : {self.__cpf}
                """



num_pessoas = int(input("digite o número de pessoas que deseja adicionar: "))
print("=-"*20)

for x in range(num_pessoas):
    nome = input("digite o nome: ")
    idade = input("digite a idade: ")
    cpf = input("digite o cpf: ")
    print(f"""{"=-"*3}próximo aluno{"=-"*3}""")
    lista_pessoas.append(cidadao(nome=nome, idade=idade, cpf=cpf))


for ind in lista_pessoas:
    print (ind)