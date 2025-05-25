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
    def __init__(self):
        self.produtos = {}

    def cadastrar_produto(self, id_produto, nome, preco, quantidade):
        if id_produto in self.produtos:
            raise ValueError("Produto já cadastrado.")
        if preco < 0 or quantidade < 0:
            raise ValueError("Preço e quantidade devem ser não negativos.")
        self.produtos[id_produto] = {
            'nome': nome,
            'preco': preco,
            'quantidade': quantidade
        }

    def entrada_estoque(self, id_produto, quantidade):
        if id_produto not in self.produtos:
            raise KeyError("Produto não encontrado.")
        if quantidade <= 0:
            raise ValueError("Quantidade deve ser positiva.")
        self.produtos[id_produto]['quantidade'] += quantidade

    def saida_estoque(self, id_produto, quantidade):
        if id_produto not in self.produtos:
            raise KeyError("Produto não encontrado.")
        if quantidade <= 0:
            raise ValueError("Quantidade deve ser positiva.")
        if quantidade > self.produtos[id_produto]['quantidade']:
            raise ValueError("Estoque insuficiente.")
        self.produtos[id_produto]['quantidade'] -= quantidade

    def listar_produtos(self):
        if not self.produtos:
            print("Nenhum produto cadastrado.")
            return
        print("\n--- Lista de Produtos ---")
        for id_produto, dados in self.produtos.items():
            print(f"ID: {id_produto}")
            print(f"Nome: {dados['nome']}")
            print(f"Preço: R$ {dados['preco']:.2f}")
            print(f"Quantidade em estoque: {dados['quantidade']}")
            print("------------------------")


clientes = []
estoque = Estoque()

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
    id_produto = input("ID produto: ")
    nome = input("Nome do produto: ")

    try:
        preco = float(input("Preço do produto: "))
        quantidade = int(input("Quantidade: "))
    except:
        print("Erro: preço ou quantidade inválidos.")
        return

    if nome != "":
        estoque.cadastrar_produto(id_produto, nome, preco, quantidade)
        print("Produto cadastrado com sucesso!")
    else:
        print("O nome do produto não pode estar vazio.")

def mostrar_produtos():
    print("\n--- Lista de Produtos ---")
    if not estoque.produtos:
        print("Nenhum produto cadastrado ainda.")
    else:
        for id_produto, p in estoque.produtos.items():
            produto_temp = Produto(p['nome'], p['preco'], p['quantidade'])
            print(f"\nProduto {id_produto}")
            print("Nome:", produto_temp.nome)
            print("Preço: R$", round(produto_temp.preco, 2))
            print("Quantidade:", produto_temp.quantidade)
            print("Imposto: R$", round(produto_temp.calcular_imposto(), 2))
            print("Preço final com imposto: R$", round(produto_temp.preco_final(), 2))

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
