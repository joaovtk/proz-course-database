# importação das classes
from Class import (Aluno, Professor, UnidadeEscolar, Turma, Disciplina, cursor, db, pause, clear)

if __name__ == "__main__":
    while True:
        clear()
        print("Escolha uma opção:")
        print("1. Cadastrar Aluno")
        print("2. Listar Alunos")
        print("3. Alterar Aluno")
        print("4. Remover Aluno")
        print("5. Cadastrar Professor")
        print("6. Listar Professores")
        print("7. Alterar Professor")
        print("8. Remover Professor")
        print("9. Cadastrar Turma")
        print("10. Listar Turmas")
        print("11. Alterar Turma")
        print("12. Remover Turma")
        print("13. Cadastrar Disciplina")
        print("14. Listar Disciplinas")
        print("15. Alterar Disciplina")
        print("16. Remover Disciplina")
        print("17. Cadastrar Unidade Escolar")
        print("18. Listar Unidades Escolares")
        print("19. Alterar Unidade Escolar")
        print("20. Remover Unidade Escolar")
        print("0. Sair")

        opcao = input("Opção: ")
        clear()

        if opcao == "1":
            nome = input("Nome do Aluno: ")
            data_nascimento = input("Data de Nascimento (YYYY-MM-DD): ")
            turma_id = int(input("ID da Turma: "))
            aluno = Aluno(nome, data_nascimento, turma_id)
            aluno.salvar()

        elif opcao == "2":
            Aluno.listar()
            pause()

        elif opcao == "3":
            aluno_id = int(input("ID do Aluno: "))
            novo_nome = input("Novo Nome: ")
            Aluno.alterar(aluno_id, novo_nome)
            print("Nome do Aluno alterado com sucesso!")

        elif opcao == "4":
            aluno_id = int(input("ID do Aluno: "))
            Aluno.remover(aluno_id)
            print("Aluno removido com sucesso!")

        elif opcao == "5":
            nome = input("Nome do Professor: ")
            data = input("Data de Nascimento (YYYY-MM-DD): ") 
            cnpj = int(input("CNPJ: "))
            salario = float(input("Salario: "))
            professor = Professor(nome, cnpj, salario, data)
            professor.salvar()
            print("Professor cadastrado com sucesso!")

        elif opcao == "6":
            Professor.listar()
            pause()

        elif opcao == "7":
            professor_id = int(input("ID do Professor: "))
            novo_nome = input("Novo Nome: ")
            Professor.alterar(professor_id, novo_nome)
            print("Nome do Professor alterado com sucesso!")

        elif opcao == "8":
            professor_id = int(input("ID do Professor: "))
            Professor.remover(professor_id)
            print("Professor removido com sucesso!")

        elif opcao == "9":
            nome_turma = input("Nome da Turma: ")
            professor_id = int(input("ID do Professor: "))
            turma = Turma(nome_turma, professor_id)
            turma.salvar()
            print("Turma cadastrada com sucesso!")

        elif opcao == "10":
            Turma.listar()
            pause()

        elif opcao == "11":
            turma_id = int(input("ID da Turma: "))
            novo_nome = input("Novo Nome da Turma: ")
            Turma.alterar(turma_id, novo_nome)
            print("Nome da Turma alterado com sucesso!")

        elif opcao == "12":
            turma_id = int(input("ID da Turma: "))
            Turma.remover(turma_id)
            print("Turma removida com sucesso!")

        elif opcao == "13":
            nome_disciplina = input("Nome da Disciplina: ")
            turma_id = int(input("ID da Turma: "))
            disciplina = Disciplina(nome_disciplina, turma_id)
            disciplina.salvar()
            print("Disciplina cadastrada com sucesso!")

        elif opcao == "14":
            Disciplina.listar()
            pause()

        elif opcao == "15":
            disciplina_id = int(input("ID da Disciplina: "))
            novo_nome = input("Novo Nome da Disciplina: ")
            Disciplina.alterar(disciplina_id, novo_nome)
            print("Nome da Disciplina alterado com sucesso!")

        elif opcao == "16":
            disciplina_id = int(input("ID da Disciplina: "))
            Disciplina.remover(disciplina_id)
            print("Disciplina removida com sucesso!")
        elif opcao == "17":
            nome_unidade = input("Nome da Unidade Escolar: ")
            endereco = input("CEP da Unidade Escolar: ")
            unidade = UnidadeEscolar(nome_unidade, endereco)
            unidade.salvar()
            print("Unidade Escolar cadastrada com sucesso!")

        elif opcao == "18":
            UnidadeEscolar.listar()
            pause()

        elif opcao == "19":
            unidade_id = int(input("ID da Unidade Escolar: "))
            novo_nome = input("Novo Nome da Unidade Escolar: ")
            novo_cep = input("Novo CEP da Unidade Escolar: ")
            UnidadeEscolar.alterar(unidade_id, novo_nome, novo_cep)
            print("Nome e CEP da unidade escolar alterado com sucesso alterados com sucesso!")

        elif opcao == "20":
            unidade_id = int(input("ID da Unidade Escolar: "))
            UnidadeEscolar.remover(unidade_id)
            print("Unidade Escolar removida com sucesso!")
        elif opcao == "0":
            break

        else:
            print("Opção inválida. Tente novamente.")


# Fechar a conexão com o banco de dados
cursor.close()
db.close()