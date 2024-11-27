from funcoes import criar_contato, listar_contatos, atualizar_contato, deletar_contato

def exibir_menu():
    while True:
        print("\nMenu de Navegação:")
        print("1. Criar contato")
        print("2. Listar contatos")
        print("3. Atualizar contato")
        print("4. Deletar contato")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            criar_contato()
        elif escolha == "2":
            listar_contatos()
        elif escolha == "3":
            atualizar_contato()
        elif escolha == "4":
            deletar_contato()
        elif escolha == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")
