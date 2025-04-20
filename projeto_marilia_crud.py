
# Simulando um "banco de dados" com dicionário
banco_dados = {}

# Função para criar um novo registro
def criar(id, nome, email):
    if id in banco_dados:
        print("ID já existe. Use outro ID.")
    else:
        banco_dados[id] = {"nome": nome, "email": email}
        print("Usuário criado com sucesso.")

# Função para ler um registro
def ler(id):
    if id in banco_dados:
        print(f"ID: {id} -> Nome: {banco_dados[id]['nome']}, Email: {banco_dados[id]['email']}")
    else:
        print("Usuário não encontrado.")

# Função para atualizar um registro
def atualizar(id, nome=None, email=None):
    if id in banco_dados:
        if nome:
            banco_dados[id]["nome"] = nome
        if email:
            banco_dados[id]["email"] = email
        print("Usuário atualizado com sucesso.")
    else:
        print("Usuário não encontrado.")

# Função para deletar um registro
def deletar(id):
    if id in banco_dados:
        del banco_dados[id]
        print("Usuário deletado com sucesso.")
    else:
        print("Usuário não encontrado.")

# Menu simples para interagir com o CRUD
def menu():
    while True:
        print("\n--- MENU CRUD ---")
        print("1. Criar")
        print("2. Ler")
        print("3. Atualizar")
        print("4. Deletar")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            id = input("ID: ")
            nome = input("Nome: ")
            email = input("Email: ")
            criar(id, nome, email)

        elif opcao == "2":
            id = input("ID: ")
            ler(id)

        elif opcao == "3":
            id = input("ID: ")
            nome = input("Novo nome (ou pressione Enter para manter): ")
            email = input("Novo email (ou pressione Enter para manter): ")
            atualizar(id, nome or None, email or None)

        elif opcao == "4":
            id = input("ID: ")
            deletar(id)

        elif opcao == "5":
            print("Encerrando programa.")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
