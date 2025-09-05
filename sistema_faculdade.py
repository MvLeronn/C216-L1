dados_alunos = []  # lista de dicionários com alunos
contador_matriculas = {}  # controla a contagem de alunos em cada curso


def cadastrarAluno():
    nome = input("Digite o nome do aluno: ")
    email = input("Digite o email do aluno: ")
    curso = input("Digite o curso do aluno: ").upper() # deixar em maiúsculo para padronizar

    # Se o curso ainda não tem contador, inicia em 0
    if curso not in contador_matriculas:
        contador_matriculas[curso] = 0

    matricula = f"{curso}{contador_matriculas[curso]}" # Gera a matricula única com base no nome do curso + o número de pessoas nesse curso

    contador_matriculas[curso] += 1 # Aumenta a contagem de alunos naquele curso

    aluno = {
        "nome": nome,
        "email": email,
        "curso": curso,
        "matricula": matricula
    }

    dados_alunos.append(aluno)
    print(f"Aluno {nome} com matrícula {matricula} cadastrado com sucesso!")

def listarAlunos():
    if not dados_alunos:
        print("Nenhum aluno cadastrado.")
    else:
        for aluno in dados_alunos:
            print(f"Matrícula: {aluno['matricula']} - Nome: {aluno['nome']} - Email: {aluno['email']} - Curso: {aluno['curso']}")

def atualizarAluno():
    matricula = input("Digite a matrícula do aluno a ser atualizado: ").upper()
    for aluno in dados_alunos:
        if aluno["matricula"] == matricula:
            aluno["nome"] = input("Digite o novo nome do aluno: ")
            aluno["email"] = input("Digite o novo email do aluno: ")
            print("Aluno atualizado com sucesso!")
            return
    print("Nenhum aluno com essa matrícula foi encontrado!")

def deletarAluno():
    matricula = input("Digite a matrícula do aluno a ser deletado: ").upper()
    for aluno in dados_alunos:
        if aluno["matricula"] == matricula:
            dados_alunos.remove(aluno)
            print("Aluno deletado com sucesso!")
            return
    print("Nenhum aluno com essa matrícula foi encontrado!")

def main():
    while True:
        print("\nMenu de Opções:")
        print("1 - Cadastrar Aluno")
        print("2 - Listar Alunos")
        print("3 - Atualizar Aluno")
        print("4 - Remover Aluno")
        print("5 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrarAluno()
        elif opcao == "2":
            listarAlunos()
        elif opcao == "3":
            atualizarAluno()
        elif opcao == "4":
            deletarAluno()
        elif opcao == "5":
            print("Saindo do sistema da faculdade...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
