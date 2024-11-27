import csv

ARQUIVO = 'contatos.csv'

def ler_dados():
    try:
        with open(ARQUIVO, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        return []

def escrever_dados(dados):
    with open(ARQUIVO, mode='w', newline='') as file:
        fieldnames = ['nome', 'telefone', 'email', 'endereco']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(dados)

def criar_contato():
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    endereco = input("Endereço: ")
    dados = ler_dados()
    dados.append({'nome': nome, 'telefone': telefone, 'email': email, 'endereco': endereco})
    escrever_dados(dados)
    print("Contato criado com sucesso!")

def listar_contatos():
    dados = ler_dados()
    for contato in dados:
        print(f"Nome: {contato['nome']}, Telefone: {contato['telefone']}, Email: {contato['email']}, Endereço: {contato['endereco']}")

def atualizar_contato():
    nome = input("Nome do contato a ser atualizado: ")
    dados = ler_dados()
    for contato in dados:
        if contato['nome'] == nome:
            contato['telefone'] = input("Novo Telefone: ")
            contato['email'] = input("Novo Email: ")
            contato['endereco'] = input("Novo Endereço: ")
            escrever_dados(dados)
            print("Contato atualizado com sucesso!")
            return
    print("Contato não encontrado.")

def deletar_contato():
    nome = input("Nome do contato a ser deletado: ")
    dados = ler_dados()
    dados = [contato for contato in dados if contato['nome'] != nome]
    escrever_dados(dados)
    print("Contato deletado com sucesso!")
