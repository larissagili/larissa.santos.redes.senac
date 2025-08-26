#==============================
# Sistema de Controle de Alunos
#==============================

#Função para calcular média das avaliações - recebe uma lista de notas chamadas avaliações
def calcular_media(avaliações):
    return sum(avaliações) / len(avaliações)

#Função para exibir todos os alunos - recebe uma lista de alunos 
def exibir_alunos(alunos):
    for aluno in alunos:
        print(f"Nome: {aluno['nome']}")
        print(f"Idade: {aluno['idade']}")
        print(f"Altura: {aluno['altura']} m")
        print(f"Ativo: {aluno['ativo']}")
        print(f"Média avaliações: {calcular_media(aluno['avaliações']):.2f}")
        print("-"*30)
    if "ativo" == False:
        print("Aluno não ativo")

#Função para listar apenas os alunos ativos - define qual função recebe a lista alunos
def listar_ativos(alunos):
    ativos = [aluno for aluno in alunos if aluno['ativo']]
    return ativos

#Função para cadastrar aluno - cria um novo dicionário aluno 
def cadastrar_aluno(alunos, nome, idade, altura, ativo, avaliações):
    aluno = {
        "nome": nome,
        "idade": idade,
        "altura": altura,
        "ativo": ativo,
        "avaliações": avaliações
    }
    alunos.append(aluno) #adiciona o dicionário na lista de alunos

# ==============================================

#Lista inicial de alunos
alunos = [
    {
    "nome": "Beatriz",
    "idade": 18,
    "altura": 1.64,
    "ativo": True,
    "avaliações": [7.0, 9.5, 6.5]
    },
    {
    "nome": "João",
    "idade": 22,
    "altura": 1.80,
    "ativo": False,
    "avaliações": [10, 9.5, 7.5]
    }
]

# Exibir todos os alunos cadastrados
print("=== Lista de Alunos ===")
exibir_alunos(alunos)

#Cadastrar novos alunos
cadastrar_aluno(alunos, "Mariana", 25, 1.70, True, [7.0, 4.5, 9.2])

#Mostrar alunos ativos
print("\n=== Alunos Ativos ===")
exibir_alunos(listar_ativos(alunos))