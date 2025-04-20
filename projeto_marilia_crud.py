# crud.py

# ----------------------------------------
# O que é um BRANCH?
# ----------------------------------------
# Um *branch* é uma ramificação do código principal onde podemos desenvolver novas
# funcionalidades sem afetar diretamente o que já está funcionando.
# Por exemplo, ao criar um branch chamado 'feature-novo-projeto', você pode desenvolver
# uma nova função ou módulo, testá-la, e somente depois integrar ao projeto principal
# (geralmente chamado de 'main' ou 'master').
# Isso evita conflitos e permite um desenvolvimento mais organizado e colaborativo.

# Neste exemplo, foi criado um novo branch chamado: 'feature-novo-projeto'
# E neste branch foi adicionada uma nova funcionalidade: a função `projeto()` abaixo

# Nova funcionalidade adicionada no branch 'feature-novo-projeto'
def projeto(nome, idade=None):
    if idade:
        return f"Olá, {nome}! Você tem {idade} anos."
    return f"Olá, {nome}!"

# Exemplo de uso:
# print(projeto("Maria", 30))
# print(projeto("Carlos"))

# ----------------------------------------
# Código original do CRUD
# ----------------------------------------

banco_dados = {}

def criar(id, nome, email):
    if id in banco_dados:
        print("ID já existe. Use outro ID.")
    else:
        banco_dados[id] = {"nome": nome, "email": email}
        print("Usuário criado com sucesso.")

def ler(id):
    if id in banco_dados:
        print(f"ID: {id} -> Nome: {banco_dados[id]['nome']}, Email: {banco_dados[id]['email']}")
    else:
        print("Usuário não encontrado.")

def atualizar(id, nome=None, email=None):
    if id in banco_dados:
        if nome:
            banco_dados[id]["nome"] = nome
        if email:
            banco_dados[id]["email"] = email
        print("Usuário atualizado com sucesso.")
    else:
        print("Usuário não encontrado.")

def deletar(id):
    if id in banco_dados:
        del banco_dados[id]
        print("Usuário deletado com sucesso.")
    else:
        print("Usuário não encontrado.")

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
