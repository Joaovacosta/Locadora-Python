#Classes

class locadora:
    def __init__(self, nome, cidade):
        self.__nome = nome
        self.__cidade = cidade
        self.__clientes = []
    
    #Cadastro e Listagem de Clientes    
        
    def cadastrar_cliente(self, cliente):
        self.__clientes.append(cliente)
        print(f"Cliente '{cliente.getNome()}' cadastrado com sucesso.")
        
    def listar_clientes(self):
        if not self.__clientes:
            print("Nenhum cliente cadastrado.")
        else:
            print("Clientes cadastrados:")
            for cliente in self.__clientes:
                print(f"- {cliente.getNome()} (CPF: {cliente.getCpf()})")
                
    def adicionar_item(self, item):
        self.__itens.append(item)
        
    #GETs e SETs
    
    #DEFs        
    def getNome(self):
        return self.__nome

    def  getCidade(self):
        return self.__cidade      

    #SETs
    
    def setNome(self, nome):
        self.__nome = nome
    
    def setCidade(self, cidade):
        self.__cidade = cidade
class item:
    
    def __init__(self, filme, classificacao, genero, disponivel):
        self.__filme = filme
        self.__classificacao = classificacao
        self.__genero = genero
        self.__disponivel = disponivel
        
    def alugar(self):
        if self.__disponivel:
            self.__disponivel = False
            print(f"{self.__filme} foi alugado.")
        else:
            print(f"{self.__filme} não está disponível.")

    def devolver(self):
        if not self.__disponivel:
            self.__disponivel = True
            print(f"{self.__filme} foi devolvido.")
        else:
            print(f"{self.__filme} já está disponível.")
class Cliente:
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf
        self.__item_locado = None
    
    #GETs
        
    def getNome(self):
        return self.__nome
    
    def getCpf(self):
        return self.__cpf
    
    def getITlocado(self):
        return self.__item_locado
    
    #SETs

    def setNome(self, nome):
        self.__nome = nome
    
    def setCpf(self, cpf):
        self.__cpf = cpf
    
    def setITlocado(self, item_locado):
        self.__item_locado = item_locado
    
