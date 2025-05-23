class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

class Produto:
    def __init__(self, nome, preco, quantidade):
        if preco < 0:
            print("Erro: preço não pode ser negativo.")
            preco = 0  # evita valores negativos
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def calcular_imposto(self):
        return self.preco * 0.15

    def preco_final(self):
        return (self.preco + self.calcular_imposto()) * self.quantidade

class Estoque:
    def __init__(self, cod_product, valor):
        self.cod_product = cod_product
        self.valor = valor


clientes = []
produtos = []

def cadastrar_cliente():
    print("\n--- Cadastro de Cliente ---")
    nome = input("Digite o nome do cliente: ")
    email = input("Digite o e-mail do cliente: ")

    if nome != "" and email != "":
        novo_cliente = Cliente(nome, email)
        clientes.append(novo_cliente)
        print("Cliente cadastrado com sucesso!")
    else:
        print("Por favor, preencha todos os campos.")

def cadastrar_produto():
    print("\n--- Cadastro de Produto ---")
    nome = input("Nome do produto: ")

    try:
        preco = float(input("Preço do produto: "))
        quantidade = int(input("Quantidade: "))
    except:
        print("Erro: preço ou quantidade inválidos.")
        return

    if nome != "":
        novo_produto = Produto(nome, preco, quantidade)
        produtos.append(novo_produto)
        print("Produto cadastrado com sucesso!")
    else:
        print("O nome do produto não pode estar vazio.")

def mostrar_produtos():
    print("\n--- Lista de Produtos ---")
    if len(produtos) == 0:
        print("Nenhum produto cadastrado ainda.")
    else:
        for i, p in enumerate(produtos):
            print(f"\nProduto {i+1}:")
            print("Nome:", p.nome)
            print("Preço: R$", round(p.preco, 2))
            print("Quantidade:", p.quantidade)
            print("Imposto: R$", round(p.calcular_imposto(), 2))
            print("Preço final com imposto: R$", round(p.preco_final(), 2))

def menu():
    while True:
        print("\n=== MENU ===")
        print("1 - Cadastrar Cliente")
        print("2 - Cadastrar Produto")
        print("3 - Mostrar Produtos")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_cliente()
        elif opcao == "2":
            cadastrar_produto()
        elif opcao == "3":
            mostrar_produtos()
        elif opcao == "4":
            print("Saindo... Até mais!")
            break
        else:
            print("Opção inválida. Tente de novo.")

# Início do programa
menu()
